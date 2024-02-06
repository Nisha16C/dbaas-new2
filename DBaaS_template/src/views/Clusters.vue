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

          <div class="col-lg-3 col-md-12 col-12">
              <div class="mb-4 card">
                <div class="p-3 card-body">
                  <div class="px-4">
                    <div class="mb-3 mt-4">
                      
                    
                   
                      <router-link to="/cluster-create">
                        <argon-button color="success" size="md" variant="gradient"
                        >Create  Cluster</argon-button>
                      </router-link>

                    </div>
                  </div>
                </div>
              </div>
            </div>


            <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <div class="ml-4">
                  <!-- Project Dropdown -->
                  <span class="font-extrabold">Projects:</span>
                  <select v-model="selectedProject" @change="fetchClustersByProject" class="rounded-md">
                    <option value="">All Projects</option>
                    <option v-for="project in projects" :key="project.id" :value="project.id">
                      {{ project.project_name }}
                    </option>
                  </select>
                </div>
                <authors-table :selectedProject="selectedProject" />
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
import AuthorsTable from "./components/AuthorsTable.vue";
import ArgonButton from "@/components/ArgonButton.vue";
import axios from "axios";

export default {
  name: "Cluster",
  components: {
    Card, AuthorsTable,ArgonButton
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Clusters ",
          value: " ",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "since today",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
  created() {
    // Fetch clusters when the component is created
    this.fetchClusters();
  },

  methods: {
    // Method to fetch clusters and update totalClusters
    fetchClusters() {
      axios.get(`http://172.16.1.69:8000/api/v2/cluster/`)
        .then(response => {
          this.stats.money.value = response.data.length.toString();  // Update totalClusters
        })
        .catch(error => {
          console.error('Error fetching clusters:', error);
        });
    },
    // ... (rest of your methods)
  },
};

</script>
