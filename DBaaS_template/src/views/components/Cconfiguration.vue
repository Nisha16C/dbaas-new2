
<template>
    <div>
      <label for="compute-offering">Select Compute Offering:</label>
      <select v-model="selectedComputeOffering" id="compute-offering">
        <option v-for="offering in computeOfferings" :key="offering.name" :value="offering.name">
          {{ offering.name }}
        </option>
      </select>
  
      <div v-if="selectedComputeOffering">
        <h3>Selected Compute Offering Details:</h3>
        <p>CPU Number: {{ selectedOffering.cpunumber }}</p>
        <p>CPU Speed: {{ selectedOffering.cpuspeed }}</p>
        <p>Memory: {{ selectedOffering.memory }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        computeOfferings: [],
        selectedComputeOffering: null,
      };
    },
    computed: {
      selectedOffering() {
        // Find the selected offering based on its name
        return this.computeOfferings.find(offering => offering.name === this.selectedComputeOffering) || {};
      },
    },
    mounted() {
      // Fetch data from the backend
      // Replace this with your actual API endpoint
      fetch('http://172.16.1.92:8002/api/v2/compute_offerings/')
        .then(response => response.json())
        .then(data => {
          // Assuming the data is structured as { "compute_offerings": [...] }
          this.computeOfferings = data.compute_offerings || [];
        })
        .catch(error => console.error('Error fetching data:', error));
    },
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  
 