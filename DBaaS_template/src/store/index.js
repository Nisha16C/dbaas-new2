
import { createStore } from "vuex";
 
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
    showSidenav: true,
    showNavbar: true,
    showFooter: true,
    showMain: true,
    layout: "default",
    username: null,
    selectedType: '',
    selectedProvider: '',
    postgres_version:'',
  },
  mutations: {
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
    updateSelectedType(context, selectedType) {
      context.commit('setSelectedType', selectedType);
    },
    updateSelectedProvider(context, selectedProvider) {
      context.commit('setSelectedProvider', selectedProvider);
    },
    updateSelectedVersion(context, postgres_version) {
      context.commit('setSelectedVersion', postgres_version);
    },
    toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },
 
    setUsername({ commit }, username) {
      commit("setUsername", username);
    },
  },
  getters: {
    getUsername: (state) => state.username,
  },
});
 