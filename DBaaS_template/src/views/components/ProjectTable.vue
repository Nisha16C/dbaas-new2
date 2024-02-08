<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Projects info </h6>
    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> PROJECT ID & NAME </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> CREATE_DATE </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> UPDATED_DATE </th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, index) in projects" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img src="@/assets/img/projectTable.png" class="avatar avatar-sm me-3" alt="logo" />
                  </div>
                <div class="d-flex flex-column">
                  <h6 class="mb-0 text-sm">{{ project.id }}</h6>
                  <p class="text-xs font-weight-bold mb-0">{{ project.project_name }}</p>
                </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(project.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(project.updated_date) }}</span>
              </td>
              <td class="align-middle">
                <!-- You can customize the Edit link as per your requirements -->
                <a href="javascript:;" class="text-secondary font-weight-bold text-xs" data-toggle="tooltip"
                  data-original-title="Edit cluster">Edit</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<!-- ... (rest of the component) -->

  <script>
import axios from "axios";

export default {
  name: "projects-table",
  data() {
    return {
      projects: [], // Initialize clusters as an empty array
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchProjects();
  },
  methods: {
    async fetchProjects() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get('http://172.16.1.97:8002/api/v2/project/');
        
        // Update the clusters data with the fetched data
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching clusters:', error);
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
  