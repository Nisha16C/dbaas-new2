import { createStore } from "vuex";
import axios  from "axios";

export default createStore({
  state: {
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

    backup_method:'',
    showSidenav: true,
    
    showNavbar: true,
    showFooter: true,
    showMain: true,
    layout: "default",
    username: null,
    selectedType: 'Standalone',
    selectedProvider: 'Cloudstack',
    postgres_version:'',

    project_name: '',
    project_id: '',
    selectedComputeOffering: null,
  },
  mutations: {
    setGlobalProjectName(state, project_name) {
      state.project_name = project_name;
    },
    setGlobalProjectId(state, project_id) {
      state.project_id = project_id;
    },
    setSelectedMethod(state, backup_method) {
      state.backup_method= backup_method;
    },


    setSelectedType(state, selectedType) {
      state.selectedType = selectedType;
    },
    setSelectedProvider(state, selectedProvider) {
      state.selectedProvider = selectedProvider;
    },
    setSelectedVersion(state, postgres_version) {
      state.postgres_version = postgres_version;
    },
    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },
    setSelectedOffering(state, selectedComputeOffering) {
      state.selectedComputeOffering = selectedComputeOffering;
    },
    // setSelectedMemory(state, memory) {
    //   state.selectedMemory = memory;
    // },
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
  },
  actions: {
    updateGlobalProjectName(context, project_name) {
      context.commit('setGlobalProjectName', project_name);
    },
    updateGlobalProjectId(context, project_id) {
      context.commit('setGlobalProjectId', project_id);
    },
    
    updateSelectedMethod(context, backup_method) {
      context.commit('setSelectedMethod', backup_method);
    },

    updateSelectedType(context, selectedType) {
      context.commit('setSelectedType', selectedType);
    },
    updateSelectedProvider(context, selectedProvider) {
      context.commit('setSelectedProvider', selectedProvider);
    },
    updateSelectedVersion(context, postgres_version) {
      context.commit('setSelectedVersion', postgres_version);
    },
    // updateSelectedCPUNumber(context, cpunumber) {
    //   context.commit('setSelectedCPUNumber', cpunumber);
    // },
    // updateSelectedMemory(context, memory) {
    //   context.commit('setSelectedMemory', memory);
    // },
    updateComputeOffering(context, selectedComputeOffering){
      context.commit('setSelectedOffering', selectedComputeOffering);
    },
    
    toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },

    // selectedOffering(project) {
    //   this.$store.commit('setSelectedCPUNumber', project.cpunumber);
    //   this.$store.commit('setSelectedMemory', project.memory);
    //   this.selectedComputeOffering = project.name;
    // },
 
    fetchFirstProject({ commit,  }, userId) {
      console.log(`store.js se call ${userId}`);
      axios.get(`http://172.16.1.56:8002/api/v2/project/user/${userId}/`)
        .then(response => {
          const firstProject = response.data[0];
          commit('setGlobalProjectName', firstProject.project_name);
          commit('setGlobalProjectId', firstProject.id);
        })
        .catch(error => {
          console.error('Error fetching first project:', error);
        });
    },
  },
  getters: {
    getUsername: (state) => state.username,
    getSelectedCPUNumber: (state) => state.selectedCPUNumber,
    getSelectedMemory: (state) => state.selectedMemory,
  },
   

});
 