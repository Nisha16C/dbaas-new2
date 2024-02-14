<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Server Name and Backup Name.</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg">
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Server and Backup Name</h6>
            <form>
              <label class="mt-3 text-sm">Server Name</label>
              <select v-model="serverName" class="form-select" aria-label="Default select example">
                <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{
                  serverName }}
                </option>

              </select>

              <div class="form-group mt-3">
                <label class="text-sm" for="">Backup Name</label>
                <input v-model="backup_name" type="email" class="form-control" id="backup_name"
                  placeholder="Backup Name" />
              </div>

              <label class="mt-3 text-sm">Backup Method</label>
            <select class="form-select" aria-label="Default select example"
              v-model="backup_method">
              <option value="nfs">nfs</option>
              <option value="s3">s3</option>
            </select>

              <div>
                <div class="form-check form-switch mt-3">
                  <input class="form-check-input" @click="toggleBackupSchedule()" type="checkbox">
                  <label class=" text-sm mt-2" for="backupSwitch">Schedule Backup (Optional)</label>
                </div>

                <div v-if="isBackupScheduled" class="form-group mt-3">
                  <label class="text-sm" for="retentionPeriod">Retention Period:</label>
                  <div class="input-group">
                  <input type="number" class="form-control" id="retentionPeriod" v-model="retentionPeriod">
                  <span class="input-group-text bg-light px-5 font-semibold" id="days">days</span>
                  
                  </div>
                </div>
              </div>

            </form>
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
import ArgonButton from "@/components/ArgonButton.vue";

import axios from "axios";
export default {
  name: "backup-card",
  components: {
    ArgonButton,
  },
  data() {
    return {
      servers: [],
      serverName: '',
      backup_name: '',
      isBackupScheduled: false,
      retentionPeriod: '',
      backup_method:'',
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchServers();
  },
  methods: {
    toggleBackupSchedule() {
      this.isBackupScheduled = !this.isBackupScheduled;
      // Optionally, you can perform other actions here based on the state change.
    },
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
    Backup() {
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
    scheduleBackup() {
      axios
        .post(`http://172.16.1.131:5000/barman/backup?server_name=${this.serverName}&backup_name=${this.retentionPeriod}&storage_method=nfs`,)
        .then((response) => {
          console.log(response)
          console.log("Backup scheduled successfully");
          this.$router.push('/admin-backup');
        })
        .catch((error) => {
          console.log(error);

        });

    },

  },
};
</script>