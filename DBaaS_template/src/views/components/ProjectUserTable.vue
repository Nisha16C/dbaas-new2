<template>
  <div class="card">
    <div class="card-header pb-0">
      <h6> Projects info User </h6>
    </div>

    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
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
                    <img src="../../assets/img/projectTable.png" class="avatar avatar-sm me-3 w-3 h-3" alt="clusterImage" />
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
              <td class="align-middle">
                <!-- You can customize the Edit link as per your requirements -->
                <a href="javascript:;" class="text-secondary font-weight-bold text-xs" data-toggle="tooltip"
                  data-original-title="Edit cluster">Edit</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<!-- ... (rest of the component) -->

<script> 
export default {
  name: "projects-table",
  props: {
  projects: {
    type: Array,
    required: true,
  },
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
}

};
</script>
  