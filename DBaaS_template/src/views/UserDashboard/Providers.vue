[9:24 AM] Ashish Sahu
 
 
<template>
  <main>
    <div class="container-fluid">
      <div class="page-header min-height-300" style="
          background-image: url('https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80');
          margin-right: -24px;
          margin-left: -34%;
        ">
        <span class="mask bg-gradient-success opacity-6"></span>
      </div>
 
      <div class="card shadow-lg mt-n6">
        <button @click.prevent="toggleModal('Cloudstack')" class="btn btn-light">
 
          <div class="card-body p-3">
            <div class="row gx-4">
              <div class="col-auto">
                <div class="avatar avatar-xl position-relative">
 
                  <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/cloudstack.png " alt="Cloudstack" />
 
                </div>
              </div>
 
              <div class="col-auto my-auto">
                <div class="h-100">
                  <h5 class="mb-1">Cloudstack</h5>
                  <p class="mb-0 font-weight-bold text-sm">Private Cloud</p>
                </div>
              </div>
              <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                <div class="nav-wrapper position-relative end-0">
                  <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                    <li class="nav-item">
                      <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                        aria-selected="false">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Cloudstack')"
                          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                          viewBox="0 0 100 100">
                          <circle cx="50" cy="50" r="40" fill="red" />
                          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
                          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
                        </svg>
                        <div class="provider_stat">
                          <div class="text-green-500" v-if="isProviderConnected('Cloudstack')">Connected</div>
                          <div class="text-red-500" v-else>Not Connected </div>
                        </div>
                      </a>
                    </li>
 
                  </ul>
                </div>
              </div>
 
 
 
            </div>
          </div>
 
        </button>
        <!-- vmware -->
        <button @click.prevent="toggleModal('Vmware')" class="btn btn-light">
          <div class="card-body p-3">
            <div class="row gx-4">
              <div class="col-auto">
                <div class="avatar avatar-xl position-relative">
                  <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/Vmware.png " alt="Vmware" />
                </div>
              </div>
 
              <div class="col-auto my-auto">
                <div class="h-100">
                  <h5 class="mb-1">Vmware</h5>
                  <p class="mb-0 font-weight-bold text-sm">Private Cloud</p>
                </div>
              </div>
              <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                <div class="nav-wrapper position-relative end-0">
                  <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                    <li class="nav-item">
                      <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                        aria-selected="false">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Vmware')"
                          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                          viewBox="0 0 100 100">
                          <circle cx="50" cy="50" r="40" fill="red" />
                          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
                          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
                        </svg>
                        <div class="provider_stat">
                          <div class="text-green-500" v-if="isProviderConnected('Vmware')">Connected</div>
                          <div class="text-red-500" v-else>Not Connected </div>
                        </div>
                      </a>
                    </li>
 
                  </ul>
                </div>
              </div>
 
 
 
            </div>
          </div>
        </button>
        <!--  -->
        <button @click.prevent="toggleModals('Kubernetes')" class="btn btn-light">
          <div class="card-body p-3">
            <div class="row gx-4">
              <div class="col-auto">
                <div class="avatar avatar-xl position-relative">
                  <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/k8s.png " alt="Kubernetes" />
                </div>
              </div>
 
              <div class="col-auto my-auto">
                <div class="h-100">
                  <h5 class="mb-1">Kubernetes</h5>
                  <p class="mb-0 font-weight-bold text-sm">Private Cloud</p>
                </div>
              </div>
              <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                <div class="nav-wrapper position-relative end-0">
                  <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                    <li class="nav-item">
                      <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                        aria-selected="false">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Kubernetes')"
                          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                          viewBox="0 0 100 100">
                          <circle cx="50" cy="50" r="40" fill="red" />
                          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
                          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
                        </svg>
                        <div class="provider_stat">
                          <div class="text-green-500" v-if="isProviderConnected('Kubernetes')">Connected</div>
                          <div class="text-red-500" v-else>Not Connected</div>
                        </div>
 
 
                        <!-- <span class="ms-1">Connected</span> -->
                      </a>
                    </li>
 
                  </ul>
                </div>
              </div>
 
 
 
            </div>
          </div>
        </button>
        <!-- d -->
 
 
 
        <!-- openstack -->
        <button @click.prevent="OpenstackModal('Openstack')" class="btn btn-light">
 
 
          <div class="card-body p-3">
            <div class="row gx-4">
              <div class="col-auto">
                <div class="avatar avatar-xl position-relative">
                  <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/Openstack.png " alt="Cloudstack" />
                </div>
              </div>
 
              <div class="col-auto my-auto">
                <div class="h-100">
                  <h5 class="mb-1">Openstack</h5>
                  <p class="mb-0 font-weight-bold text-sm">Private Cloud</p>
                </div>
              </div>
              <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                <div class="nav-wrapper position-relative end-0">
                  <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                    <li class="nav-item">
                      <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                        aria-selected="false">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Openstack')"
                          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                          viewBox="0 0 100 100">
                          <circle cx="50" cy="50" r="40" fill="red" />
                          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
                          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
                        </svg>
                        <div class="provider_stat">
                          <div class="text-green-500" v-if="isProviderConnected('Openstack')">Connected</div>
                          <div class="text-red-500" v-else>Not Connected</div>
                        </div>
 
 
                        <!-- <span class="ms-1" v-if="isProviderConnected">Connected</span>
                      <span class="ms-1 v-else">Not connected</span> -->
                      </a>
                    </li>
 
                  </ul>
                </div>
              </div>
 
 
 
            </div>
          </div>
        </button>
 
        <!-- harvester -->
        <button @click.prevent="toggleModal('Harvester')" class="btn btn-light">
          <div class="card-body p-3">
            <div class="row gx-4">
              <div class="col-auto">
                <div class="avatar avatar-xl position-relative">
                  <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/harvester.jpg " alt="harvester" />
                </div>
              </div>
 
              <div class="col-auto my-auto">
                <div class="h-100">
                  <h5 class="mb-1">Harvester</h5>
                  <p class="mb-0 font-weight-bold text-sm">Private Cloud</p>
                </div>
              </div>
              <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                <div class="nav-wrapper position-relative end-0">
                  <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                    <li class="nav-item">
                      <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                        aria-selected="false">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Harvester')"
                          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                          viewBox="0 0 100 100">
                          <circle cx="50" cy="50" r="40" fill="red" />
                          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
                          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
                        </svg>
                        <div class="provider_stat">
                          <div class="text-green-500" v-if="isProviderConnected('Harvester')">Connected</div>
                          <div class="text-red-500" v-else>Not Connected</div>
                        </div>
                      </a>
                    </li>
 
                  </ul>
                </div>
              </div>
 
 
 
            </div>
          </div>
        </button>
        <!-- nutanix -->
        <button @click.prevent="toggleModal('Nutanix')" class="btn btn-light">
 
 
          <div class="card-body p-3">
            <div class="row gx-4">
              <div class="col-auto">
                <div class="avatar avatar-xl position-relative">
                  <img class="shadow-sm w-100 border-radius-lg" src="@/assets/img/nutanix.png " alt="Nutanix" />
                </div>
              </div>
 
              <div class="col-auto my-auto">
                <div class="h-100">
                  <h5 class="mb-1">Nutanix</h5>
                  <p class="mb-0 font-weight-bold text-sm">Private Cloud</p>
                </div>
              </div>
              <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
                <div class="nav-wrapper position-relative end-0">
                  <ul class="p-1 bg-transparent nav nav-pills nav-fill" role="tablist">
                    <li class="nav-item">
                      <a class="px-0 py-1 mb-0 nav-link" data-bs-toggle="tab" href="javascript:;" role="tab"
                        aria-selected="false">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="isProviderConnected('Nutanix')"
                          class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="20" height="24" class="mr-2"
                          viewBox="0 0 100 100">
                          <circle cx="50" cy="50" r="40" fill="red" />
                          <line x1="20" y1="20" x2="80" y2="80" stroke="white" stroke-width="8" />
                          <line x1="20" y1="80" x2="80" y2="20" stroke="white" stroke-width="8" />
                        </svg>
                        <div class="provider_stat">
                          <div class="text-green-500" v-if="isProviderConnected('Nutanix')">Connected</div>
                          <div class="text-red-500" v-else>Not Connected</div>
                        </div>
                      </a>
                    </li>
 
                  </ul>
                </div>
              </div>
 
 
 
            </div>
          </div>
        </button>
 
 
      </div>
 
 
 
      <!--1st working vm other modal -->
      <div>
        <div v-show="isModalVisible" class="modal-container" tabindex="-1" role="dialog">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
              <!-- Modal Header -->
              <div class="modal-header">
                <h5 class="modal-title">Add Provider</h5>
                <button type="button" class="close" @click="toggleModal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
 
              <!-- Modal Body -->
              <div class="modal-body">
                <!-- Form with 5 fields -->
                <form>
                  <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
                    {{ selectedProvider }}
                  </h3>
                  <div class="mb-3">
                    <label for="api_name" class="form-label">API Name</label>
                    <input type="text" class="form-control" id="api_name" v-model="api_name" required>
                    <argon-alert v-if="!api_name && showErrorMessages" color="danger" icon="icon-danger" dismissible>
                      API Name is required
                    </argon-alert>
                  </div>
 
                  <div class="mb-3">
                    <label for="api_endpoint" class="form-label">API Endpoint</label>
                    <input type="text" class="form-control" id="api_endpoint" v-model="api_endpoint" required>
                    <argon-alert v-if="!api_endpoint && showErrorMessages" color="danger" icon="icon-danger" dismissible>
                      API Endpoint is required
                    </argon-alert>                  </div>
 
                  <div class="mb-3">
                    <label for="access_key" class="form-label">Access key</label>
                    <input type="text" class="form-control" id="access_key" v-model="access_key" required>
                    <argon-alert v-if="!access_key && showErrorMessages" color="danger" icon="icon-danger" dismissible>
                      Access Key is required
                    </argon-alert>
                  </div>
 
                  <div class="mb-3">
                    <label for="secret_key" class="form-label">Secret Key</label>
                    <input type="text" class="form-control" id="secret_key" v-model="secret_key" required>
                    <!-- <span class="text-danger" v-if="!secret_key && showErrorMessages">Secret Key is required</span> -->
                    <argon-alert v-if="!secret_key && showErrorMessages" color="danger" icon="icon-danger" dismissible>
                      Secret Key is required
                    </argon-alert>
 
                  </div>
                  <!-- <div v-if="error" class="mb-3">
                    <span class="text-danger">{{ error }}</span>
                  </div> -->
 
                  <!-- Modal Footer with Add Provider and Close buttons -->
                  <div class="modal-footer">
                    <argon-button color="success" size="md" variant="gradient" @click="addProvider" type="submit">
                      Add Provider
                    </argon-button>
 
                    <argon-button color="danger" size="md" variant="gradient" @click="toggleModal">
                      Close
                    </argon-button>
                  </div>
 
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
 
      <!-- working k8s modal -->
      <div>
 
        <!-- Modal -->
        <div v-show="isModalVisibles && selectedModal === 'Kubernetes'" class="modal-container" tabindex="-1"
          role="dialog">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
              <!-- Modal Header -->
              <div class="modal-header">
                <h5 class="modal-title">Add Provider</h5>
                <button type="button" class="close" @click="toggleModals" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
 
              <!-- Modal Body -->
              <div class="modal-body">
                <!-- Form with 5 fields -->
                <form>
                  <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
                    {{ selectedModal }}
                  </h3>
 
                  <div class="mb-3">
                    <label for="Api_name" class="form-label">Key name</label>
                    <input type="text" class="form-control"  v-model="api_name" placeholder="Key Name">
                    <argon-alert v-if="!api_name && showErrorMessages" color="danger" icon="icon-danger" dismissible>
                      Key name is required
                    </argon-alert>
 
                  </div>
                  <div class="mb-3">
                    <label for="kubeconfigData" class="form-label">Kubeconfig Data</label>
                    <textarea class="form-control"  v-model="kubeconfigData" placeholder="Kubeconfig Data"
                      required></textarea>
                    <argon-alert v-if="!kubeconfigData && showErrorMessages" color="danger" icon="icon-danger"
                      dismissible>
                      Kubeconfig Data is required
                    </argon-alert>
                  </div>
 
                  
 
 
                  <!-- Modal Footer with Add Provider and Close buttons -->
 
                  <div class="modal-footer">
                    <argon-button color="success" size="md" variant="gradient" @click="addProviderk8s" type="submit">
                      Add Provider
                    </argon-button>
 
                    <argon-button color="danger" size="md" variant="gradient" @click="toggleModals">
                      Close
                    </argon-button>
                  </div>
 
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
 
 
      <!-- Openstack mOdel -->
      <div>
 
