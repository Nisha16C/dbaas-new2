
<template>
  <div class="card h-100 mb-4">
    <div class="card-header pb-0 px-3">
      <div class="row">
        <div class="col-md-6">
          <h6 class="mb-0">Your Cluster Summary</h6>
        </div>
        <div class="col-md-6 d-flex justify-content-end align-items-center">
          <i class="far fa-calendar-alt me-2" aria-hidden="true"></i>
          <small>{{ currentDateTime }}</small>
        </div>
      </div>
    </div>
    <div class="card-body pt-4 p-3">
      <div class="table-responsive">
        <table class="table table-borderless">
          <tbody>
            <tr>
              <th>Cluster Type</th>
              <td>{{selectedType}}</td>              
            </tr>
 
            <tr>
              <th>Cluster Nodes</th>
              <td v-if="selectedType=='Standalone'"> 1 Node</td>
        
              <td v-if="selectedType=='multiple'"> 3 Node</td>
           
            </tr>
 
            <tr>
              <th>Provider</th>
              <td>{{selectedProvider}}</td>           
            </tr>
 
            <tr>
              <th>Cluster Name</th>
              <td>Default</td>           
            </tr>
 
            <tr>
              <th>Postgress Type</th>
              <td>PostreSQL</td>           
            </tr>
 
            <tr>
              <th>Postgres Versions</th>
              <td>{{postgres_version}}</td>           
            </tr>
 
            <tr>
              <th>Instance Size</th>
              <td>2vcpu, 8gb</td>           
            </tr>
 
            <tr>
              <th>Volume Type</th>
              <td>General Purpose SSD(gp3)</td>           
            </tr>
            <tr>
              <th>Volume Properties</th>
              <td>4 Gi, 3000 IOPS, 125 Mb/s Disk</td>           
            </tr>
 
            <tr>
              <th>Networking</th>
              <td>Private</td>           
            </tr>
 
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
 
<script>
// import ArgonButton from "@/components/ArgonButton.vue";
import { mapState } from 'vuex';
 
export default {
  name: "transaction-card",
  components: {
    // ArgonButton,
  },
  data() {
    return {
      currentDateTime: new Date().toLocaleString(),
    };
  },
  mounted() {
    this.updateDateTime();
    setInterval(this.updateDateTime, 1000);
  },
  methods: {
    updateDateTime() {
      this.currentDateTime = new Date().toLocaleString();
    },
  },
  computed: {
    ...mapState(['selectedType', 'selectedProvider','postgres_version']),
 
  },
};
</script>
 