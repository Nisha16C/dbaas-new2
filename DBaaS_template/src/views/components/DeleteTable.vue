<template>
    <div class="container mt-5">
      <div class="alert  text-center" v-show="!isCompleted && !isFailed">
        <h4 class="font-weight-bold p-2 text-danger">
          Please do not refresh or close this page until the progress is
          completed!
        </h4>
      </div>
  
      <div class="card shadow-sm" v-show="!isCompleted">
        <div class="card-header text-center justify-content-between">
          <h5 class="mb-0">Database Deletion Result</h5>
          
          <div class="spinner-border mt-3 p-4 spinner-border-md text-primary" v-show="!isCompleted" role="status" aria-hidden="true"></div>
        </div>
        <div class="card-body">
          <h2 class="card-title">Deletion Status...</h2>
          <div class="progress">
            <div class="progress-bar progress-bar-striped progress-bar-animated" :style="{ width: progress }" role="progressbar" aria-valuenow="progress" aria-valuemin="0" aria-valuemax="100">{{ progress }}</div>
          </div>
          <div class="mt-3"> Database Deletion Status: {{ latestPipelineStatus }} </div> 
          <!-- <ul class="list-group list-group-flush mt-3" v-for="(status, index) in latestPipelineStatus" :key="index">
            <li class="list-group-item">{{ status }}</li>
          </ul> -->
  
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
import { API_ENDPOINT } from '@/../apiconfig.js';

 
export default {
    
    data() {
        return {
            apiUrl: API_ENDPOINT, 
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
            this.$router.push("/Clusters");
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
            const formdata = {
                    "user_id" : this.user_id,
                }
            const url = `${this.apiUrl}/api/v2/get_dele_pipeline_status/`;
 
            try {
                const response = await axios.post(url,formdata);
                const data = response.data                    
                console.log(data);
                this.latestPipelineStatus = data.status;
               
                // Update the component's data properties based on the received data
                this.averageProgress = this.calculateAverageProgress(this.latestPipelineStatus);

 
                this.isCompleted = this.averageProgress === 100;
                this.isFailed = this.averageProgress === 99;
                this.completionText = this.isCompleted ? 'Completed' : (this.isFailed ? 'Failed' : 'Loading...');
                this.completionColor = this.isCompleted ? 'green' : (this.isFailed ? 'red' : '');
 
                // this.latestPipelineStatus = data.pipelines.map(pipeline => `Database Deletion Status : ${pipeline.status}`);
                this.artifacts = this.extractArtifacts(data.pipelines);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
 
            if (this.isCompleted) {
                this.showSuccessPopup();
            } else if (this.isFailed) {
                this.showFailedPopup();
            }
 
            setTimeout(this.updateLatestPipelineStatusAndArtifacts, 5000);
        },
        calculateAverageProgress(pipeline) {
            console.log("Calculate pipeline ",pipeline); // Calculate pipeline running
            let totalProgress = 0;
            // let numPipelines = pipelines.length;
            
                switch (pipeline) {
                    case 'created':
                        totalProgress += 20;
                        break;
                    case 'pending':
                        totalProgress += 40;
                        break;
                    case 'running':
                        totalProgress += 70;
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
        

            let averageProgress = Math.floor(totalProgress);

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
        this.user_id = sessionStorage.getItem('user_id');
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
        setTimeout(() => {
            this.updateLatestPipelineStatusAndArtifacts();
        }, 1000);
        
       
    },
    unmounted(){
        this.popupMessage = '',
        window.location.reload()
        this.stopFetching = true;
    },
    beforeUnmount(){
        this.stopFetching = true
        this.popupMessage = '',
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
  
  