<!-- Modal -->
<div v-show="isModalVisibles && selectedModal === 'Openstack'" class="modal-container" tabindex="-1"
   role="dialog">
   <div class="modal-dialog modal-dialog-centered" role="document">
     <div class="modal-content">
       <!-- Modal Header -->
       <div class="modal-header">
         <h5 class="modal-title">Add Provider</h5>
         <button type="button" class="close" @click="OpenstackModal" aria-label="Close">
           <span aria-hidden="true">&times;</span>
         </button>
       </div>
 
       <!-- Modal Body -->
       <div class="modal-body">
         <!-- Form with 5 fields -->
         <form>
           <h3 class="mb-5 text-lg font-normal text-dark dark:text-gray-400">
             {{ selectedModal }}
           </h3>

           <div class="mb-3">
             <label for="Api_name" class="form-label">API Name</label>
             <input type="text" class="form-control"  v-model="api_name" placeholder="api_name">
             <argon-alert v-if="!api_name && showErrorMessages" color="danger" icon="icon-danger" dismissible>
               apiname is required
             </argon-alert>
 
           </div>
 
           <div class="mb-3">
             <label for="Api_name" class="form-label">Username</label>
             <input type="text" class="form-control"  v-model="OpenstackUser" placeholder="Username">
             <argon-alert v-if="!OpenstackUser && showErrorMessages" color="danger" icon="icon-danger" dismissible>
               Username name is required
             </argon-alert>
 
           </div>
           <div class="mb-3">
             <label for="Api_name" class="form-label">Tenant/Project Name</label>
             <input type="text" class="form-control"  v-model="tenant_name" placeholder="Tenant/Project Name">
             <argon-alert v-if="!tenant_name && showErrorMessages" color="danger" icon="icon-danger" dismissible>
              Tenant/Project Name is required
             </argon-alert>
 
           </div>
           <div class="mb-3">
             <label for="Api_name" class="form-label">Password</label>
             <input type="password" class="form-control"  v-model="OpenstackPassword" placeholder="Password">
             <argon-alert v-if="!OpenstackPassword && showErrorMessages" color="danger" icon="icon-danger" dismissible>
               Password is required
             </argon-alert>
 
           </div>
           <div class="mb-3">
             <label for="Api_name" class="form-label">Auth URL</label>
             <input type="text" class="form-control" v-model="auth_url" placeholder="Auth URL">
             <argon-alert v-if="!auth_url && showErrorMessages" color="danger" icon="icon-danger" dismissible>
               AUTH URL name is required
             </argon-alert>
 
           </div>
           <div class="mb-3">
             <label for="Api_name" class="form-label">Region</label>
             <input type="text" class="form-control"  v-model="region" placeholder="Region">
             <argon-alert v-if="!region && showErrorMessages" color="danger" icon="icon-danger" dismissible>
               Region is required
             </argon-alert>
 
           </div>
           
 
           
 
 
           <!-- Modal Footer with Add Provider and Close buttons -->
 
           <div class="modal-footer">
             <argon-button color="success" size="md" variant="gradient" @click="addOpenstack" type="submit">
               Add Provider
             </argon-button>
 
             <argon-button color="danger" size="md" variant="gradient" @click="OpenstackModal">
               Close
             </argon-button>
           </div>
 
         </form>
       </div>
     </div>
   </div>
