<template>
    <main>
        <!-- Your existing HTML -->

        <div class="container-fluid mt-7">
            <div class="card shadow-lg mt-n6">
                <div class="card-body p-3">
                    <div class="row gx-4">
                        <div class="col-auto my-auto">
                            <div class="h-100">
                                <router-link to="/ADauthprovider">
                                    <i class="fas fa-arrow-left mr-2"></i>
                                </router-link>
                                <h5 class="mb-1 text-2xl">List Of Active Directory Groups</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Display groups and their members -->

        <div class="py-4 container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="card" style="height: 650px; overflow-y: auto;">
                        <div class="card-body">
                            <!-- Iterate over each AD group -->
                            <div v-for="group in adGroups" :key="group.group_name">
                                <!-- Group name with buttons on the same line -->
                                <div class="d-flex justify-content-between align-items-center">
                                    <h6 @click="toggleMembers(group)" class="group-name">{{ group.group_name }}</h6>
                                    <div>
                                        <!-- Assign Roles button -->
                                        <argon-button color="success" size="md" variant="gradient"
                                            @click="prepareAssignRoles(group)" type="button" class="ml-4 btn btn-danger"
                                            data-toggle="modal" data-target="#exampleModal">
                                            Assign Roles
                                        </argon-button>
                                    </div>
                                </div>
                                <!-- Horizontal line below group name -->
                                <hr />
                                <!-- Member list -->
                                <ul v-if="group.showMembers">
                                    <li v-for="member in group.members" :key="member">{{ member }}</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <!-- Role assignment modal -->
        <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog"
            aria-labelledby="exampleModalLabel" aria-hidden="true" @show="setSelectedRole">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2 class="modal-title" id="exampleModalLabel">Select Roles</h2>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <!-- Inside your modal body -->
                    <div class="form-check" v-for="role in roles" :key="role.id">
                        <input v-model="selectedRoles" class="form-check-input" type="radio" :value="role.name"
                            :id="'roleCheckbox_' + role.name" />
                        <label class="form-check-label" :for="'roleCheckbox_' + role.name">{{ role.name }}</label>
                    </div>
                    <div class="modal-footer">
                        <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false"
                            type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                            Cancel
                        </argon-button>
                        <argon-button color="danger" size="md" variant="gradient" @click.prevent="assignGroupRoles()"
                            type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                            Assign Role
                        </argon-button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from 'axios'; // Import axios for HTTP requests
import ArgonButton from "@/components/BB_Button.vue";

export default {
    data() {
        return {
            apiUrl: API_ENDPOINT,
            adGroups: [],
            roles: [
                { id: 1, name: 'Admin' },
                { id: 2, name: 'Standard' },
                // Add more roles as needed
            ],
            selectedGroup: null,
            selectedRoles: '', // Track selected roles for the current group
            selectedGroupRoles: {}, // Track selected roles for each group
        };
    },
    components: {
        ArgonButton,
    },
    created() {
        // Retrieve previously selected roles from local storage
        const storedRoles = JSON.parse(localStorage.getItem('selectedGroupRoles'));
        if (storedRoles) {
            this.selectedGroupRoles = storedRoles;
        }
        // Fetch AD groups
        this.fetchADGroups();
    },
    watch: {
        // Watch for changes in selectedGroupRoles and save to local storage
        selectedGroupRoles: {
            handler(newValue) {
                localStorage.setItem('selectedGroupRoles', JSON.stringify(newValue));
            },
            deep: true,
        },
    },
    methods: {
        fetchADGroups() {
            axios
                .get(`${this.apiUrl}/api/v1/list-gmember/`)
                .then(response => {
                    this.adGroups = response.data.groups.map(group => ({ ...group, showMembers: false }));
                })
                .catch(error => {
                    console.error('Error fetching AD groups:', error);
                });
        },
        toggleMembers(group) {
            group.showMembers = !group.showMembers;
        },
        prepareAssignRoles(group) {
            this.selectedGroup = group;
            this.selectedRoles = this.selectedGroupRoles[group.group_name] || ''; // Retrieve selected role or set to empty
            this.$refs.myModal.show(); // Show the role assignment modal
        },
        async assignGroupRoles() {
            try {
                if (!this.selectedGroup || !this.selectedRoles) {
                    console.error('Group or roles not selected.');
                    return;
                }

                // Prepare data for the API request
                const requestData = {
                    group_name: this.selectedGroup.group_name,
                    role_name: this.selectedRoles,
                    sAMAccountNames: this.selectedGroup.members, // Assuming members are needed for role assignment
                };

                // Make the API request to assign roles
                const response = await axios.post(`${this.apiUrl}/api/v1/adgroup-role/`, requestData);

                if (response.data.success) {
                    console.log('Roles assigned successfully:', response.data.message);

                    // Update local state with assigned role
                    this.selectedGroupRoles[this.selectedGroup.group_name] = this.selectedRoles;

                    // Optionally, you can close the modal or update UI here
                    // this.$refs.myModal.hide(); // Hide the modal after assignment
                } else {
                    console.error('Error assigning roles:', response.data.message);
                    // Handle error scenario
                }
            } catch (error) {
                console.error('Error assigning roles:', error);
                // Handle exception
            }
        },

    },
};
</script>

<style scoped>
.group-name {
    cursor: pointer;
}

.group-name:hover {
    color: blue;
}
</style>