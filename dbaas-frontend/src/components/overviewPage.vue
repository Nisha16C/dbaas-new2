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
  <div v-show="!loading ">
    <div class="cluster p-4 sm:ml-64 mt-40 flex">
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

      <!-- <ul class="flex space-x-10 mx-10">
        <li>
          <a href="#" class="link-style text-2xl" :class="{ 'link-style-default': isActive }"
            @mouseenter="isActive = true" @mouseleave="isActive = false">
            Active Database
          </a>
        </li>
        <li>
          <a href="#" class="link-style text-2xl" :class="{ 'link-style-default': isDeleted }"
            @mouseenter="isDeleted = true" @mouseleave="isDeleted = false">
            Deleted
          </a>
        </li> 
      </ul> -->

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
                    View </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>


  <div v-show="isModalVisible" tabindex="-1" class="fixed top-0 left-0 right-0 bottom-0
      z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
    <div class="relative w-2/4">
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-100 bg-purple-600">
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
          <h3 class="mb-5 text- font-normal text-black dark:text-gray-400">
            {{ selectedCluster }}
          </h3>

          <!-- Input fields for provider -->
          <div class="px-4 mt-10">
            <div>
              <p v-if="contentList.length > 1" v-html="addLineBreaks(contentList[0].content)"></p>
              <p v-else class="mb-10">
                <svg aria-hidden="true"
                  class="inline w-10 h-10 text-gray-200 animate-spin dark:text-gray-200 fill-blue-600"
                  viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                    fill="currentColor" />
                  <path
                    d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                    fill="currentFill" />
                </svg>
                <span class="sr-only">Loading...</span>
              </p>
            </div>
            <div v-if="error" class="text-red-500 text-center mb-4">{{ error }}</div>
          </div>

          <button @click="toggleModal"
            class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 group-hover:from-green-400 group-hover:to-blue-600 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800">
            <span
              class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
              Close
            </span>
          </button>
        
        </div>
      </div>
    </div>
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


    };
  },
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.fetchProjects();
    this.fetchClusters();
  },
  methods: {
    toggleDarkMode() {
      this.toggleDark();
    },
    toggleModal(selectedCluster) {
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
      axios.get(`http://127.0.0.1:8000/api/v2/result/content/${this.selectedCluster}/`)
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
      axios.get(`http://127.0.0.1:8000/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects = response.data;

        });
    },
    fetchClusters() {
      axios.get(`http://127.0.0.1:8000/api/v2/cluster/user/${this.user_id}/`)
        .then(response => {
          this.clusters = response.data;
          this.loading = false;
        });
    },
    fetchClustersByProject() {
      if (this.selectedProject) {
        axios.get(`http://127.0.0.1:8000/api/v2/cluster/project/${this.selectedProject}/`)
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

b{
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
}</style>
