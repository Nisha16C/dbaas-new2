<template>
    <div class="card">
      <div class="card-header pb-0 ">
        
          <h6 class=""> Server List </h6>
       
        
      </div>
  
      <div class="card-body px-0 pt-0 pb-2">
        <div class="table-responsive p-0">
          <table class="table align-items-center mb-0">
            <thead>
              <tr>
                <th class="text-secondary opacity-7 align-middle">Server Name</th>
                <th class="text-secondary opacity-7 ">Retention Period</th>
                <th class="text-secondary opacity-7">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="backup in backups" :key="backup.id">
                <td>
                  <div class="d-flex px-2 py-1">
                    <div>
                      <img src="../../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                    </div>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">{{ backup.server_name }}</h6>
                    </div>
                  </div>
                </td>
                <td class="align-middle">
                    <div class="">
                      <h6 class="mb-0 text-sm">{{ backup.retention_period }}</h6>
                    </div>
                </td>
                <td class="align-middle">
                  <a href="javascript:;" class="text-secondary font-weight-bold " data-toggle="tooltip"
                    data-original-title="View server">Change</a>
                    <a href="javascript:;" class="text-secondary font-weight-bold ml-3" data-toggle="tooltip"
                    data-original-title="View server">Unschedule</a>
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
        backups: [],
        serverName: '', // Initialize clusters as an empty array
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
          const response = await axios.get(`http://172.16.1.131:5000/barman/scheduled-servers`);
  
          // Update the clusters data with the fetched data
          this.backups = response.data.message;
          console.log(this.backups);
        } catch (error) {
          console.error('Error fetching servers:', error);
        }
      },

      Unschedule() {
      axios
        .post(`http://172.16.1.131:5000/barman/backup?server_name=${this.serverName}&backup_name=${this.backup_name}&storage_method=${this.backup_method}`,)
        .then((response) => {
          console.log(response)
          console.log("Backup done successfully");
          this.$router.push('/admin-backup');
        })
        .catch((error) => {
          console.log(error);

        });

    },
      
    },
  };
  </script>
  
    