<template>
  <div class="collapse navbar-collapse w-auto h-auto h-100 mt-3 " id="sidenav-collapse-main">
    <hr style="margin: 0; padding: 0; border: none;">
    <ul class="navbar-nav">
      <li class="nav-item" v-if="!checkuser(username)">
        <router-link to="/Project-Select" class="nav-link">
          <span class="nav-link-text text-center" :class="'ms-1'">{{ project_name ? project_name : ' SELECT PROJECT '
            }}</span>
        </router-link>
        <hr style="margin: 0; padding: 0; border: none;">

      </li>

      <li class="nav-item" v-if="checkuser(username)">
        <sidenav-item url="/admin-dashboard" :class="getRoute() === 'admin-dashboard' ? 'active' : ''"
          :navText="'Admin Dashboard'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item" v-else>
        <sidenav-item url="/User-dashboard" :class="getRoute() === 'User-dashboard' ? 'active' : ''"
          :navText="'Overview'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="checkuser(username)">
        <sidenav-item url="/Clusters-Management" :class="getRoute() === 'Clusters' ? 'active' : ''"
          :navText="'Clusters Management'">
          <template v-slot:icon>
            <!-- <i class="ni ni-umbrella-13 text-info text-sm opacity-10"></i> -->
            <i class="fa fa-database text-info text-sm opacity-10"></i>

          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/Clusters" :class="getRoute() === 'Clusters' ? 'active' : ''" :navText="'Clusters '">
          <template v-slot:icon>
            <i class="fa fa-database text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item" v-if="checkuser(username)">
        <sidenav-item url="/Project-Management" :class="getRoute() === 'Projects' ? 'active' : ''"
          :navText="'Projects Management'">
          <template v-slot:icon>
            <i class="far fa-folder text-info text-sm opacity-10"></i> </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/Projects" :class="getRoute() === 'Projects' ? 'active' : ''" :navText="'Projects '">
          <template v-slot:icon>
            <i class="far fa-folder text-info text-sm opacity-10"></i> </template>
        </sidenav-item>
      </li>

      <li class="nav-item" v-if="checkuser(username)" style="margin-right: 10px;">
        <a href="#" @click="toggleDropdown('user-management')" class="nav-link">
          <i class="fa fa-users text-info text-sm opacity-10"></i>
          <span class="nav-link-text text-center" style="margin-right: 7px;">User Management</span>
          <i class="fa fa-angle-down"></i>
        </a>
        <ul v-show="isOpen('user-management')" class="sub-nav">
          <li>
            <router-link to="/User-Management" class="nav-link">
              <i class="fa fa-user-plus"></i> <!-- SVG icon for User Creation -->
              <span class="nav-link-text text-center">User Creation</span>
            </router-link>
          </li>
          <li>
            <router-link to="/ADauthoprovider" class="nav-link">
              <i class="fa fa-lock"></i> <!-- SVG icon for Auth Providers -->
              <span class="nav-link-text text-center">Auth Providers</span>
            </router-link>
          </li>
        </ul>

      </li>


      <li class="nav-item" v-else>
        <sidenav-item url="/Provider" :class="getRoute() === 'Provider' ? 'active' : ''" :navText="'Provider'">
          <template v-slot:icon>
            <i class="fa fa-cogs text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="mt-3 nav-item" v-if="checkuser(username)">
        <h6 class="text-xs ps-1  text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          Observability & Backup
        </h6>
      </li>

      <li class="mt-3 nav-item" v-else>
        <h6 class="text-xs ps-3 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          Database Backup
        </h6>
      </li>
      <li class="nav-item" v-if="checkuser(username)">
        <sidenav-item url="/profile" :class="getRoute() === 'profile' ? 'active' : ''" :navText="'Monitoring'">
          <template v-slot:icon>
            <i class="ni ni-single-02 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="checkuser(username)">
        <sidenav-item url="/mount-backup-method" :class="getRoute() === 'mount-backup-method' ? 'active' : ''"
          :navText="'Backup & Restore'">
          <template v-slot:icon>
            <i class="ni ni-money-coins text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item url="/mount-backup-method" :class="getRoute() === 'mount-backup-method' ? 'active' : ''"
          :navText="'Backup & Restore'">
          <template v-slot:icon>
            <i class="ni ni-money-coins text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item" v-if="checkuser(username)">
        <sidenav-item url="/ActivityLog" :class="getRoute() === ' ' ? 'active' : ''" :navText="'Activity Log'">
          <template v-slot:icon>
            <i class="ni ni-ui-04 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

    </ul>
  </div>

  <div class="pt-2 mx-3 mt-3 sidenav-footer">
    <sidenav-card :class="cardBg" textPrimary="Need Help?" />
  </div>
</template>
<script>
import { mapState } from 'vuex';
import SidenavItem from "./SidenavItem.vue";
import SidenavCard from "./SidenavCard.vue";
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';

export default {
  name: "SidenavList",
  props: {
    cardBg: String,
  },
  computed: {
    ...mapState(['project_name', 'project_id']),
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      title: "BitBlast",
      controls: "dashboardsExamples",
      isActive: "active",
      username: "",
      user_id: '',
      userRoles: {}, // Initialize userRoles as an empty object
      openDropdown: null, // Track which dropdown is open
    };
  },
  created() {
    this.username = sessionStorage.getItem('username');
    this.user_id = sessionStorage.getItem('user_id');
  },
  components: {
    SidenavItem,
    SidenavCard,
  },
  mounted() {
    this.fetchProject();
    this.fetchUserRoles(); // Fetch user roles when the component is mounted
  },
  methods: {
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },
    fetchProject() {
      this.$store.dispatch('fetchFirstProject', this.user_id);
    },
    fetchUserRoles() {
      axios.get(`${this.apiUrl}/api/v1/user-roles/`)
        .then(response => {
          this.userRoles = response.data.user_roles;
          console.log('User Roles:', this.userRoles);
        })
        .catch(error => {
          console.error('Error fetching user roles:', error);
        });
    },
    checkuser(user) {
      return this.userRoles[user] && this.userRoles[user].includes('Admin');
    },

    toggleDropdown(section) {
      if (this.openDropdown === section) {
        this.openDropdown = null; // Close the dropdown if already open
      } else {
        this.openDropdown = section; // Open the specified dropdown
      }
    },
    isOpen(section) {
      return this.openDropdown === section;
    },
  },
};
</script>
<style scoped>
  .sub-nav {
    list-style: none; /* Hide default bullet points */
    padding: 0; /* Remove default padding */
    margin: 0; /* Remove default margin */
  }
</style>