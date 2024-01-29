<template>
  <leftSidebar />
 
  <div class="mt-20 w-auto">
    <div class="w-full h-15 border-b-2 border-solid text-center">
      <div class="font-4xl text-semibold">Create Cluster</div>
    </div>
 
    <div>
      <ul class="flex justify-center space-x-10 mt-10 mx-10">
        <li><router-link to="/clusterCreate">Cluster Info</router-link></li>
        <li><router-link to="/cluster-setting">Cluster Settings</router-link></li>
        <li><a href="#" class="link-style cursor-not-allowed">DB Configuration</a></li>
        <li><a href="#" class="link-style cursor-not-allowed">Additional Settings</a></li>
      </ul>
    </div>
 
    <div class="p-4 sm:ml-64 flex ">
 
      <div class="mt-10">
        <h1>Cluster Name and Password</h1>
 
        <div class="mb-6">
          <label for="cname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Cluster Name</label>
          <input type="text" v-model="cluster_name"
          @blur="checkClusterNameExists"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm
             rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5
              dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400
               dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Cluster Name" required>
          <!-- Error message for cluster name -->
          <div v-if="errorClusterName" class="text-red-500 mt-2">{{ errorClusterName }}</div>
          <!-- Error message for cluster name already exists -->
          <div v-if="errorClusterNameExists" class="text-red-500 mt-2">{{ errorClusterNameExists }}</div>
        </div>
        <div class="mb-6">
          <label for="cname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Postgres
            Username</label>
          <input type="text" v-model="db_user"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Postgres">
        </div>
 
        <div class="mb-6">
          <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Your password</label>
          <input type="password" id="password" placeholder="*************" v-model="db_password"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required>
        </div>
        <p class="text-gray-400 mt-2">Your password is very secure,we do not misuse your password you can change your password if you forgot your password..
         </p>
 
        <div class="mt-5">
          <h1>Database Type and Versions</h1>
          <!-- <p class="mb-3">Postgres Type</p>
          <button class="p-3 bg-gray-600 hover:bg-gray-800">PostgreSQL</button>
          <button class="p-3 bg-gray-800 hover:bg-gray-600">Postgres Advanced Server</button> -->
 
          <p class="mt-3 mb-3">Postgres Version </p>
          <select class="select w-40 p-11" @change="updateVersion" v-model="postgres_version">
            <option @change="updateVersion" value="15" class="w-40">15</option>
            <option @change="updateVersion" value="14" class="w-40">14</option>
            <option @change="updateVersion" value="13" class="w-40">13</option>
          </select>
          <!-- Error message for database version -->
          <div v-if="errorDatabaseVersion" class="text-red-500 mt-2">{{ errorDatabaseVersion }}</div>
          <br>

          <button to="Createuser" @click="createCluster"
            class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
            <span
              class="relative px-5 py-2.5 transition-all ease-in duration-75 text-black bg-white rounded-md group-hover:bg-opacity-0">
              Create New Cluster
            </span>
          </button>
          
 
          <!-- Error message for no selected project -->
          <div v-if="errorNoSelectedProject" class="text-red-500 mt-2">{{ errorNoSelectedProject }}</div>
          
          <div v-if="backendError" class="text-red-500 mt-2">{{ backendError }}</div>
        </div>
      </div>
 
      <clusterSummary :selectedType="selectedType"/>
    </div>
  </div>
 
  <fooTer />
</template>
<script>
import axios from 'axios';
 
import { useInputStore } from '@/stores/clusterStore';
import leftSidebar from '@/components/leftSidebar.vue';
import clusterSummary from '@/components/clusterSummary.vue';
import fooTer from '@/components/fooTer.vue';
 
export default {
  components: {
    leftSidebar,
    fooTer,
    clusterSummary,
  },
  data() {
    return {
      selectedTools: [],
      postgres_version: '',
      cluster_name: '',
      project_id: '',
      user_id: '',
      provider_info: '',
      errorClusterName: '',
      errorDatabaseVersion: '',
      errorClusterNameExists: '',
      errorNoSelectedProject: '',
      backendError: '',
      db_user: '',
      db_password: '',Username: ''
    };
  },
  created() {
    this.user_id = sessionStorage.getItem('user_id');
    this.project_id = sessionStorage.getItem('project_id');
    this.Username = sessionStorage.getItem('username');
  },
  methods: {
    checkClusterNameExists() {
        // Reset error message
        this.errorClusterNameExists = '';

        if (!this.cluster_name) {
          // No need to check if the cluster name is empty
          return;
        }

        // Check if cluster name already exists
        axios
        .get(`http://172.16.1.69:8002/api/v2/cluster/check_cluster_exists/?cluster_name=${this.cluster_name}&project_id=${this.project_id}`)
          .then((response) => {
            if (response.data.exists) {
              // Cluster name already exists
              this.errorClusterNameExists = 'Cluster with the same name already exists';
              setTimeout(() => {
                this.errorClusterNameExists = '';
              }, 5000);
            }
          })
          .catch((error) => {
            // Handle errors from the cluster check API if needed
          });
      },

    updateVersion() {
         this.postgres_version = this.postgres_version
         const store = useInputStore();
         store.setVersion(this.postgres_version);    
      },
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
 
      this.project_id = sessionStorage.getItem('project_id');
     
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
        .get(`http://172.16.1.69:8002/api/v3/providers/by-username-and-name/${this.Username}/${this.selectedProvider}/`)
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
            .post(`http://172.16.1.69:8002/api/v2/cluster/`, fromData)
            .then((response) => {
               console.log("CLuster creation successfull");
            })
            .catch((error) => {
             
             
            });
        })

      
        
         
    },
  },
  computed: {
    selectedType() {
      return useInputStore().selectedType;
    },
    selectedProvider() {
      return useInputStore().selectedProvider;
    },
  },
};
</script>
 
 
 
<style scoped>
  h1 {
    font-weight: bold;
    margin-bottom: 20px;
  }
 
  #heading {
    margin-bottom: 31px;
  }
 
  .password-info {
    font-size: 12px;
    color: #999;
    margin-top: 5px;
  }
 
  .select {
    width: 100px;
    padding: 5px;
    border: 1px solid #000000;
    border-radius: 5px;
    margin-bottom: 10px;
  }
 
  input {
    width: 400px;
  }
</style>