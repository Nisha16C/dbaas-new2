<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Server List </h6>
    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Server Name</th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr  v-for="(description, serverName) in servers" :key="serverName">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img
                      src="../../assets/img/db-png.png"
                      class="avatar avatar-sm me-3"
                      alt="user1"
                    />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ serverName }}</h6>
                    <p class="text-xs text-secondary mb-0"></p>
                  </div>
                </div>
              </td>
              <td class="align-middle">
                <a
                href="javascript:;"
                class="text-secondary font-weight-bold text-xs"
                data-toggle="tooltip"
                data-original-title="View server"
                @click="viewServer(serverName)"
              >View</a>
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
  name: "server-table",
  data() {
  return {
    servers: [],
    serverName:'', // Initialize clusters as an empty array
  };
},
mounted() {
  // Fetch data when the component is mounted
  this.fetchServers();
},
methods: {
  async fetchServers() {
    try {
      // Make a GET request to the endpoint
      const response = await axios.get('http://172.16.1.131:5000/barman/list-servers?storage_method=nfs');
      
      // Update the clusters data with the fetched data
      this.servers = response.data.message;
      console.log(this.servers);
    } catch (error) {
      console.error('Error fetching servers:', error);
    }
  },
  viewServer(serverName) {
    console.log(serverName)
    this.serverName=serverName
    // Navigate to another component with the server name
    this.$router.push({ name: 'BackupDetails', params: { serverName } });
  
  }
},
};
</script>

