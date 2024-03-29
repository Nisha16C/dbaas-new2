<template>
  <div class="card">
    <div v-if="successMessage" class="alert alert-success mb-3">
      <!-- Show success message when backup is completed -->
      {{ successMessage }}
    </div>
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Database Name and Backup Name.</h6>
    </div>
    <div class="card-body pt-4 p-3">

      <ul class="list-group">
        <li class="list-group-item border-0  p-4 mb-2 bg-gray-100 border-radius-lg">

          <div v-if="loading" class="text-center">
            <!-- Show loader while loading -->
            <h6 class="mb-2">
              Backup in progress...
            </h6>
            <div class="spinner-border spinner-border-lg p-3 text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
          <div class="d-flex">
            <div class="d-flex flex-column">
              <form>

                <label class="mt-1 text-sm">Backup Method</label>
                <select :class="{ 'BGdark': isDarkMode }" class="form-select" aria-label="Default select example" v-model="backup_method"
                  @click="fetchServers()">
                  <option value="nfs">NFS</option>
                  <option value="s3">S3</option>
                </select>

                <label class="mt-3 text-sm">Select Database</label>
                <select :class="{ 'BGdark': isDarkMode }" v-model="serverName" class="form-select" aria-label="Default select example">
                  <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{
                    serverName }}
                  </option>

                </select>

                <div v-show="!isBackupScheduled" class="form-group mt-3">
                  <label class="text-sm" for="">Backup Name</label>
                  <bb-input v-model="backup_name" type="email" class="" id="backup_name"
                    placeholder="Backup Name" />
                </div>


                <div>
                  <div class="form-check form-switch mt-3">
                    <input class="form-check-input" @click="toggleBackupSchedule()" type="checkbox">
                    <label class=" text-sm mt-2" for="backupSwitch">Schedule Backup (Optional)</label>
                  </div>

                  <div v-if="isBackupScheduled" class="form-group mt-3">
                    <label class="text-sm" for="retentionPeriod">Retention Period:</label>
                    <div class="input-group">
                      <bb-input type="email" class="" id="retentionPeriod" v-model="retentionPeriod"/>
                      <select :class="{ 'BGdark': isDarkMode }"  class="form-select bg-light" aria-label="Default select example" v-model="selected_value">
                        <option value="d" selected>days</option>
                        <option value="m">months</option>
                        <option value="y">years</option>
                      </select>

                    </div>
                  </div>
                </div>

              </form>
            </div>
          </div>
        </li>
      </ul>

      <div class="px-2">
        <argon-button v-show="!isBackupScheduled" @click="Backup()" color="success" size="md" variant="gradient">
          Create Backup
        </argon-button>
        <argon-button v-show="isBackupScheduled" @click="scheduleBackup()" color="success" size="md" variant="gradient">
          Schedule Backup
        </argon-button>
      </div>
    </div>
  </div>
</template>
 
 
<script>
import argonButton from "@/components/BB_Button.vue";
import bbInput from "@/components/BB_Input.vue";

import axios from "axios";
export default {
  name: "backup-card",
  components: {
    argonButton,
    bbInput
  },
  data() {
    return {
      servers: [],
      serverName: '',
      backup_name: '',
      isBackupScheduled: false,
      retentionPeriod: '',
      selected_value: '',
      backup_method: '',
      username: '',
      loading: false, // Track loading state
      successMessage: "", // Success message
    };
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },
  created() {
    this.username = sessionStorage.getItem('username');
  },

  methods: {
    toggleBackupSchedule() {
      this.isBackupScheduled = !this.isBackupScheduled;
      // Optionally, you can perform other actions here based on the state change.
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
    Backup() {
      this.loading = true; // Set loading to true before making the request
      axios
        .post(
          `http://172.16.1.131:8000/api/v4/barman/backup?server_name=${this.serverName}&backup_name=${this.backup_name}&storage_method=${this.backup_method}&username=${this.username}`
        )
        .then(() => {
         
          this.successMessage = "Backup done successfully"; // Set success message
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

    // Schedule backup method
    scheduleBackup() {
      this.loading = true; // Set loading to true before making the request
      axios
        .post(
          `http://172.16.1.131:8000/api/v4/barman/schedule-backup?server_name=${this.serverName}&retention=${this.retentionPeriod}${this.selected_value}&storage_method=${this.backup_method}&username=${this.username}`
        )
        .then(() => {
          this.successMessage = "Backup scheduled successfully";
          setTimeout(() => {
            this.$router.push("/scheduled-backups"); 
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
