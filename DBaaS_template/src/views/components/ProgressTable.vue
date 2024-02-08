<template>
    <div class="container mt-5">
      <div class="alert  text-center" v-show="!isCompleted && !isFailed">
        <h4 class="font-weight-bold blink p-2 text-danger">
          Please do not refresh or close this page until the progress is
          completed!
        </h4>
      </div>
  
      <div class="card shadow-sm" v-show="!isCompleted">
        <div class="card-header text-center justify-content-between">
          <h5 class="mb-0">Database Installation Result</h5>
          
          <div class="spinner-border mt-3 p-4 spinner-border-md text-primary" v-show="!isCompleted" role="status" aria-hidden="true"></div>
        </div>
        <div class="card-body">
          <h2 class="card-title">Installation Status...</h2>
          <div class="progress">
            <div class="progress-bar progress-bar-striped progress-bar-animated" :style="{ width: progress }" role="progressbar" aria-valuenow="progress" aria-valuemin="0" aria-valuemax="100">{{ progress }}</div>
          </div>
  
          <ul class="list-group list-group-flush mt-3" v-for="(status, index) in latestPipelineStatus" :key="index">
            <li class="list-group-item">{{ status }}</li>
          </ul>
  
        </div>
      </div>
  
      <div class="card shadow-sm" v-show="isCompleted">
        <div class="card-header">
          <h5 class="mb-0">Database Credentials</h5>
        </div>
        <div class="card-body">
          <ul class="list-group list-group-flush">
            <li v-for="(artifact, index) in extractedArtifacts" :key="index" class="list-group-item" v-html="addLineBreaks(artifact.value)"></li>
          </ul>
  
          <div class="text-center mt-3">
            <h4 class="text-primary">
              We are redirecting you to the cluster list page. If you are not redirected,
              <a @click.prevent="RedirectclusterPage" class="text-dark">click here</a>
            </h4>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script>

import axios from "axios";

export default {
    
    data() {
        return {
            isDropdownOpen: false,
            ProjectToggle: false,
            UserToggle: false,
            Username: '',
            user_id: null,
            projects: [],
            selectedProject: "",
            clusters: [],
            isCompleted: false,
            isFailed: false,
            completionText: 'Loading...',
            completionColor: '',
            averageProgress: 0,
            latestPipelineStatus: '',
            extractedArtifacts: [],
            stopFetching: false,
            isPopupVisible: false,
            popupMessage: "",showcred: false,

        };
    },

    methods: {
        RedirectclusterPage(){
            this.$router.push("/overview");
        },
        logout() {
            console.log("logout");
            sessionStorage.removeItem('user_id');
            sessionStorage.removeItem('username');
            sessionStorage.removeItem('project_id');
            sessionStorage.removeItem('project_name');
            window.location.reload()
        },
        getFirstLetter(username) {
            return username.charAt(0, 1).toUpperCase();
        },
        toggleDarkMode() {
            this.toggleDark();
        },

        toggleDropdown() {

            this.isDropdownOpen = !this.isDropdownOpen
        },

        userToggle() {
            this.UserToggle = !this.UserToggle;
        },

        async updateLatestPipelineStatusAndArtifacts() {
            if (this.stopFetching) {
                return;
            }
            const url = 'http://172.16.1.97:8002/api/v2/get_pipeline_status/';

            try {
                const response = await axios.get(url);
                const data = response.data;

                // Update the component's data properties based on the received data
                this.averageProgress = this.calculateAverageProgress(data.pipelines);

                this.isCompleted = this.averageProgress === 100;
                this.isFailed = this.averageProgress === 99;
                this.completionText = this.isCompleted ? 'Completed' : (this.isFailed ? 'Failed' : 'Loading...');
                this.completionColor = this.isCompleted ? 'green' : (this.isFailed ? 'red' : '');

                this.latestPipelineStatus = data.pipelines.map(pipeline => `Database Installation Status : ${pipeline.status}`);
                this.artifacts = this.extractArtifacts(data.pipelines);
            } catch (error) {
                console.error('Error fetching data:', error);
            }

            if (this.isCompleted) {
                console.log("Success");
                this.showSuccessPopup();
            } else if (this.isFailed) {
                console.log("Failed");
                this.showFailedPopup();
            }

            setTimeout(this.updateLatestPipelineStatusAndArtifacts, 5000);
        },
        calculateAverageProgress(pipelines) {
            let totalProgress = 0;
            let numPipelines = pipelines.length;

            pipelines.forEach(pipeline => {
                switch (pipeline.status) {
                    case 'created':
                        totalProgress += 10;
                        break;
                    case 'pending':
                        totalProgress += 25;
                        break;
                    case 'running':
                        totalProgress += 50;
                        break;
                    case 'success':
                        totalProgress += 100;
                        break;
                    case 'failed':
                        // Handle 'failed' status separately (you can adjust the value as needed)
                        totalProgress += 99.9;
                        break;
                    default:
                        // Handle other statuses if needed
                        break;
                }
            });

            // Calculate the average progress
            let averageProgress =  Math.floor(totalProgress / numPipelines);

            return averageProgress;
        },

        extractArtifacts(pipelines) {
            const artifacts = [];

            pipelines.forEach(pipeline => {
                pipeline.artifacts.forEach(artifact => {
                    
                     if (artifact.filename === 'info.txt') {
                        artifacts.push({
                            type: 'Info',
                            value: artifact.content,
                        });
                    }
                });
            });

            this.extractedArtifacts = artifacts;
        },
        showSuccessPopup() {
            this.popupMessage = "Installation successful!";
            
            this.showcred = true
            setTimeout(() => {
                
                // Redirect to the overview page here
                this.$router.push("/Clusters");
            }, 10000);
        },

        showFailedPopup() {
            console.log("faild");
            this.popupMessage = "Installation failed. Please try again.";
          
            this.showcred = true
            setTimeout(() => {
                
                // Redirect to the overview page here
                this.$router.push("/Clusters");
            }, 10000);
        },
        addLineBreaks(text) {
      // Replace '\n' with '<br>' for rendering line breaks in HTML
      return text.replace(/\n/g, '<br>');
    },
     

    },

    created(){
        this.Username = sessionStorage.getItem('username');
    },

    computed: {
        progress() {
            return this.averageProgress + '%'
        }
    },
    // beforeMount(){
    //     window.location.reload()
    // },
    mounted() {
        console.log("mount mtd run");
        setTimeout(() => {
            console.log("after 10sec. mount mtd run");
            this.updateLatestPipelineStatusAndArtifacts();
        }, 10000);
        
        // setInterval(this.updateLatestPipelineStatusAndArtifacts, 5000);
    },
    unmounted(){
        console.log("unmount");
        this.popupMessage = '',
        window.location.reload()
        this.stopFetching = true;
    },
    beforeUnmount(){
        this.stopFetching = true
        this.popupMessage = '',
        console.log("before-unmount");
        window.location.reload();
        // this.stopFetching = true

    }

};
</script>

<style scoped>
.blink {
    animation:
        blinker 1.5s linear infinite;
    color:
        red;
    font-family:
        sans-serif;
}

@keyframes blinker {
    50% {
        opacity:
            0;
    }
}
</style>
  
  