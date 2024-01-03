

<template>
  <nav class=" bg-purple-600 Navbar fixed top-0 z-50 w-full border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
  <div class="px-3 py-3 lg:px-5 lg:pl-3">
    <div style="max-height: 33px;" class="flex items-center justify-between">
      <div class="flex items-center justify-start">

        <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar"
          type="button"
          class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
          <span class="sr-only">Open sidebar</span>
          <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" fill-rule="evenodd"
              d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z">
            </path>
          </svg>
        </button>

        <router-link to='/home' class="flex ml-2 md:mr-24">

          <span class="self-center text-xl font-semibold sm:text-2xl text-white dark:text-white">
            BitBlast
             <span class="text-gray-50 text-sm "> PostgreSQL Lifecycle Management </span>
             </span>
        </router-link>
      </div>
      <div class="flex items-center">
        <div class=" flex items-center ml-3">
          <div class="flex">
            <!-- <button v-if="isDark === false" @click="toggleDarkMode" id="theme-toggle" type="button"
              class=" mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
              <svg id="theme-toggle-dark-icon" class=" w-8 h-8" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
              </svg>
            </button>
            <button v-else @click="toggleDarkMode" id="theme-toggle" type="button"
              class="mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
              <svg id="theme-toggle-light-icon" class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                  fill-rule="evenodd" clip-rule="evenodd"></path>
              </svg>
            </button> -->

            <div @click="userToggle" class="flex mt-3 items-center justify-center h-8 w-8 text-lg text-purple-700 bg-white rounded-full">
              <button>A</button> 
            </div>
            <!-- <button @click="userToggle" type="button" class="flex text-sm mt-3 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" aria-expanded="false" data-dropdown-toggle="dropdown-user">
              <span class="sr-only">Open user menu</span>
                      <img class="w-8 h-8 rounded-full" src="@/assets/static/admin.jpeg" alt="user photo">
                    </button> -->
          </div>

          <div :class="{ 'hidden': !UserToggle }" class="fixed top-11 right-1
                  z-50  my-4 text-base list-none bg-white divide-y divide-gray-100
                  rounded shadow  dark:bg-gray-700 dark:divide-gray-600">
            <div class="px-4 py-3" role="none">
              <p class="text-sm text-gray-900 dark:text-white "  role="none">
                {{ Username }}
              </p>
              <p class="text-sm font-medium text-gray-900 truncate dark:text-gray-300" role="none">
                {{ Username }}comapny.com
              </p>
            </div>
            <ul class="py-1" role="none">
              <li>
                <a href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                  role="menuitem">Dashboard</a>
              </li>
              <li>
                <a href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                  role="menuitem">Settings</a>
              </li>
              <li>
                <a href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                  role="menuitem">Billing</a>
              </li>
              <li>
                <a @click.prevent="logout" href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                  role="menuitem">Sign out</a>
              </li>
            </ul>
          </div>

        </div>
      </div>
    </div>
  </div>
