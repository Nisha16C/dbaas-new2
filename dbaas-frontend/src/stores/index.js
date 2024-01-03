// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    hasResultPageReloaded: false,
  },
  mutations: {
    setResultPageReloaded(state, value) {
      state.hasResultPageReloaded = value;
    },
  },
});
