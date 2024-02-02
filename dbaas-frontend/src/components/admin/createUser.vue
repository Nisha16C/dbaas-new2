<template>
  <adminLeftsidebar />

  <div class="container sm:ml-72 mt-20">
    <h2 class="text-lg mb-10 font-semibold text-gray-700 capitalize">
      New User Create
    </h2>
    <div class="grid gap-6 mb-6 md:grid-cols-2">
      <div>
        <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>
        <input v-model="userData.first_name" type="text" id="first_name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="First Name" required>
      </div>
      <div>
        <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>
        <input v-model="userData.last_name" type="text" id="last_name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Last Name" required>
      </div>
      <div>
        <label for="company" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Username</label>
        <input v-model="userData.username" type="text" id="company"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Username" required>
      </div>
      <div>
        <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone number</label>
        <input v-model="userData.phone" type="tel" id="phone"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="123-45-678" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required>
      </div>

    </div>
    <div class="mb-6">
      <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>
      <input v-model="userData.email" type="email" id="email"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="name@company.com" required>
    </div>
    <div class="mb-6">
      <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
      <input v-model="userData.password" type="password" id="password"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="•••••••••" required>
    </div>
    <div class="mb-6">
      <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm
        password</label>
      <input v-model="userData.cpassword" type="password" id="confirm_password"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="•••••••••" required>
    </div>
    <div class="flex items-start mb-6">
      <div class="flex items-center h-5">
        <input id="remember" type="checkbox" value=""
          class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800"
          required>
      </div>
      <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I agree with the <a href="#"
          class="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>
    </div>
    <button @click="createUserAdmin"
      class="relative inline-flex items-center justify-center  p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
      <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white  rounded-md group-hover:bg-opacity-0">
        Create New User
      </span>
    </button>
  </div>
</template>
<script>
import axios from 'axios';
import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue'

export default {
  components: {
    adminLeftsidebar
  },
  data() {
    return {
      userData: {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        username: '',
        password: '',
        cpassword: '',

      },
    };
  },
  methods: {
    async createUserAdmin() {
      // const toast = useToast(); // Initialize toast

      try {
        console.log('Sending User Data:', this.userData);

        const response = await axios.post('http://172.16.1.158:8002/api/v1/users/', this.userData);
        console.log('Response:', response.data);

        this.$router.push('/role-assign');
        // Clear the form after successful user creation
        this.userData = {
          first_name: '',
          last_name: '',
          email: '',
          phone: '',
          username: '',
          password: '',
          cpassword: '',

        };
      } catch (error) {
        // Handle errors (e.g., display error messages to the user)
        console.error('Error creating user:', error.response.data);

        // Display a toast notification for the error
        // toast.error('Failed to create user. Please check your data and try again.');
      }

    },
  },
}
</script>


<style scoped>
.blur-container {
  background-image: url('your-image-url.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  /* Adjust text color for visibility on the background */
  backdrop-filter: blur(10px);
  /* Adjust the blur intensity */
}
</style>