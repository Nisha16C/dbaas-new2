<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Select the type of cluster you want to use</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg">
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Cluster type</h6>
            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" style="width: 106.6667%">
              <div class="col">
                <div class="h-100 w-100 bg-white border-primary rounded-md text-center text-wrap   p-3 "
                  :class="{ 'border-info': selectedType === 'Standalone' }">
                  <label for="Standalone" class="">
                    <input type="radio" id="Standalone" value="Standalone" v-model="selectedType" @change="updateType" />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Standalone cluster
                    </p>
                    <p class="pt-4 text-gray-500 text-sm text-wrap ">
                      A Standalone Node Cluster refers to a cluster
                      configuration in a distributed computing environment where
                      all cluster components, such as databases, services, or
                      applications, run on a Standalone node or machine.
                    </p>
                  </label>
                </div>
              </div>
              <div class="col">
                <div class="h-100 bg-white border-4 rounded-md text-center p-3 "
                  :class="{ 'border-info': selectedType === 'multiple' }">
                  <label for="multiple">
                    <input type="radio" id="multiple" value="multiple" v-model="selectedType" @change="updateType" />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Primary/Standby High Availability
                    </p>
                    <p class="text-gray-500 text-sm text-wrap">
                      A Primary/Standby High Availability (HA) Cluster refers to
                      a configuration in a distributed computing environment
                      where two nodes (or more) operate in tandem to provide
                      fault tolerance and redundancy.
                    </p>
                  </label>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="list-group-item border-0 d-flex p-4 mb-2 mt-3 bg-gray-100 border-radius-lg">
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Providers</h6>

            <div class="row row-cols-1 row-cols-md-2 g-4" style="width: 66.6667%">
              <!-- Cloudstack Provider -->
              <div class="col">
                <div class="bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Cloudstack' ? 'selected' : '' }}">
                  <label>
                    <input type="radio"  id="Cloudstack" value="Cloudstack"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 50.6667%" class="object-contain max-w-full rounded-lg" src="@/assets/img/cloudstack.png" alt="Cloudstack" />
                  </label>
                </div>
              </div>

              <!-- Harvester Provider -->
              <div class="col">
                <div class="ml-md-4 bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Harvester' ? 'selected' : '' }}">
                  <label>
                    <input type="radio"  id="Harvester" value="Harvester"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 50.6667%" class="object-contain max-w-full rounded-lg" src="@/assets/img/apple-icon.png" alt="Harvester" />
                  </label>
                </div>
              </div>

              <!-- Vmware Provider -->
              <div class="col">
                <div class="bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Vmware' ? 'selected' : '' }}">
                  <label>
                    <input type="radio"  id="Vmware" value="Vmware" v-model="selectedProvider"
                      @change="updateProvider" />
                    <img style="width: 50.6667%" class="object-contain max-w-full rounded-lg" src="@/assets/img/Vmware.png" alt="Vmware" />
                  </label>
                </div>
              </div>

              <!-- Kubernetes Provider -->
              <div class="col">
                <div class="ml-md-4 bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Kubernetes' ? 'selected' : '' }}">
                  <label>
                    <input type="radio"  id="Kubernetes" value="Kubernetes"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 50.6667%" class="object-contain max-w-full rounded-lg" src="@/assets/img/k8s.png" alt="Kubernetes" />
                  </label>
                </div>
              </div>

              <!-- Nutanix Provider -->
              <div class="col">
                <label>
                <div class="bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Nutanix' ? 'selected' : '' }}">
                 
                    <input type="radio" class="visually-hidden" id="Nutanix" value="Nutanix" v-model="selectedProvider"
                      @change="updateProvider" />
                    <img style="width: 50.6667%" class="object-contain max-w-full rounded-lg" src="@/assets/img/nutanix.png" alt="Nutanix" />
                  
                </div>
              </label>
              </div>

              <!-- Openstack Provider -->
              <div class="col">
                <div class="ml-md-4 bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Openstack' ? 'selected' : '' }}">
                  <label>
                    <input type="radio" class="visually-hidden" id="Openstack" value="Openstack"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 50.6667%" class="object-contain max-w-full rounded-lg" src="@/assets/img/Openstack.png " alt="Openstack" />
                  </label>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
      <argon-button @click="Next()" color="success" size="md" variant="gradient">
        NEXT
      </argon-button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ArgonButton from "@/components/ArgonButton.vue";
// import { useInputStore } from '../../store/clusterStore';
import axios from 'axios';
 
export default {
  name: "billing-card",
  components: {
    ArgonButton,
  },
  data() {
    return {
      selectedType: 'Standalone',
      selectedProvider: 'Cloudstack',
 
      // user_id: '26',
      provider_info: [],
      error: ''
    };
  },
  created() {
    // const store = useInputStore();
    // store.setType(this.selectedType);
    // store.setProvider(this.selectedProvider);
 
    this.user_id = sessionStorage.getItem('user_id');
    this.getAllProviderData();
 
  },
  methods: {
    ...mapActions(['updateSelectedType', 'updateSelectedProvider']),
    updateType() {
      this.updateSelectedType(this.selectedType);
    },
    updateProvider() {
      this.updateSelectedProvider(this.selectedProvider);
    },
 
    Next() {
      this.$router.push('/Cluster-Setting');
    },
 
    getAllProviderData() {
      axios.get(`http://172.16.1.69:8000/api/v3/providers/by-user/${this.user_id}/`)
        .then((response) => {
          this.provider_info = response.data
          console.log(response.data);
        })
    },
 
  },
 
  computed: {
    ...mapState(['selectedType', 'selectedProvider']),
  },
};
</script>

