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

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <Backuplist />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Backuplist from "./components/Backuplist.vue";
import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "Cluster",
  components: {
    Backuplist,
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
};
</script>

