<!-- RoleAssignmentModal.vue -->
<template>
  <adminLeftsidebar />
  <div class="fixed mt-20 left-0 right-0 bottom-0
        z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
    <div class="relative w-[500px] h-96 relative bg-purple-600 rounded-lg shadow dark:bg-gray-800 ">
      <h2 class="m-5 text-2xl font-bold text-white dark:text-gray-400">Select Roles</h2>
      <hr class="h-px my-4 bg-gray-200 border-0 h-1 dark:bg-gray-700">
      <div class="mx-5 my-4 flex" v-for="role in roles" :key="role.id">
        <input class="pb-4" type="checkbox" v-model="selectedRoles" :value="role.role" />
        <label class=" mx-2 text-lg text-white dark:text-white">{{ role.role }}</label>
        <hr>
      </div>
      <button class="m-5 relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 
        rounded-lg group bg-white group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white 
        dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800"
        @click="assignRoles"><span class="relative text-lg px-5 py-2 duration-75 bg-white dark:bg-gray-900 rounded-md ">
          Assign Roles
        </span></button>
    </div>
  </div>
</template>
  
<script>
import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue';

export default {
  components: {
    adminLeftsidebar,
  },
  props: {
    roles: Array, // Array of available roles
  },
  data() {
    return {
      selectedRoles: [],
      roles: [],
    };
  },
  created() {
    this.fetchRoles();
  },
  methods: {
    assignRoles() {
      this.$emit('assign-roles', this.selectedRoles);
    },
    fetchRoles() {
      this.roles = [
        { id: 1, role: 'owner', name: 'Admin' },
        { id: 2, role: 'Viewer', name: 'User' },
        { id: 3, role: 'Editor', name: 'edit' },
      ];
    },
  },
};
</script>
  

  