<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.money.title" :value="stats.money.value" :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass" :iconBackground="stats.money.iconBackground" :detail="stats.money.detail"
              directionReverse>
            </card>
          </div>

          <div class="col-lg-3 col-md-12 col-12">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class="row px-4 text-center">
                  <div class="col-lg-5 mb-3 mt-4">
                    <router-link to="/admin-backup/form">
                      <argon-button color="success" size="md" variant="gradient">Backup</argon-button>
                    </router-link>
                  </div>
                  <div class="col-lg-5 mb-3 mt-4">
                    <router-link to="/admin-backup/restore-backup">
                      <argon-button color="success" size="md" variant="gradient">Restore</argon-button>
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
                    <h6> Backup List </h6>
                  </div>

                  <div class="card-body px-0 pt-0 pb-2">
                    <div class="table-responsive p-0">
                      <table class="table align-items-center mb-0">
                        <thead>
                          <tr>
                            <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Server Name
                            </th>
                            <th class="text-secondary opacity-7"></th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="(description, serverName) in servers" :key="serverName">
                            <td>
                              <div class="d-flex px-2 py-1">
                                <div>
                                  <img src="../assets/img/db-png.png" class="avatar avatar-sm me-3" alt="user1" />
                                </div>
                                <div class="d-flex flex-column justify-content-center">
                                  <h6 class="mb-0 text-sm">{{ serverName }}</h6>
                                  <p class="text-xs text-secondary mb-0"></p>
                                </div>
                              </div>
                            </td>
                            <td class="align-middle">
                              <a href="javascript:;" class="text-secondary font-weight-bold text-xs" data-toggle="tooltip"
                                data-original-title="View server" @click="viewServer(serverName)">View</a>
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
import Card from "@/examples/Cards/Card.vue";
import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "backup-details",
  components: {
    Card,
    ArgonButton
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Backups",
          value: "2",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "Till Today",
          iconBackground: "bg-gradient-primary",
        },
      },
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
        const response = await axios.get('http://172.16.1.131:5000/barman/list-servers');

        // Update the clusters data with the fetched data
        this.servers = response.data.message;
        console.log(this.servers);
      } catch (error) {
        console.error('Error fetching servers:', error);
      }
    },

  },
};
</script>
  