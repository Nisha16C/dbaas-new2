<template>

    <main>

        <div class="container-fluid mt-7">

            <div class="card shadow-lg mt-n6">

                <div class="card-body p-3">

                    <div class="row gx-4">

                        <div class="col-auto my-auto">

                            <div class="h-100">

                                <h3 class="mb-1">Authentication Provider: ActiveDirectory <span class="badge badge-sm"
                                        :class="statusClass">{{ status }}</span></h3>

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

                            <p :class="`${this.$store.state.darkMode ? 'w-background' : 'y-background'}`" class="text-sm">The ActiveDirectory authentication provider is

                                currently Enable.</p>

                            <hr>

                            <form @submit.prevent="submitForm">

                                <div class="row">

                                    <h4>Configure an Active Directory account</h4> <br>

                                    <hr>

                                    <div class="col-md-6">

                                        <label for="last_name" class="form-control-label">Server URI *</label>

                                        <argon-input v-model="ldapServerURI" type="text"
                                            placeholder="ldap://0.0.0.0:Port" @input="validateServerURI" />

                                        <!-- Display error message if Server URI format is invalid -->

                                        <p v-if="errors.ldapServerURI" class="text-danger">{{ errors.ldapServerURI }}

                                        </p>

                                    </div>

                                    <div class="col-md-6">

                                        <label for="username" class="form-control-label">Server Connection Timeout

                                            (milliseconds) *</label>

                                        <argon-input v-model="serverConnectionTimeout" type="text"  value="10000"/>

                                    </div>

                                    <p :class="`${this.$store.state.darkMode ? 'w-background' : 'r-background'}`" class="text-sm"> BitBlast needs a service account that has

                                        read-only access to all of the domains that will be able to login,so that we can

                                        determine what groups a user is a member of when they make a request with an API

                                        key. </p>

                                    <div class="col-md-6">

                                        <label for="first_name" class="form-control-label">Service Account Distinguished

                                            Name *</label>

                                        <argon-input v-model="ServiceAccountDistinguishedName" type="text" placeholder="Service Account Name "
                                             />

                                    </div>

                                    <div class="col-md-6">

                                        <label for="last_name" class="form-control-label">Service Account Password

                                            *</label>

                                        <argon-input v-model="ldapServerBIND_PASSWORD" type="text" placeholder="" />

                                    </div>

                                    <div class="col-md-12">

                                        <label for="username" class="form-control-label">Default Login Domain *</label>

                                        <argon-input v-model="DefaultLoginDomain" type="text"
                                            placeholder="eg:mycompany " />

                                    </div>

                                    <div class="col-md-6">

                                        <label for="phone" class="form-control-label">User Search Base *</label>

                                        <argon-input v-model="ldapServerBIND_DN" type="text"
                                            placeholder="e.g.ou=users,dc=mycompany,dc=com" />

                                    </div>

                                    <div class="col-md-6">

                                        <label for="group_search_base" class="form-control-label">Group Search Base

                                            *</label>

                                        <argon-input v-model="ldapGroupSearch" type="text"
                                            placeholder="e.g. ou=groups,dc=mycompany,dc=com" />

                                    </div>

                                    <h4>Customize Schema</h4> <br>

                                    <hr>

                                    <!-- Users -->

                                    <div class="col-md-6">

                                        <h6>Users</h6>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Object Class

                                            </label>

                                            <argon-input v-model="userObjectClass" type="text" value="person" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Username

                                                Attribute</label>

                                            <argon-input v-model="usernameAttribute" type="text" value="name" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Login

                                                Attribute</label>

                                            <argon-input v-model="userLoginAttribute" type="text" value="sAMAccountName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">User Member

                                                Attribute</label>

                                            <argon-input v-model="userMemberAttribute" type="text"
                                                placeholder="e.g.ou=users,dc=mycompany,dc=com" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Search

                                                Attribute</label>

                                            <argon-input v-model="userData.m11" type="text"
                                                value="sAMAccountName|sn|givenName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Search Filter

                                            </label>

                                            <argon-input v-model="userSearchFilter" type="text" placeholder="" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">User Enable

                                                Attribute</label>

                                            <argon-input v-model="userEnableAttribute" type="text" value="userAccountControl" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="user_search_base" class="form-control-label">Disabled Status

                                                Bitmask</label>

                                            <argon-input v-model="disabledStatusBitmask" type="text" value="2" />

                                        </div>

                                    </div>
                                    <!-- Groups -->

                                    <div class="col-md-6">

                                        <h6>Groups</h6>

                                        <div class="col-md-12">

                                            <label class="form-control-label">Object Class

                                            </label>

                                            <argon-input v-model="groupObjectClass" type="text" value="group" />

                                        </div>

                                        <div class="col-md-12">

                                            <label class="form-control-label">Name

                                                Attribute</label>

                                            <argon-input v-model="groupNameAttribute" type="text" value="name" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Group Member User

                                                Attribute</label>

                                            <argon-input v-model="groupMemberUserAttribute" type="text"  value="distinguishedName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Search

                                                Attribute</label>

                                            <argon-input v-model="groupSearchAttribute" type="text" value="sAMAccountName" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Search

                                                Filter</label>

                                            <argon-input v-model="groupSearchFilter" type="text" placeholder="" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Group Member

                                                Mapping

                                                Attribute</label>

                                            <argon-input v-model="groupMamberMappingAttribute" type="text" value="member" />

                                        </div>

                                        <div class="col-md-12">

                                            <label for="group_search_base" class="form-control-label">Group DN

                                                Attribute</label>

                                            <argon-input v-model="groupDNattribute" type="text" value="distinguishedName" />

                                        </div><br>

                                        <div class="col-md-12">

                                            <input type="radio" /> Search direct and nested group memberships

                                            <br><input type="radio" /> Search only direct group memberships

                                        </div>

                                    </div>

                                    <h4>Test and Enable Authentication</h4> <br>

                                    <hr>

                                    <div class="col-md-6">

                                        <label for="first_name" class="form-control-label">Username *</label>

                                        <argon-input v-model="testUsername" type="text" placeholder="username" />

                                    </div>

                                    <div class="col-md-6">

                                        <label for="last_name" class="form-control-label">Password *</label>

                                        <argon-input v-model="testPassword" type="password"
                                            placeholder="password" />

                                    </div>

                                    <p class="text-sm">Note: The ActiveDirectory user you authenticate as will be

                                        associated

                                        as an alternate way to login to the Rancher user you are currently logged in as

                                        admin; all the global permissions, project, and cluster role bindings of this

                                        Rancher user will also apply to the ActiveDirectory user.</p>

                                    <div class="modal-footer">

                                        <BB_Button color="danger" size="md" variant="gradient"
                                            @click.prevent="OpenstackModal">

                                            Cancel

                                        </BB_Button>

                                        <BB_Button color="success" size="md" variant="gradient"
                                            @click.prevent="enableActiveDirectoryAndSubmit">

                                            Enable

                                        </BB_Button>

                                    </div>

                                </div>

                            </form>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </main>

