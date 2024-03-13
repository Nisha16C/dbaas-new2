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
                  <scheduleList />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import scheduleList from "./components/scheduleList.vue";
  import ArgonButton from "@/components/ArgonButton.vue";
  
  export default {
    name: "Cluster",
    components: {
      scheduleList,
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
            detail: "",
            iconBackground: "bg-gradient-primary",
          },
        },
      };
    },
  };
  </script>
  
