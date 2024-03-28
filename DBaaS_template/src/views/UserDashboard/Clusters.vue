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
          


          <div class="col-lg-3 col-md-12 col-12  ">
    <div class="mb-4 card">
        <div class="p-3 card-body">
            <div class="px-4">
              <div class="mb-2 mt-2">
                <!-- Update the option for "All Projects" to call fetchClusters() -->
                <select :class="{ 'BGdark': isDarkMode }" class="form-select" v-model="selectedProject" @change="fetchClustersByProject">
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
            <div class="mb-4 card">
              <div class="card-body px-0 pt-0 pb-2">
                <div class="text-center"  style= "height: 100px;" v-if="clusters.length === 0">
                  <span class="text-gray-400 text-2xl mt-5">No Cluster found in the Selected Project</span>
                </div>

                <div v-else class="table-responsive p-0">
                  <clusters-table :clusters="clusterData" />
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
import Card from "@/examples/Cards/Card.vue";
import ClustersTable from "@/views/components/ClusteruserTable.vue";
import argonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';

 
 
import axios from "axios";
export default {
  name: "Cluster",
  components: {
    Card,
    ClustersTable,
    argonButton,
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.fetchProjects();
    this.fetchClusters();
 
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    }
  },
  data() {
    return {
      apiUrl: API_ENDPOINT, 
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
      clusterData: [], 
      user_id: '',
      selectedProject: "", // New property to store the selected project ID
      projects: [], 
      contentList: [],
      deleteClusterName: '',
      clusterName: '',
      selectedCluster: '',
      
 
 
 
      clusters: {
        type: Array,
        required: true,
      },
      deleteModal: false,
      viewModal: false
    };
  },
  methods: {
    prepareDelete(clusterName) {
      this.deleteModal = true
      this.deleteClusterName = clusterName;
 
    },
    deleteCluster() {
 
      const formData = {
        cluster_name: this.deleteClusterName
      };
 
      this.$router.push('/delete');
      axios.post(`${this.apiUrl}/api/v2/deletecluster/`, formData)
        .then(() => {
          this.deleteModal = false
          this.fetchclusters_list();
        })
        .catch(error => {
          console.error('Error deleting cluster:', error);
          this.toggleModal1();
        });
    },
 
    viewCluster(clusterName) {
      this.clusterName = clusterName;
      axios.get(`${this.apiUrl}/api/v2/result/content/${clusterName}/`)
        .then(response => {
          this.contentList = response.data;
 
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    addLineBreaks(text) {
      const formattedContent = text.replace(/([^:\n]+):/g, '<h class="text-sm fw-bolder">$1</h>:');
      return formattedContent.replace(/\n/g, '<br>');
 
    },
 
   
 
    fetchProjects() {
      axios.get(`${this.apiUrl}/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects = response.data;
 
        });
    },
    fetchClusters() {
      axios.get(`${this.apiUrl}/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusterData = response.data;
          this.stats.money.value = this.clusterData.length

          this.loading = false;
        });
    },
    fetchClustersByProject() {
      if (this.selectedProject) {
        axios.get(`${this.apiUrl}/api/v2/cluster/project/${this.selectedProject}/`)
          .then(response => {
            this.clusters = response.data;
          });
      } else {
        this.fetchClusters();
      }
    },
    toggleModal1: function () {
      this.showModal = !this.showModal;
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
  }
};
</script>

<style scoped>
    .custom-right-align {
        direction: rtl;
        text-align: right;
    }
.BGdark {
  background-color: #1d1e52;; /* Choose your dark mode background color */
  color: #fff; /* Choose your dark mode text color */
}

</style>

 