</div>
</div>
    </div>
 
  </main>
</template>
 
<script>
import setNavPills from "@/assets/js/nav-pills.js";
import setTooltip from "@/assets/js/tooltip.js";
import axios from 'axios';
 
// import ProfileCard from "@/views/components/profileCard.vue";
import ArgonAlert from "@/components/ArgonAlert.vue";
import ArgonButton from "@/components/ArgonButton.vue";
 
const body = document.getElementsByTagName("body")[0];
 
export default {
  name: "profile",
  data() {
    return {
      OpenstackUser: '',
      tenant_name: '',
      OpenstackPassword: '',
      auth_url: '',
      region: '',
 
      isModalVisibles: false, selectedModal: '', kubeconfigData: '',
      isModalVisible: false, user_id: '',
      selectedProvider: '',
      api_name: '', api_endpoint: '', secret_key: '', access_key: '', error: '',
      showErrorMessages: false,
 
      provider_info: [],
      showMenu: false
    };
  },
  components: {
    // ProfileCard,
    ArgonAlert,
    ArgonButton,
  },
 
 
  mounted() {
    this.$store.state.isAbsolute = true;
    setNavPills();
    setTooltip();
  },
  beforeMount() {
    this.$store.state.imageLayout = "profile-overview";
    this.$store.state.showNavbar = false;
    this.$store.state.showFooter = true;
    this.$store.state.hideConfigButton = true;
    body.classList.add("profile-overview");
  },
  beforeUnmount() {
    this.$store.state.isAbsolute = false;
    this.$store.state.imageLayout = "default";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    this.$store.state.hideConfigButton = false;
    body.classList.remove("profile-overview");
  },
  computed: {
    isProviderConnected() {
      return (providerName) => {
        return this.provider_info.some(
          (provider) =>
            provider.provider_name.toLowerCase() === providerName.toLowerCase() &&
            provider.is_connected
        );
      };
    },
  },
 
 
  created() {
    this.user_id = sessionStorage.getItem("user_id");
    this.getAllProviderData();
  },
  methods: {
    toggleModal(selectedProvider) {
      // Reset form fields
      this.api_name = '';
      this.api_endpoint = '';
      this.secret_key = '';
      this.access_key = '';
      this.error = '';
      this.selectedProvider = selectedProvider
      this.isModalVisible = !this.isModalVisible;
      console.log(this.selectedProvider)
    },
    // New method to open kubeconfig_data modal
    toggleModals(selectedProvider) {
      this.kubeconfigData = '';
      this.error = ''; // Assuming you have an error property for validation messages
      this.api_name = '';
 
 
      this.selectedProvider = selectedProvider;
      this.selectedModal = 'Kubernetes';
      this.isModalVisibles = !this.isModalVisibles;
      console.log(this.selectedModal);
    },
    OpenstackModal(selectedProvider) {
      this.OpenstackUser = '';
      this.tennat_name = '';
      this.OpenstackPassword = '';
      this.auth_url = '';
      this.region = '';



      this.selectedProvider = selectedProvider;
      this.selectedModal = 'Openstack';
      this.isModalVisibles = !this.isModalVisibles;
      console.log(this.selectedModal);
    },
    async addProviderk8s() {
      if (!this.api_name || !this.kubeconfigData) {
        this.showErrorMessages = true; // Show error messages
        setTimeout(() => {
          this.showErrorMessages = false; // Hide error messages after 5 seconds
        }, 5000);
        return;
      }
 
      console.log("k8s");
      const fromData = {
        user_id: this.user_id,
        provider_name: this.selectedProvider,
        key_name: this.api_name,
 
 
        // Include kubeconfigDataModal in the payload for Kubernetes Provider
        kubeconfig_data: this.kubeconfigData,
 
      };
      console.log("data")
      await axios.post(`http://172.16.1.56:8002/api/v3/providers/`, fromData)
        .then(() => {
          this.getAllProviderData();
          this.isModalVisibles = !this.isModalVisibles;
        })
        .catch((error) => {
          this.error = "Error adding provider: " + error.message;
        });
    },
 
    async addProvider() {
      // Check for form validation before making the API call
      console.log('addprovider');
      if (!this.api_name || !this.api_endpoint || !this.access_key || !this.secret_key || !this.OpenstackUser || !this.tenant_name  ) {
        this.showErrorMessages = true; // Show error messages
        setTimeout(() => {
          this.showErrorMessages = false; // Hide error messages after 5 seconds
        }, 5000);
        return;
      }
      console.log('addpro');
 
      const fromData = {
        "user_id": this.user_id,
        "provider_name": this.selectedProvider,
        "key_name": this.api_name,
        "provider_url": this.api_endpoint,
        "secret_key": this.secret_key,
        "access_token": this.access_key,

        "OpenstackUsername": this.OpenstackUser,
        "tenant_name": this.tenant_name,
        "OpenstackPassword": this.OpenstackPassword,
        "auth_url": this.auth_url,
        "region": this.region,


      };
      console.log(fromData);
 
      await axios.post(`http://172.16.1.56:8002/api/v3/providers/`, fromData)
        .then(() => {
          this.getAllProviderData();
          this.isModalVisible = !this.isModalVisible;
        })
        .catch((error) => {
          this.error = "Error adding provider: " + error.message;
        });
    },

    async addOpenstack() {
      // Check for form validation before making the API call
      console.log('addprovider');
      // if (!this.OpenstackUser || !this.OpenstackPassword || !this.auth_url || !this.region || !this.tenant_name  ) {
      //   this.showErrorMessages = true; // Show error messages
      //   setTimeout(() => {
      //     this.showErrorMessages = false; // Hide error messages after 5 seconds
      //   }, 5000);
      //   return;
      // }
      console.log('addpro');
 
      const fromData = {
        "user_id": this.user_id,

        "provider_name": this.selectedProvider,
        "key_name": this.api_name,
       

        "OpenstackUsername": this.OpenstackUser,
        "tenant_name": this.tenant_name,
        "OpenstackPassword": this.OpenstackPassword,
        "auth_url": this.auth_url,
        "region": this.region,


      };
      console.log(fromData);
 
      await axios.post(`http://172.16.1.56:8002/api/v3/providers/`, fromData)
        .then(() => {
          this.getAllProviderData();
          this.isModalVisible = !this.isModalVisible;
        })
        .catch((error) => {
          this.error = "Error adding provider: " + error.message;
        });
    },
    getAllProviderData() {
      axios.get(`http://172.16.1.56:8002/api/v3/providers/by-user/${this.user_id}/`)
        .then((response) => {
          this.provider_info = response.data;
          console.log(response.data);
        })
 
    },
  },
};
</script>
 
<style scoped>
.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 130%;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1050;
  overflow: auto;
}
</style>