<!-- RoleAssignmentModal.vue -->
<template>
    <div class="modal">
      <div class="modal-content">
        <h2>Select Roles</h2>
        <div v-for="role in roles" :key="role.id">
          <input type="checkbox" v-model="selectedRoles" :value="role.id" />
          <label>{{ role.role }}</label>
        </div>
        <button @click="assignRoles">Assign Roles</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      roles: Array, // Array of available roles
    },
    data() {
      return {
        selectedRoles: [],
      };
    },
    methods: {
      assignRoles() {
        // Handle the logic to assign roles to the user
        // You can send an API request here to update the user's roles
        // using this.selectedRoles and this.userId
        // For simplicity, I'll just emit an event
        this.$emit('assign-roles', this.selectedRoles);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your modal styles here */
  .modal {
    /* Style your modal to overlay the page */
  }
  
  .modal-content {
    /* Style your modal content */
  }
  </style>
  