<template>
  <leftSidebar />
  <div class=" mx-10 w-full h-[100vh]">

  <div class="provider bg-gray-100 p-4 sm:ml-64 mt-20 mx-20 flex">
    <div class="text-black font-semibold text-4xl">Providers</div>
  </div>

  <!-- Deployment Section -->
  <!-- <div class="provider  p-4 sm:ml-64 mt-4">
  <div class="text-black font-semibold text-2xl mb-2">Deployment</div>
  <button class="btn" @click="showConnectedProviders">BitBlast</button>
  <button class="btn" @click="showNotConnectedProviders">Your Private Cloud Account</button>
</div> -->

  <!-- Connection Status -->
  <div class="text-gray-700 text-sm sm:ml-64 mt-2 flex justify-center">
    Connection Status
  </div>


  <!-- VMware Provider -->
  <button @click.prevent="toggleModal('vmware')">
    <div class="provider-item rounded border border-gray-300 p-4 w-[1330px] sm:ml-64 mt-4 flex justify-between">

      <div>
        <img src="@/assets/static/vmware-logo.png" alt="VMware Logo" class="provider-logo" />
        <div class="provider-title">VMware</div>
      </div>
      <div class="flex items-left">
        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('vmware')" class="h-6 w-6 text-green-500 mr-2"
          fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="40" fill="red" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
        </svg>
        <div class="provider_stat">
          <div class="text-green-500" v-if="isProviderConnected('vmware')">

            Connected</div>
          <div class="text-red-500" v-else>Not Connected </div>
        </div>
      </div>
    </div>
  </button>

  <!-- Harvester Provider -->
  <button @click.prevent="toggleModal('Harvester')">
    <div class="provider-item rounded border border-gray-300 w-[1330px] p-4 sm:ml-64 mt-4 flex justify-between">

      <div>
        <img src="@/assets/static/Harvester.png" alt="Harvester Logo" class="provider-logo" />
        <div class="provider-title">Harvester</div>
      </div>
      <div class="flex items-center">

        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Harvester')"
          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="40" fill="red" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
        </svg>
        <div class="provider_stat">
          <div class="text-green-500" v-if="isProviderConnected('Harvester')">

            Connected</div>
          <div class="text-red-500" v-else>Not Connected </div>
        </div>
      </div>

    </div>
  </button>

  <!-- Apache CloudStack Provider -->
  <button @click.prevent="toggleModal('Cloudstack')">
    <div class="provider-item rounded border border-gray-300 w-[1330px] p-4 sm:ml-64 mt-4 flex justify-between">

      <div>
        <img src="@/assets/static/apachecloudstack.png" alt="Apache CloudStack Logo" class="provider-logo" />
        <div class="provider-title">Apache CloudStack</div>
      </div>
      <div class="flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Cloudstack')"
          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="40" fill="red" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
        </svg>
        <div class="provider_stat">
          <div class="text-green-500" v-if="isProviderConnected('Cloudstack')">

            Connected</div>
          <div class="text-red-500" v-else>Not Connected </div>
        </div>
      </div>
    </div>
  </button>


  <!-- Openstack -->
  <button @click.prevent="toggleModal('Openstack')">
    <div class="provider-item rounded border border-gray-300 w-[1330px] p-4 sm:ml-64 mt-4 flex justify-between">

      <div>
        <img src="@/assets/static/Openstack.png" alt=" Openstack Logo" class="provider-logo" />
        <div class="provider-title">Open Stack</div>
      </div>
      <div class="flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Openstack')"
          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="40" fill="red" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
        </svg>
        <div class="provider_stat">
          <div class="text-green-500" v-if="isProviderConnected('Openstack')">

            Connected</div>
          <div class="text-red-500" v-else>Not Connected </div>
        </div>
      </div>
    </div>
  </button>

  <!-- Nutanix Provider -->
  <button @click.prevent="toggleModal('Nutanix')">
    <div class="provider-item rounded border border-gray-300 w-[1330px] p-4 sm:ml-64 mt-4 flex justify-between">
      <div>
        <img src="@/assets/static/Nutanix.png" alt="Nutanix Logo" class="provider-logo" />
        <div class="provider-title">Nutanix</div>
      </div>
      <div class="flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Nutanix')" class="h-6 w-6 text-green-500 mr-2"
          fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="40" fill="red" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
        </svg>
        <div class="provider_stat">
          <div class="text-green-500" v-if="isProviderConnected('Nutanix')">Connected</div>
          <div class="text-red-500" v-else>Not Connected</div>
        </div>
      </div>
    </div>
  </button>

  <!-- Kubernetes Provider -->
  <button @click.prevent="toggleModals('Kubernetes')">
    <div class="provider-item rounded border border-gray-300 w-[1330px] p-4 sm:ml-64 mt-4 flex justify-between">
      <div>
        <img src="@/assets/static/Kubernetes.png" alt="Kubernetes Logo" class="provider-logo" />
        <div class="provider-title">Kubernetes</div>
      </div>
      <div class="flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Kubernetes')"
          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="40" fill="red" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
        </svg>
        <div class="provider_stat">
          <div class="text-green-500" v-if="isProviderConnected('Kubernetes')">Connected</div>
          <div class="text-red-500" v-else>Not Connected</div>
        </div>
      </div>
    </div>
  </button>



  <fooTer />

  <!-- Modal -->
  <div v-show="isModalVisible" tabindex="-1" class="fixed top-0 left-0 right-0 bottom-0
        z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
    <div class="relative w-[700px] ">
      <div  class="relative bg-white rounded-lg shadow dark:bg-gray-800 bg-gradient-to-l from-blue-300 to-purple-600">
        <button @click="toggleModal" type="button" class="absolute top-3
          right-2.5 text-gray-400 bg-transparent hover:bg-gray-200
           hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex
           justify-center items-center dark:hover:bg-gray-600
            dark:hover:text-white" data-modal-hide="popup-modal">
          <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
        <div class="p-6 ">
          <h3 class="mb-5 text-lg font-normal text-white dark:text-gray-400">
            {{ selectedProvider }}
          </h3>

          <!-- Input fields for provider -->
          <div class="px-4 mt-10">
            <div class="mb-6">
              <label for="Api_name" class="block mb-2 text-sm font-medium text-white dark:text-white">Api Name</label>
              <input type="text" v-model="api_name"
                class="w-[300px] bg-gray-50 border border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Api Name" required>
            </div>
            <div class="mb-6">
              <label for="Access_token" class="block mb-2 text-sm font-medium text-white dark:text-white">Api
                Endpoint</label>
              <input type="text" v-model="api_endpoint" placeholder="Api Endpoint"
                class="w-[300px] bg-gray-50 border border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="mb-6">
              <label for="Access_token" class="block mb-2 text-sm font-medium text-white dark:text-white">Access
                key</label>
              <input type="text" v-model="access_key" placeholder="Access Token"
                class="w-[300px] bg-gray-50 border border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="mb-6">
              <label for="Access_token" class="block mb-2 text-sm font-medium text-white dark:text-white">Secret
                key</label>
              <input type="text" v-model="secret_key" placeholder="Secret Key"
                class="w-[300px] bg-gray-50 border border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>

            <div v-if="error" class="text-red-500 text-center mb-4">{{ error }}</div>
          </div>


          <button @click.prevent="addProvider"
            class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
            <span
              class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
              Add Provider
            </span>
          </button>
          <button @click="toggleModal"
            class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 
            group-hover:from-green-400 group-hover:to-blue-600 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800">
            <span
              class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
              Cancle
            </span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Kubernetes Provider Modal -->
  <div v-show="isModalVisibles && selectedModal === 'Kubernetes'" tabindex="-1"
  class="fixed top-0 left-0 right-0 bottom-0 z-50 flex justify-center p-4 overflow-x-hidden overflow-y-auto md:inset-0">
  <div class="relative w-[700px]">
    <div  class="relative bg-white rounded-lg shadow dark:bg-gray-800 bg-gradient-to-l from-blue-300 to-purple-600">
      <button @click="toggleModals('Kubernetes')" type="button"
        class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
        data-modal-hide="popup-modal">
        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
          </svg>
          <span class="sr-only">Close modal</span>
      </button>
      <div class="p-6">
        <h3 class="mb-5 text-lg font-normal text-white dark:text-gray-400"> {{ selectedModal }} Provider</h3>

        <!-- Input fields for Kubernetes provider -->
        <div class="px-4 mt-10">
          <div class="mb-6">
            <label for="kubeconfigData" class="block mb-2 text-sm font-medium text-white dark:text-white">Kubeconfig
              Data</label>
            <textarea v-model="kubeconfigData"
              class="w-[600px] h-32 bg-gray-50 border border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Paste your kubeconfig data here" required></textarea>
          </div>

          <div v-if="error" class="text-red-500 text-center mb-4">{{ error }}</div>
        </div>

          <button @click.prevent="addProviderk8s"
          class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
          <span
            class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
            Add Provider
          </span>
        </button>
        <button @click="toggleModals"
          class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 group-hover:from-green-400 group-hover:to-blue-600 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800">
          <span
            class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
            Cancle
          </span>
        </button>
      </div>
    </div>
  </div>
