<template>

    <main>

        <div class="container-fluid mt-7">

            <div class="card shadow-lg mt-n6">

                <div class="card-body p-3">

                    <div class="row gx-4">

                        <div class="col-auto my-auto">

                            <div class="h-100">

                                <h3 class="mb-1">Authentication Provider: ActiveDirectory <span

                                        class="badge badge-sm bg-gradient-danger rounded-pill">Inactive</span></h3>
 
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

                            <p class="text-sm yellow-background ">The ActiveDirectory authentication provider is

                                currently Disable.</p>

                            <hr>

                            <form @submit.prevent="submitForm">

                                <div class="row">

                                    <div class="modal-footer">

                                        <BB_Button color="success" size="md" variant="gradient"

                                            @click.prevent="disableLDAP" type="submit">

                                            Disable

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

// import ArgonInput from "@/components/BB_Input.vue";

import BB_Button from "@/components/BB_Button.vue";

import { API_ENDPOINT } from '@/../apiconfig.js';
 
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

        };

    },

    components: {  BB_Button },

    methods: {

        disableLDAP() {

            axios.post(`${this.apiUrl}/api/v5/reset_ldap_settings/`)

                .then(response => {

                    this.$router.push('/User-Management');

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
 
<style>

.yellow-background {

    background-color: rgb(252, 252, 128);

    color: black;

}
 
.red-background {

    background-color: rgb(255, 183, 116);

    color: black;

}

</style>