</template>

<script>

import setNavPills from "@/assets/js/nav-pills.js";

import setTooltip from "@/assets/js/tooltip.js";

// import ProfileCard from "./components/ProfileCard.vue";

import ArgonInput from "@/components/BB_Input.vue";

import BB_Button from "@/components/BB_Button.vue";

import { API_ENDPOINT } from '@/../apiconfig.js';

import { mapState, mapMutations } from 'vuex'; // Import mapState and mapMutations from vuex

import axios from 'axios';

const body = document.getElementsByTagName("body")[0];

export default {

    name: "USER",

    data() {

        return {

            apiUrl: API_ENDPOINT,

            showMenu: false,

            ldapServerURI: "",

            userData: {

                first_name: '',

                username: '',

                email: '',

                phone: '',

                password: '',

                cpassword: '',

            },

            errors: {

                first_name: '',

                username: '',

                email: '',

                phone: '',

                password: '',

                cpassword: '',

            },

            successMessage: '',

            agreeTerms: false,

            ldapGroupSearch: '', // Initialize ldapGroupSearch data property
            serverConnectionTimeout: 10000,
            userObjectClass: 'person',
            usernameAttribute: 'name',
            userLoginAttribute: 'sAMAccountName',
            userSearchAttribute : 'sAMAccountName|sn|givenName',
            userEnableAttribute : 'userAccountControl',
            disabledStatusBitmask: 2, // Default value for Disabled Status Bitmask

            groupObjectClass: 'group',
            groupNameAttribute:'name',
            groupMemberUserAttribute: 'distinguishedName',
            groupSearchAttribute: 'sAMAccountName',
            groupMamberMappingAttribute: 'member',
            groupDNattribute: 'distinguishedName',


        };

    },

    components: { ArgonInput, BB_Button },

    computed: {
        ...mapState(['activeDirectoryStatus']), // Map activeDirectoryStatus from store to a computed property

        status() {

            return this.$store.state.activeDirectoryStatus;

        },

        statusClass() {

            return this.status === 'Active' ? 'bg-gradient-success rounded-pill' : 'bg-gradient-danger rounded-pill';

        }

    },

    methods: {

        ...mapMutations(['enableActiveDirectory']),

        submitForm() {

            // Check if the Server URI is valid before submitting the form

            if (!this.isValidUri(this.ldapServerURI)) {

                this.errors.ldapServerURI = 'Please enter a valid Server URI in the format ldap://0.0.0.0:Port';

                return; // Prevent form submission if input is invalid

            }

            const formdata = {

                ldapServerURI: this.ldapServerURI,

                ldapServerBIND_DN: this.ldapServerBIND_DN,

                ldapServerBIND_PASSWORD: this.ldapServerBIND_PASSWORD,

                ldapGroupSearch: this.ldapGroupSearch,
                serverConnectionTimeout: this.serverConnectionTimeout,
                ServiceAccountDistinguishedName: this. tuy,
                DefaultLoginDomain: this.DefaultLoginDomain,
                userObjectClass: this.userObjectClass,
                usernameAttribute: this.usernameAttribute,
                userLoginAttribute:this.userLoginAttribute,
                userMemberAttribute: this.userMemberAttribute,
                userSearchAttribute: this.userSearchAttribute,
                userSearchFilter: this.userSearchFilter,
                userEnableAttribute: this.userEnableAttribute,
                disabledStatusBitmask: this.disabledStatusBitmask,

                // ------------ group ------------------------

                groupObjectClass: this.groupObjectClass,
                groupNameAttribute: this.groupNameAttribute,
                groupMemberUserAttribute: this.groupMemberUserAttribute,
                groupSearchAttribute: this.groupSearchAttribute,
                groupSearchFilter:this.groupSearchFilter,
                groupMamberMappingAttribute:this.groupMamberMappingAttribute,
                groupDNattribute:this.groupDNattribute,
                testUsername:this.testUsername,
                testPassword:this.testPassword,

            }

            console.log(formdata);

            axios.post(`${this.apiUrl}/api/v5/update_ldap_settings/`, formdata)

                .then(response => {

                    console.log(response.data);

                    this.$router.push('/ADsave');

                }).catch(error => {

                    console.error(error);

                })

        },

        enableActiveDirectoryAndSubmit() {

            // Call the Vuex mutation to update the status

            this.enableActiveDirectory();

            // Call the submitForm() method to submit the form data

            this.submitForm();

        },

        // Method to validate Server URI input format using regular expression

        isValidUri(uri) {

            const uriPattern = /^ldap:\/\/\d+\.\d+\.\d+\.\d+:\d+$/;

            return uriPattern.test(uri);

        },

        // Method to validate Server URI on input

        validateServerURI() {

            if (!this.isValidUri(this.ldapServerURI)) {

                this.errors.ldapServerURI = 'Please enter a valid Server URI in the format ldap://0.0.0.0:Port';

            } else {

                this.errors.ldapServerURI = '';

            }

        },

        disableLDAP() {

            axios.post(`${this.apiUrl}/api/v5/reset_ldap_settings/`)

                .then(response => {

                    console.log(response.data);

                    // handle success

                })

                .catch(error => {

                    console.error(error);

                    // handle error

                });

        },

        mounted() {

            this.$store.state.isAbsolute = true;

            setNavPills();

            setTooltip();

        },

        beforeMount() {

            this.$store.state.imageLayout = "profile-overview";

            this.$store.state.showNavbar = false;

            this.$store.state.showFooter = true;

            this.$store.state.hideConfigButton = true;

            body.classList.add("profile-overview");

        },

        beforeUnmount() {

            this.$store.state.isAbsolute = false;

            this.$store.state.imageLayout = "default";

            this.$store.state.showNavbar = true;

            this.$store.state.showFooter = true;

            this.$store.state.hideConfigButton = false;

            body.classList.remove("profile-overview");

        },

    },

};

</script>


<style scoped>
.y-background {

    background-color: rgb(252, 252, 128);

    color: black;

}

.r-background {

    background-color: rgb(255, 183, 116);

    color: black;

}
.w-background {
  background-color: rgb(29, 31, 129);
  color: rgb(255, 255, 255);
}
</style>