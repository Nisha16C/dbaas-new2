<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Cluster Name and it's Password.</h6>
    </div>
 
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg">
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Cluster Name and Password</h6>
            <form>
              <div class="form-group">
                <label for="Cluster_Name"> Cluster Name</label>
                <bb-input class="" type="email" id="example-text-input" placeholder="Enter Your Cluster Name"
                  v-model="cluster_name" @blur="checkClusterNameExists" />
                <!-- Error message for cluster name -->
                <div v-if="errorClusterName" class="text-danger mt-2">{{ errorClusterName }}</div>
                <!-- Error message for cluster name already exists -->
                <div v-if="errorClusterNameExists" class="text-danger mt-2">{{ errorClusterNameExists }}</div>
 
              </div>
 
              <div class="form-group">
                <label for="Postgres_Username"> Postgres Username</label>
                <bb-input type="email" class="" id="Postgres_Username"
                  placeholder="Enter Your Postgres Username" v-model="db_user" />
              </div>
 
              <div class="form-group">
                <label for="Cluster_Name"> Your Password</label>
                <bb-input type="password" class="" id="Password" placeholder="Enter Your Password "
                  v-model="db_password" @input="validatePassword" />
                <div v-if="passwordLengthError" class="text-danger mt-2" >{{ passwordLengthError }}</div>  
              </div>
            </form>
 
            <h6 class="mb-3 text-sm">Database Type and Versions</h6>
            <select :class="{ 'BGdark': isDarkMode }" class="form-select" aria-label="Default select example" @change="updateVersion"
              v-model="postgres_version">
              <option value="16" selected>16</option>
              <option value="15" >15</option>
              <option value="14">14</option>
              <option value="13">13</option>
              <option value="12">12</option>
            </select>
            <!-- Error message for database version -->
            <div v-if="errorDatabaseVersion" class="text-danger mt-2">{{ errorDatabaseVersion }}</div>
 
            <h6 class="mb-3 mt-3 text-sm">Backup Method</h6>
            <select :class="{ 'BGdark': isDarkMode }" class="form-select" aria-label="Default select example" v-model="backup_method">
              <option value="nfs" selected>NFS</option>
              <option value="s3">S3</option>
            </select>
            <div class="text-danger">
              {{ backupError }}
            </div>
          </div>
        </li>
      </ul>
      <div class="text-danger mb-3">
        {{ typeError }}
      </div>
      <div class="text-danger mb-3">
        {{ providerError }}
      </div>
      <div class="text-danger mb-3">
        {{ computeOfferingError }}
      </div>
      <div class="text-danger mb-3">
        {{ storageOfferingError }}
      </div>
 
      <argon-button @click="createCluster" color="success" size="md" variant="gradient">
        Create Cluster </argon-button>
    </div>
  </div>
</template>
 
<script>
import axios from 'axios';
import { mapState, mapActions } from 'vuex';
import ArgonButton from "@/components/BB_Button.vue";
import { API_ENDPOINT } from '@/../apiconfig.js';
import bbInput from "@/components/BB_Input.vue";

 
 
