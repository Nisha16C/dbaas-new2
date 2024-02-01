<template>
  <nav
    class="bg-purple-600 Navbar fixed top-0 z-50 w-full border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
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
              <span class="text-gray-50 text-sm "> (PostgreSQL Lifecycle Management) </span>
            </span>
          </router-link>

        </div>
        <div class="flex items-center">
          <div class=" flex items-center ml-3">
            <div class="flex">
              <!-- <button  id="theme-toggle" type="button"
                class=" mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
                <svg id="theme-toggle-dark-icon" class=" w-8 h-8" fill="currentColor" viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg">
                  <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
                </svg>
              </button>
              <button  id="theme-toggle" type="button"
                class="mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
                <svg id="theme-toggle-light-icon" class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                    fill-rule="evenodd" clip-rule="evenodd"></path>
                </svg>
              </button> -->

              <button @click="userToggle"
                class="flex  items-center justify-center text-purple-600 h-8 w-8 text-lg bg-white rounded-full">
                {{ getFirstLetter(Username) }}
              </button>
              <!-- <button @click="userToggle" type="button" class="flex text-sm mt-3 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" aria-expanded="false" data-dropdown-toggle="dropdown-user">
                <span class="sr-only">Open user menu</span>
                        <img class="w-8 h-8 rounded-full" src="@/assets/static/admin.jpeg" alt="user photo">
                    </button>
               -->
            </div>

            <div :class="{ 'hidden': !UserToggle }" class="fixed top-11 right-1
                    z-50  my-4 text-base list-none bg-white divide-y divide-gray-100
                    rounded shadow  dark:bg-gray-700 dark:divide-gray-600">
              <div class="px-4 py-3" role="none">
                <p class="text-sm text-gray-900 dark:text-white " role="none">
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
    class="bg-gradient-to-br from-purple-600 to-blue-500 fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform
         -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0 dark:dark:bg-gray-400  dark:border-gray-700"
    aria-label="Sidebar">
    <div
      class="bg-gradient-to-br from-purple-600 to-blue-500  h-full px-3 pb-4 overflow-y-auto bg-white dark:dark:bg-zinc-900"
      style="background-color: #5F6F94; overflow-x: auto; scrollbar-width: thin; scrollbar-color: #000000 #ddd;">
      <ul class="space-y-2 font-medium">
        <li>
          <!-- showing project_name button-->
          <button @click="projectToggle" v-if="!project_name" class="flex items-center p-2 mt-1 text-gray-900 rounded-lg
              w-56 bg-white  dark:text-white dark:bg-gray-800
             hover:bg-gray-300 dark:hover:bg-gray-800 group">Select Projects

          </button>

          <button @click="projectToggle" v-else class="flex items-center p-2 mt-1 bg-white text-gray-900 rounded-lg
              w-56 dark:text-white dark:bg-gray-800
             hover:bg-gray-300 dark:hover:bg-gray-800 group"> {{ project_name }}
            <span class="relative left-20  "> <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none"
                xmlns="http://www.w3.org/2000/svg" transform="rotate(270)">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M12.7071 14.7071C12.3166 15.0976 11.6834 15.0976 11.2929 14.7071L6.29289 9.70711C5.90237 9.31658 5.90237 8.68342 6.29289 8.29289C6.68342 7.90237 7.31658 7.90237 7.70711 8.29289L12 12.5858L16.2929 8.29289C16.6834 7.90237 17.3166 7.90237 17.7071 8.29289C18.0976 8.68342 18.0976 9.31658 17.7071 9.70711L12.7071 14.7071Z"
                    fill="#000000"></path>
                </g>
              </svg></span>
          </button>


          <!-- Dropdown menu -->
          <div style="max-height: 250px;" v-if="projects_list.length > 0" :class="{ 'hidden': !ProjectToggle }" class="ml-[245px] 
              absolute top-0 mt-[59px]  overflow-auto w-[250px]  text-black divide-y p-6
             divide-gray-100  z-50  shadow bg-purple-500 dark:bg-gray-700 dark:divide-gray-600">
            <p class="bg-gray-100 p-2 rounded-md mb-4">Projects list</p>

            <ul v-for="(project, index) in projects_list" :key="index">
              <li class="mb-5 bg-white p-2 rounded-md">

                <button @click="selected_project(project.project_name, project.id)">
                  {{ project.project_name }}
                </button>

              </li>
            </ul>
            <label class="mt-12  ">

              <router-link to="/projects"
                class="relative inline-flex items-center justify-center p-0.5 mb-5 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
                <span
                  class="relative px-5 py-2.5 transition-all ease-in duration-75 text-black bg-white rounded-md group-hover:bg-opacity-0">
                  Create New Project
                </span>
              </router-link>

            </label>
          </div>

          <div v-else :class="{ 'hidden': !ProjectToggle }" class="ml-[245px] absolute top-0 mt-[59px]
          bg-gray-300 text-black w-56 
          divide-y p-3
          divide-gray-100  z-50  shadow  dark:divide-gray-600 dark:text-white dark:bg-gray-800">

            <label for="" class="mb-10 p-5"> No Projects found </label> <br>
            <br>

            <label>
              <router-link to="/projects"
                class="bg-gray-200 text-black w-96 p-2 mt-10 text-center  dark:bg-gray-700 dark:text-white rounded-md">
                Create New Project
              </router-link>
            </label>
          </div>



        </li>
        <hr>
        <li>
          <router-link to="/home" :class="{ 'bg-slate-400 ': currentPage === 'home' }" class="flex items-center p-2 mt-5 bg-white text-black rounded-lg dark:text-white dark:bg-gray-800
         hover:bg-gray-300 dark:hover:bg-gray-700 group">
            <!-- SVG -->
            <svg class="w-6 h-6" viewBox="64 64 896 896" focusable="false" data-icon="layout" width="1em" height="1em"
              fill="currentColor" aria-hidden="true">
              <path
                d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32zm-696 72h136v656H184V184zm656 656H384V384h456v456zM384 320V184h456v136H384z">
              </path>
            </svg>
            <span class="ml-3">Overview</span>
          </router-link>
        </li>

        <li>
          <router-link to="/Projects" :class="{ 'bg-slate-400 ': currentPage === 'projects' }" class="flex items-center p-2  bg-white text-black  rounded-lg  hover:bg-gray-300
         dark:hover:bg-gray-700 group dark:text-white dark:bg-gray-800">
            <svg class="w-6 h-6" viewBox="64 64 896 896" focusable="false" data-icon="unordered-list" width="1em"
              height="1em" fill="currentColor" aria-hidden="true">
              <path
                d="M912 192H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zm0 284H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zm0 284H328c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h584c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zM104 228a56 56 0 10112 0 56 56 0 10-112 0zm0 284a56 56 0 10112 0 56 56 0 10-112 0zm0 284a56 56 0 10112 0 56 56 0 10-112 0z">
              </path>
            </svg>
            <span class="ml-3"> Projects </span>
          </router-link>
        </li>

        <li>
          <router-link to="/overview" :class="{ 'bg-slate-900 ': currentPage === 'overview' }"
            class="flex items-center p-2  bg-white text-black  rounded-lg dark:text-white dark:bg-gray-800 hover:bg-gray-300 dark:hover:bg-gray-700 group">
            <svg class="w-6 h-6" viewBox="64 64 896 896" focusable="false" data-icon="database" width="1em" height="1em"
              fill="currentColor" aria-hidden="true">
              <path
                d="M832 64H192c-17.7 0-32 14.3-32 32v832c0 17.7 14.3 32 32 32h640c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32zm-600 72h560v208H232V136zm560 480H232V408h560v208zm0 272H232V680h560v208zM304 240a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0z">
              </path>
            </svg>
            <span class="ml-3"> Clusters </span>
          </router-link>
        </li>

        <li>
          <router-link to="/providers" :class="{ 'bg-slate-900 ': currentPage === 'providers' }"
            class="flex items-center p-2  bg-white text-black rounded-lg dark:text-white dark:bg-gray-800 hover:bg-gray-300 dark:hover:bg-gray-700 group">
            <svg class="w-6 h-6" viewBox="64 64 896 896" focusable="false" data-icon="cloud" width="1em" height="1em"
              fill="currentColor" aria-hidden="true">
              <path
                d="M811.4 418.7C765.6 297.9 648.9 212 512.2 212S258.8 297.8 213 418.6C127.3 441.1 64 519.1 64 612c0 110.5 89.5 200 199.9 200h496.2C870.5 812 960 722.5 960 612c0-92.7-63.1-170.7-148.6-193.3zm36.3 281a123.07 123.07 0 01-87.6 36.3H263.9c-33.1 0-64.2-12.9-87.6-36.3A123.3 123.3 0 01140 612c0-28 9.1-54.3 26.2-76.3a125.7 125.7 0 0166.1-43.7l37.9-9.9 13.9-36.6c8.6-22.8 20.6-44.1 35.7-63.4a245.6 245.6 0 0152.4-49.9c41.1-28.9 89.5-44.2 140-44.2s98.9 15.3 140 44.2c19.9 14 37.5 30.8 52.4 49.9 15.1 19.3 27.1 40.7 35.7 63.4l13.8 36.5 37.8 10c54.3 14.5 92.1 63.8 92.1 120 0 33.1-12.9 64.3-36.3 87.7z">
              </path>
            </svg>
            <span class="ml-3"> Providers </span>
          </router-link>
        </li>

        <hr>
        <li>
          <router-link to="/user-monitoring" :class="{ 'bg-slate-900 ': currentPage === 'providers' }"
            class="flex items-center p-2 mt-5  bg-white text-black rounded-lg dark:text-white dark:bg-gray-800 hover:bg-gray-300 dark:hover:bg-gray-700 group">
            <svg class="w-6 h-6" fill="#000000" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink" width="64px" height="64px" viewBox="0 0 412.998 412.998"
              xml:space="preserve">
              <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
              <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
              <g id="SVGRepo_iconCarrier">
                <g>
                  <g>zz
                    <g>
                      <path
                        d="M392.998,28.339H20c-11.046,0-20,8.954-20,20v234c0,11.046,8.954,20,20,20h139.499v45.32h-54.283 c-10.201,0-18.5,8.299-18.5,18.5s8.299,18.5,18.5,18.5h202.566c10.201,0,18.5-8.299,18.5-18.5s-8.299-18.5-18.5-18.5h-54.283 v-45.32h139.499c11.046,0,20-8.954,20-20v-234C412.998,37.293,404.044,28.339,392.998,28.339z M382.998,272.339H30v-214h352.998 V272.339z">
                      </path>
                      <path
                        d="M134.589,235.304c7.563,0,13.701-6.136,13.701-13.699v-65.156c0-7.564-6.139-13.697-13.701-13.697 c-7.564,0-13.695,6.133-13.695,13.697v65.155C120.894,229.168,127.024,235.304,134.589,235.304z">
                      </path>
                      <path
                        d="M182.53,235.304c7.564,0,13.695-6.136,13.695-13.699V108.506c0-7.564-6.131-13.695-13.695-13.695 c-7.566,0-13.699,6.131-13.699,13.695v113.099C168.831,229.168,174.964,235.304,182.53,235.304z">
                      </path>
                      <path
                        d="M230.468,235.304c7.566,0,13.699-6.136,13.699-13.699v-84.333c0-7.564-6.133-13.695-13.699-13.695 c-7.562,0-13.693,6.131-13.693,13.695v84.333C216.771,229.168,222.902,235.304,230.468,235.304z">
                      </path>
                      <path
                        d="M278.411,235.304c7.562,0,13.692-6.136,13.692-13.699v-98.714c0-7.564-6.132-13.697-13.692-13.697 c-7.564,0-13.701,6.133-13.701,13.697v98.714C264.71,229.168,270.847,235.304,278.411,235.304z">
                      </path>
                    </g>
                  </g>
                </g>
              </g>
            </svg>

            <span class="ml-3"> Monitoring </span>
          </router-link>
        </li>
        <li>
          <router-link to="" :class="{ 'bg-slate-900 ': currentPage === 'providers' }"
            class="flex items-center p-2  bg-white text-black rounded-lg dark:text-white dark:bg-gray-800 hover:bg-gray-300 dark:hover:bg-gray-700 group">
            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
              <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
              <g id="SVGRepo_iconCarrier">
                <path d="M19 16V22M19 22L22 19M19 22L16 19" stroke="#000000" stroke-width="1.5" stroke-linecap="round"
                  stroke-linejoin="round"></path>
                <path d="M4 6V12C4 12 4 15 11 15C18 15 18 12 18 12V6" stroke="#000000" stroke-width="1.5"
                  stroke-linecap="round" stroke-linejoin="round"></path>
                <path d="M11 3C18 3 18 6 18 6C18 6 18 9 11 9C4 9 4 6 4 6C4 6 4 3 11 3Z" stroke="#000000"
                  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                <path d="M11 21C4 21 4 18 4 18V12" stroke="#000000" stroke-width="1.5" stroke-linecap="round"
                  stroke-linejoin="round"></path>
              </g>
            </svg>
            <span class="ml-3"> Backup </span>
          </router-link>
        </li>

        <li class="absolute bottom-14">
          <a href="https://www.postgresql.org/docs/" :class="{ 'bg-slate-900 ': currentPage === 'overview' }" class="flex items-center p-2  bg-white text-black  transition duration-75 rounded-lg hover:bg-gray-300
         dark:hover:bg-gray-700 dark:text-white dark:bg-gray-800 group w-[220px] ">
            <svg
              class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
              aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
              <path
                d="M16 14V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 0 0 0-2h-1v-2a2 2 0 0 0 2-2ZM4 2h2v12H4V2Zm8 16H3a1 1 0 0 1 0-2h9v2Z" />
            </svg>
            <span class="ml-3">Documentation</span>
          </a>
        </li>
        <li class="absolute bottom-2">
          <a href="#" class="flex items-center p-2 cursor-not-allowed  bg-white text-black  transition duration-75 rounded-lg
         hover:bg-gray-300 dark:hover:bg-gray-700 dark:text-white dark:bg-gray-800 group w-[220px] ">
            <svg
              class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
              aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 21 21">
              <path
                d="m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z" />
            </svg>
            <span class="ml-3">Help</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>
 
 
