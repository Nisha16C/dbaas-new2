[11:55 AM] Nisha Chaurasiya
<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Database info </h6>
    </div>
    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
 
    <div v-else class="card-body px-0 pt-0 pb-2">
      <div v-if="clusters.length === 0" class="text-center">No Cluster found in the Selected Project</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Database Name & ID </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Database Type &
                Versions</th>
 
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Provider Name
              </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Created On</th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Updated On</th>
 
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
 
          <tbody>
            <tr v-for="(cluster, index) in clusters" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <!-- You can customize the image source or remove it based on your needs -->
                    <img :src="
            this.$store.state.darkMode ||
            this.$store.state.sidebarType === 'bg-default'
              ? logoWhite
              : logo"
               class="avatar avatar-sm me-3" alt="clusterImage" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ cluster.id }}</h6>
                    <p class="text-xs text-secondary mb-0">{{ cluster.cluster_name }}</p>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">{{ cluster.cluster_type }}</p>
                <p class="text-xs text-secondary mb-0">{{ cluster.database_version }}</p>
                <p class="text-xs text-secondary mb-0">{{ cluster.backup_method  }}</p>
              </td>
              <td class="align-middle text-center text-sm">
                <!-- Assuming 'provider' is a property in your cluster data -->
                <span class="badge badge-sm bg-gradient-success">{{ cluster.provider }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(cluster.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(cluster.updated_date) }}</span>
              </td>
              <td class="align-middle">
             
              <argon-button color="success" size="md" variant="gradient" @click="viewCluster(cluster.cluster_name)" type="button"
                class="btn btn-danger" data-toggle="modal" data-target="#viewModal">
                View
              </argon-button>
              <argon-button color="danger" size="md" variant="gradient" @click="prepareDelete(cluster.cluster_name, cluster.provider)" type="button"
                class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                Delete
              </argon-button>
            </td>
            </tr>
          </tbody>
 
        </table>
      </div>
    </div>
  </div>
  
 
  <div class="modal fade" id="viewModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
  aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content"  :class="{ 'dark-mode': isDarkMode }" >
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Cluster Details</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <h3>{{ clusterName }}</h3>
        <p v-if="contentList.length > 0" v-html="addLineBreaks(contentList[0].content)"></p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        
      </div>
    </div>
  </div>
</div>
<!-- Delete Modal -->
<div v-show="deleteModal" class="modal fade" id="exampleModal" tabindex="-1" role="dialog"
    aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content"  :class="{ 'dark-mode': isDarkMode }" >
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Delete Cluster</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          Are You Sure Want to delete cluster "{{ deleteClusterName }}" !!
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button @click="deleteCluster()" type="button" data-dismiss="modal" class="btn btn-danger"> Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>
 
<script>
import axios from "axios";
import ArgonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/db-png.png";
import logoWhite from "@/assets/img/logo3.png";
 
export default {
  name: "UserCluster-table",
  components: {
 
  ArgonButton,
},
data(){
  return{
      apiUrl: API_ENDPOINT,
      contentList: [],
      deleteClusterName: '',
      selectedProvider: '',
      provider_info: '',
      loading: true,
      logo,
      logoWhite
  }
},
  props: {
  clusters: {
    type: Array,
    required: true,
  },
},
 
computed: {
  isDarkMode() {
    return this.$store.state.darkMode;
  }
},
 
created() {
    this.Username = sessionStorage.getItem('username');
    this.user_id = sessionStorage.getItem('user_id');
    this.fetchclusters_list(); // Fetch clusters on component creation
    // this.fetchComputeOfferings();
  },
methods: {
 
  prepareDelete(clusterName, provider_name) {
    this.deleteClusterName = clusterName;
    this.selectedProvider = provider_name
 
    
  },
  deleteCluster() {
    
 
    console.log('Deleting cluster with name:', this.deleteClusterName);
 
    axios
        .get(`${this.apiUrl}/api/v3/providers/by-username-and-name/${this.Username}/${this.selectedProvider}/`)
        .then((response)=>{
          this.provider_info = response.data;
          
          const formData = {
            cluster_name: this.deleteClusterName,
            provider_name: this.selectedProvider,
            provider_endpoint: this.provider_info.provider_url,
            provider_access_token: this.provider_info.access_token,
            provider_secret_key: this.provider_info.secret_key,
            kubeconfig_data: this.provider_info.kubeconfig_data,
 
          };
          this.$router.push('/delete');
          axios.post(`${this.apiUrl}/api/v2/deletecluster/`, formData)
           .then(response => {
        console.log('Cluster deleted successfully:', response.data);
 
        this.fetchclusters_list();
 
      })
      .catch(error => {
        console.error('Error deleting cluster:', error);
        // Handle error, show a message, etc.
        this.toggleModal1();
      });
        })       
    },
  viewCluster(clusterName) {
    this.clusterName=clusterName;
    axios.get(`${this.apiUrl}/api/v2/result/content/${clusterName}/`)
      .then(response => {
        this.contentList = response.data;
        console.log(this.contentList);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    },
    addLineBreaks(text) {
    const formattedContent = text.replace(/([^:\n]+):/g, '<h class="text-sm text-purple-600">$1</h>:');
    return formattedContent.replace(/\n/g, '<br>');
    // Replace '\n' with '<br>' for rendering line breaks in HTML
    // return text.replace(/\n/g, '<br>');
  },
 
  async fetchclusters_list() {
    try {
      // Make a GET request to the endpoint
      const response = await axios.get(`${this.apiUrl}/api/v2/cluster/`);
 
      // Update the clusters_list data with the fetched data
      this.clusters_list = response.data;
      this.loading = false ;
    } catch (error) {
      console.error('Error fetching clusters_list:', error);
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
.dark-mode { /* Define dark mode styles */
  background-color: #1d1e52;
  color: #ffffff;
}
</style>