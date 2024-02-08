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
import AuthorsTable from "./components/ProjectTable.vue";
// import ArgonInput from "@/components/ArgonInput.vue";
// import ArgonButton from "@/components/ArgonButton.vue";
import axios from "axios"

export default {
  name: "Project",
  components: {
    Card,
    AuthorsTable,
    // ArgonInput,
    // ArgonButton,
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Projects",
          value: "",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "Till Today",
          iconBackground: "bg-gradient-primary",
        },
      },
      project: {
        project_name: "", // Make sure project_name is defined
        // ... other project properties
      },
      input1Error: false,
      shakingInput: null,
      error: "",
    };
  },

  methods: {
    // ... other methods ...
    saveProject() {
      console.log("Save Project button clicked");
      console.log("Project Data:", this.project);
      this.input1Error = this.project.project_name === "";
      console.log("Input Error:", this.input1Error);
      if (this.input1Error) {
        this.shakingInput = "project.project_name";
        setTimeout(() => {
          this.shakingInput = null;
        }, 500);
      } else {
        console.log("About to send API request to create a project")
        axios
          .post("http://172.16.1.97:8002/api/v2/project/", this.project)
          .then((response) => {
            console.log("Project created successfully:", response)
            this.fetchProjectCount();
            // window.location.reload();
          })
          .catch((error) => {
            console.error("Error creating projects:", error);
            this.error = error.response ? error.response.data.error : "Unknown error";
            setTimeout(() => {
              this.error = "";
            }, 3000);
          });
      }
    },
    fetchProjectCount() {
      // Make an API request to get the project count
      axios.get(`http://172.16.1.97:8002/api/v2/project/`)
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


