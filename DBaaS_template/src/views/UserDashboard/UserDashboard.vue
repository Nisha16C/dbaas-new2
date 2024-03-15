<template>
  <!-- Nav and sidenav -->

  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.project.title"
              :value="stats.project.value"
              :percentage="stats.project.percentage"
              :iconClass="stats.project.iconClass"
              :iconBackground="stats.project.iconBackground"
              :detail="stats.project.detail"
              directionReverse
            ></card>
          </div>

          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.cluster.title"
              :value="stats.cluster.value"
              :percentage="stats.cluster.percentage"
              :iconClass="stats.cluster.iconClass"
              :iconBackground="stats.cluster.iconBackground"
              :detail="stats.cluster.detail"
              directionReverse
            ></card>
          </div>
        </div>

        <div class="row mt-4">
          <div class="col-lg-14 mb-lg-0 mb-4">
            <div class="card">
              <div class="card-header">Welcome {{ getUsername() }}!!</div>
              <div class="card-body">
                <h5 class="card-title">
                  Empower Your Data Journey with BitBlast!!
                </h5>
                <p class="card-text">
                  Experience the transformational power of BitBlast as it
                  propels your data journey forward!
                </p>
                <router-link to="/cluster-create">
                      <argon-button color="success" size="md" variant="gradient"
                        >Create New Cluster</argon-button
                      >
                </router-link>
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
// import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
// import Carousel from "./components/Carousel.vue";
import ArgonButton from "@/components/ArgonButton.vue";
import axios from 'axios'
// import CategoriesCard from "./components/CategoriesCard.vue";

export default {
  name: "user-dashboard",
  data() {
    return {
      stats: {
        project: {
          title: "All Project",
          value: "",
          percentage: "",
          iconClass: "ni ni-project-coins",
          detail: " ",
          iconBackground: "bg-gradient-primary",
        },
        cluster: {
          title: "All Clusters",
          value: "",
          percentage: "",
          iconClass: "ni ni-world",
          iconBackground: "bg-gradient-danger",
          detail: " ",
        },
      },
  clusterData: [],
  username: "",

    };
  },
  components: {
    Card,
    ArgonButton,
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.getProject();
    this.getCluster();
    this.username = sessionStorage.getItem("username");
  },

  methods:{
    getUsername(){
      return this.username || "User";
    },
    getCluster(){
 
      axios.get(`http://172.16.1.190:8002/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
    
          this.stats.cluster.value =  response.data.length.toString();
          
        });

    },
    getProject(){
      axios.get(`http://172.16.1.190:8002/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.stats.project.value = response.data.length.toString();
          console.log(response.data.length.toString);
        })
        .catch(error => {
          console.error("Error fetching project count:", error);
        });
    }
  }
};
</script>
