<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          

          <div class="col-lg-3 col-md-12 col-12 d-flex">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class=" px-4 d-flex">
                  <div class="mb-3 mt-4 mx-2">
                    <router-link to="/admin-backup/form">
                      <argon-button color="success" size="md" variant="gradient">Backup/Schedule</argon-button>
                    </router-link>
                  </div>
                  <div class="mb-3 mt-4 mx-2">
                    <router-link to="/admin-backup/restore-backup">
                      <argon-button color="success" size="md" variant="gradient">Restore</argon-button>
                    </router-link>
                  </div>
                  
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-12 col-12 d-flex">
                        <div class="mb-4 card">
                            <div class="p-3 card-body">
                                <div class=" px-3 d-flex">
                                    <div class="mb-3 mt-4 mx-1">
                                        <router-link to="/admin-backup">
                                            <argon-button color="success" size="md" variant="gradient">Backups
                                                List</argon-button>
                                        </router-link>
                                    </div>
                                    <div class="mb-3 mt-4 mx-1">
                                        <router-link to="/scheduled-backups">
                                            <argon-button color="success" size="md" variant="gradient">Schedule Backups
                                                List</argon-button>
                                        </router-link>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h6> Backup List</h6>
                  </div>


                  <div class="card-body px-0 pt-0 pb-2">
                    <div class="pl-4">
                      <h6>{{ serverName }}</h6>
                    </div>
                    <div class="table-responsive p-0">
                      <table class="table align-items-center mb-0">
                        <thead>
                          <tr>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Backup Id
                            </th>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Backup Name</th>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Status</th>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Time</th>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7">Size</th>
                          </tr>
                        </thead>
                        <tbody v-for="backup in backupList[serverName]" :key="backup.backup_id">
                          <tr >
                            <td>
                              <div class="d-flex px-2 py-1">
                                <div>
                                  <img src="../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                                </div>
                                <div class="d-flex flex-column justify-content-center">
                                  <h6 class="mb-0 text-sm">{{ backup.backup_id }}</h6>
                                  <p class="text-xs text-secondary mb-0"></p>
                                </div>
                              </div>
                            </td>
                            <td class="align-middle pl-4">
                              {{backup.backup_name}}
                            </td>
                            <td class="align-middle">
                              {{backup.status}}
                            </td>
                            <td class="align-middle">
                              {{backup.end_time}}
                            </td>
                            <td class="align-middle">
                              {{backup.size}}
                            </td>
                          </tr>

                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>

import axios from "axios";
import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "BackupDetails",
  props: {
    serverName: {
      type: String,
      required: true
    }
  },
  components: {
    ArgonButton
  },
  
  data() {
    return {
      backupList:[],
      backup_method: '',
      username:'',
      stats: {
        money: {
          title: "All Backups",
          value: "2",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchBackupMethod();
    this.fetchBackups();

  },
  created() {
    this.username = sessionStorage.getItem('username');
  },
  methods: {

    async fetchBackupMethod() {
     
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`${this.apiUrl}/api/v2/get_backup_method/${this.server_name}/`);

        // Update the clusters data with the fetched data
        this.backup_method = response.data.backup_method;
        console.log(this.backup_method);
      } catch (error) {
        console.error('Error fetching backup-method:', error);
      }
    },
    async fetchBackups() {
      console.log(this.serverName)
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`http://172.16.1.131:8000/api/v4/barman/list-backups?server_name=${this.serverName}&storage_method=${this.backup_method}&username=${this.username}`);

        // Update the clusters data with the fetched data
        this.backupList = response.data.message;
        console.log(this.backupList);
      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },

  },
};
</script>
  
