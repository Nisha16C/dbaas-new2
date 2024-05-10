import { createStore } from "vuex";
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';


export default createStore({
  state: {
    apiUrl: API_ENDPOINT,

    hideConfigButton: false,

    isPinned: true,

    showConfig: false,

    sidebarType: "bg-white",

    isRTL: false,

    mcolor: "",

    darkMode: false,

    isNavFixed: false,

    isAbsolute: false,

    showNavs: true,

    showSidenav: true,

    showNavbar: true,

    showFooter: true,

    showMain: true,

    layout: "default",

    username: null,

    clusterType: "",

    clusterName: "",

    dbUsername: "",

    dbPassword: "",

    backupMethod: "",

    providerName: "",

    postgres_version: "",

    flavors: [],

    project_name: "",

    project_id: "",

    computeOfferings: null,

    selectedStorageOffering: null,

    selectedComputeOffering: null,
    // Other state properties
    activeDirectoryStatus: localStorage.getItem('activeDirectoryStatus') || 'Inactive' // Initialize status from local storage

  },

  mutations: {
    setGlobalProjectName(state, project_name) {
      state.project_name = project_name;
    },

    setGlobalProjectId(state, project_id) {
      state.project_id = project_id;
    },

    setSelectedType(state, clusterType) {
      state.clusterType = clusterType;
    },

    setSelectedProvider(state, providerName) {
      state.providerName = providerName;
    },

    setClusterName(state, clusterName) {
      state.clusterName = clusterName;
    },

    setDbUsername(state, dbUsername) {
      state.dbUsername = dbUsername;
    },

    setPassword(state, dbPassword) {
      state.dbPassword = dbPassword;
    },

    setBackupMethod(state, backupMethod) {
      state.backupMethod = backupMethod;
    },

    setSelectedVersion(state, postgres_version) {
      state.postgres_version = postgres_version;
    },

    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },

    setSelectedOffering(state, computeOfferings) {
      state.computeOfferings = computeOfferings;
    },

    setSelectedStorage(state, selectedStorageOffering) {
      state.selectedStorageOffering = selectedStorageOffering;
    },

    navbarMinimize(state) {
      const sidenav_show = document.querySelector(".g-sidenav-show");

      if (sidenav_show.classList.contains("g-sidenav-hidden")) {
        sidenav_show.classList.remove("g-sidenav-hidden");

        sidenav_show.classList.add("g-sidenav-pinned");

        state.isPinned = true;
      } else {
        sidenav_show.classList.add("g-sidenav-hidden");

        sidenav_show.classList.remove("g-sidenav-pinned");

        state.isPinned = false;
      }
    },

    sidebarType(state, payload) {
      state.sidebarType = payload;
    },

    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state.isNavFixed = true;
      } else {
        state.isNavFixed = false;
      }
    },

    setUsername(state, username) {
      state.username = username;
    },

    updateFlavors(state, newFlavors) {
      state.flavors = newFlavors;
    },
    // Mutation to update the status to Active
    enableActiveDirectory(state) {
      state.activeDirectoryStatus = 'Active';
      localStorage.setItem('activeDirectoryStatus', 'Active'); // Store status in local storage

    },
    // Mutation to update the status to Inactive
    disableActiveDirectory(state) {
      state.activeDirectoryStatus = 'Inactive';
      localStorage.setItem('activeDirectoryStatus', 'Inactive'); // Store status in local storage

    }

  },

  actions: {
    setFlavors({ commit }, newFlavors) {
      commit("updateFlavors", newFlavors);
    },

    updateGlobalProjectName(context, project_name) {
      context.commit("setGlobalProjectName", project_name);
    },

    updateGlobalProjectId(context, project_id) {
      context.commit("setGlobalProjectId", project_id);
    },

    updateSelectedType(context, clusterType) {
      context.commit("setSelectedType", clusterType);
    },

    updateSelectedProvider(context, providerName) {
      context.commit("setSelectedProvider", providerName);
    },

    updateClusterName(context, clusterName) {
      context.commit("setClusterName", clusterName);
    },

    updateUsername(context, dbUsername) {
      context.commit("setDbUsername", dbUsername);
    },

    updatePassword(context, dbPassword) {
      context.commit("setPassword", dbPassword);
    },

    updateBackupMethod(context, backupMethod) {
      context.commit("setBackupMethod", backupMethod);
    },

    updateSelectedVersion(context, postgres_version) {
      context.commit("setSelectedVersion", postgres_version);
    },

    updateSelectedStorage(context, selectedStorageOffering) {
      context.commit("setSelectedStorage", selectedStorageOffering);
    },

    updateComputeOffering(context, computeOfferings) {
      context.commit("setSelectedOffering", computeOfferings);
    },

    toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },

    // selectedOffering(project) {

    //   this.$store.commit('setSelectedCPUNumber', project.cpunumber);

    //   this.$store.commit('setSelectedMemory', project.memory);

    //   this.computeOfferings = project.name;

    // },

    fetchFirstProject({ commit }, userId) {
      axios

        .get(`${this.apiUrl}/api/v2/project/user/${userId}/`)

        .then((response) => {
          const firstProject = response.data[0];

          commit("setGlobalProjectName", firstProject.project_name);

          commit("setGlobalProjectId", firstProject.id);
        })

        .catch((error) => {
          console.error("Error fetching first project:", error);
        });
    },
  },

  getters: {
    getUsername: (state) => state.username,

    getSelectedCPUNumber: (state) => state.selectedCPUNumber,

    getSelectedMemory: (state) => state.selectedMemory,
  },
});
