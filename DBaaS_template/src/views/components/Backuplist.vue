<template>
  <div class="card">
    <div class="card-header pb-0 d-flex">
      
        <h6 class=""> Server List </h6>
      
      <div class="col-lg-5">
        <div class="d-flex">
          <label class="text-sm  col-sm-3">Backup Method :</label>
          <select @click="fetchServers()" class="form-select col-sm-5 mb-2" aria-label="Default select example"
            v-model="backup_method">
            <option value="nfs">nfs</option>
            <option value="s3">s3</option>
          </select>
        </div>
        </div>
      <div class="col-lg-6">
        <router-link to="/scheduled-backups" class="text-xl text-success font-weight-bold">
         See Scheduled Backups Lists
        </router-link>
      </div>
    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary  font-weight-bolder opacity-7">Server Name</th>
              <th class="text-uppercase text-secondary  font-weight-bolder opacity-7"> View Backups</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(description, serverName) in servers" :key="serverName">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img src="../../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ serverName }}</h6>
                    <p class="text-xs text-secondary mb-0"></p>
                  </div>
                </div>
              </td>
              <td class="align-middle ">
                <argon-button color="success" size="md" variant="gradient"  @click="viewServer(serverName)" type="button"
                  class="btn btn-danger" data-toggle="modal" data-target="#viewModal">
                  View
                </argon-button>
                <!-- <a href="javascript:;" class="text-secondary font-weight-bold text-xs" data-toggle="tooltip"
                  data-original-title="View server" @click="viewServer(serverName)">View</a> -->
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
import ArgonButton from '@/components/ArgonButton.vue';
export default {
  name: "server-table",
  components:{
    ArgonButton

  },
  data() {
    return {
      servers: [],
      serverName: '', // Initialize clusters as an empty array
      backup_method: 'nfs',
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
        const response = await axios.get(`http://172.16.1.69:8000/api/v4/barman/list-servers/?storage_method=${this.backup_method}`);

        // Update the clusters data with the fetched data
        this.servers = response.data.message;
        console.log(this.servers);
      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },
    viewServer(serverName) {
      console.log(serverName)
      this.serverName = serverName
      // Navigate to another component with the server name
      this.$router.push({ name: 'BackupDetails', params: { serverName } });

    }
  },
};
</script>

  