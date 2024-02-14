<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Server Name and Restore Backup.</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li
          class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
        >
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Server and Backup id</h6>
            <form>
              <label class="mb-3 text-sm">Database Name</label>
              <select v-model="serverName" class="form-select"  @click="fetchBackups()" aria-label="Default select example">
              <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{ serverName }}
              </option>

            </select>
           
              <div class="form-group mt-3">
                <label class="text-sm" for=""> Backup id</label>
                <select v-model="backup_id" class="form-select" aria-label="Default select example">
              <option v-for="backup in backupList[serverName]" :key="backup.backup_id" selected>{{ backup.backup_id }}
              </option>

            </select>
              </div>


              <div class="form-group mt-3">
                <label class="text-sm" for="">Destination Directory</label>
                <input
                  type="email"
                  class="form-control"
                  id="Postgres_Username"
                  placeholder="Destination directory"
                  v-model="destination_dir"
                />
              </div>
              <div class="form-group mt-3">
                <label class="text-sm" for=""> Target server Name</label>
                <select v-model="target_server" class="form-select" aria-label="Default select example">
              <option v-for="(description, serverName) in servers" :key="serverName" :value=serverName selected>{{ serverName }}
              </option>

            </select>
            </div>

          
            </form>
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
      backup_id:'',
      destination_dir:'',
      target_server:'',
      backupList:[],
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
    async fetchBackups() {
    console.log(this.serverName)
    try {
      // Make a GET request to the endpoint
      const response = await axios.get(`http://172.16.1.131:5000/barman/list-backups?server_name=${this.serverName}&storage_method=nfs`);

      // Update the clusters data with the fetched data
      this.backupList = response.data.message;
      console.log(this.backupList);
    } catch (error) {
      console.error('Error fetching servers:', error);
    }
  },
    Restore() {
      axios
        .post(`http://172.16.1.131:5000/barman/recover?server_name=${this.serverName}&backup_id=${this.backup_id}&destination_directory=${this.destination_dir}&target_server_name=${this.target_server}&storage_method=nfs`, )
        .then((response) => {
          console.log(response)
          console.log("Backup done successfully");
        })
        .catch((error) => {
          console.log(error);

        });

    },

  },
};
</script>
