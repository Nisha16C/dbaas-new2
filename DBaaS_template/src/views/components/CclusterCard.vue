
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
 
              <div class="col mx-auto">
                <div class="h-100 w-100 border border-success rounded-md text-center text-wrap p-3"
                  :class="{ 'bg-light': clusterType === 'Standalone' }">
                  <label for="Standalone">
                    <input type="radio" id="Standalone" class="visually-hidden" value="Standalone"
                      v-model="selectedType" @change="updateType" />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Standalone cluster
                    </p>
                    <p class="pt-4 text-gray-500 text-sm text-wrap ">
                      A Standalone Node Cluster refers to a cluster configuration in a distributed computing environment
                      where
                      all cluster components, such as databases, services, or applications, run on a Standalone node or
                      machine.
                    </p>
                  </label>
                </div>
              </div>
              <div class="col mx-auto">
                <div :class="{ 'bg-light': clusterType === 'Multiple' }"
                  class="h-100  border border-success  rounded-md text-center p-3">
                  <label for="Multiple">
                    <input type="radio" class="visually-hidden" id="Multiple" value="Multiple" v-model="selectedType"
                      @change="updateType" />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Primary/Standby High Availability
                    </p>
                    <p class="text-gray-500 text-sm text-wrap">
                      A Primary/Standby High Availability (HA) Cluster refers to a configuration in a distributed
                      computing environment
                      where two nodes (or more) operate in tandem to provide fault tolerance and redundancy.
                    </p>
                  </label>
                </div>
              </div>
            </div>
 
          </div>
        </li>
        <div v-if="typeError" class="text-danger">{{ typeError }}</div>
        
        <!-- Providers Lists row 1 -->
        <li class="list-group-item border-0 d-flex pb-5 mb-2 mt-3 bg-gray-100 border-radius-lg">
          <div class="d-flex flex-column">
            <h6 class="mb-3  text-sm">Providers</h6>
            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" style="width: 200.6667%">
 
              <div class="col mx-auto" :class="{ 'bg-light': providerName === 'Cloudstack' }">
                <div class="bg-transparent border-4 rounded-md text-center p-3 d-flex align-items-center">
                  <label>
                    <input class="visually-hidden" type="radio" id="Cloudstack" value="Cloudstack"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 150px;;height: 120px;" class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/withoutcloud-removebg-preview.png" alt="Cloudstack" />
                  </label>
                </div>
              </div>
              <div class="col mx-auto" :class="{ 'bg-light': providerName === 'Harvester' }">
                <div class="bg-transparent border-4 rounded-md text-center p-5  d-flex align-items-center">
                  <label>
                    <input class="visually-hidden" type="radio" id="Harvester" value="Harvester"
                      v-model="selectedProvider" @change="updateProvider" />
                    <div class="avatar avatar-xl position-relative">
                      <img style="width: 150px;;height: 100px;  " class="object-contain max-w-full rounded-lg"
                        src="@/assets/img/wh1.webp" alt="harvester" />
                    </div>
                  </label>
                </div>
              </div>
 
 
            </div>
            <br>
            <!-- provider image row2-->
            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" style="width: 200.6667%">
 
              <!-- vmware -->
              <div class="col mx-auto" :class="{ 'bg-light': providerName === 'Vmware' }">
                <div class="bg-transparent border-4 rounded-md text-center p-3  d-flex align-items-center
            {{ providerName === 'Vmware' ? 'selected' : '' }}">
                  <label>
                    <input type="radio" class="visually-hidden" id="Vmware" value="Vmware" v-model="selectedProvider"
                      @change="updateProvider" />
                    <img style="width: 150px;;height: 100px;" class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/wv1-removebg-preview.png" alt="Vmware" />
                  </label>
                </div>
              </div>
 
              <!-- k8s -->
              <div class="col mx-auto" :class="{ 'bg-light': providerName === 'Kubernetes' }">
                <div class="bg-transparent border-4 rounded-md text-center p-3  d-flex align-items-center
            {{ providerName === 'Kubernetes' ? 'selected' : '' }}">
                  <label>
                    <input type="radio" class="visually-hidden" id="Kubernetes" value="Kubernetes"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 150px;;height: 100px;" class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/wk1.png" alt="Kubernetes" />
                  </label>
                </div>
              </div>
 
 
            </div>
 
            <br>
            <!-- ro3 -->
            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" style="width: 200.6667%">
              <!-- nutanix -->
              <div class="col mx-auto" :class="{ 'bg-light': providerName === 'Nutanix' }">
                <label>
                  <div class="bg-transparent border-4 rounded-md text-center p-3  d-flex align-items-center
            {{ providerName === 'Nutanix' ? 'selected' : '' }}">
 
                    <input type="radio" class="visually-hidden" id="Nutanix" value="Nutanix" v-model="selectedProvider"
                      @change="updateProvider" />
                    <img style="width: 150px;;height: 120px;" class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/wn1-removebg-preview.png" alt="Nutanix" />
 
                  </div>
                </label>
              </div>
 
              <!-- openstack -->
              <div class="col mx-auto" :class="{ 'bg-light': providerName === 'Openstack' }">
                <div class="bg-transprent border-4 rounded-md text-center p-3  d-flex align-items-center
            {{ providerName === 'Openstack' ? 'selected' : '' }}">
                  <label>
                    <input type="radio" class="visually-hidden" id="Openstack" value="Openstack"
                      v-model="selectedProvider" @change="updateProvider" />
                    <img style="width: 150px;;height: 100px;" class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/Openstack.png " alt="Openstack" />
                  </label>
                </div>
              </div>
 
 
            </div>
 
            <div class="row row-cols-1 row-cols-md-2 g-5" style="width: 66.6667% ">
              <!-- Cloudstack Provider -->
 
 
              <!-- Harvester Provider -->
 
 
 
              <!-- comment -->
 
 
              <!-- Kubernetes Provider -->
 
 
              <!-- Nutanix Provider -->
 
 
              <!-- Openstack Provider -->
 
 
 
 
            </div>
            <argon-alert v-if="error" color="danger" icon="icon-danger" dismissible>
              This Provider is not connected. <router-link to="/Providers" class="text-danger">Click here</router-link>
            </argon-alert>
 
          </div>
        </li>
        <div v-if="providerError" class="text-danger">{{ providerError }}</div>
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
import { API_ENDPOINT } from '@/../apiconfig.js';

