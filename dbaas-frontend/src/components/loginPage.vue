<template>
  <section class="bg-gray-100  dark:bg-gray-900">

    <div class="flex flex-column items-center justify-center py-8  h-screen lg:py-0">
      <div
        class="w-[700px]  flex flex-column w-full bg-white h-[650px] shadow-xl dark:border md:mt-0 sm:max-w-[1200px] xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <div class="items-center justify-center">
            <a href="#" class="flex items-center mx-auto mb-6 text-2xl font-sans text-4xl text-gray-900 dark:text-white">
              BitBlast
            </a>
          </div>

          <h1 class="text-xl mt-20 leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Sign in to Your account
          </h1>
          <div class="space-y-4 md:space-y-6" action="#">
            <form @submit.prevent="login">
              <div>
                <label for="username" class="block mb-2 mt-5 text-sm font-medium text-gray-900 dark:text-white">Your
                  username</label>
                <input type="username" v-model="username"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-[400px] p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="username or email" required="">
              </div>
              <div>
                <label for="password"
                  class="block mb-2 mt-6 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                <input type="password" v-model="password" placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-[400px] p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  required="">
              </div>
              <!-- <div class="flex items-center mt-5 mb-10 justify-between">
                <a href="#" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">Forgot password?</a>
              </div> -->
              <div v-if="error" class="text-red-500 text-center  ">{{ error }}</div>
              <button @click="login"
                class="relative inline-flex items-center  justify-center w-[400px] p-0.5 mb-2 mt-10 me-2 overflow-hidden font-medium 
                text-gray-900  group bg-blue-700 group-hover:from-purple-600 group-hover:to-blue-500 
                hover:bg-blue-500 dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
                <span
                  class="relative px-5 py-2.5 transition-all ease-in duration-75 text-black">
                  Login
                </span>
              </button>
            </form>
          </div>
        </div>
        <div class="ml-[40px] r-0 ">
          <img class="w-[600px] rounded-l-3xl" src="../assets/static/login.png" alt="">
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'


export default {

  data() {
    return {
      tab: 'login',
      email: null,
      username: null,
      password: null,
      error: null,
      userdata: [],

    }

  },
  // computed:{
  //   ...mapWritableState(userModelstore, ['user_id'])
  // },

  methods: {
    login() {
      const formData = {
        username_or_email: this.username,
        password: this.password
      }
      axios
        .post('http://172.16.1.69:8002/api/v1/login/', formData)
        .then((response) => {
          this.success = 'Successfull LoggedIn!'

          const token = response.data.token

          this.userdata = response.data.user_data
          const user_id = this.userdata.id
          const username = this.userdata.username

          sessionStorage.setItem('user_id', user_id);
          sessionStorage.setItem('username', username);

          if (username == 'admin') {
            this.$router.push('/AdminDashboard')
          } else {
            this.$router.push('/home')
          }

        })
        .catch((error) => {
          this.error = error.response.data.error;
          this.password = null
          this.username = null
          setTimeout(() => {
            this.error = null;
          }, 1000);

        })
    },

  }
}
</script>



