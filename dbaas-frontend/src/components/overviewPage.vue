<template>
  <div v-show="loading" class="spinner">
    <div class="bg-white opacity-60% absolute right-1/2 bottom-1/2 transform translate-x-1/2 translate-y-1/2">
      <div class="p-4 bg-gradient-to-tr animate-spin from-green-500 to-blue-500 via-purple-500 rounded-full">
        <div class="bg-white rounded-full">
          <div class="w-24 h-24 rounded-full"></div>
        </div>
      </div>
    </div>
  </div>
  <leftSidebar />
  <div v-show="!loading">
    <div class="cluster p-4 sm:ml-64 mt-20 flex">
      <div class="text-black font-semibold text-4xl">
        Clusters
      </div>
      <div class="ml-auto">

        <router-link to="/clusterCreate"
          class="relative inline-flex items-center justify-center  p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
          <span
            class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white text-black rounded-md group-hover:bg-opacity-0">
            Create New Cluster
          </span>
        </router-link>

      </div>
    </div>
    <div class="w-full h-15 border-b-2 p-4 sm:ml-64 border-solid mt-10 flex items-center">
      <div class=" ">
        <div class="flex items-center px-5 py-6 bg-gray-100 rounded-md shadow-sm">
          <div class="p-3 bg-indigo-600 bg-opacity-75 rounded-full">
            <svg viewBox="64 64 896 896" focusable="false" data-icon="database" width="1em" height="1em"
              fill="currentColor" class="w-6 h-6" aria-hidden="true">
              <path
                d="M832 64H192c-17.7 0-32 14.3-32 32v832c0 17.7 14.3 32 32 32h640c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32zm-600 72h560v208H232V136zm560 480H232V408h560v208zm0 272H232V680h560v208zM304 240a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0z">
              </path>
            </svg>
          </div>

          <div class="mx-5">
            <h4 class="text-2xl font-semibold text-gray-700"> {{ clusters.length }} </h4>
            <div class="text-gray-500">Total Running Clusters</div>
          </div>
        </div>
      </div>



      <!-- Search Bar -->
      <div class="relative ml-4 mr-4">
        <input type="text"
          class="pl-8 pr-3 py-2 border rounded-lg w-48 bg-white border-gray-400 focus:border-primary-500 focus:ring-primary-500"
          placeholder="Search" />
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M21 21l-5.2-5.2M15 10.5a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z"></path>
          </svg>
        </div>
      </div>
      <div class="ml-4">
        <!-- Project Dropdown -->
        <span class="font-extrabold "> Projects: </span>
        <select v-model="selectedProject" @change="fetchClustersByProject" class="rounded-md ">
          <option value="">All Projects</option>
          <option v-for="project in projects" :key="project.id" :value="project.id">{{ project.project_name }}</option>
        </select>
      </div>
      <!-- <button
        class="relative inline-flex items-center ml-10 justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
        <span
          class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white text-black rounded-md group-hover:bg-opacity-0">
          Delete Cluster
        </span>
      </button> -->
    </div>

    <!-- New Table  -->
    <div class="flex flex-col mt-8 sm:ml-64">
      <div class="py-2 -my-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
        <div class="" v-if="clusters.length === 0">
          <span class="text-gray-400 mb-2 text-2xl ml-96 ">No Cluster found in the Selected Project</span>
        </div>

        <div v-else
          class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
          <table class="min-w-full">
            <thead>
              <tr>
                <th
                  class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                  ID & Database Name
                </th>
                <th
                  class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                  Database Type
                </th>
                <th
                  class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                  Database Versions
                </th>
                <th
                  class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                  Provider
                </th>
                <th
                  class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                  Created On
                </th>
                <th
                  class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                  Updated On
                </th>
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50"></th>
              </tr>
            </thead>

            <tbody class="bg-white" v-for="(cluster, index) in clusters" :key="index">
              <tr>
                <td class=" border-b border-gray-200 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 ">
                      <button class="flex mt-3 items-center justify-center h-8 w-8 bg-indigo-200 rounded-full">
                        {{ cluster.id }}
                      </button>
                    </div>

                    <div class="ml-4">
                      <div class="text-sm font-medium leading-5 text-gray-900">
                        {{ cluster.cluster_name }}
                      </div>
                      <div class="text-sm leading-5 text-gray-500">
                        {{ }}
                      </div>
                    </div>
                  </div>
                </td>

                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                  <div class="text-sm leading-5 text-gray-900">
                    <span class="inline-flex px-2 text-xs font-semibold leading-5
                   text-green-800 bg-green-100 rounded-full"> {{ cluster.cluster_type }} </span>

                  </div>

                </td>

                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                  <span class="inline-flex px-2 text-xs  font-semibold leading-5
                  text-gray-500 rounded-full">Postgres {{ cluster.database_version }} </span>
                </td>

                <td class="px-6 py-4 text-sm leading-5 text-gray-500 border-b border-gray-200 whitespace-nowrap">
                  {{ cluster.provider }}
                </td>

                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                  <span class="inline-flex px-2 text-xs font-semibold leading-5
               text-yellow-500 bg-yellow-100 rounded-full">{{ formatTimeAgo(cluster.created_date) }} </span>
                </td>
                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                  <span class="inline-flex px-2 text-xs font-semibold leading-5
               text-yellow-500 bg-yellow-100 rounded-full">{{ formatTimeAgo(cluster.updated_date) }} </span>
                </td>


                <td class="px-6 py-4 text-sm font-medium leading-5 text-right border-b border-gray-200 whitespace-nowrap">
                  <a href="#" @click="toggleModal(cluster.cluster_name)" class="text-indigo-600 hover:text-indigo-900">
                    View / </a>
                  <!-- <a href="#" @click=" " class="text-indigo-600 hover:text-indigo-900">
                    Delete </a> -->
                  <button class=" text-indigo-600 hover:text-indigo-900" type="button" v-on:click="toggleModal1()">
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div v-if="showModal" 
      class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
      <div class="relative w-auto my-6 mx-auto max-w-sm">
        <!--content-->
        <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold">
              Cluster Name
            </h3>
            <button
              class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
              v-on:click="toggleModal()">
              <span class="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div v-if="showModal" class="relative p-6 flex-auto">
            <label>Enter Cluster Name :</label>
            <input v-model="newClusterName" type="text" placeholder="Cluster Name"
              class="mt-2 px-4 py-2 border rounded-md w-full" />
            <span v-if="error" class="text-red-500">{{ error }}</span>
          </div>
          <!--footer-->
          <div class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
            <button @click="toggleModal1()"
              class="text-purple-500 bg-transparent border border-solid border-purple-500 hover:bg-purple-500 hover:text-white active:bg-purple-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150">
              Cancel
            </button>
            <button @click="deleteCluster()"
              class="text-purple-500 bg-transparent border border-solid border-purple-500 hover:bg-purple-500 hover:text-white active:bg-purple-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150">
              Delete Cluster
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>



  </div>