import ArgonAlert from "@/components/ArgonAlert.vue";
 
// import { useInputStore } from '../../store/clusterStore';
import axios from 'axios';
 
export default {
  name: "billing-card",
  components: {
    ArgonButton,
    ArgonAlert,
  },
  data() {
    return {
      apiUrl: API_ENDPOINT, 
      selectedType: '',
      selectedProvider: '',
      typeError: '',
      providerError: '',
 
      user_id: '',
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
      if (!this.clusterType) {
 
        this.typeError = 'Cluster type is required';
        setTimeout(() => {
          this.typeError = '';
        }, 5000);
        return;
      }
      if (!this.providerName) {
 
        this.providerError = 'Provider is required';
        setTimeout(() => {
          this.providerError = '';
        }, 5000);
        return;
      }
      const selectedProviderInfo = this.provider_info.find(
        (provider) => provider.provider_name.toLowerCase() === this.providerName.toLowerCase()
      );
 
      if (selectedProviderInfo && selectedProviderInfo.is_connected) {
        if (this.providerName === 'Kubernetes') {
          this.$router.push('/Cluster-Setting');
        } else {
          this.$router.push('/Cconfiguration');
        }
      } else {
        this.error = "This provider is not connected";
        setTimeout(() => {
          this.error = '';
        }, 5000);
      }
    },
 
    getAllProviderData() {
      axios.get(`${this.apiUrl}/api/v3/providers/by-user/${this.user_id}/`)
        .then((response) => {
          this.provider_info = response.data
          console.log(response.data);
        })
    },
 
  },
 
  computed: {
    ...mapState(['clusterType', 'providerName']),
  },
};
</script>