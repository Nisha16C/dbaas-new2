<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.money.title"
              :value="stats.money.value"
              :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass"
              :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail"
              directionReverse
            >
            </card>
          </div>

          <div class="col-lg-8 col-md-12 col-12">
            <div class="card">
              <div class="p-3 card-body">
                <div class="">
                  <div class="">
                    <label
                      for="projectname"
                      class="block  text-sm font-medium text-gray-900 dark:text-black"
                      >Project Name</label
                    >
                    <argon-input type="text" placeholder="Project Name" v-model="project.project_name"
                    :class="{
              error: input1Error,
              shake: shakingInput === 'project.project_name',
            }" />
                    <argon-button color="success" size="md" variant="gradient"
                     @click="saveProject" >Create Project</argon-button
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <project-table :projects="projectsData"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import Card from "@/examples/Cards/Card.vue";
import ProjectTable from "@/views/components/ProjectUserTable.vue";
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "Cluster",
  components: {
    Card,
    ProjectTable,
    ArgonInput,
    ArgonButton,
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Projects",
          value: "",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "since today",
          iconBackground: "bg-gradient-primary",
        },
      },
      project: {
        project_name: '',
        user: '',
      },
      input1Error: false, shakingInput: null,

      projectsData: [],
    };
  },
  created() {
    this.project.user = sessionStorage.getItem('user_id');
    this.fetchProject()
  },
  methods: {
    fetchProject() {
      
      const user_id = this.project.user
      console.log(user_id);
      axios.get(`http://172.16.1.97:8002/api/v2/project/user/${user_id}/`)
        .then((response) => {
          this.projectsData = response.data;
          this.stats.money.value = this.projectsData.length
          this.loading = false;
        })
    },
    saveProject() {   
      this.input1Error = this.project.project_name === '';
      if (this.input1Error) {
        this.shakingInput = 'project.project_name'
        setTimeout(() => {
          this.shakingInput = null;
        }, 500);
      }
      else {
        console.log(this.project)
        axios.post("http://172.16.1.97:8002/api/v2/project/", this.project)
          .then(() => {
            this.fetchProject()
            this.project.project_name =''
            
          
          })
          .catch(error => {
            this.error = error.response.data.error;
            setTimeout(() => {
              this.error = '';
            }, 3000);
          });
      }
    },
  }
};
</script>

<style scoped>
.error {
  border: 2px solid red;
}

.main_content {
  background: linear-gradient(90deg, #25316D 0%, #8b7c59 100%);

}

.shake {
  animation: shake 0.5s ease-in-out 8 alternate;
}

@keyframes shake {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(10px, 0);
  }
}
</style>