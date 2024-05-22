<template>

  <main class="mt-0 main-content">

    <section>

      <div class="page-header min-vh-100">

        <div class="container">

          <div class="row">

            <div class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0">

              <div class="card card-plain">

                <div class="pb-0 card-header text-start">

                  <h4 class="font-weight-bolder">

                    Sign In as {{ username }}

                  </h4>

                  <p class="mb-0">Enter your Username and Password to sign in</p>

                </div>

                <div class="card-body">

                  <form role="form">

                    <div class="mb-3">

                      <argon-input type="text" v-model="username" placeholder="Username" name="Username" size="lg"
                        isRequired="true" />

                      <span class="text-danger" v-if="!username && showErrorMessages">Username is required</span>

                    </div>

                    <div class="mb-3 password-input">
                      <argon-input v-model="password" :type="showPassword ? 'text' : 'password'" placeholder="Password"
                        name="password" size="lg" @keyup.enter="login" />
                      <span class="toggle-password" @click="togglePasswordVisibility">
                        <i class="fas fa-eye" v-if="!showPassword"></i>
                        <i class="fas fa-eye-slash" v-else></i>
                      </span>
                      <span class="text-danger" v-if="!password && showErrorMessages">Password is required</span>
                    </div>

                    


                    <div class="text-center" v-if="showLoginWithLDAPButton">
                      <div v-if="error" class="text-danger">{{ error }}</div>
                      <argon-button v-if="showSignInButton" @click.prevent="login" class="mt-4" variant="gradient"
                        color="success" fullWidth size="lg">Sign In</argon-button>

                      <argon-button v-else @click.prevent="loginWithLDAP" class="mt-4" variant="gradient"
                        color="success" fullWidth size="lg">Login with Active Directory</argon-button>
                      <br><br>

                      <a v-if="showSignInButton" @click.prevent="showLDAPLogin" class="mt-2 text-success">Login with
                        Active Directory</a>
                      <a v-else @click.prevent="showSignIn" class="mt-2 text-success">Sign in</a>
                    </div>
                    <div class="text-center" v-else>
                      <div v-if="error" class="text-danger">{{ error }}</div>
                      <argon-button v-if="showSignInButton" @click.prevent="login" class="mt-4" variant="gradient"
                        color="success" fullWidth size="lg">Sign In</argon-button>
                    </div>

                  </form>
                </div>
              </div>
            </div>
            <div
              class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column">
              <div
                class="position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden"
                style="background-image: url('@/assets/img/login.svg'); background-size: cover;">
                <span class="mask bg-gradient-success opacity-6"></span>
                <h4 class="mt-5 text-white font-weight-bolder position-relative">
                  "Empower Your Data Journey with BitBlast!!"
                </h4>
                <p class="text-white position-relative">
                  The most effortless way to manage your database.
                </p>

              </div>

            </div>

          </div>

        </div>

      </div>

    </section>

  </main>

</template>

<script>

import axios from 'axios';

import ArgonInput from "@/components/BB_Input.vue";

import argonButton from "@/components/BB_Button.vue";

import { API_ENDPOINT } from '@/../apiconfig.js';

const body = document.getElementsByTagName("body")[0];


export default {

  name: "signin",

  components: {

    ArgonInput,

    argonButton,

  },

  data() {

    return {

      username: '',

      password: '',

      error: null,

      showErrorMessages: false,

      apiUrl: API_ENDPOINT,
      showSignInButton: true, // Initially show the Sign in button
      showLoginWithLDAPButton: false,
      showPassword: false, // Add this property


    };

  },

  created() {

    this.$store.state.hideConfigButton = true;

    this.$store.state.showNavbar = false;

    this.$store.state.showSidenav = false;

    this.$store.state.showFooter = false;

    body.classList.remove("bg-gray-100");
    this.fetchIsConnected();


  },

  beforeUnmount() {

    this.$store.state.hideConfigButton = false;

    this.$store.state.showNavbar = true;

    this.$store.state.showSidenav = true;

    this.$store.state.showFooter = true;

    body.classList.add("bg-gray-100");

  },

  methods: {
    fetchIsConnected() {
      axios.get(`${this.apiUrl}/api/v1/is-connected/`)
        .then(response => {
          const isConnectedValue = response.data.is_connected;
          console.log("jhingur", isConnectedValue)
          if (isConnectedValue === "True") {
            this.showLoginWithLDAPButton = true;
          } else if (isConnectedValue === "None") {
            this.showLoginWithLDAPButton = false;
          } else {
            console.error('Unexpected value for is_connected:', isConnectedValue);
            console.log("response do ", response)
          }
        })
        .catch(error => {
          console.error('Error fetching is_connected:', error);
          this.showLoginWithLDAPButton = false;
        });
    },

    loginWithLDAP() {

      // Make a POST request to your Django backend to initiate LDAP authentication

      axios.post(`${this.apiUrl}/api/v1/ldap-login/`, {

        username: this.username,

        password: this.password

      })

        .then(response => {

          // this.userdata = response.data.user_data;
          /// Extract user data from the response
          console.log("response : ", response)
          const userData = response.data.user_data;
          const userId = userData.id;
          const username = userData.username;
          console.log(" ldap user ");
          console.log("userData :", userData);
          console.log("userId :", userId);
          console.log("username :", username);

          // Store user_id and username in sessionStorage
          sessionStorage.setItem('user_id', userId);
          sessionStorage.setItem('username', username);

          if (username === 'admin' && username === 'Administrator') {

            this.$router.push('/admin-dashboard');

          } else {

            this.$router.push('/User-dashboard');

          }

        })

        .catch((error) => {

          this.error = error.response.data.error;

          this.error = "Invalid credentials. Please check again";

          this.password = null;

          this.username = null;

          setTimeout(() => {

            this.error = null;

          }, 3000);

        });

    },

    login() {

      if (!this.username || !this.password) {

        this.showErrorMessages = true;

        setTimeout(() => {

          this.showErrorMessages = false;

        }, 5000);

        return; // Do not proceed with login if fields are empty

      }

      const formData = {

        username_or_email: this.username,  // Use 'username' instead of 'username_or_email'

        password: this.password

      };

      axios

        .post(`${this.apiUrl}/api/v1/login/`, formData)

        .then((response) => {

          // const token = response.data.token;

          this.userdata = response.data.user_data;

          const user_id = this.userdata.id;

          const username = this.userdata.username;

          sessionStorage.setItem('user_id', user_id);

          sessionStorage.setItem('username', username);

          if (username === 'admin') {

            this.$router.push('/admin-dashboard');

          } else {

            this.$router.push('/User-dashboard');

          }

        })

        .catch((error) => {

          this.error = error.response.data.error;

          this.error = "Invalid credentials. Please check again";

          this.password = null;

          this.username = null;

          setTimeout(() => {

            this.error = null;

          }, 3000);

        });

    },
    showSignIn() {
      this.showSignInButton = true; // Show the Sign in button
    },
    showLDAPLogin() {
      this.showSignInButton = false; // Hide the Sign in button
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },

  },

};

</script>
<style scoped>
.password-input {
  position: relative;
}

.toggle-password {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  cursor: pointer;
}
</style>
