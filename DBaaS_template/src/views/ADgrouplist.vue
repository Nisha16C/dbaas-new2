<template>
  <main>
      <!-- Container for displaying Active Directory groups -->
      <div class="container-fluid mt-7">
          <div class="card shadow-lg mt-n6">
              <div class="card-body p-3">
                  <div class="row gx-4">
                      <div class="col-auto my-auto">
                          <div class="h-100">
                              <router-link to="/User-Management">
                                  <i class="fas fa-arrow-left mr-2"></i>
                              </router-link>
                              <h5 class="mb-1 text-2xl">List Of Active Directory Groups</h5>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>

      <!-- Display groups and their members -->
      <div class="py-4 container-fluid">
          <div class="row">
              <div class="col-md-12">
                  <div class="card" style="height: 650px; overflow-y: auto;">
                      <div class="card-body">
                          <!-- Iterate over each AD group -->
                          <div v-for="group in adGroups" :key="group.group_name">
                              <!-- Group name with buttons on the same line -->
                              <div class="d-flex justify-content-between align-items-center">
                                  <h6 @click="toggleMembers(group)" class="group-name">{{ group.group_name }}</h6>
                                  <argon-button color="success" size="md" variant="gradient" @click="prepareAssignRoles(group)" class="ml-4">
                                      Assign Roles
                                  </argon-button>
                              </div>
                              <hr />
                              <!-- Member list -->
                              <ul v-if="group.showMembers">
                                  <li v-for="member in group.members" :key="member">{{ member }}</li>
                              </ul>
                              <!-- Display assigned role for the group -->
                              <div v-if="group.assignedRole">
                                  <p>Assigned Role: {{ group.assignedRole }}</p>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>

      <!-- Role assignment modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" :class="{ 'show': isModalVisible }">
          <div class="modal-dialog" role="document">
              <div class="modal-content">
                  <div class="modal-header">
                      <h2 class="modal-title" id="exampleModalLabel">Select Role</h2>
                      <button type="button" class="close" @click="closeModal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="modal-body">
                      <div class="form-check" v-for="role in roles" :key="role.id">
                          <input v-model="selectedRole" class="form-check-input" type="radio" :id="'roleCheckbox_' + role.name" :value="role.name" />
                          <label class="form-check-label" :for="'roleCheckbox_' + role.name">{{ role.name }}</label>
                      </div>
                  </div>
                  <div class="modal-footer">
                      <argon-button color="secondary" size="md" variant="gradient" @click="closeModal">
                          Cancel
                      </argon-button>
                      <argon-button color="danger" size="md" variant="gradient" @click.prevent="assignGroupRoles">
                          Assign Role
                      </argon-button>
                  </div>
              </div>
          </div>
      </div>
  </main>
</template>

<script>
import { API_ENDPOINT } from '@/../apiconfig.js';
import axios from 'axios';
import ArgonButton from "@/components/BB_Button.vue"; // Import ArgonButton component

export default {
  data() {
      return {
          apiUrl: API_ENDPOINT,
          adGroups: [],
          roles: [{ id: 1, name: 'Admin' }, { id: 2, name: 'Standard' }],
          selectedRole: '',
          selectedGroup: null,
          isModalVisible: false, // Track modal visibility
      };
  },
  components: {
      ArgonButton,
  },
  created() {
      this.fetchADGroups();
  },
  methods: {
      fetchADGroups() {
          axios
              .get(`${this.apiUrl}/api/v1/list-gmember/`)
              .then(response => {
                  this.adGroups = response.data.groups.map(group => ({
                      ...group,
                      showMembers: false,
                      assignedRole: group.assignedRole || '', // Initialize assignedRole from backend
                  }));
              })
              .catch(error => {
                  console.error('Error fetching AD groups:', error);
              });
      },
      fetchGroupRole(group) {
          axios
              .get(`${this.apiUrl}/api/v1/get-group-role/${encodeURIComponent(group.group_name)}/`)
              .then(response => {
                  if (response.data.success) {
                      this.selectedRole = response.data.roles[0] || ''; // Assuming one role per group
                  } else {
                      console.error('Error fetching group role:', response.data.message);
                  }
              })
              .catch(error => {
                  console.error('Error fetching group role:', error);
              });
      },
      toggleMembers(group) {
          group.showMembers = !group.showMembers;
      },
      prepareAssignRoles(group) {
          this.selectedGroup = group;
          this.selectedRole = ''; // Reset selectedRole

          this.fetchGroupRole(group); // Fetch the role for the selected group
          this.isModalVisible = true; // Show the modal
      },
      assignGroupRoles() {
          if (!this.selectedGroup || !this.selectedRole) {
              console.error('Group or role not selected.');
              return;
          }
          axios
              .post(`${this.apiUrl}/api/v1/adgroup-role/`, {
                  group_name: this.selectedGroup.group_name,
                  role_name: this.selectedRole,
                  sAMAccountNames: this.selectedGroup.members,
              })
              .then(response => {
                  if (response.data.success) {
                      console.log('Role assigned successfully:', response.data.message);
                      this.selectedGroup.assignedRole = this.selectedRole; // Update assignedRole in adGroups
                      this.closeModal(); // Hide the modal after role assignment
                  } else {
                      console.error('Error assigning role:', response.data.message);
                  }
              })
              .catch(error => {
                  console.error('Error assigning role:', error);
              });
      },
      closeModal() {
          this.selectedRole = ''; // Reset selected role
          this.isModalVisible = false; // Hide the modal
      },
  },
};
</script>

<style scoped>
.group-name {
  cursor: pointer;
}

.group-name:hover {
  color: blue;
}

.modal.show {
  display: block !important;
}
</style>
