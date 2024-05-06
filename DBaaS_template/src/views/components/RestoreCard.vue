<template>
  <div class="card">
    <div v-if="successMessage" class="alert alert-success mb-3">
      <!-- Show success message when backup is completed -->
      <div class="text-center">
        {{ successMessage }}
      </div>
    </div>
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Database Name and Restore Backup.</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li class="list-group-item border-0 p-4 mb-2 bg-gray-100 border-radius-lg">
          <div v-if="loading" class="text-center">
            <!-- Show loader while loading -->
            <h6 class="mb-2">
              Restore in progress...
            </h6>
            <div class="spinner-border spinner-border-lg p-3 text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>

          <div class="d-flex">
            <div class="d-flex flex-column">
              <h6 class="mb-3 text-sm">Database and Backup ID</h6>
              <form>

                <label class="mt-3 text-sm">Storage Provider</label>
                <select :class="{ 'BGdark': isDarkMode }" class="form-select " aria-label="Default select example"
                  v-model="backup_method" @click="fetchServers()">
                  <option value="nfs">NFS</option>
                  <option value="s3">S3</option>
                </select>

                <label class="mt-3 text-sm">Cluster Name</label>
                <select :class="{ 'BGdark': isDarkMode }" v-model="serverName" class="form-select"
                  @click="fetchBackups()" aria-label="Default select example">
                  <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{
      serverName }}
                  </option>

                </select>

                <div class="form-group mt-3">
                  <label class="text-sm" for=""> Backup ID</label>
                  <select :class="{ 'BGdark': isDarkMode }" v-model="backup_id" class="form-select"
                    aria-label="Default select example">
                    <option v-for="backup in backupList[serverName]" :key="backup.backup_id" selected>{{
      backup.backup_id }}
                    </option>

                  </select>
                </div>


                <!-- <div class="form-group mt-3">
                  <label class="text-sm" for="">Destination Directory</label>
                  <bb-input type="email" class="" id="Postgres_Username" placeholder="Destination directory"
                    v-model="destination_dir" />
                </div> -->
                <div class="form-group mt-3">
                  <label class="text-sm" for="targetClusterName">Target Cluster Name</label>
                  <select :class="{ 'BGdark': isDarkMode }" v-model="serverNames" class="form-select"
                    @click="fetchServerNames()" aria-label="Default select example">
                    <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{
                      serverName }}
                    </option>

                  </select>
                </div>



              </form>
            </div>
          </div>
        </li>
      </ul>
      <div class="px-2">
        <argon-button @click="Restore()" color="success" size="md" variant="gradient">
          Restore Backup
        </argon-button>
      </div>
    </div>
  </div>
</template>

<script>
import argonButton from "@/components/BB_Button.vue";
// import bbInput from "@/components/BB_Input.vue";


import axios from "axios";
export default {
  name: "backup-card",
  components: {
    argonButton,
    // bbInput
  },
  data() {
    return {
      servers: [],
      serverName: '',
      serverNames: '',
      backup_id: '',
      username: '',
      destination_dir: '',
      target_server: '',
      backupList: [],
      loading: false, // Track loading state
      successMessage: "", // Success message
    };
  },
  created() {
    this.username = sessionStorage.getItem('username');
    this.fetchServerNames(); // Call the method to fetch server names

  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },
  methods: {
    async fetchServerNames() {
      try {
        const response = await axios.get(`http://172.16.1.131:8000/api/v4/barman/list-servers?storage_method=${this.backup_method}&username=${this.username}`);
        this.servers = response.data.message; // Assuming the response contains an array of server objects with a 'name' property
      } catch (error) {
        console.error('Error fetching server names:', error);
      }
    },
    async fetchServers() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`http://172.16.1.131:8000/api/v4/barman/list-servers?storage_method=${this.backup_method}&username=${this.username}`);

        // Update the clusters data with the fetched data
        this.servers = response.data.message;
      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },
    async fetchBackups() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`http://172.16.1.131:8000/api/v4/barman/list-backups?server_name=${this.serverName}&storage_method=${this.backup_method}&username=${this.username}`);
        this.backupList = response.data.message;
      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },
    Restore() {
      this.loading = true;
      axios
        .post(`http://172.16.1.131:8000/api/v4/barman/recover?server_name=${this.serverName}&backup_id=${this.backup_id}&destination_directory=${this.destination_dir}&target_server_name=${this.target_server}&storage_method=${this.backup_method}&username=${this.username}`,)
        .then(() => {

          this.successMessage = "Backup restored successfully"; // Set success message
          setTimeout(() => {
            this.$router.push("/admin-backup"); // Redirect after 5 seconds
          }, 5000);
        })
        .catch(() => {

        })
        .finally(() => {
          this.loading = false; // Set loading to false regardless of success or failure
        });
    },


  },
};
</script>

<style scoped>
.BGdark {
  background-color: #1d1e52;
  color: #fff;

}
</style>