</template>

<script>
import leftSidebar from "@/components/leftSidebar.vue";
import fooTer from "@/components/fooTer.vue";
import axios from "axios";

export default {
  components: {
    leftSidebar,
    fooTer,
  },
  data() {
    return {
      isModalVisible: false,
      selectedCluster: '',
      contentList: [],
      error: '',
      isActive: false,
      isDeleted: false,
      user_id: null,
      projects: [],
      selectedProject: "",
      clusters: [],
      loading: true,
      showModal: false

    };
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.fetchProjects();
    this.fetchClusters();
  },
  methods: {


    deleteCluster() {

      if (!this.newClusterName) {
        this.error = 'Cluster name is required';
        return; // Prevent API call
      }
      const formData = {
        cluster_name: this.newClusterName
      };

      console.log('Deleting cluster with name:', this.newClusterName);
     // this.$router.push('/deleteResult');
      axios.post("http://172.16.1.69:8002/api/v2/deletecluster/", formData)
        .then(response => {
          // Handle successful deletion
          console.log('Cluster deleted successfully:', response.data);
          this.fetchClusters();
          this.toggleModal1(); 
        })
        .catch(error => {
          console.error('Error deleting cluster:', error);
          // Handle error, show a message, etc.
          this.toggleModal1();
        });
    },

    toggleModal1: function () {
      this.showModal = !this.showModal;
    },
    toggleDarkMode() {
      this.toggleDark();
    },
    toggleModal(selectedCluster) {
      console.log(selectedCluster)
      this.selectedCluster = selectedCluster
      this.isModalVisible = !this.isModalVisible;
      this.getClusterDetails();
    },

    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    projectToggle() {
      this.ProjectToggle = !this.ProjectToggle;
    },
    userToggle() {
      this.UserToggle = !this.UserToggle;
    },
    logout() {

      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      window.location.reload();
    },
    addLineBreaks(text) {
      const formattedContent = text.replace(/([^:\n]+):/g, '<h class="text-sm text-purple-600">$1</h>:');
      return formattedContent.replace(/\n/g, '<br>');
      // Replace '\n' with '<br>' for rendering line breaks in HTML
      // return text.replace(/\n/g, '<br>');
    },

    getClusterDetails() {
      axios.get(`http://172.16.1.69:8002/api/v2/result/content/${this.selectedCluster}/`)
        .then(response => {
          this.contentList = response.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },

    getFirstLetter(username) {
      return username.charAt(0, 1).toUpperCase();
    },
    fetchProjects() {
      axios.get(`http://172.16.1.69:8002/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects = response.data;

        });
    },
    fetchClusters() {
      axios.get(`http://172.16.1.69:8002/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusters = response.data;
          this.loading = false;
        });
    },
    fetchClustersByProject() {
      if (this.selectedProject) {
        axios.get(`http://172.16.1.69:8002/api/v2/cluster/project/${this.selectedProject}/`)
          .then(response => {
            this.clusters = response.data;
          });
      } else {
        this.fetchClusters();
      }
    },
    formatTimeAgo(createdAt) {
      const createdTime = new Date(createdAt);
      const currentTime = new Date();
      const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000);

      if (timeDifferenceInSeconds < 60) {
        return `${timeDifferenceInSeconds} sec ago`;
      } else if (timeDifferenceInSeconds < 3600) {
        const minutes = Math.floor(timeDifferenceInSeconds / 60);
        return `${minutes} min ago`;
      } else if (timeDifferenceInSeconds < 86400) {
        const hours = Math.floor(timeDifferenceInSeconds / 3600);
        return `${hours} hour ago`;
      } else {
        const days = Math.floor(timeDifferenceInSeconds / 86400);
        return `${days} days ago`;
      }
    },
  },



};
</script>

<style scoped>
b {
  font-weight: 5px;

}

.link-style {
  text-decoration: none;
  color: black;
  font-weight: 600;
  transition: color 0.2s, border-bottom-color 0.2s;
}

.link-style-default {
  color: #ff007f;
  border-bottom: 2px solid #ff007f;
}


.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text {
  font-size: 20px;
  font-weight: bold;
  text-align: left;
  line-height: 30px;
}

.subtext {
  font-size: 16px;
  text-align: left;
  margin-top: 5px;
  line-height: 24px;
}

.delete-button {
  display: inline-block;
  vertical-align: middle;

  margin-left: 20px;
}

.progress-bar {
  width: 1800px;
  /* or any other desired width */
}
</style>
