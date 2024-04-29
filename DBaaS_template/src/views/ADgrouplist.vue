[5:47 PM] Aastha Gupta
<template>

    <main>

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

        <div class="py-4 container-fluid">

            <div class="row">

                <div class="col-md-12">

                    <div class="card">

                        <div class="card-body">

                            <h6>Active Directory Groups info</h6>

                            <div class="table-responsive p-0 mt-3">

                                <table class="table align-items-center mb-0">

                                    <thead>

                                        <tr>

                                            <th
                                                class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">

                                                Group Name

                                            </th>

                                            <th
                                                class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">

                                                Members

                                            </th>

                                        </tr>

                                    </thead>

                                    <tbody>

                                        <tr v-for="group in adGroups" :key="group.group_name">

                                            <td>

                                                <div>

                                                    <img :src="this.$store.state.darkMode || this.$store.state.sidebarType === 'bg-default' ? logoWhite : logo"
                                                        class="avatar avatar-sm me-3" />

                                                    {{ group.group_name }}

                                                </div>

                                            </td>

                                            <td>

                                                <ul class="list-unstyled m-0">

                                                    <li v-for="member in group.members" :key="member">

                                                        {{ member }}

                                                    </li>

                                                </ul>

                                            </td>
                                            <td class="align-middle">
                                                <argon-button color="success" size="md" variant="gradient"
                                                    @click="prepareUserRole(user)" type="button"
                                                    class="ml-4 btn btn-danger" data-toggle="modal"
                                                    data-target="#exampleModal2">
                                                    View Role
                                                </argon-button>
                                                <argon-button color="success" size="md" variant="gradient"
                                                    @click="prepareAssignRoles(user)" type="button"
                                                    class="ml-4 btn btn-danger" data-toggle="modal"
                                                    data-target="#exampleModal">
                                                    Assign Roles
                                                </argon-button>
                                            </td>

                                        </tr>

                                    </tbody>

                                </table>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </main>
    <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true">
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
                        :id="'roleCheckbox_' + role.name">
                    <label class="form-check-label" :for="'roleCheckbox_' + role.name">{{ role.name }}</label>
                </div>

                <div class="modal-footer">
                    <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false"
                        type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                        Cancel
                    </argon-button>
                    <argon-button color="danger" size="md" variant="gradient" @click.prevent="assignRoles(user)"
                        type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                        Assign Roles
                    </argon-button>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" ref="myModal" id="exampleModal2" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
                <div class="modal-header">
                    <h3 class="modal-title" id="exampleModalLabel">User Role</h3>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <!-- Inside your modal body -->
                <div class="form-check" v-if="selectedUser">
                    <label class="form-check-label">Username: {{ selectedUser.username }}</label><br>
                    <label class="form-check-label">Assigned Role: {{ formattedRoles || 'No Role Assign' }}</label>
                </div>

                <div class="modal-footer">
                    <argon-button color="secondary" size="md" variant="gradient" @click="isModalVisible = false"
                        type="button" class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal2">
                        Close
                    </argon-button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>

import { API_ENDPOINT } from '@/../apiconfig.js'; // Replace with actual API endpoint
// import axios from "axios";

import logo from "@/assets/img/userTable.png";
import ArgonButton from "@/components/BB_Button.vue";

import logoWhite from "@/assets/img/user.png";

export default {
    components: {
        ArgonButton,
    },

    data() {

        return {

            apiUrl: API_ENDPOINT,

            adGroups: [],

            logo,

            logoWhite,
            selectedRoles: '', // Changed to a string
            selectedUser: null,
            roles: [
                { id: 1, name: 'Admin' },
                { id: 2, name: 'Standard' },
                // Add more roles as needed
            ],

        };

    },

    created() {

        this.fetchADgroups();

    },
    computed: {

    },

    methods: {

        fetchADgroups() {

            fetch(`${this.apiUrl}/api/v1/ad-groups/`)

                .then(response => response.json())

                .then(data => {

                    if (data.error) {

                        console.error('Error fetching AD groups:', data.error);

                    } else {

                        this.adGroups = data.groups;

                    }

                })

                .catch(error => {

                    console.error('Error fetching AD groups:', error);

                });

        },
        assignRoleToGroup(groupName, roleName) {
            fetch(`${this.apiUrl}/api/assign-role/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    group_name: groupName,
                    role_name: roleName,
                }),
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.message);
                    } else {
                        alert('Failed to assign role: ' + data.message);
                    }
                })
                .catch(error => {
                    console.error('Error assigning role:', error);
                    alert('Failed to assign role. Please try again later.');
                });
        },
        prepareAssignRoles(group) {
            const roleName = this.selectedRoles;
            if (!roleName) {
                alert('Please select a role.');
                return;
            }
            if (!group || !group.group_name) {
                alert('Invalid group.');
                return;
            }
            this.assignRoleToGroup(group.group_name, roleName);
        },


    },

};

</script>

<style scoped>
.custom-age {

    width: 300px;

    height: 150px;

}
</style>
