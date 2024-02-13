<template>
    <div class="card">
        <div class="card-header pb-0">
            <h6> Selected Projects Info : {{ project_name }} </h6>
        </div>

        <div class="card-body px-0 pt-0 pb-2">
            <div class="table-responsive p-0">
                <table class="table align-items-center mb-0">
                    <thead>
                        <tr>
                            <th class="text-uppercase text-secondary font-weight-bolder opacity-7"> Select</th>
                            <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                                project id & Name</th>
                            <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                                CREATE DATE </th>
                            <th class="text-center text-uppercase text-secondary  font-weight-bolder opacity-7">
                                Update Date </th>
                            <th class="text-secondary opacity-7"> </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(project, index) in projects" :key="index">
                            <td>
                                <button @click="selectProject(project)" class="btn  mb-0  btn-info">Select</button>
                            </td>
                            <td>
                                <div class="d-flex flex-column text-center">
                                    <h6 class="mb-0 text-sm">{{ project.id }}</h6>
                                    {{ project.project_name }}
                                </div>
                            </td>
                            <td>
                                <div class="d-flex flex-column text-center">
                                    {{ formatDate(project.created_date) }}
                                </div>
                            </td>
                            <td class="align-middle text-center">
                                <span class="d-flex flex-column text-center">{{ formatDate(project.updated_date) }}</span>
                            </td>
                            <td class="align-middle  text-center">
                                <span v-if="isSelected(project.project_name)"
                                    class="d-flex flex-column text-center text-success">SELECTED</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>


        </div>
    </div>
</template>
  
<script>
import { mapState, mapActions } from 'vuex';

export default {
    name: "projects-table",
    props: {
        projects: {
            type: Array,
            required: true,
        },
    },
    created() {
        // this.updateGlobalProjectName()
    },
    data() {
        return {
            currentProject: '',
        }
    },

    computed: {
        ...mapState(['project_name', 'project_id']),
    },
    methods: {
        ...mapActions(['updateGlobalProjectName', 'updateGlobalProjectId']),
        async selectProject(project) {
            try {
                await this.updateGlobalProjectName(project.project_name);

                await this.updateGlobalProjectId(project.id);
                console.log('State updated successfully');
            } catch (error) {
                console.error(error);
            }
        },

        isSelected(projectName) {
            if (this.project_name === projectName) {
                console.log("true");
                return true
            } else {
                return false;
            }

        },

        formatDate(dateString) {
            const options = { year: 'numeric', month: 'short', day: 'numeric' };
            return new Date(dateString).toLocaleDateString('en-US', options);
        },

    },
};
</script>
    