<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.money.title" :value="stats.money.value" :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass" :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail" directionReverse>
            </card>
          </div>
 
          <div class="col-lg-3 col-md-12 col-12 ">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class="px-4 text-center ">
                  <div class="mb-2 mt-2  ">
                    <router-link to="/cluster-create">
                      <argon-button color="success" size="md" variant="gradient">Create New Cluster</argon-button>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-lg-3 col-md-12 col-12 mx-auto">
    <div class="mb-4 card">
      <div class="p-3 card-body">
        <div class="px-4">
          <div class="mb-2 mt-2">
            <select class="form-select" v-model="selectedProject" @change="fetchClustersByProject">
              <option value="">All Projects</option>
              <option v-for="project in projects" :key="project.id" :value="project.id">{{ project.project_name }}</option>
            </select>
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
          detail: "",
          iconBackground: "bg-gradient-primary",
        },
      },
      clusterData: [], user_id: '',
      selectedProject: "", // New property to store the selected project ID
      projects: [], 
    };
  },
  methods: {
    fetchClusters() {
      axios.get(`http://172.16.1.56:8002/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusterData = response.data;
          console.log(response.data);
          this.stats.money.value = this.clusterData.length
          
        });
    },
    fetchProjects() {
      axios.get(`http://172.16.1.56:8002/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects = response.data;
        });
    },
    // ... (your existing methods) ...
    fetchClustersByProject() {
      if (this.selectedProject) {
        axios.get(`http://172.16.1.56:8002/api/v2/cluster/project/${this.selectedProject}/`)
          .then(response => {
            this.clusterData = response.data;
          })
          .catch(error => {
            console.error('Error fetching clusters by project:', error);
          });
      } else {
        this.fetchClusters();
      }
    },
  
  }
};
</script>
 