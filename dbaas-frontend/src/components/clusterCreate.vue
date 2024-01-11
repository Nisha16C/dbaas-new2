<template>
   <leftSidebar />

   <div class="mt-20 w-auto ">
      <div class="w-full h-15 border-b-2 border-solid text-center">
         <div class="font-4xl text-semibold">Create Cluster</div>
      </div>
   </div>

   <div>
      <ul class="flex justify-center space-x-10 mt-10 mx-10"> <!-- Adjust mx-10 for the desired left space -->
         <li><router-link to="/clusterCreate">Cluster Info</router-link></li>
         <li><button @click.prevent="Next(selectedProvider)" to="/cluster-setting">Cluster Settings</button></li>
         <li><a href="#" class="link-style cursor-not-allowed">DB Configuration</a></li>
         <li><a href="#" class="link-style cursor-not-allowed">Additional Settings</a></li>
      </ul>
   </div>
   <div class="flex sm:ml-64 ">
      <div>
         <h1 class="ml-[40px] mt-10 py-4 text-gray-900 text-xl font-semibold">Select the type of cluster you want to use
         </h1>
         <div class="ml-[40px]">
            <div class="col-span-2 mb-5">
               <div>
                  <h1 class="py-4 text-gray-900 text-xl font-semibold">Cluster Type</h1>
               </div>
               <div class="grid grid-cols-2 md:grid-cols-3 ">
                  <div class="h-72 w-72 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedType == 'Standalone' }">
                     <label for="Standalone">
                        <input type="radio" class="hidden" id="Standalone" value="Standalone" v-model="selectedType"
                           @change="updateType">
                        <h1 class="pt-2 text-gray-900 font-semibold">Standalone cluster</h1>
                        <p class="pt-8 px-5 text-gray-500 text-sm">A Standalone Node Cluster refers to a cluster
                           configuration in a distributed computing environment where all cluster
                           components, such as databases, services, or applications, run on a Standalone node or machine.
                        </p>
                     </label>
                  </div>
                  <div class="h-72 w-72 ml-12 bg-white border-4 rounded-md text-center"
                     :class="{ 'selected': selectedType == 'multiple' }">
                     <label for="multiple">
                        <input type="radio" id="multiple" class="hidden" value="multiple" v-model="selectedType"
                           @change="updateType">
                        <h1 class="pt-2 text-gray-900 font-semibold">Primary/Standby High Availability</h1>
                        <p class="pt-2 px-5 text-gray-500 text-sm">A Primary/Standby High Availability (HA) Cluster refers
                           to a configuration in a distributed computing environment where two nodes (or more) operate in
                           tandem to provide fault tolerance and redundancy.</p>
                     </label>
                  </div>
               </div>

               <!-- Providers Type -->
               <div class="mt-5">
                  <h1 class="py-4 text-gray-900 text-xl font-semibold"> Providers </h1>
               </div>
               <div class="grid grid-cols-2 gap-4 w-2/3 ">

                  <!-- Cloudstack Provider -->
                  <div class=" bg-white border-4 rounded-md text-center p-3"
                     :class="{ 'selected': selectedProvider == 'Cloudstack' }">
                     <label>
                        <input type="radio" class="hidden" id="Cloudstack" value="Cloudstack" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain max-w-full rounded-lg" src="@/assets/static/apachecloudstack.png"
                           alt="">
                     </label>
                  </div>

                  <!-- Harvester Provider -->
                  <div class=" ml-12 bg-white border-4 rounded-md text-center p-3"
                     :class="{ 'selected': selectedProvider == 'Harvester' }">
                     <label>
                        <input type="radio" class="hidden" id="Harvester" value="Harvester" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain max-w-full rounded-lg" src="@/assets/static/Harvester.png" alt="">
                     </label>
                  </div>

                  <!-- Vmware Provider -->
                  <div class=" bg-white border-4 rounded-md text-center p-3"
                     :class="{ 'selected': selectedProvider == 'Vmware' }">
                     <label>
                        <input type="radio" class="hidden" id="Vmware" value="Vmware" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain max-w-full rounded-lg" src="@/assets/static/Vmware.png" alt="">
                     </label>
                  </div>

                  <!-- Kubernetes Provider -->
                  <div class=" ml-12 bg-white border-4 rounded-md text-center p-3"
                     :class="{ 'selected': selectedProvider == 'Kubernetes' }">
                     <label>
                        <input type="radio" class="hidden" id="Kubernetes" value="Kubernetes" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain max-w-full rounded-lg" src="@/assets/static/Kubernetes.png" alt="">
                     </label>
                  </div>
                  <!-- Nutanix Provider -->
                  <div class=" bg-white border-4 rounded-md text-center p-3"
                     :class="{ 'selected': selectedProvider == 'Nutanix' }">
                     <label>
                        <input type="radio" class="hidden" id="Nutanix" value="Nutanix" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain max-w-full rounded-lg" src="@/assets/static/Nutanix.png" alt="">
                     </label>
                  </div>

                  <!-- Openstack Provider -->
                  <div class=" ml-12 bg-white border-4 rounded-md text-center p-3"
                     :class="{ 'selected': selectedProvider == 'Openstack' }">
                     <label>
                        <input type="radio" id="Openstack" class="hidden" value="Openstack" v-model="selectedProvider"
                           @change="updateProvider">
                        <img class="object-contain max-w-full rounded-lg" src="@/assets/static/Openstack.png " alt="">
                     </label>
                  </div>
               </div>

               <p class="text-red-500" v-if="this.error">This Provider is not connected to connect
                  <router-link to="/providers" class="text-red-900"> Click here</router-link>
               </p>

               <div class="pt-10">
                  <button to="Createuser" @click.prevent="Next(this.selectedProvider)"
                     class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
                     <span
                        class="relative w-32 px-5 py-2.5 transition-all ease-in duration-75 text-black bg-white rounded-md group-hover:bg-opacity-0">
                        Next
                     </span>
                  </button>
               </div>
            </div>
         </div>
      </div>

      <clusterSum />
   </div>

   <!-- Cluster summary -->


   <fooTer />
