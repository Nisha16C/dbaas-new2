[7:11 AM] Nisha Chaurasiya
<template>

    <main>

        <div class="container-fluid mt-7">

            <div class="card shadow-lg mt-n6">

                <div class="card-body p-3">

                    <div class="row gx-4">

                        <div class="col-auto">

                            <div class="avatar avatar-xl position-relative">

                                <img src="../assets/img/cloudProvider.png" alt="profile_image"

                                    class="shadow-sm w-100 border-radius-lg" />

                            </div>

                        </div>

                        <div class="col-auto my-auto">

                            <div class="h-100">

                                <h5 class="mb-1 text-2xl" style="display: inline; margin-right: 15px;">Auth Providers</h5>

                                <router-link to="/ADuserlist" >

                                    <argon-button color="info" size="sm" variant="gradient" style="font-size: 15px;">

                                        List Of Acitve Directory

                                        Users

                                    </argon-button>

                                </router-link>
 
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

                            <p class="text-uppercase text-sm">Authentication Providers </p>

                            <p class="text-sm blue-background ">Local Authentication is always enabled, but you may select another additional authentication provider from those shown below.</p>

                            <br><br>

                            <div class="col-auto">
 
                                <!-- <router-link to="/ADuserForm">

                                    <img src="../assets/img/AD.webp" alt="profile_image"

                                    class="shadow-sm border-radius-lg auto custom-image" />

                                </router-link> -->

                                <router-link to="/ADuserForm" style="margin-right: 15px;">

                                    <img src="../assets/img/server.png" alt="profile_image"

                                        class="shadow-sm border-radius-lg auto custom-age image-hover" />

                                </router-link>

                                <!-- <router-link to="/ADuserForm">

                                    <img src="../assets/img/keycloak.png" alt="profile_image"

                                        class="shadow-sm border-radius-lg auto custom-age" />

                                </router-link> -->

                            </div>

                        </div>

                    </div>
 
                </div>

            </div>

        </div>
 
 
    </main>

</template>
 
<script>

// import ProfileCard from "./components/ProfileCard.vue";

// import ArgonInput from "@/components/BB_Input.vue";

import argonButton from "@/components/BB_Button.vue";

// import { API_ENDPOINT } from '@/../apiconfig.js';
 
// import axios from 'axios';
 
export default {

    // name: "Auth",

    // data() {

    //     return {

    //         },

    //     };

    // },

    components: {

        argonButton,

        // ArgonAlert,

    },

    // methods: {

    // },

};

</script>

<style scoped>

/* .custom-image {

        width: 200px;

        height: 200px;

    } */

.custom-age {

    width: 300px;

    height: 150px;

}

/* .image-hover:hover {

    transform: translateY(-5px); 

    transition: transform 0.3s ease; 

} */

.blue-background {

    background-color: rgb(128, 215, 252);

    color: black;
 
}

</style>