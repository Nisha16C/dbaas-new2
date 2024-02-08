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
                <div class="px-4">
                  <div class="mb-3 mt-4">
                    <router-link to="/cluster-create">
                      <argon-button color="success" size="md" variant="gradient"
                        >Create New Cluster</argon-button
                      >
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <clusters-table :clusters="clusterData" />
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
import ClustersTable from "@/views/components/ClusteruserTable.vue";
import ArgonButton from "@/components/ArgonButton.vue";


import axios from "axios";
export default {
  name: "Cluster",
  components: {
    Card,
    ClustersTable,
    ArgonButton,
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    // this.fetchProjects();
    this.fetchClusters();
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Clusters",
          value: '',
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "Till Today",
          iconBackground: "bg-gradient-primary",
        },
      },
      clusterData: [], user_id: '',
    };
  },
  methods:{
    fetchClusters() {
      axios.get(`http://172.16.1.97:8002/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusterData = response.data;
          console.log(response.data);
          this.stats.money.value = this.clusterData.length
          // this.loading = false;
        });
    },
  }
};
</script>
