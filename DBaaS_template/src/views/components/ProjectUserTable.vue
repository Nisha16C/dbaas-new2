[11:57 AM] Nisha Chaurasiya
<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Projects info </h6>
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
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> CREATE_DATE </th>
              <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> UPDATED_DATE </th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, index) in projects" :key="index">
              <td>
                <div class="d-flex px-2 py-1">
                  <div>
                    <!-- You can customize the image source or remove it based on your needs -->
                    <img :src="
            this.$store.state.darkMode ||
            this.$store.state.sidebarType === 'bg-default'
              ? logoWhite
              : logo"
              class="avatar avatar-sm me-3 w-3 h-3" alt="clusterImage" />
                  </div>
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ project.id }}</h6>
                    <p class="text-xs text-secondary mb-0">{{ project.project_name }}</p>
                  </div>
                </div>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatTimeAgo(project.created_date) }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-secondary text-xs font-weight-bold">{{ formatTimeAgo(project.updated_date) }}</span>
              </td>
              <!-- <td class="align-middle">
                
                <a href="javascript:;" class="text-secondary font-weight-bold text-xs" data-toggle="tooltip"
                  data-original-title="Edit cluster">Edit</a>
              </td> -->
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
 
<!-- ... (rest of the component) -->
 
<script>
import logo from "@/assets/img/projectTable.png";
import logoWhite from "@/assets/img/project.png";
 
 
export default {
  name: "projects-table",
  props: {
  projects: {
    type: Array,
    required: true,
  },
},
data() {
    return {
      loading: true, // Add loading state
      logo,
      logoWhite
    };
  },
methods:{
  formatTimeAgo(createdAt) {
    const createdTime = new Date(createdAt)
    const currentTime = new Date()
    const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000)
 
    if (timeDifferenceInSeconds < 60) {
      return `${timeDifferenceInSeconds} sec ago`
    } else if (timeDifferenceInSeconds < 3600) {
      const minutes = Math.floor(timeDifferenceInSeconds / 60)
      return `${minutes} min ago`
    } else if (timeDifferenceInSeconds < 86400) {
      const hours = Math.floor(timeDifferenceInSeconds / 3600)
      return `${hours} hour ago`
    } else {
      const days = Math.floor(timeDifferenceInSeconds / 86400)
      return `${days} days ago`
    }
  },
},
created() {
    // Simulate loading delay with setTimeout
    setTimeout(() => {
      this.loading = false; // Set loading to false after delay
    }, 500); // Adjust delay time as needed
  },
 
};
</script>
  

