<template>
  <div class=" w-full h-[100vh]">
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
      <div class="container sm:ml-72">
        <div class="mt-20 p-4 w-full bg-gray-100 flex">
          <div class="text-black font-semibold text-4xl">Projects</div>
        </div>
        <div class="px-4 mt-10">
          <div class="mb-6">
            <label for="projectname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Project
              Name</label>
            <input type="text" id="projetname" v-model="project.project_name" :class="{
              error: input1Error,
              shake: shakingInput === 'project.project_name',
            }"
              class="w-[300px] bg-gray-50 border border-gray-500 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5  dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Project Name" required />
          </div>

          <div v-if="error" class="text-red-500">{{ error }}</div>
          <div class="mt-10">
            <button to="Createuser" @click="saveProject"
              class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
              <span
                class="relative px-5 py-2.5 transition-all ease-in duration-75 text-black bg-white rounded-md group-hover:bg-opacity-0">
                Create New Project
              </span>
            </button>


          </div>
        </div>
        <div class="w-full h-15 border-b-2 p-4 border-solid mt-20 flex items-center">

          <div class=" ">
            <div class="flex items-center px-5 py-6 bg-gray-100 rounded-md shadow-sm">
              <div class="p-3 bg-indigo-600 bg-opacity-75 rounded-full">
                <svg viewBox="64 64 896 896" focusable="false" data-icon="unordered-list" width="1em" height="1em"
                  class="w-6 h-6" fill="currentColor" aria-hidden="true">
                  <path
                    d="M912 192H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zm0 284H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zm0 284H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zM104 228a56 56 0 10112 0 56 56 0 10-112 0zm0 284a56 56 0 10112 0 56 56 0 10-112 0zm0 284a56 56 0 10112 0 56 56 0 10-112 0z">
                  </path>
                </svg>
              </div>

              <div class="mx-5">
                <h4 class="text-2xl font-semibold text-gray-700"> {{ projects.length }} </h4>
                <div class="text-gray-500">Total Running Projects</div>
              </div>
            </div>
          </div>

        </div>

        <!-- New Table  -->
        <div class="flex flex-col mt-8 ">
          <div class="py-2 -my-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
            <div class="" v-if="projects.length === 0">
              <span class="text-gray-400 mb-2 text-2xl ml-96 ">No Projects found..</span>
            </div>

            <div v-else
              class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
              <table class="min-w-full">
                <thead>
                  <tr>
                    <th
                      class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                      ID & Project Name
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

                <tbody class="bg-white" v-for="(project, index) in projects" :key="index">
                  <tr>
                    <td class=" border-b border-gray-200 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="flex-shrink-0 ">
                          <button class="flex mt-3 items-center justify-center h-8 w-8 bg-indigo-200 rounded-full">
                            {{ project.id }}
                          </button>
                        </div>

                        <div class="ml-4">
                          <div class="text-sm font-medium leading-5 text-gray-900">
                            {{ project.project_name }}
                          </div>
                          <div class="text-sm leading-5 text-gray-500">
                            <!-- {{  }} -->
                          </div>
                        </div>
                      </div>
                    </td>


                    <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                      <span class="inline-flex px-2 text-xs font-semibold leading-5
                 text-yellow-500 bg-yellow-100 rounded-full">{{ formatTimeAgo(project.created_date) }} </span>
                    </td>
                    <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                      <span class="inline-flex px-2 text-xs font-semibold leading-5
                 text-yellow-500 bg-yellow-100 rounded-full">{{ formatTimeAgo(project.updated_date) }} </span>
                    </td>
                    <td
                      class="px-6 py-4 text-sm font-medium leading-5 text-right border-b border-gray-200 whitespace-nowrap">
                      <button @click.prevent="toggleModal(project.id, project.project_name)"
                        class="text-indigo-600 hover:text-indigo-900"> Edit </button>


                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>



        <!-- Project rename Model -->
        <div v-show="isModalVisible" tabindex="-1"
          class="fixed top-0 left-0 right-0 bottom-0 z-50 flex justify-center p-4 overflow-x-hidden overflow-y-auto md:inset-0">
          <div class="relative w-2/4">
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-100">
              <button @click="toggleModal" type="button"
                class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white">
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                  viewBox="0 0 14 14">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                </svg>
                <span class="sr-only">Close modal</span>
              </button>
              <div class="p-6">
                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <h3 class="text-lg leading-6 font-medium text-gray-900">Rename Project : {{ newProjectName }} </h3>
                  <div class="mb-6 mt-10">
                    <label for="Access_token" class="block mb-2 text-sm font-medium text-gray-700">
                      New Project Name:
                    </label>
                    <input type="text" v-model="newProjectName"
                      class="w-[300px] bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-blue-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                  </div>
                </div>

                <button to="Createuser" @click.prevent="renameProject"
                  class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
                  <span
                    class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                    Rename Project
                  </span>
                </button>




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
      </div>
      <!-- <fooTer /> -->
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
      loading: true,
      isActive: false,
      isDeleted: false,
      projects: [],
      error: '',
      user_id: null,
      project_name: '',
      input1Error: false,
      shakingInput: null,
      project: {
        project_name: '',
        user: '',
      }, newProjectName: '',

    };
  },
  methods: {
    saveProject() {
      this.input1Error = this.project.project_name === '';
      if (this.input1Error) {
        this.shakingInput = 'project.project_name'
        setTimeout(() => {
          this.shakingInput = null;
        }, 500);
      }
      else {
        console.log(this.project)
        axios.post("http://172.16.1.69:8002/api/v2/project/", this.project)
          .then(response => {
            this.fetchProject()
            window.location.reload()
          })
          .catch(error => {
            this.error = error.response.data.error;
            setTimeout(() => {
              this.error = '';
            }, 3000);
          });
      }
    },
    fetchProject() {
      const user_id = this.project.user
      axios.get(`http://172.16.1.69:8002/api/v2/project/user/${user_id}/`)
        .then(response => {
          this.projects = response.data;
          console.log(this.projects);
          this.loading = false;
        })
    },
    formatTimeAgo(createdAt) {
      const createdTime = new Date(createdAt)
      const currentTime = new Date()
      const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000)

      if (timeDifferenceInSeconds < 60) {
        return `${timeDifferenceInSeconds} sec ago`
      } else if (timeDifferenceInSeconds < 3600) {
        const minutes = Math.floor(timeDifferenceInSeconds / 60)
        return `${minutes} min ago`
      } else if (timeDifferenceInSeconds < 86400) {
        const hours = Math.floor(timeDifferenceInSeconds / 3600)
        return `${hours} hour ago`
      } else {
        const days = Math.floor(timeDifferenceInSeconds / 86400)
        return `${days} days ago`
      }
    },
  },
  created() {
    this.project.user = sessionStorage.getItem('user_id');
    this.fetchProject()
  },
  resetError(fieldName) {
    if (fieldName === 'project_name') {
      this.input1Error = false;
    } else if (fieldName === 'input2') {
      this.input2Error = false;
    }
  },

};
</script>
 
<style scoped>
.error {
  border: 2px solid red;
}

.main_content {
  background: linear-gradient(90deg, #25316D 0%, #8b7c59 100%);

}

.shake {
  animation: shake 0.5s ease-in-out 8 alternate;
}

@keyframes shake {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(10px, 0);
  }
}
</style>