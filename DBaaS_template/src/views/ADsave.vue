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

                            <p :class="`${this.$store.state.darkMode ? 'w-background' : ' green-background'}`"
                                class="text-sm"
                                style="display: flex; justify-content: space-between; align-items: center;">

                                <span>The ActiveDirectory authentication provider is currently Enable.</span>

                                <span>

                                    <router-link to="ADuserForm">

                                        <BB_Button color="info" size="md" variant="gradient"
                                            style="font-size: 13px; margin-right: 10px; " type="submit">

                                            Edit Config

                                        </BB_Button>

                                    </router-link>

                                    <BB_Button color="danger" size="md" type="button" variant="gradient"
                                        style="font-size: 13px;" data-toggle="modal" data-target="#exampleModal">

                                        Disable

                                    </BB_Button>

                                    <!-- <BB_Button color="success" size="md" variant="gradient" 

                                        class="ml-4 btn btn-danger">

                                        Disable

                                    </BB_Button> -->

                                </span>

                            </p>

                            <hr><br>

                            <div>

                                <p>Server: http://172.16.1.69:8080/</p>

                                <p> Client ID: Administrator </p>

                            </div>

                            <hr>

                            <div>

                                <h4>Configure who should be able to login and use Rancher</h4><br>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="flexRadioDefault"
                                        id="flexRadioDefault1">
                                    <label class="form-check-label" for="flexRadioDefault1">
                                        Allow any valid user
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="flexRadioDefault"
                                        id="flexRadioDefault2" checked>
                                    <label class="form-check-label" for="flexRadioDefault2">
                                        Allow members of clusters and projects , plus authorized

                                        users & groups
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="flexRadioDefault"
                                        id="flexRadioDefault3" checked>
                                    <label class="form-check-label" for="flexRadioDefault2">
                                        Restrict access to only the authorized users & groups
                                    </label>
                                </div>

                            </div>

                            <form @submit.prevent="submitForm">

                                <div class="row">

                                    <div class="modal-footer">

                                        <BB_Button :color="buttonColor" :size="buttonSize" :variant="buttonVariant"
                                            @click.prevent="saveAndDisplayMessage" :disabled="isButtonDisabled">

                                            {{ buttonText }}

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

    <div v-show="deleteModal" class="modal fade" id="exampleModal" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalLabel" aria-hidden="true">

        <div class="modal-dialog" role="document">

            <div class="modal-content" :class="{ 'd-mode': isDarkMode }">
                <div class="modal-header">

                    <h5 class="modal-title" id="exampleModalLabel">Are you sure? </h5>

                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">

                        <span aria-hidden="true">&times;</span>

                    </button>

                </div>

                <div class="modal-body">

                    <p>You are attempting to disable this Auth Provider.</p>

                    <p>Be aware that cluster role template bindings,

                        project role template bindings, global role bindings , users,

                        tokens

                        will be all deleted.</p>

                    <p> Are you sure you want to proceed?</p>

                </div>

                <div class="modal-footer">

                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>

                    <!-- <router-link to="/signin"> -->

                    <button type="button" @click.prevent="disableActiveDirectoryAndSubmit" data-dismiss="modal"
                        class="btn btn-danger">

                        Disable</button>

                    <!-- </router-link> -->

                    <!-- <BB_Button color="success" size="md" variant="gradient" @click.prevent="disableLDAP" type="submit">

                        Disable

                    </BB_Button> -->

                </div>

            </div>

        </div>

    </div>

</template>

<script>

import setNavPills from "@/assets/js/nav-pills.js";

import setTooltip from "@/assets/js/tooltip.js";

// import ProfileCard from "./components/ProfileCard.vue";

// import ArgonInput from "@/components/BB_Input.vue";

import BB_Button from "@/components/BB_Button.vue";

import { API_ENDPOINT } from '@/../apiconfig.js';

import { mapMutations } from 'vuex';

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

            buttonColor: 'success',

            buttonSize: 'md',

            buttonVariant: 'gradient',

            buttonText: 'Save',

            isButtonDisabled: false

        };

    },

    components: { BB_Button },

    computed: {
        isDarkMode() {
            return this.$store.state.darkMode;
        },

        status() {

            return this.$store.state.activeDirectoryStatus;

        },

        statusClass() {

            return this.status === 'Active' ? 'bg-gradient-success rounded-pill' : 'bg-gradient-danger rounded-pill';

        }

    },

    methods: {

        ...mapMutations(['disableActiveDirectory']),

        disableLDAP() {

            axios.post(`${this.apiUrl}/api/v5/reset_ldap_settings/`)

                .then(response => {

                    this.$router.push('/signin');

                    console.log(response.data);

                    // handle success


                })

                .catch(error => {

                    console.error(error);

                    // handle error

                });

        },

        disableActiveDirectoryAndSubmit() {

            // Call the Vuex mutation to update the status

            this.disableActiveDirectory();

            // Call the submitForm() method to submit the form data

            this.disableLDAP();

        },

        saveAndDisplayMessage() {

            this.buttonText = 'Saved';

            this.isButtonDisabled = true;

            setTimeout(() => {

                this.buttonText = 'Save';

                this.isButtonDisabled = false;

            }, 3000); // 5000 milliseconds = 5 seconds

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
.green-background {

    background-color: rgb(192, 251, 125);

    color: black;

}

.red-background {

    background-color: rgb(255, 17, 0);


}

.w-background {
    background-color: rgb(29, 31, 129);
    color: rgb(255, 255, 255);
}

.d-mode {
    background-color: #1d1e52;
    color: #ffffff;
}
</style>
