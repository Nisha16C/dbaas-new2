// store.js
import { defineStore } from 'pinia';
 
export const useInputStore = defineStore('input', {
  state: () => ({
    selectedType: '',
    selectedProvider: '',
    postgres_version:'',
  }),
  actions: {
    setType(value) {
      this.selectedType = value;
    },
    setProvider(value) {
      this.selectedProvider = value;
    },
    setVersion(value) {
      this.postgres_version = value;
    },
  },
});