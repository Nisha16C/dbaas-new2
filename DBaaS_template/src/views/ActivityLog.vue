
<template>
    <main>
      <div class="container-fluid">
        <div
          class="page-header min-height-100"
          style="
            /* background-image: url('https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80'); */
            margin-right: -24px;
            margin-left: -34%;
          "
        >
          <span class="mask bg-gradient-success opacity-6"></span>
        </div>
        <div class="card shadow-lg mt-n6  w-full" >
          <div class="card-body p-3">
            <div class="row gx-4">
        <iframe class="min-vh-100" width="100%" height="100%" :src="embedUrl2" frameborder="0" allowfullscreen></iframe>
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
  // import ArgonInput from "@/components/ArgonInput.vue";
  // import ArgonButton from "@/components/ArgonButton.vue";
   
  const body = document.getElementsByTagName("body")[0];
   
  export default {
    name: "profile",
    data() {
      return {
        showMenu: false,
        embedUrl2: 'http://172.16.1.54:3000/d/a13b79ff-237d-4f2c-897b-60e721e7b2b7/new-dashboard?orgId=1&from=1707202959501&to=1707375759501&theme=light'
      };
    },
    components: {
      
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
    }
  };
  </script>
   