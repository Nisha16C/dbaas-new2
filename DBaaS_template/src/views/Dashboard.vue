<template>
  <!-- Nav and sidenav -->

  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.project.title" :value="stats.project.value" :percentage="stats.project.percentage"
              :iconClass="stats.project.iconClass" :iconBackground="stats.project.iconBackground"
              :detail="stats.project.detail" directionReverse></card>
          </div>

          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.cluster.title" :value="stats.cluster.value" :percentage="stats.cluster.percentage"
              :iconClass="stats.cluster.iconClass" :iconBackground="stats.cluster.iconBackground"
              :detail="stats.cluster.detail" directionReverse></card>
          </div>

          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.user.title" :value="stats.user.value" :percentage="stats.user.percentage"
              :iconClass="stats.user.iconClass" :iconBackground="stats.user.iconBackground" :detail="stats.user.detail"
              directionReverse></card>
          </div>
        </div>

        <!-- <div class="row mt-4">
          <div class="col-lg-14 mb-lg-0 mb-4">
            <div class="card">
              <div class="p-3 pb-0 card-header">
                <div class="d-flex justify-content-between">
                  <h6 class="mb-2">See all Details</h6>
                </div>
              </div>
           
              <div class="table-responsive">
                <table class="table align-items-center">
                  <tbody>
                    <tr v-for="(sale, index) in sales" :key="index">
                      <td class="w-30">
                        <div class="px-2 py-1 d-flex align-items-center">
                          <div>
                            <img alt="img" /> 
                          </div>
                          <div class="ms-4">
                            <p class="mb-0 text-xs font-weight-bold">Name:</p>
                            <h6 class="mb-0 text-sm">{{ sale.country }}</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Count:</p>
                          <h6 class="mb-0 text-sm">{{ sale.sales }}</h6>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Value:</p>
                          <h6 class="mb-0 text-sm">{{ sale.value }}</h6>
                        </div>
                      </td>
                    <td class="text-sm align-middle">
                          <div class="text-center col">
                            <p class="mb-0 text-xs font-weight-bold">Bounce:</p>
                            <h6 class="mb-0 text-sm">{{ sale.bounce }}</h6>
                          </div>
                        </td> 
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="col-lg-5">
             <categories-card /> 
          </div>
        </div> -->
        <div class="row mt-4">
          <div class="col-lg-14 mb-lg-0 mb-4">
            <div class="card">
              <div class="card-header">Welcome Admin</div>
              <div class="card-body">
                <h5 class="card-title">
                  Empower Your Data Journey with BitBlast!!
                </h5>
                <p class="card-text">
                  Experience the transformational power of BitBlast as it
                  propels your data journey forward!
                </p>

              </div>
            </div>
          </div>
          <div class="col-lg-5">
            <!-- <categories-card /> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Card from "@/examples/Cards/Card.vue";
import axios from "axios";

export default {
  name: "user-dashboard",
  data() {
    return {
      stats: {
        cluster: {
          title: "All Clusters",
          value: " ",
          percentage: "",
          iconClass: "ni ni-world",
          iconBackground: "bg-gradient-danger",
          detail: "Till Today",
        },
        user: {
          title: "All Users",
          value: " ",
          percentage: "",
          iconClass: "ni ni-world",
          iconBackground: "bg-gradient-danger",
          detail: "Till Today",
        },
        project: {
        title: "All Projects",
        value: " ",
        percentage: " ",
        iconClass: "ni ni-money-coins",
        detail: "Till Today",
        iconBackground: "bg-gradient-primary",
      },

      },
      sales: {
        us: {
          country: "Projects",
          sales: 12,
          value: "$20",
          bounce: "29.9%",
        },
        germany: {
          country: "Clusters",
          sales: "23",
          value: "$44",
          bounce: "40.22%",
        },
        britain: {
          country: "Users",
          sales: "23",
          value: "$19",
          bounce: "23.44%",
        },
        brasil: {
          country: "Providers",
          sales: "6",
          value: "$14",
          bounce: "32.14%",
        },
      },
    };
  },
  components: {
    Card,
    // GradientLineChart,

    // CategoriesCard,
  },

  methods: {
    // Method to fetch clusters and update stats.cluster.value
    fetchClusters() {
      axios.get(`http://172.16.1.97:8002/api/v2/cluster/`)
        .then(response => {
          this.stats.cluster.value = response.data.length.toString();  // Update stats.cluster.value
        })
        .catch(error => {
          console.error('Error fetching clusters:', error);
        });
    },
    fetchUsers(){
      axios.get(`http://172.16.1.97:8002/api/v1/users/`)
        .then(response => {
          this.stats.user.value = response.data.length.toString();  // Update totalClusters
        })
        .catch(error => {
          console.error('Error fetching users:', error);
        });
    },
    fetchProjectCount() {
      // Make an API request to get the project count
      axios.get(`http://172.16.1.97:8002/api/v2/project/`)
        .then(response => {
          this.stats.project.value = response.data.length.toString();
        })
        .catch(error => {
          console.error("Error fetching project count:", error);
        });
    },
  },
  created() {
    // Fetch clusters when the component is created
    this.fetchClusters();
    this.fetchProjectCount();
    this.fetchUsers();
  },

};
</script>
