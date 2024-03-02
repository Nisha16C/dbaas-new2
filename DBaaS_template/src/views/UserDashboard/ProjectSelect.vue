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
  import { mapState } from 'vuex';
  import axios from 'axios';
  import Card from "@/examples/Cards/Card.vue";
  import ProjectTable from "@/views/components/ProjectselectTable.vue";
//   import ArgonInput from "@/components/ArgonInput.vue";
//   import ArgonButton from "@/components/ArgonButton.vue";
  
  export default {
    name: "Cluster",
    components: {
      Card,
      ProjectTable,
    //   ArgonInput,
    //   ArgonButton,
    },
    computed:{
      ...mapState(['project_name', 'project_id']),
    },
    data() {
      return {
        stats: {
          money: {
            title: "Total Projects",
            value: "",
            percentage: "",
            iconClass: "ni ni-money-coins",
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
        axios.get(`http://172.16.1.92:8002/api/v2/project/user/${user_id}/`)
          .then((response) => {
            this.projectsData = response.data;
            this.stats.money.value = this.projectsData.length        
          })
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