</nav> 
  

  <aside id="logo-sidebar"
  class="fixed bg-gradient-to-br from-purple-600 to-blue-500 top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform
       -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0 dark:dark:bg-gray-400  dark:border-gray-700"
  aria-label="Sidebar" style="background-color: #5F6F94;">
  <div class="bg-gradient-to-br from-purple-600 to-blue-500 h-full px-3 pb-4 overflow-y-auto bg-white dark:dark:bg-zinc-900" style="background-color: #5F6F94;">
    <ul class="space-y-2 font-medium">
      <li>
        <router-link to="/AdminDashboard" class="flex items-center p-2 bg-white text-gray-900 rounded-lg dark:bg-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <svg class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 21">
               <path d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z"/>
               <path d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"/>
            </svg>
            <span class="ms-3">Admin Dashboard</span>
         </router-link>
      </li>
  <hr>

  <li>
    <router-link to="/projects-management"
    :class="{ 'bg-slate-900 ': currentPage === 'projectsManagement' }"
      class="flex items-center p-2 bg-white dark:bg-gray-900 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group">
      <svg viewBox="64 64 896 896" focusable="false" data-icon="unordered-list" width="1em" height="1em"
       class="w-6 h-6" fill="currentColor" aria-hidden="true">
        <path
          d="M912 192H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zm0 284H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zm0 284H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zM104 228a56 56 0 10112 0 56 56 0 10-112 0zm0 284a56 56 0 10112 0 56 56 0 10-112 0zm0 284a56 56 0 10112 0 56 56 0 10-112 0z">
        </path>
      </svg>
      <span class="ml-3"> Projects  Management</span> 
    </router-link>
  </li>

  <li>
    <router-link to="/cluster-management" 
    :class="{ 'bg-slate-900 ': currentPage === 'clustersManagement' }"
      class="flex items-center p-2 bg-white text-gray-900 rounded-lg dark:bg-gray-900 dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group">
      <svg viewBox="64 64 896 896" focusable="false" data-icon="database" width="1em" height="1em" fill="currentColor"
        class="w-6 h-6" aria-hidden="true">
        <path
          d="M832 64H192c-17.7 0-32 14.3-32 32v832c0 17.7 14.3 32 32 32h640c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32zm-600 72h560v208H232V136zm560 480H232V408h560v208zm0 272H232V680h560v208zM304 240a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0z">
        </path>
      </svg>
      <span class="ml-3"> Clusters Management</span>
    </router-link>
  </li>

  <li>
    <router-link to="/users-management"
    :class="{ 'bg-slate-900 ': currentPage === 'usersManagement' }"
      class="flex items-center p-2 bg-white text-gray-900 rounded-lg dark:bg-gray-900 dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group">
      <svg
      class="w-8 h-8 text-black" 
      viewBox=""
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M18.2 9.08889C18.2 11.5373 16.3196 13.5222 14 13.5222C11.6804 13.5222 9.79999 11.5373 9.79999 9.08889C9.79999 6.64043 11.6804 4.65556 14 4.65556C16.3196 4.65556 18.2 6.64043 18.2 9.08889Z"
        fill="currentColor"
      />
      <path
        d="M25.2 12.0444C25.2 13.6768 23.9464 15 22.4 15C20.8536 15 19.6 13.6768 19.6 12.0444C19.6 10.4121 20.8536 9.08889 22.4 9.08889C23.9464 9.08889 25.2 10.4121 25.2 12.0444Z"
        fill="currentColor"
      />
      <path
        d="M19.6 22.3889C19.6 19.1243 17.0927 16.4778 14 16.4778C10.9072 16.4778 8.39999 19.1243 8.39999 22.3889V26.8222H19.6V22.3889Z"
        fill="currentColor"
      />
      <path
        d="M8.39999 12.0444C8.39999 13.6768 7.14639 15 5.59999 15C4.05359 15 2.79999 13.6768 2.79999 12.0444C2.79999 10.4121 4.05359 9.08889 5.59999 9.08889C7.14639 9.08889 8.39999 10.4121 8.39999 12.0444Z"
        fill="currentColor"
      />
      <path
        d="M22.4 26.8222V22.3889C22.4 20.8312 22.0195 19.3671 21.351 18.0949C21.6863 18.0039 22.0378 17.9556 22.4 17.9556C24.7197 17.9556 26.6 19.9404 26.6 22.3889V26.8222H22.4Z"
        fill="currentColor"
      />
      <path
        d="M6.64896 18.0949C5.98058 19.3671 5.59999 20.8312 5.59999 22.3889V26.8222H1.39999V22.3889C1.39999 19.9404 3.2804 17.9556 5.59999 17.9556C5.96219 17.9556 6.31367 18.0039 6.64896 18.0949Z"
        fill="currentColor"
      />
    </svg>
      <span class="ml-3"> Users Management</span>
    </router-link>
  </li>

  <hr>
 
  </ul>
  </div>
</aside>
</template>

<script>
// import { useDark, useToggle } from "@vueuse/core";
import fooTer from '@/components/fooTer.vue';

export default {
  
   components: {  
      fooTer,
   },
   data(){
  //  const isDark = useDark();
  //  const toggleDark = useToggle(isDark);
      return{
      //  isDark,
      //  toggleDark,
      Username: '', 
      UserToggle: false,
      }    
   },
   computed: {
    currentPage() {   
      return this.$route.name;
    },
  },

   created(){
      this.Username = sessionStorage.getItem("username");
   },
   methods: {
    toggleDarkMode() {
      this.toggleDark();
    },
    logout() {
      console.log("logout");
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      sessionStorage.removeItem('project_id');
      sessionStorage.removeItem('project_name');
      window.location.reload()
    },
    userToggle() {
      this.UserToggle = !this.UserToggle;
      },
   }


}
</script>
