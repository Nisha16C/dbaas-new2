<template>
  <div class="card" style="height: 650px; overflow-y: auto;">
    <div class="card-header pb-0">
      <h6 class="text-2xl">Users Info</h6>
      <div class="mb-3">
        <select v-model="selectedFilter" class="form-select" @change="filterUsers">
          <option value="all">All Users</option>
          <option value="local">Local Users</option>
          <option value="ad">AD Users</option>
        </select>
      </div>
    </div>

    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else class="card-body px-0 pt-0 pb-2">
      <div v-if="users.length === 0" class="text-center">No Users are Available</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-md font-weight-bolder opacity-7">User Name</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Email Address</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Created On</th>
              <th class="text-center text-uppercase text-secondary text-md font-weight-bolder opacity-7">Last Login</th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in filteredUsers" :key="user.id">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img :src="isDarkMode ? logoWhite : logo" class="avatar avatar-sm me-3" :alt="`user-avatar-${user.id}`" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <p class="text-md text-secondary mb-0">{{ user.username }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ user.email }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(user.date_joined) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-md font-weight-bold">{{ formatDate(user.last_login) }}</span>
              </td>
              <td class="align-middle">
                <argon-button color="success" size="md" variant="gradient" @click="prepareAssignRoles(user)" type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                  Assign Roles
                </argon-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" :class="{ 'show': isModalVisible }">
    <div class="modal-dialog" role="document">
      <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
        <div class="modal-header">
          <h2 class="modal-title" id="exampleModalLabel">Select Role</h2>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="form-check" v-for="role in roles" :key="role.name">
            <input v-model="selectedRole" class="form-check-input" type="radio" :value="role.name" :id="'roleRadio_' + role.name">
            <label class="form-check-label" :for="'roleRadio_' + role.name">{{ role.name }}</label>
          </div>
        </div>
        <div class="modal-footer">
          <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false" type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Cancel
          </argon-button>
          <argon-button color="danger" size="md" variant="gradient" @click.prevent="assignRoles" type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Assign Role
          </argon-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ArgonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/userTable.png";
import logoWhite from "@/assets/img/user.png";

export default {
  name: "users-table",
  components: {
    ArgonButton,
  },
  data() {
    return {
      selectedFilter: "all",
      apiUrl: API_ENDPOINT,
      users: [],
      isModalVisible: false,
      roles: [
        { id: 1, name: 'Admin' },
        { id: 2, name: 'Standard' },
        // Add more roles as needed
      ],
      selectedRole: '',
      selectedUser: null,
      loading: true,
      logo,
      logoWhite
    };
  },
  mounted() {
    this.fetchUsers();
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
    filteredUsers() {
      if (this.selectedFilter === "local") {
        return this.users.filter(user => user.groups.includes(1));
      } else if (this.selectedFilter === "ad") {
        return this.users.filter(user => user.groups.length === 0);
      } else {
        return this.users;
      }
    }
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/users/`);
        this.users = response.data;
        this.loading = false;
      } catch (error) {
        console.error('Error fetching users:', error);
        this.loading = false;
      }
    },
    filterUsers() {
      this.loading = true;
      this.fetchUsers();
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
    async prepareAssignRoles(user) {
      this.selectedUser = user;
      await this.fetchUserRoles(user.id);
      this.isModalVisible = true;
    },
    async fetchUserRoles(userId) {
      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/get_user_role/${userId}/`);
        if (response.data && Array.isArray(response.data.user_roles)) {
          this.selectedRole = response.data.user_roles.length ? response.data.user_roles[0].split(' - ')[1] : '';
        } else {
          console.error('Failed to fetch user roles:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching user roles:', error);
      }
    },
    async assignRoles() {
      try {
        if (!this.selectedUser || !this.selectedRole) {
          console.error('No user or role selected.');
          return;
        }
        const response = await axios.post(`${this.apiUrl}/api/v1/add_roles_to_user/`, {
          user_id: this.selectedUser.id,
          roles: [this.selectedRole],
        });
        if (response.data.success) {
          console.log('Role assigned successfully:', response.data.message);
        }
        this.isModalVisible = false;
        await this.fetchUsers(); // Refresh the users list after assigning roles
      } catch (error) {
        console.error('Error assigning roles:', error);
      }
    }
  }
};
</script>

<style scoped>
.dark-mode {
  background-color: #1d1e52;
  color: #ffffff;
}
select.form-select {
  width: 150px;
  font-size: 14px;
  padding: 8px;
  border-radius: 9px;
}
</style>
