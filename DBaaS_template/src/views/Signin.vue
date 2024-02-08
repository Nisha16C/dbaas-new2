
<template>
  <main class="mt-0 main-content">
    <section>
      <div class="page-header min-vh-100">
        <div class="container">
          <div class="row">
            <div
              class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0"
            >
              <div class="card card-plain">
                <div class="pb-0 card-header text-start">
                  <h4 class="font-weight-bolder">
                    Sign In As {{ username }}
                  </h4>
                  <p class="mb-0">Enter your email and password to sign in</p>
                </div>
                <div class="card-body">
                  <form role="form">
                    <div class="mb-3">
                      <argon-input
                        type="text"
                        v-model="username"
                        placeholder="Username"
                        name="Username"
                        size="lg"
                        isRequired="true"
                      />
                    </div>
                    <div class="mb-3">
                      <argon-input
                        v-model="password"
                        type="password"
                        placeholder="Password"
                        name="password"
                        size="lg"
                      />
                    </div>
 
                    <div class="text-center">
 
                      <argon-button
                        @click.prevent="login"
                        class="mt-4"
                        variant="gradient"
                        color="success"
                        fullWidth
                        size="lg"
                        >Sign in</argon-button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div
              class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column"
            >
              <div
                class="position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden"
                style="
                  background-image: url('@/assets/img/login.svg');
                  background-size: cover;
                "
              >
                <span class="mask bg-gradient-success opacity-6"></span>
                <h4
                  class="mt-5 text-white font-weight-bolder position-relative"
                >
                  "Attention User is the new Database"
                </h4>
                <p class="text-white position-relative">
                  The more effortless way to manage you databases.
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
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";
const body = document.getElementsByTagName("body")[0];
 
 
export default {
  name: "signin",
  components: {
 
    ArgonInput,
 
    ArgonButton,
  },
 
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
 
  created() {
    this.$store.state.hideConfigButton = true;
    this.$store.state.showNavbar = false;
    this.$store.state.showSidenav = false;
    this.$store.state.showFooter = false;
    body.classList.remove("bg-gray-100");
  },
  beforeUnmount() {
    this.$store.state.hideConfigButton = false;
    this.$store.state.showNavbar = true;
    this.$store.state.showSidenav = true;
    this.$store.state.showFooter = true;
    body.classList.add("bg-gray-100");
  },
 
  methods: {
    login() {
      console.log('login form')
      const formData = {
        username_or_email: this.username,  // Use 'username' instead of 'username_or_email'
        password: this.password
      };
      console.log(formData)
 
      axios
        .post('http://172.16.1.97:8002/api/v1/login/', formData)
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
          this.password = null;
          this.username = null;
          setTimeout(() => {
            this.error = null;
          }, 1000);
        });
    },
  },
};
</script>