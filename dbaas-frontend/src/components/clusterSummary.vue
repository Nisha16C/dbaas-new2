<template>
  <div class=" cluster-sum  h-auto mt-20 p-5">
    <h1 class="text-2xl mb-5">Cluster Summary</h1>
    <table class="bg-gray-100 ">
      <tr>
        <th>Cluster Type</th>
        <td v-if="selectedType"> {{ selectedType }} </td>
        
      </tr>
      <tr>
        <th>Cluster Nodes</th>
        
        <td v-if="selectedType=='Standalone'"> 1 Node</td>
        
        <td v-if="selectedType=='multiple'"> 3 Node</td>
      </tr>
     
      <tr>
        <th>Provider</th>
        <td v-if="selectedProvider"> {{selectedProvider}} </td>
       
      </tr>
  
      <tr>
        <th>Cluster Name</th>
        <td>Default</td>
      </tr>
      <tr>
        <th>Postgres Type</th>
        <td>PostgreSQL</td>
      </tr>
      <tr>
        <th>Postgres Version</th>
        <td>{{postgres_version}}</td>
      </tr>
      <tr>
        <th>Instance Size</th>
        <td>2vcpu, 8gb </td>
      </tr>
      <tr>
        <th>Volume Type</th>
        <td>General Purpose SSD (gp3)</td>
      </tr>
      <tr>
        <th>Volume Properties</th>
        <td>4 Gi, 3000 IOPS, 125 MB/s Disk Throughput</td>
      </tr>
      <tr>
        <th>Networking</th>
        <td>Private</td>
      </tr>
      <!-- <tr>
        <th>Backups Retention</th>
        <td>30 Days</td>
      </tr> -->
      <!-- <tr>
        <th>Maintenance Window</th>
        <td>Not Enabled</td>
      </tr> -->
      <!-- <tr>
        <th>PgBouncer</th>
        <td>Not Enabled</td>
      </tr>
      <tr>
        <th>pgvector</th>
        <td>Not Enabled</td>
      </tr> -->
    </table>

  </div>
</template>

<script>
import { useInputStore } from '@/stores/clusterStore';
export default {
  
  data() {
    return {
      defaultCluster: 'Standalone',
      defaultNode: 1, defaultProvider: 'Cloudstack',
      selectedTools: [],
      database_version: '',
      cluster_name: '',
      selectedType: 'Standalone',
      selectedProvider: 'Cloudstack',
    };
  },
  computed: {
    selectedType() {
      return useInputStore().selectedType;
    },
    selectedProvider() {
      return useInputStore().selectedProvider;
    },
    postgres_version() {
      return useInputStore().postgres_version;
    },
  },
};
</script>