</div>

</div>
</template>
 
<script>
import leftSidebar from '@/components/leftSidebar.vue';
import fooTer from '@/components/fooTer.vue';
import axios from 'axios';

export default {
  components: {
    leftSidebar,
    fooTer,
  },
  data() {
    return {
      isModalVisibles: false,selectedModal: '', kubeconfigData: '',
      isModalVisible: false, user_id: '',
      selectedProvider: '',
      api_name: '', api_endpoint: '', secret_key: '', access_key: '', error: '',

      provider_info: []
    }
  },
  computed: {
    isProviderConnected() {
      return (providerName) => {
        return this.provider_info.some(
          (provider) =>
            provider.provider_name.toLowerCase() === providerName.toLowerCase() &&
            provider.is_connected
        );
      };
    },
  },


  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.getAllProviderData();
  },
  methods: {
    toggleModal(selectedProvider) {
      this.selectedProvider = selectedProvider
      this.isModalVisible = !this.isModalVisible;
    },
     // New method to open kubeconfig_data modal
     toggleModals(selectedProvider) {
      this.selectedProvider = selectedProvider;
      this.selectedModal = 'Kubernetes'; 
      this.isModalVisibles = !this.isModalVisibles;
    },
    async addProviderk8s() {
      console.log("k8s");
      const fromData = {
        user_id: this.user_id,
        provider_name: this.selectedProvider,
        key_name: this.api_name,

        
        // Include kubeconfigDataModal in the payload for Kubernetes Provider
        kubeconfig_data: this.kubeconfigData,
       
      };
      console.log ("data")
      await axios.post(`http://172.16.1.69:8000/api/v3/providers/`, fromData)
        .then((response) => {
          this.getAllProviderData();
          this.isModalVisibles = !this.isModalVisibles;
        });
    },

    async addProvider() {
      const fromData = {
        "user_id": this.user_id,
        "provider_name": this.selectedProvider,
        "key_name": this.api_name,
        "provider_url": this.api_endpoint,
        "secret_key": this.secret_key,
        "access_token": this.access_key,
      }
      await axios.post(`http://172.16.1.69:8000/api/v3/providers/`, fromData)
        .then((response) => {
          this.getAllProviderData();
          this.isModalVisible = !this.isModalVisible;
        })

    },
    getAllProviderData() {
      axios.get(`http://172.16.1.69:8000/api/v3/providers/by-user/${this.user_id}/`)
        .then((response) => {
          this.provider_info = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          // Handle error
          console.error("Failed to fetch provider data for the user.");
        });
    }
  }
}
</script>
 
<style scoped>
.provider-item {
  text-align: center;
}

.provider-logo {
  max-width: 100px;
}

.btn {
  margin-right: 10px;
  padding: 8px 16px;
  border: 2px solid #9BC666;
  border-radius: 8px;
  background-color: #fff;
  color: #9BC666;
  cursor: pointer;
}

.main_content {
   background: linear-gradient(90deg, #25316D 0%, #8b7c59 100%);

}

.btn:hover {
  background-color: #9BC666;
  color: #fff;
}

.provider-title {
  margin-top: 8px;
  font-weight: bold;
}</style>