<script>
// import { useDark, useToggle } from "@vueuse/core";
import axios from "axios";

export default {
  data() {
    // const isDark = useDark();
    // const toggleDark = useToggle(isDark);

    return {
      // isDark,
      // toggleDark,

      isDropdownOpen: false,
      ProjectToggle: false,
      UserToggle: false,
      Username: '',
      user_id: '',
      project_name: '',
      project_id: '',
      projects_list: [],

    };
  },
  created() {
    this.Username = sessionStorage.getItem('username');
    this.user_id = sessionStorage.getItem("user_id");


    this.fetchProject();

    this.project_name = sessionStorage.getItem('project_name');
    this.project_id = sessionStorage.getItem('project_id');

  },
  computed: {
    currentPage() {
      return this.$route.name;
    },
  },
  methods: {
    fetchProjectName() {
      this.project_name = sessionStorage.getItem('project_name');
      this.ProjectToggle = !this.ProjectToggle;
    },
    fetchFirstProjectName() {
      this.project_name = sessionStorage.getItem('project_name');

    },
    toggleDarkMode() {
      this.toggleDark();
    },
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen
    },
    projectToggle() {
      this.ProjectToggle = !this.ProjectToggle;
    },
    userToggle() {
      this.UserToggle = !this.UserToggle;
    },
    selected_project(project_name, project_id) {
      sessionStorage.setItem('project_id', project_id);
      sessionStorage.setItem('project_name', project_name);
      this.fetchProjectName();
    },
    logout() {
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      sessionStorage.removeItem('project_id');
      sessionStorage.removeItem('project_name');
      window.location.reload()
    },
    getFirstLetter(username) {
      return username.charAt(0, 1).toUpperCase();
    },

    fetchProject() {
      axios.get(`http://172.16.1.69:8002/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.projects_list = response.data;
          sessionStorage.setItem('project_id', this.projects_list[0].id)
          sessionStorage.setItem('project_name', this.projects_list[0].project_name)

          this.fetchFirstProjectName();
        })
    },
  },

};
</script>

<style scoped> .leftsidebar {
   background: linear-gradient(90deg, #25316D 0%, #8b7c59 100%);

 }</style>