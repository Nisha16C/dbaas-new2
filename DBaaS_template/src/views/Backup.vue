<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.money.title"
              :value="stats.money.value"
              :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass"
              :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail"
              directionReverse
            >
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
import Card from "@/examples/Cards/Card.vue";
import Backuplist from "./components/Backuplist.vue";
import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "Cluster",
  components: {
    Card,
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