</template>

<script>

import leftSidebar from '@/components/leftSidebar.vue';
import fooTer from '@/components/fooTer.vue';
import clusterSum from '@/components/clusterSummary.vue';

import { useInputStore } from '@/stores/clusterStore';
import axios from 'axios';

export default {
   components: {
      leftSidebar,
      fooTer, clusterSum
   },
   data() {
      return {
         selectedType: 'Standalone',
         selectedProvider: 'Cloudstack',

         user_id: '',
         provider_info: [],
         error: ''

      };
   },
   created() {
      const store = useInputStore();
      store.setType(this.selectedType);
      store.setProvider(this.selectedProvider);

      this.user_id = sessionStorage.getItem('user_id');
      this.getAllProviderData();

   },
   methods: {
      updateType() {
         this.selectedType = this.selectedType
         const store = useInputStore();
         store.setType(this.selectedType);
      },
      updateProvider() {
         this.selectedProvider = this.selectedProvider
         const store = useInputStore();
         store.setProvider(this.selectedProvider);
      },

      Next(providerName) {
         const store = useInputStore();
         store.setType(this.selectedType);
         store.setProvider(this.selectedProvider);

         if (
            this.provider_info.some(
               (provider) =>
                  provider.provider_name.toLowerCase() === providerName.toLowerCase() &&
                  provider.is_connected
            )
         ) {

            console.log(`${providerName} is connected!`);
            this.$router.push('/cluster-setting');
         } else {

            this.error = "providerError"
            setTimeout(() => {
               this.error = '';
            }, 5000);
         }
      },

      getAllProviderData() {
         axios.get(`http://172.16.1.69:8000/api/v3/providers/by-user/${this.user_id}/`)
            .then((response) => {
               this.provider_info = response.data
               console.log(response.data);
            })
      },

   },
};
</script>


<style > table,
 th,
 td {
    border: none;
    border-collapse: separate;
 }

 th,
 td {
    padding: 5px 10px;
 }

 table {
    width: 100%;
 }

 .link-style {
    text-decoration: none;
    /* Remove the default underline */
    /* Set the dfault text color */
    font-weight: 600;
    /* Set the default font weight to make it bold */
    transition: color 0.2s, border-bottom-color 0.2s;
    /* Add a smooth transition effect */
 }

 .selected {
    color: rgb(229 231 235);
    box-shadow: grey;
    border-color: rgb(30 41 59);
 }</style> 