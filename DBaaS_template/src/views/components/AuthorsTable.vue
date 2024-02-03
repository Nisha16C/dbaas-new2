<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Database info </h6>
    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Database Name & ID </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Database Type &
                Versions</th>

              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Provider Name
              </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Created On</th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Updated On</th>

              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(cluster, index) in clusters" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <!-- You can customize the image source or remove it based on your needs -->
                    <img src="../../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="clusterImage" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ cluster.id }}</h6>
                    <p class="text-xs text-secondary mb-0">{{ cluster.cluster_name }}</p>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">{{ cluster.cluster_type }}</p>
                <p class="text-xs text-secondary mb-0">{{ cluster.database_version }}</p>
              </td>
              <td class="align-middle text-center text-sm">
                <!-- Assuming 'provider' is a property in your cluster data -->
                <span class="badge badge-sm bg-gradient-success">{{ cluster.provider }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(cluster.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(cluster.updated_date) }}</span>
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

<script>
import axios from "axios";

export default {
  name: "authors-table",
  data() {
    return {
      clusters: [], // Initialize clusters as an empty array
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchClusters();
  },
  methods: {
    async fetchClusters() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get('http://172.16.1.97:8002/api/v2/cluster/');
        
        // Update the clusters data with the fetched data
        this.clusters = response.data;
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
