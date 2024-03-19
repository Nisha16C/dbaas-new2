<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Users info </h6>
    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> User Name & ID </th>

              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Status </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Created On</th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Last Login</th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Email Address</th>

              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <!-- <tr v-for="(user, index) in users" :key="index"></tr> -->
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img src="@/assets/img/userTable.png" class="avatar avatar-sm me-3" :alt="`user-avatar-${user.id}`" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ user.id }}</h6>
                    <p class="text-xs text-secondary mb-0">{{ user.username }}</p>
                  </div>
                </div>
              </td>

              <td class="align-middle text-center text-sm">
                <span v-if="!user.isActive" class="badge badge-sm bg-gradient-success">Active</span>
                <span v-else class="badge badge-sm bg-gradient-danger">Inactive</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(user.date_joined) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(user.last_login) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{user.email}}</span>
              </td>
              <!-- <td class="align-middle">
                <argon-button color="success" size="md" variant="gradient" @click="prepareUserRole(user)" type="button"
                  class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal2">
                  View Role
                </argon-button>
                <argon-button color="success" size="md" variant="gradient" @click="prepareAssignRoles(user)" type="button"
                  class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                  Assign Roles
                </argon-button>
              </td> -->
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h2 class="modal-title" id="exampleModalLabel">Select Roles</h2>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <!-- Inside your modal body -->
        <div class="form-check" v-for="role in roles" :key="role.name">
          <input v-model="selectedRoles" class="form-check-input" type="checkbox" :value="role.name"
            :id="'roleCheckbox_' + role.name">
          <label class="form-check-label" :for="'roleCheckbox_' + role.name">{{ role.name }}</label>
        </div>

        <div class="modal-footer">
          <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false" type="button"
            class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Cancel
          </argon-button>
          <argon-button color="danger" size="md" variant="gradient" @click.prevent="assignRoles(user)" type="button"
            class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Assign Roles
          </argon-button>
        </div>
      </div>
    </div>
  </div>


  <div class="modal fade" ref="myModal" id="exampleModal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title" id="exampleModalLabel">User Role</h3>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <!-- Inside your modal body -->
        <div class="form-check" v-if="selectedUser">
          <label class="form-check-label">Username: {{ selectedUser.username }}</label><br>
          <label class="form-check-label">Assigned Role: {{ formattedRoles || 'No Role Assign' }}</label>
        </div>

        <div class="modal-footer">
          <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false" type="button"
            class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal2">
            Close
          </argon-button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";
import ArgonButton from "@/components/ArgonButton.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

// import ArgonInput from "@/components/ArgonInput.vue";

export default {
  name: "users-table",
  components: {
    // Card,
    // projectsTable,
    ArgonButton,
    // ArgonInput
  },
  data() {
    return {
      apiUrl: API_ENDPOINT, 
      users: [], // Initialize clusters as an empty array
      isModalVisible: false,
      roles: [
        { id: 1, name: 'Owner' },
        { id: 2, name: 'Viewer' },
        { id: 3, name: 'Editor' },
        // Add more roles as needed
      ],
      selectedRoles: [],
      selectedUser: null,
      successMessage: null,
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchusers();
    this.fetchRoles();
  },
  computed: {
    formattedRoles() {
      if (Array.isArray(this.selectedRoles)) {
        return this.selectedRoles.join(', ');
      }
      return ''; // or some default value if selectedRoles is not an array
    },
  },

  methods: {
    async prepareUserRole(user) {
      try {
        // Assign the user before fetching user roles
        this.selectedUser = user;
        // Fetch user roles dynamically using the user's ID
        const response = await axios.get(`${this.apiUrl}/api/v1/get_user_role/${this.selectedUser.id}/`);
        console.log('API Response:', response);

        if (response.data && Array.isArray(response.data.user_roles)) {
          // Extract roles from the array of strings
          this.selectedRoles = response.data.user_roles.map(roleString => {
            // Assuming roleString is in the format 'username - role'
            const parts = roleString.split(' - ');
            return parts[1];  // Extract the role part
          });

          console.log('User roles fetched successfully:', this.selectedRoles);
          this.isModalVisible = true;
        } else {
          console.error('Failed to fetch user roles:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching user roles:', error);
      }
    },
    prepareAssignRoles(user) {
      // Set the selected user and reset selected roles
      this.selectedUser = user;
      this.selectedRoles = [];
      // Show the modal
      this.isModalVisible = true;
      this.fetchRoles(user.id);
    },
    async fetchRoles() {
      try {
        const response = await axios.get(`${this.apiUrl}/api/v1/users/`,
          {
            user_id: this.selectedUser.id,
          });
        console.log('API Response:', response)

        if (response && response.data && response.data.success) {
          // Update the roles for the selected user
          this.selectedRoles = response.data.roles.map(role => role.name);
          console.log('Roles fetched successfully:', this.selectedRoles);
        } else {
          console.error('Failed to fetch roles:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching roles:', error);
      }
    },
    async assignRoles() {
      try {
        // Check if selectedUser is defined
        if (!this.selectedUser) {
          console.error('No user selected.');
          return;
        }
        const response = await axios.post(`${this.apiUrl}/api/v1/add_roles_to_user/`,
          {
            user_id: this.selectedUser.id,
            roles: this.selectedRoles,
          }
        );

        if (response.data.success) {
          console.log('Roles assigned successfully:', response.data.message);
          // Assuming the API response structure includes an updatedRoles field
          const updatedRoles = response.data.updatedRoles.map(role => role.name);

          // Update the roles array with the updated roles at the 0 index
          this.selectedRoles.splice(0, this.selectedRoles.length, ...updatedRoles);
        }
        // Close the modal
        this.isModalVisible = false;
      } catch (error) {
        console.error('Error assigning roles:', error);
      }
    },


    async fetchusers() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`${this.apiUrl}/api/v1/users/`);

        // Update the clusters data with the fetched data
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    formatDate(dateString) {
      // Format the date as per your requirement using a library like moment.js
      // Example using JavaScript built-in methods (customize as needed):
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },

  },
};
</script>