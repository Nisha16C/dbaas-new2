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
  <adminLeftsidebar />
  <div v-show="!loading">

    <div class="container sm:ml-72">
      <div class="mt-20 p-4 w-full bg-gray-100 flex">
        <div class="text-black font-semibold text-4xl">Users Management</div>
      </div>
      <div class="px-4 mt-10">

        <div v-if="error" class="text-red-500 ">{{ error }}</div>
        <div class="mt-10">

          <router-link to="Createuser"
            class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
            <span
              class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
              Create New User
            </span>
          </router-link>

        </div>
      </div>
      <div class="w-full h-15 border-b-2 p-4 border-solid mt-20 flex items-center">


        <div class=" ">
          <div class="flex items-center px-5 py-6 bg-gray-100 rounded-md shadow-sm">
            <div class="p-3 bg-indigo-600 bg-opacity-75 rounded-full">
              <svg class="w-8 h-8 text-white" viewBox="0 0 28 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M18.2 9.08889C18.2 11.5373 16.3196 13.5222 14 13.5222C11.6804 13.5222 9.79999 11.5373 9.79999 9.08889C9.79999 6.64043 11.6804 4.65556 14 4.65556C16.3196 4.65556 18.2 6.64043 18.2 9.08889Z"
                  fill="currentColor" />
                <path
                  d="M25.2 12.0444C25.2 13.6768 23.9464 15 22.4 15C20.8536 15 19.6 13.6768 19.6 12.0444C19.6 10.4121 20.8536 9.08889 22.4 9.08889C23.9464 9.08889 25.2 10.4121 25.2 12.0444Z"
                  fill="currentColor" />
                <path
                  d="M19.6 22.3889C19.6 19.1243 17.0927 16.4778 14 16.4778C10.9072 16.4778 8.39999 19.1243 8.39999 22.3889V26.8222H19.6V22.3889Z"
                  fill="currentColor" />
                <path
                  d="M8.39999 12.0444C8.39999 13.6768 7.14639 15 5.59999 15C4.05359 15 2.79999 13.6768 2.79999 12.0444C2.79999 10.4121 4.05359 9.08889 5.59999 9.08889C7.14639 9.08889 8.39999 10.4121 8.39999 12.0444Z"
                  fill="currentColor" />
                <path
                  d="M22.4 26.8222V22.3889C22.4 20.8312 22.0195 19.3671 21.351 18.0949C21.6863 18.0039 22.0378 17.9556 22.4 17.9556C24.7197 17.9556 26.6 19.9404 26.6 22.3889V26.8222H22.4Z"
                  fill="currentColor" />
                <path
                  d="M6.64896 18.0949C5.98058 19.3671 5.59999 20.8312 5.59999 22.3889V26.8222H1.39999V22.3889C1.39999 19.9404 3.2804 17.9556 5.59999 17.9556C5.96219 17.9556 6.31367 18.0039 6.64896 18.0949Z"
                  fill="currentColor" />
              </svg>
            </div>

            <div class="mx-5">
              <h4 class="text-2xl font-semibold text-gray-700"> {{ users.length }} </h4>
              <div class="text-gray-500">Total Users</div>
            </div>
          </div>
        </div>


        <!-- Search option will hide here -->
        <!-- <div class="relative ml-4">
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
          </div> -->
      </div>

      <div class="flex flex-col mt-8">
        <div class="py-2 -my-2 overflow-x-hidden sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
          <div class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
            <table class="min-w-full">
              <thead>
                <tr>
                  <th
                    class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Name
                  </th>
                  <th
                    class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Status
                  </th>
                  <th
                    class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Role
                  </th>
                  <th
                    class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Created On
                  </th>
                  <th
                    class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Last Login
                  </th>
                  <th class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">Action</th>
                </tr>
              </thead>

              <tbody class="bg-white" v-for="(user, index) in users" :key="index">
                <tr v-if="user.username !== 'admin'">
                  <td class=" border-b border-gray-200 whitespace-nowrap">
                    <div class="flex items-center">
                      <div class="flex-shrink-0 ">
                        <button class="flex mt-3 items-center justify-center h-8 w-8 bg-indigo-200 rounded-full">
                          {{ getFirstLetter(user.username) }}
                        </button>
                      </div>

                      <div class="ml-4">
                        <div class="text-sm font-medium leading-5 text-gray-900">
                          {{ user.username }}
                        </div>
                        <div class="text-sm leading-5 text-gray-500">
                          {{ user.email }}
                        </div>
                      </div>
                    </div>
                  </td>

                  <td class=" py-4 border-b border-gray-200 whitespace-nowrap">
                    <div class="text-sm leading-5 text-gray-900">
                      <span v-if="user.is_active === true" class="inline-flex px-2 text-xs font-semibold leading-5
                         text-green-800 bg-green-100 rounded-full"> Active </span>

                    </div>

                  </td>

                  <td class=" py-4 border-b border-gray-200 whitespace-nowrap">
                    <span class="inline-flex px-2 text-xs  font-semibold leading-5
                        text-gray-500 rounded-full"> Owner </span>
                  </td>

                  <td class=" py-4 text-sm leading-5 text-gray-500 border-b border-gray-200 whitespace-nowrap">
                    {{ formatTimeAgo(user.date_joined) }}
                  </td>

                  <td class=" py-4 border-b border-gray-200 whitespace-nowrap">
                    <div><span class="inline-flex px-2 text-xs font-semibold leading-5
                     text-yellow-500 bg-yellow-100 rounded-full">{{ formatTimeAgo(user.last_login) }} </span>
                     </div>
                  </td>


                  <td
                    class="py-4 border-b border-gray-200 whitespace-nowrap">
                    <span @click="navigateToUser(user.id)"  class="text-indigo-600 hover:text-indigo-900">Edit</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
    
<script>
import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue'
import axios from 'axios';


export default {
  components: {
    adminLeftsidebar
  },

  data() {
    return {
      users: [],
      loading: true,
      project: {
        project_name: '',
        user: '', Username: '',

      }
    }
  },
  created() {
    this.Username = sessionStorage.getItem('username');
    this.fetchUsers()
  },
  methods: {
    getFirstLetter(username) {
      return username.charAt(0, 1).toUpperCase();
    },
    fetchUsers() {
      const user_id = this.project.user
      axios.get(`http://172.16.1.69:8000/api/v1/users/`)
        .then(response => {
          this.users = response.data;
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
    navigateToUser(userId) {
      this.$router.push({ name: 'roles', params: { userId: userId } });
    },
  }
}

</script>