<template>
    <main>
        <!-- Your existing HTML -->
        <div class="container-fluid mt-7">
            <div class="card shadow-lg mt-n6">
                <div class="card-body p-3">
                    <div class="row gx-4">
                        <div class="col-auto my-auto">
                            <div class="h-100">
                                <h5 class="mb-1 text-2xl">List Of Active Directory Groups</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Display groups and their members -->
        <!-- Display groups and their members -->
        <div class="py-4 container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-body">
                            <!-- Iterate over each AD group -->
                            <div v-for="group in adGroups" :key="group.name">
                                <!-- Group name with buttons on the same line -->
                                <div class="d-flex justify-content-between align-items-center">
                                    <h6 @click="toggleMembers(group)" class="group-name">{{ group.name }}</h6>
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
                                <hr>
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



    </main>
    <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true" @show="setSelectedRole">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h2 class="modal-title" id="exampleModalLabel">Select Roles</h2>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <!-- Inside your modal body -->

                <div class="form-check" v-for="role in roles" :key="role.name">
                    <input v-model="selectedRoles" class="form-check-input" type="radio" :value="role.name"
                        :id="'roleCheckbox_' + role.name" :checked="role.name === selectedRole">
                    <!-- Check if role matches the selected role -->
                    <label class="form-check-label" :for="'roleCheckbox_' + role.name">{{ role.name }}</label>
                </div>


                <div class="modal-footer">
                    <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false"
                        type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                        Cancel
                    </argon-button>
                    <argon-button color="danger" size="md" variant="gradient" @click.prevent="assignGroupRoles(group)"
                        type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                        Assign Roles
                    </argon-button>
                </div>
            </div>
        </div>
    </div>


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
            selectedGroupRoles: {}, // Track selected roles for each group

        };
    },
    components: {
        ArgonButton,
    },
    created() {
        this.fetchADGroups();
    },
    methods: {
        setSelectedRole() {
            // Set the selected role for the current group
            this.selectedRole = this.selectedGroupRoles[this.selectedGroup.name];
        },
        fetchADGroups() {
            fetch(`${this.apiUrl}/api/v1/list-gmember/`)
                .then(response => response.json())
                .then(data => {
                    this.adGroups = data.ad_groups.map(group => ({ ...group, showMembers: false }));
                })
                .catch(error => {
                    console.error('Error fetching AD groups:', error);
                });
        },
        toggleMembers(group) {
            group.showMembers = !group.showMembers;
        },
        prepareAssignRoles(group) {
            // Set the selected group for role assignment
            this.selectedGroup = group;

            // Retrieve previously assigned role for the current group from local storage
            const savedRole = this.selectedGroupRoles[group.name];

            // If a role was previously assigned to the current group, set it as the selected role
            if (savedRole) {
                this.selectedRole = savedRole;
            } else {
                // If no role was previously assigned, set an empty string
                this.selectedRole = '';
            }
        },
        async assignGroupRoles() {
            try {
                if (!this.selectedGroup) {
                    console.error('No group selected.');
                    return;
                }
                const response = await axios.post(`${this.apiUrl}/api/v1/adgroup-role/`, {
                    group_name: this.selectedGroup.name, // Send selected group name for role assignment
                    role_name: this.selectedRoles, // Send selected roles for group assignment
                });
                if (response.data.success) {
                    console.log('Roles assigned to group successfully:', response.data.message);
                    // Update the UI or any other necessary actions after successful assignment
                    this.selectedGroupRoles[this.selectedGroup.name] = this.selectedRoles;
                    localStorage.setItem('selectedRoles', JSON.stringify(this.selectedGroupRoles));
                }
                this.isModalVisible = false;
            } catch (error) {
                console.error('Error assigning roles to group:', error);
            }
        }

    }
};
</script>



<style scoped>
.group-name {
    cursor: pointer;
}

.group-name:hover {
    color: blue;
}

.custom-age {
    width: 300px;
    height: 150px;
}

</style>
