
<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card :title="stats.money.title" :value="stats.money.value" :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass" :iconBackground="stats.money.iconBackground" :detail="stats.money.detail"
              directionReverse>
            </card>
          </div>
 
          <div class="col-lg-8 col-md-12 col-12">
            <div class="mb-4 card">
              <div class="p-3 card-body">
                <div class="px-4">
                  <div class="mb-6">
                    <label for="projectname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Project
                      Name</label>
                    <argon-input v-model="project.project_name" type="text" placeholder="Project Name"
                      :class="{ error: input1Error, shake: shakingInput === 'project.project_name' }" />
                    <argon-button color="success" size="md" variant="gradient" @click="saveProject">Create New
                      Project</argon-button>
                  </div>
                  <div v-if="error" class="text-red-500">{{ error }}</div>
                </div>
              </div>
            </div>
          </div>
 
          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
 
<script>
import Card from "@/examples/Cards/Card.vue";
import AuthorsTable from "@/views/components/ProjectTable.vue";
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";
import axios from "axios";
 
export default {
  name: "Project",
  components: {
    Card,
    AuthorsTable,
    ArgonInput,
    ArgonButton,
  },
  data() {
    return {
      input1Error: false,
      shakingInput: null,
      user_id:'26',
      project: {
        project_name: '',
        user: '',
      },
      stats: {
        money: {
          title: "All Projects",
          value: " ",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "since today",
          iconBackground: "bg-gradient-primary",
        },
      },
 
    };
  },
  methods: {
    // createNewProject() {
    //   // axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    //   // axios.defaults.xsrfCookieName = "csrftoken";
    //   const user_id = sessionStorage.getItem('user_id');
    //   if (!user_id) {
    //     console.error('user_id is not available in sessionStorage');
    //     return;
    //   }
    //   const projectData = { user_id, project_name: this.newProjectName };
    //   console.log('Request Payload:', projectData);
    //   axios.post(`http://172.16.1.69.8000/api/v2/project/`, projectData)
    //     .then(response => {
    //       console.log('Project created successfully:', response.data);
    //       this.fetchProjectCount();
    //     })
    //     .catch(error => {
    //       console.error('Error creating project:', error);
 
    //       // Log the full error response
    //       if (error.response) {
    //         console.error('Response Data:', error.response.data);
    //       }
    //     });
    // },
    saveProject() {
      this.input1Error = this.project.project_name === '';
      if (this.input1Error) {
        this.shakingInput = 'project.project_name';
        setTimeout(() => {
          this.shakingInput = null;
        }, 500);
      } else {
        // Retrieve user_id from sessionStorage
        // const user_id = sessionStorage.getItem('user_id');
 
        // Check if user_id is available
        if (!this.user_id) {
          console.error('user_id is not available in sessionStorage');
          return;
        }
 
        // Set user_id in the project data
        this.project.user = this.user_id;
        axios.post(`http://172.16.1.69.8000/api/v2/project/`, this.project)
          .then(response => {
            console.log('Project created successfully:', response);
            // Assuming you have a fetchProjects method to update the project list
            this.$emit('project-saved'); // Emit an event to notify the parent component
            this.resetForm(); // Reset the form or clear the project name
          })
          .catch(error => {
            console.error('Error creating project:', error);
            // Handle the error, show a message, etc.
          });
      }
    },
    resetForm() {
      // Reset the form or clear the project name
      this.project.project_name = '';
    },
 
    fetchProjectCount() {
      // Make an API request to get the project count
      // const user_id = this.project.user
      // Retrieve user_id from sessionStorage
      // const user_id = sessionStorage.getItem('user_id');
 
      axios.get(`http://172.16.1.69.8000/api/v2/project/user/${this.user_id}/`)
        .then(response => {
          this.stats.money.value = response.data.length.toString();
        })
        .catch(error => {
          console.error("Error fetching project count:", error);
        });
    },
  },
  created() {
    // Call the method to fetch project count when the component is created
    this.fetchProjectCount();
  },
};
</script>