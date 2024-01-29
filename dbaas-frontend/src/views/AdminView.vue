<template>
   <adminLeftsidebar />
   <div class="main p-4 sm:ml-64 mt-20 ">
      <div class="main-content flex-1 bg-gray-100 mt-12 md:mt-2 pb-24 md:pb-5">

         <div class="bg-gray-800 pt-3">
            <div class="rounded-tl-3xl bg-gradient-to-r from-blue-900 to-gray-800 p-4 shadow text-2xl text-white">
               <h3 class="font-bold pl-2">Admin Dashboard</h3>
            </div>

         </div>

         <div class="flex flex-wrap">
            <router-link to="/users-management" class="w-full md:w-1/2 xl:w-1/3 p-6">
               <div
                  class="bg-gradient-to-b from-green-200 to-green-100 border-b-4 border-green-600 rounded-lg shadow-xl p-5">
                  <div class="flex flex-row items-center">
                     <div class="flex-shrink pr-4">
                        <div class="rounded-full p-5 bg-green-600"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                     </div>
                     <div class="flex-1 text-right md:text-center">
                        <h5 class="font-bold uppercase text-gray-600">Total Users</h5>
                        <h3 class="font-bold text-3xl"> {{ users.length }} <span class="text-green-500"><i
                                 class="fas fa-caret-up"></i></span></h3>
                     </div>
                  </div>
               </div>

            </router-link>

            <router-link to="/projects-management" class="w-full md:w-1/2 xl:w-1/3 p-6">
               <div>

                  <div
                     class="bg-gradient-to-b from-pink-200 to-pink-100 border-b-4 border-pink-500 rounded-lg shadow-xl p-5">
                     <div class="flex flex-row items-center">
                        <div class="flex-shrink pr-4">
                           <div class="rounded-full p-5 bg-pink-600"><i class="fas fa-users fa-2x fa-inverse"></i></div>
                        </div>
                        <div class="flex-1 text-right md:text-center">
                           <h5 class="font-bold uppercase text-gray-600">Total Projects</h5>
                           <h3 class="font-bold text-3xl"> {{ projects.length }} <span class="text-pink-500"><i
                                    class="fas fa-exchange-alt"></i></span></h3>
                        </div>
                     </div>
                  </div>

               </div>
            </router-link>

            <router-link to="/cluster-management" class="w-full md:w-1/2 xl:w-1/3 p-6">

                  <div
                     class="bg-gradient-to-b from-yellow-200 to-yellow-100 border-b-4 border-yellow-600 rounded-lg shadow-xl p-5">
                     <div class="flex flex-row items-center">
                        <div class="flex-shrink pr-4">
                           <div class="rounded-full p-5 bg-yellow-600"><i class="fas fa-user-plus fa-2x fa-inverse"></i>
                           </div>
                        </div>
                        <div class="flex-1 text-right md:text-center">
                           <h5 class="font-bold uppercase text-gray-600">Total Clusters</h5>
                           <h3 class="font-bold text-3xl"> {{ clusters.length }} <span class="text-yellow-600"><i
                                    class="fas fa-caret-up"></i></span></h3>
                        </div>
                     </div>
                  </div>

            </router-link>

            <button class="w-full md:w-1/2 xl:w-1/3 p-6">
               <div>

                  <div
                     class="bg-gradient-to-b from-blue-200 to-blue-100 border-b-4 border-blue-500 rounded-lg shadow-xl p-5">
                     <div class="flex flex-row items-center">
                        <div class="flex-shrink pr-4">
                           <div class="rounded-full p-5 bg-blue-600"><i class="fas fa-server fa-2x fa-inverse"></i></div>
                        </div>
                        <div class="flex-1 text-right md:text-center">
                           <h5 class="font-bold uppercase text-gray-600">Total Providers</h5>
                           <h3 class="font-bold text-3xl"> {{ providers.length }} </h3>
                        </div>
                     </div>
                  </div>

               </div>
            </button>

            <!-- <button class="w-full md:w-1/2 xl:w-1/3 p-6">
               <div
                  class="bg-gradient-to-b from-indigo-200 to-indigo-100 border-b-4 border-indigo-500 rounded-lg shadow-xl p-5">
                  <div class="flex flex-row items-center">
                     <div class="flex-shrink pr-4">
                        <div class="rounded-full p-5 bg-indigo-600"><i class="fas fa-tasks fa-2x fa-inverse"></i></div>
                     </div>
                     <div class="flex-1 text-right md:text-center">
                        <h5 class="font-bold uppercase text-gray-600"> New option </h5>
                        <h3 class="font-bold text-3xl"> data </h3>
                     </div>
                  </div>
               </div>
            </button> -->

         </div>
      </div>
   </div>
   <div class="mt-56 ">
      <fooTer />
   </div>
</template>
     
<script>
import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue'
import { useDark, useToggle } from "@vueuse/core";
import fooTer from '@/components/fooTer.vue';
import axios from 'axios';

export default {

   components: {
      adminLeftsidebar,
      fooTer,
   },
   data() {
      const isDark = useDark();
      const toggleDark = useToggle(isDark);
      return {
         isDark,
         toggleDark,
         Username: '', users: [], clusters: [], projects: [], providers: [],
      }
   },
   created() {
      this.Username = sessionStorage.getItem("username");
      this.fetchProject();
      this.fetchClusters();
      this.fetchProviders();
      this.fetchUsers();
   },
   methods: {
      fetchProject() {       
         axios.get(`http://172.16.1.69:8002/api/v2/project/`)
            .then(response => {
               this.projects = response.data;
            })
      },
      fetchClusters() {
         axios.get(`http://172.16.1.69:8002/api/v2/cluster/`)
            .then(response => {
               this.clusters = response.data;
            });
      },
      fetchUsers() {
         axios.get(`http://172.16.1.69:8002/api/v1/users/`)
            .then(response => {
               this.users = response.data;
               
            })
      },
      fetchProviders() {
         axios.get(`http://172.16.1.69:8002/api/v3/providers/`)
            .then((response) => {
               this.providers = response.data;
              
            })
            .catch((error) => {
               // Handle error
               console.error("Failed to fetch provider data for the user.");
            });
      }
   }

}
</script>
     
     