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
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Role </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Created On</th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Last Login</th>

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
                <span class="text-secondary text-xs font-weight-bold">{{ user.role }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(user.date_joined) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(user.last_login) }}</span>
              </td>
              <td class="align-middle">
                <a
                  href="javascript:;"
                  class="text-secondary font-weight-bold text-xs"
                  data-toggle="tooltip"
                  data-original-title="Edit user"
                >Edit</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";

export default {
  name: "users-table",
  data() {
    return {
      users: [], // Initialize clusters as an empty array
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchusers();
  },
  methods: {
    async fetchusers() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get('http://172.16.1.97:8002/api/v1/users/');
        
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
  