export default {
  name: "billing-card",
  components: {
    ArgonButton,
    bbInput
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      
      selectedTools: [],
      postgres_version: '',
      cluster_name: '',
      // computeOfferings: [],  // New property to store compute offerings
      // OpenstackUser: '',
      // tenant_name: '',
      // OpenstackPassword: '',
      // auth_url: '',
      // region: '',
 
 
      user_id: '',
      provider_info: '',
      errorClusterName: '',
      errorDatabaseVersion: '',
      errorClusterNameExists: '',
      errorNoSelectedProject: '',
      backendError: '',
      db_user: '',
      db_password: '',
      backup_method: '',
      Username: '',
      nfsMountpoints: '',
      s3Mountpoints: '',
      backupError: '',
      mount_point: '',
      typeError: '',
      providerError: '',
      computeOfferingError:'',
      storageOfferingError:'',
      passwordLengthError: '',
      passwordLengthTimeout: null,
 
    };
  },
 
  created() {
    this.Username = sessionStorage.getItem('username');
    this.user_id = sessionStorage.getItem('user_id');
    // this.listMountpoints();
    // this.fetchComputeOfferings();
  },

  
 
  methods: {
    ...mapActions(['updateSelectedVersion']),
    updateVersion() {
      this.updateSelectedVersion(this.postgres_version);
    },
    // ...mapActions(['updateSelectedMethod']),
    // updateMethod() {
    //   this.updateSelectedMethod(this.backup_method);
    // },
 
    validatePassword() {
      this.passwordLengthError='';
      clearTimeout(this.passwordLengthError);
 
      if (this.db_password.length < 5 || this.db_password.length > 15 ) {
        this.passwordLengthError = 'Password must be between 5 and 15 characters';
        this.passwordLengthTimeout = setTimeout(()=> {
          this.passwordLengthError = '';
        },5000);
 
      }
      
 
    },
 
 
    checkClusterNameExists() {
      this.errorClusterNameExists = '';
 
      if (!this.cluster_name) {
 
        return;
      }
 
      // Check if cluster name already exists
      axios
        .get(`${this.apiUrl}/api/v2/cluster/check_cluster_exists/?cluster_name=${this.cluster_name}&project_id=${this.project_id}`)
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
          console.log(error);
          // Handle errors from the cluster check API if needed
        });
    },
    // listMountpoints() {
    //   axios.get(
    //     `http://172.16.1.131:8000/api/v4/barman/list-mount-points?username=${this.Username}`
    //   )
    //     .then((response) => {
    //       this.nfsMountpoints = response.data.nfs_mount_points;
    //       this.s3Mountpoints = response.data.s3_mount_points;
    //     })
    //     .catch((error) => {
    //       console.error('Error mounting s3:', error);
    //     })
    // },
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
 
      // if (!this.backup_method) {
      //   this.backupError = 'This field is required';
      //   return;
      // } else {
      //   if (this.backup_method === 'nfs') {
      //     console.log("backup_method == nfs");
      //     this.mount_point = this.nfsMountpoints[0].mount_point;
      //     console.log(this.mount_point);
      //     if (this.nfsMountpoints.length <= 0) {
      //       this.backupError = "NFS is not connected";
      //       return;
      //     } else {
      //       this.backupError = '';
      //     }
      //   } else {
      //     console.log("backup_method == nfs");
      //     this.mount_point = this.s3Mountpoints[0].mount_point;
      //     console.log(this.mount_point);
      //     if (this.s3Mountpoints.length <= 0) {
      //       this.backupError = "S3 is not connected";
      //       return;
      //     } else {
      //       this.backupError = '';
      //     }
      //   }
      // }
 
      if (!this.clusterType) {
 
        this.typeError = 'Cluster type is required';
        setTimeout(() => {
          this.typeError = '';
        }, 5000);
        return;
      }
      if (!this.providerName) {
 
        this.providerError = 'Provider is required';
        setTimeout(() => {
          this.providerError = '';
        }, 5000);
        return;
      }
      if (this.providerName !== 'Kubernetes' && this.providerName !== 'Openstack' && !this.computeOfferings){
 
        this.computeOfferingError = 'Compute Offering is required';
        setTimeout(() => {
          this.computeOfferingError = '';
        }, 5000);
        return;
      }
      if (this.providerName !== 'Kubernetes'  && this.providerName !== 'Openstack' && !this.selectedStorageOffering) {
 
        this.storageOfferingError = 'Storage Offering is required';
        setTimeout(() => {
          this.storageOfferingError = '';
        }, 5000);
        return;
      }
 
      axios
        .get(`${this.apiUrl}/api/v3/providers/by-username-and-name/${this.Username}/${this.providerName}/`)
        .then((response) => {
          this.provider_info = response.data;
          this.provider_info.kubeconfig_data =   JSON.stringify(this.provider_info.kubeconfig_data)
          console.log(this.provider_info);
 
          const fromData = {
            db_user: this.db_user,
            db_password: this.db_password,
            user: this.user_id,
            project: this.project_id,
            provider: this.providerName,
 
            cluster_type: this.clusterType,
            computeOffering: this.computeOfferings,
            storageOffering: this.selectedStorageOffering,
            cluster_name: this.cluster_name,
            postgres_version: this.postgres_version,
            provider_endpoint: this.provider_info.provider_url,
            provider_access_token: this.provider_info.access_token,
            provider_secret_key: this.provider_info.secret_key,
            kubeconfig_data: this.provider_info.kubeconfig_data,
 
            OpenstackUsername: this.provider_info.openStackuser,
            tenant_name: this.provider_info.tenant_name,
            openstackPassword: this.provider_info.openstackpassword,
            auth_url: this.provider_info.auth_url,
            region: this.provider_info.region,
 
 
            // backup_method: this.backup_method,
            // mount_point: this.mount_point,
 
            
          };
          // console.log(fromData);
          console.table([fromData]);
 
 
 
          this.$router.push('/result');
          axios
            .post(`${this.apiUrl}/api/v2/cluster/`, fromData)
            .then(() => {
 
 
            })
            .catch((error) => {
              console.log(error);
 
            });
        })
    },
 
    fetchComputeOfferings() {
      axios
        .get(`${this.apiUrl}/api/v2/compute_offerings/`)
        .then((response) => {
          this.computeOfferings = response.data;
        })
        .catch((error) => {
          console.error('Error fetching compute offerings:', error);
        });
    },
  },
 
 
  computed: {
    ...mapState(['clusterType', 'computeOfferings', 'providerName', 'postgres_version', 'project_name', 'project_id', 'selectedStorageOffering']),
 
  },
};
</script>

<style scoped>
.BGdark {
  background-color: #1d1e52;
  color: #fff;
 
}
</style>
 