<!-- UserDetailsComponent.vue -->
<template>
    <div v-show="loading" class="spinner">
        <div class="bg-white opacity-60% absolute right-1/2 bottom-1/2 transform translate-x-1/2 translate-y-1/2">
            <div class="p-4 bg-gradient-to-tr animate-spin from-green-500 to-blue-500 via-purple-500 rounded-full">
                <div class="bg-white rounded-full">
                    <div class="w-24 h-24 rounded-full"></div>
                </div>
            </div>
        </div>
    </div>
    <adminLeftsidebar />
    <div v-show="!loading">
        <div class="container sm:ml-72">
            <div class="mt-20 p-4 w-full flex">
                <div v-if="user">
                    <div class="flex">
                        <button class="flex mt-3 items-center justify-center h-12 w-12 bg-indigo-200 rounded-full">
                            {{ getFirstLetter(user.username) }}
                        </button>
                        <div class="px-2">
                            <div class="text-black font-semibold text-4xl">{{ user.username }} </div>
                            <p>{{ user.email }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="px-4 mt-10">
                <div v-if="error" class="text-red-500 ">{{ error }}</div>
                <div class="mt-10">
                    <button @click="openRoleAssignmentModal"
                        class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
                        <span
                            class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                            Assign Roles
                        </span>
                    </button>
                </div>
            </div>
            <div class="flex flex-col mt-8">
                <div class="py-2 -my-2 overflow-x-hidden sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
                    <div
                        class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
                        <table class="min-w-full">
                            <thead>
                                <tr>
                                    <th
                                        class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                        Role
                                    </th>
                                    <th
                                        class=" py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                        Description
                                    </th>

                                </tr>
                            </thead>

                            <tbody class="bg-white">
                                <tr>
                                    <td class=" border-b border-gray-200 whitespace-nowrap">
                                        owner
                                    </td>

                                    <td class=" py-4 border-b border-gray-200 whitespace-nowrap">
                                        Data read/write access to User

                                    </td>


                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <role-assignment-modal v-if="showRoleAssignmentModal" :roles="roles"
                @assign-roles="handleAssignRoles"></role-assignment-modal>
        </div>

    </div>
</template>
  
<script>
import axios from 'axios';
import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue'
import RoleAssignmentModal from '@/components/admin/RoleAssignmentModal.vue';

export default {
    components: {
        adminLeftsidebar,
        RoleAssignmentModal,
    },

    props: {
        userId: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            loading: true,
            user: null,
            roles: [],
            showRoleAssignmentModal: false,
        };
    },
    created() {
        this.fetchUserDetails();
        this.fetchRoles();
    },
    methods: {
        async fetchUserDetails() {
            console.log('User ID:', this.userId);
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`);
                this.user = response.data;
                console.log(this.user)
                this.loading = false;

            } catch (error) {
                console.error('Error fetching user details:', error);
            }
        },
        getFirstLetter(username) {
            return username.charAt(0, 1).toUpperCase();
        },
        fetchRoles() {
            this.roles = [
                { id:1, role: 'owner', name: 'Admin' },
                { id:2, role: 'Viewer', name: 'User' },
                { id:3, role: 'Editor', name: 'edit' },
            ];
        },

        openRoleAssignmentModal() {
            this.showRoleAssignmentModal = true;
        },

        handleAssignRoles(selectedRoles) {
            // Handle the logic to assign roles to the user
            // You can send an API request here to update the user's roles
            // using selectedRoles and this.userId
            console.log('Assigning roles:', selectedRoles);
            // Close the modal after handling the roles
            this.showRoleAssignmentModal = false;
        },
    },
};
</script>
  