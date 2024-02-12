<template>
    <div class="card">
        <div class="card-header pb-0">
            <h6> Projects info User {{ project_name }} </h6>
        </div>

        <div class="card-body px-0 pt-0 pb-2">
            <div class="table-responsive p-0">
                <table class="table  table-responsive">
                    <thead>
                        <tr>
                            <th scope="col">Select</th>
                            <th scope="col">Project ID</th>
                            <th scope="col">Project Name</th>
                            <th scope="col">Created Date</th>
                            <th scope="col">Updated Date</th>
                            <th scope="col">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="project in projects" :key="project.id">
                            <td>
                                <button @click="selectProject(project)" class="btn btn-info">Select</button>
                            </td>
                            <td>{{ project.id }}</td>
                            <td>{{ project.project_name }}</td>
                            <td>{{ formatDate(project.created_date) }}</td>
                            <td>{{ formatDate(project.updated_date) }}</td>
                            <td>
                                <span v-if="isSelected(project.project_name)" class="text-success">Selected</span>
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
    