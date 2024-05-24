<template>
  <div v-show="this.$store.state.layout === 'default'" class="min-height-300 position-absolute w-100  "
    :class="`${this.$store.state.darkMode ? 'bg-transparent' : 'bg-success'}`" />
  <aside class="my-3 overflow-auto border-0 sidenav navbar navbar-vertical navbar-expand-xs border-radius-xl" :class="`${this.$store.state.isRTL
        ? 'me-3 rotate-caret fixed-end'
        : 'fixed-start ms-3'
      }
    ${this.$store.state.layout === 'landing'
        ? 'bg-transparent shadow-none'
        : ' '
      } ${this.$store.state.sidebarType}`" id="sidenav-main">
    <div class="sidenav-header text-center">
      <i class="top-0 p-5 cursor-pointer fas fa-times text-secondary opacity-5 position-absolute end-0 d-none d-xl-none"
        aria-hidden="true" id="iconSidenav"></i>
      <!-- <router-link class="m-0 navbar-brand" to="/">
        <div class="logo-container">
          <img :src="logoSrc" class="navbar-brand-img h-100" alt="main_logo"/>
        </div>
      </router-link> -->
      <router-link class="m-0 navbar-brand" to="/">
        <img
          :src="
            this.$store.state.darkMode ||
            this.$store.state.sidebarType === 'bg-default'
              ? logoWhite
              : logo
          "
          class="navbar-brand-img mr-4 h-100"
          alt="main_logo"
        />
      </router-link>
    </div>
    <!-- <hr class="mt-0 horizontal dark" /> -->

    <sidenav-list :cardBg="custom_class" />
  </aside>
</template>
<script>
import SidenavList from "./SidenavList.vue";
import logo from "@/assets/img/bitblastLogo.png";
import logoWhite from "@/assets/img/bitblastdarklogo.png";

export default {
  name: "index",
  components: {
    SidenavList
  },
  data() {
    return {
      logo,
      logoWhite
    };
  },
  computed: {
    logoSrc() {
      return this.$store.state.isLogoToggled ? require('@/assets/img/db-png.png') : require('@/assets/img/bitblastLogo.png');
    }
  },
  props: ["custom_class", "layout"]
};
</script>
<style scoped>
.logo-container {
  margin-right: 8px;
}
</style>