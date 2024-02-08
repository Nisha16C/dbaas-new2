
<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Cluster Name and it's Password.</h6>
    </div>
   
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li
          class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
        >
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Cluster Name and Password</h6>
            <form>
              <div class="form-group">
                <label for="Cluster_Name"> Cluster Name</label>
                <input
                  class="form-control"
                  type="email"
                  id="example-text-input"
                  placeholder="Enter Your Cluster Name"
                  v-model="cluster_name"
                  @blur="checkClusterNameExists"
                />
                <!-- Error message for cluster name -->
          <div v-if="errorClusterName" class="text-danger mt-2">{{ errorClusterName }}</div>
          <!-- Error message for cluster name already exists -->
          <div v-if="errorClusterNameExists" class="text-danger mt-2">{{ errorClusterNameExists }}</div>
 
              </div>
 
              <div class="form-group">
                <label for="Postgres_Username"> Postgres Username</label>
                <input
                  type="email"
                  class="form-control"
                  id="Postgres_Username"
                  placeholder="Enter Your Postgres Username"
                  v-model="db_user"
                />
              </div>
 
              <div class="form-group">
                <label for="Cluster_Name"> Your Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="Password"
                  placeholder="Enter Your Password "
                  v-model="db_password"
                />
              </div>
            </form>
 
            <h6 class="mb-3 text-sm">Database Type and Versions</h6>
            <select class="form-select" aria-label="Default select example" @change="updateVersion" v-model="postgres_version">
              <option value="15" selected>15</option>
              <option value="14">14</option>
              <option value="13">13</option>
              <option value="12">12</option>
            </select>
            <!-- Error message for database version -->
          <div v-if="errorDatabaseVersion" class="text-red-500 mt-2">{{ errorDatabaseVersion }}</div>
 
          </div>
        </li>
      </ul>
 
      <argon-button @click="createCluster" color="success" size="md" variant="gradient">
        Create Cluster
      </argon-button>
    </div>
  </div>
</template>
 
<script>
import axios from 'axios';
import { mapState, mapActions } from 'vuex';
import ArgonButton from "@/components/ArgonButton.vue";
 
export default {
  name: "billing-card",
  components: {
    ArgonButton,
  },
  data() {
    return {
      selectedTools: [],
      postgres_version: '',
      cluster_name: '',
      project_id: '29',
      user_id: '26',
      provider_info: '',
      errorClusterName: '',
      errorDatabaseVersion: '',
      errorClusterNameExists: '',
      errorNoSelectedProject: '',
      backendError: '',
      db_user: '',
      db_password: '',Username: 'preeti'
    };
  },
 
  methods: {
    ...mapActions(['updateSelectedVersion']),
    updateVersion() {
      this.updateSelectedVersion(this.postgres_version);
    },
    // checkClusterNameExists() {
    //     // Reset error message
    //     this.errorClusterNameExists = '';
 
    //     if (!this.cluster_name) {
    //       // No need to check if the cluster name is empty
    //       return;
    //     }
 
    //     // Check if cluster name already exists
    //     axios
    //     .get(`http://172.16.1.97:8002/api/v2/cluster/check_cluster_exists/?cluster_name=${this.cluster_name}&project_id=${this.project_id}`)
    //       .then((response) => {
    //         if (response.data.exists) {
    //           // Cluster name already exists
    //           this.errorClusterNameExists = 'Cluster with the same name already exists';
    //           setTimeout(() => {
    //             this.errorClusterNameExists = '';
    //           }, 5000);
    //         }
    //       })
    //       .catch((error) => {
    //         console.log(error);
    //         // Handle errors from the cluster check API if needed
    //       });
    //   },
    createCluster() {
      // Reset error messages
      this.errorClusterName = '';
      this.errorDatabaseVersion = '';
      this.errorClusterNameExists = '';
      this.errorNoSelectedProject = '';
      this.backendError = '';
 
      if (!this.cluster_name) {
        
        this.errorClusterName = 'Cluster name is required';
        setTimeout(() => {
          this.errorClusterName = '';
        }, 5000);
        return;
      }
      if (!this.postgres_version) {
        
        this.errorDatabaseVersion = 'Postgres version is required';
        setTimeout(() => {
          this.errorDatabaseVersion = '';
        }, 5000);
        return;
      }
 
     
        if (!this.project_id) {
          console.log(this.project_id);
 
          this.errorNoSelectedProject = 'You have not selected any Project';
          setTimeout(() => {
            this.errorNoSelectedProject = '';
          }, 5000);
          return;
        }
        // this.$router.push('/result');
        axios
        .get(`http://172.16.1.97:8002/api/v3/providers/by-username-and-name/${this.Username}/${this.selectedProvider}/`)
        .then((response)=>{
          this.provider_info = response.data;
          console.log(response.data);
          const fromData = {
            db_user: this.db_user,
            db_password: this.db_password,
            user: this.user_id,
            project: this.project_id,
            provider: this.selectedProvider,
            cluster_type: this.selectedType,
            cluster_name: this.cluster_name,
            postgres_version: this.postgres_version,
            provider_endpoint: this.provider_info.provider_url,
            provider_access_token: this.provider_info.access_token,
            provider_secret_key: this.provider_info.secret_key,
          };
 
          this.$router.push('/result');
          axios
            .post(`http://172.16.1.97:8002/api/v2/cluster/`, fromData)
            .then((response) => {
              console.log(response)
               console.log("CLuster creation successfull");
            })
            .catch((error) => {
              console.log(error);
             
            });
        })
 
      
        
         
    },
  },
 
 
  computed: {
    ...mapState(['selectedType', 'selectedProvider','postgres_version']),
    
  },
};
</script>
 