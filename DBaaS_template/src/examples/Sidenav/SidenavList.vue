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
              <i class="fa fa-user-plus" style="color: #3f775e; font-size: 13px"></i>
              <!-- SVG icon for User Creation -->
              <span class="nav-link-text text-center">User Creation</span>
            </router-link>
          </li>
          <li>
            <router-link to="/ADauthoprovider" class="nav-link">
              <!-- <i class="fa fa-lock"></i>  -->
              <i> <!-- Start of SVG icon -->
                <svg height="15px" width="15px" viewBox="0 0 502.664 502.664" fill="#3f775e">
                  <path style="fill:#3f775e;"
                    d="M132.099,230.872c55.394,0,100.088-44.759,100.088-99.937c0-55.243-44.673-99.981-100.088-99.981c-55.135,0-99.808,44.738-99.808,99.981C32.291,186.091,76.965,230.872,132.099,230.872z">
                  </path>
                  <path style="fill:#3f775e;"
                    d="M212.3,247.136H52.072C23.469,247.136,0,273.431,0,305.636v160.896c0,1.769,0.841,3.387,1.014,5.177h262.387c0.108-1.79,0.949-3.408,0.949-5.177V305.636C264.35,273.431,240.967,247.136,212.3,247.136z">
                  </path>
                  <path style="fill:#3f775e;"
                    d="M502.664,137.751c-0.108-58.673-53.711-105.934-119.33-105.783c-65.92,0.108-119.092,47.758-119.006,106.279c0.108,46.226,33.478,85.334,79.812,99.722l0.626,202.55l38.676,27.826l40.208-28.064l-0.065-26.877h-18.572l-0.086-26.338h18.616l-0.173-29.121h-18.486l-0.086-26.295h18.572l-0.086-26.316h-18.551l-0.065-26.316l18.637-0.022l-0.302-41.157C469.402,223.279,502.664,184.02,502.664,137.751z M383.399,77.612c14.776,0,26.899,12.101,26.899,26.856c0.108,14.949-12.015,27.007-26.834,27.007c-14.905,0-26.942-11.886-26.942-26.877C356.436,89.778,368.494,77.655,383.399,77.612z">
                  </path>
                </svg> <!-- End of SVG icon -->
              </i>

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
      <li class="nav-item" v-else>
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
  list-style: none;
  /* Hide default bullet points */
  padding: 0;
  /* Remove default padding */
  margin: 0;
  /* Remove default margin */
  color: #3f775e;
}
</style>