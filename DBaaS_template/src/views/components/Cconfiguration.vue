[5:41 AM] Ashish Sahu
<template>
  <div>
    <div class="card">
      <div class="card-header pb-0 px-3">
        <h6 class="mb-0">Choose you compute resource </h6>
      </div>
 
      <div class="card-body pt-4 p-3">
        <div class="table-responsive p-0">
          <table class="table align-items-center mb-0">
            <thead>
              <tr>
                <th class="text-uppercase text-secondary font-weight-bolder opacity-7"> Select</th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  Compute Offering </th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  CPU Cores</th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  CPU Speed (MHz)</th>
                <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                  Memory (MB) </th>
                <th class="text-secondary opacity-7"> </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="project in computeOfferings" :key="project.name">
                <div class="row">
                  <input type="radio" :value=project.name v-model="selectedComputeOffering" @change="updateOffering">
 
                </div>
                <td>
                  <div class="d-flex flex-column text-center">
 
                    {{ project.name }}
                  </div>
                </td>
                <td class="align-middle text-center">
                  <span class="d-flex flex-column text-center">{{ project.cpunumber }}</span>
                </td>
                <td>
                  <div class="d-flex flex-column text-center">
                    {{ project.cpuspeed }}
                  </div>
                </td>
                <td class="align-middle text-center">
                  <span class="d-flex flex-column text-center">{{ project.memory }}</span>
                </td>
                <td class="align-middle  text-center">
                  <svg xmlns="http://www.w3.org/2000/svg" v-if="isSelected(project.name)"
                    class="myclss  text-success mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <!-- <span v-if="isSelected(project.name)"
                                  class="d-flex flex-column text-center text-success">SELECTED</span> -->
                </td>
              </tr>
            </tbody>
          </table>
          <hr>
          <div class="form-group ml-3 mt-2 row">
            <label class="text-sm col-lg-5" for="retentionPeriod">Custom Storage(Gi):</label>
            <div class="input-group d-flex">
              <input type="text" class="form-control col-5" id="retentionPeriod" v-model="selectedStorageOffering" @change="updateStorage">
             <!-- <span class="text-md mt-1 ml-2"> </span> -->
              
            </div>
          </div>           
            
          <argon-button @click="Next()" color="success" size="md" variant="gradient">
            NEXT
          </argon-button>
        </div>
 
      </div>
    </div>
  </div>
</template>
 
<script>
import { mapState, mapActions } from 'vuex';
import ArgonButton from "@/components/ArgonButton.vue";
 
export default {
  components: {
    ArgonButton
  },
  data() {
    return {
      selected_value: '',
      selectedStorageOffering: null,
      computeOfferings: [],
      selectedComputeOffering: null,
    };
  },
  computed: {
    ...mapState(['selectedComputeOffering', 'selectedStorageOffering']),
 
  },
  mounted() {
    // Fetch data from the backend
    // Replace this with your actual API endpoint
    fetch('http://172.16.1.69:8000/api/v2/compute_offerings/')
      .then(response => response.json())
      .then(data => {
        // Assuming the data is structured as { "compute_offerings": [...] }
        this.computeOfferings = data.compute_offerings || [];
      })
      .catch(error => console.error('Error fetching data:', error));
  },
  methods: {
    ...mapActions(['updateComputeOffering', 'updateSelectedStorage']),
 
    updateOffering() {
      this.updateComputeOffering(this.selectedComputeOffering);
    },
    updateStorage(){
      this.updateSelectedStorage(this.selectedStorageOffering)
    },
    Next() {
      this.$router.push('/Cluster-Setting');
    },
 
    isSelected(projectName) {
      console.log("compute offering");
      if (this.selectedComputeOffering === projectName) {
 
        return true
      } else {
        return false;
      }
    },
  }
};
</script>
 
<style scoped>
.myclass {
  width: 100px;
  height: 100px;
}
 
/* Add your component-specific styles here */
</style>
 