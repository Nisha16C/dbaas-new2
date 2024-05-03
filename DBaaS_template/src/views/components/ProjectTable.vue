<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Projects Info  </h6>
    </div>
    <div v-if="loading" class="text-center mt-3">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
 
    <div v-else class="card-body px-0 pt-0 pb-2">
      <div v-if="projects.length === 0" class="text-center">No Projects are Available</div>
      <div v-else class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> PROJECT ID & NAME </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> CREATE_DATE
              </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> UPDATED_DATE
              </th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, index) in projects" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <img :src="
            this.$store.state.darkMode ||
            this.$store.state.sidebarType === 'bg-default'
              ? logoWhite
              : logo"
               class="avatar avatar-sm me-3" alt="logo" />
                  </div>
                  <div class="d-flex flex-column">
                    <h6 class="mb-0 text-sm">{{ project.id }}</h6>
                    <p class="text-xs font-weight-bold mb-0">{{ project.project_name }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(project.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatDate(project.updated_date) }}</span>
              </td>
              <td class="align-middle">
                <argon-button color="success" size="md" variant="gradient" @click="prepareRename(project)" type="button"
                  class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
                  Edit
                </argon-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content" :class="{ 'dark-mode': isDarkMode }">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Rename Your Project: {{ newProjectName }} </h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          New Project Name:
          <argon-input type="text" placeholder="New Project Name" v-model="newProjectName" class=" " />
        </div>
        <div class="modal-footer">      
          <argon-button color="secondary" size="md" variant="gradient" type="button"
            class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Close
          </argon-button>
          <argon-button color="danger" size="md" variant="gradient" @click.prevent="renameProject" type="button"
            class="ml-4 btn btn-danger" data-toggle="modal" data-target="#exampleModal">
            Rename
          </argon-button>
        </div>
      </div>
    </div>
  </div>
</template>
 
<!-- ... (rest of the component) -->
 
<script>
import ArgonButton from "@/components/BB_Button.vue";
import ArgonInput from "@/components/BB_Input.vue";
import axios from "axios";
import { API_ENDPOINT } from '@/../apiconfig.js';
import logo from "@/assets/img/db-png.png";
import logoWhite from "@/assets/img/project.png";
 
 
export default {
  name: "projects-table",
  components: {
    // Card,
    // projectsTable,
    ArgonButton,
    ArgonInput
  },
  data() {
    return {
      apiUrl: API_ENDPOINT,
      projects: [], // Initialize projects as an empty array
      renamingProjectId: null,
      newProjectName: "",
      loading: true,
      logo,
      logoWhite
    };
  },
  computed: {
  isDarkMode() {
    return this.$store.state.darkMode;
  }
},
  created() {
    // Fetch data when the component is mounted
    this.fetchProjects();
  },
  methods: {
    prepareRename(project) {
      // Emit an event to notify the parent component about the rename action
      this.renamingProjectId = project.id;
      this.newProjectName = project.project_name;
      this.$emit("rename-project", project);
    },
 
    renameProject() {
      const payload = { new_project_name: this.newProjectName };
      axios
        .put(
          `${this.apiUrl}/api/v2/project/${this.renamingProjectId}/rename/`,
          payload
        )
        .then((response) => {
          console.log('print response :', response);
          this.fetchProjects(); // You need to have a fetchProjects method to refresh the projects list
        })
        .catch((error) => {
          // Handle error
          console.error(error);
          // Optionally show an error message to the user
        });
    },
    async fetchProjects() {
      try {
        // Make a GET request to the endpoint
        const response = await axios.get(`${this.apiUrl}/api/v2/project/`);
 
        // Update the projects data with the fetched data
        this.projects = response.data;
        this.loading = false ;
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    },
    formatDate(dateString) {
      // Format the date as per your requirement using a library like moment.js
      // Example using JavaScript built-in methods (customize as needed):
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
 
  },
};
</script>
<style scoped>
.dark-mode { /* Define dark mode styles */
  background-color: #1d1e52;
  color: #ffffff;
}
</style>
  