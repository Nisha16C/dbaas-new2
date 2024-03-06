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

          <!-- <div class="col-lg-3 col-md-12 col-12 mx-auto ">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class="px-4">
                  <div class="mb-2 mt-2">
                    <select class="form-select" aria-label="Default select example">
                      <option selected>All Projects</option>
                      <option value="1">First Projects</option>
                      <option value="2">Second project</option>
                      <option value="3">Third project</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div> -->
          


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
    this.fetchProjects();
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
      axios.post("http://172.16.1.56:8002/api/v2/deletecluster/", formData)
        .then(response => {
          console.log('Cluster deleted successfully:', response.data);
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
      axios.get(`http://172.16.1.56:8002/api/v2/result/content/${clusterName}/`)
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
 
    async fetchclusters_list() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get('http://172.16.1.56:8002/api/v2/cluster/');
 
        // Update the clusters_list data with the fetched data
        this.clusters_list = response.data;
      } catch (error) {
        console.error('Error fetching clusters_list:', error);
      }
    },
 
    fetchProjects() {
      axios.get(`http://172.16.1.56:8002/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects = response.data;
 
        });
    },
    fetchClusters() {
      axios.get(`http://172.16.1.56:8002/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusters = response.data;
          this.loading = false;
        });
    },
    fetchClustersByProject() {
      if (this.selectedProject) {
        axios.get(`http://172.16.1.56:8002/api/v2/cluster/project/${this.selectedProject}/`)
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
 