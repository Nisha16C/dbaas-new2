<template>
  <adminLeftsidebar />
    <div class="flex fixed h-screen ml-[230px] mt-10 ">          
       
      <div :class="['h-screen pb-5 flex-1 flex flex-col overflow-hidden w-[1690px]']">           
     
     <div class="flex-1 overflow-x-hidden overflow-y-auto " style="margin-bottom: 20px;">

        
          <!-- <embed  width="100%"    height="100%" :src="embedUrl" frameborder="0" allowfullscreen class="m-5" > -->
      
   
          <!-- <iframe  width="100%"
                  height="100%" :src="embedUrl" frameborder="0" allowfullscreen class="m-5" >
          </iframe> -->
   
          
   
          <embed
           width="100%"    height="100%" :src="embedUrl" frameborder="0" allowfullscreen class="m-5" >
           
        </div>
       </div>
      </div>
   
  </template>
   
   
       
      
  <script>
  import { ref, computed } from 'vue';
  import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue'
   
  export default {
    components: {
      adminLeftsidebar,
    },
    setup() {
      const embedUrl = computed(() => {
        return `http://172.16.1.54:3000/d/000000039/postgresql-database?orgId=1&refresh=10s`
        // return `http://172.16.1.55:5601/app/dashboards?auth_provider_hint=anonymous1#/view/1002c610-a23f-11ed-9c45-1d7f2cbf4bd8?embed=true&_g=(refreshInterval%3A(pause%3A!t%2Cvalue%3A60000)%2Ctime%3A(from%3Anow-1y%2Fd%2Cto%3Anow))&show-top-menu=true&show-query-input=true&show-time-filter=true%22`;
      });
      
      return {
        embedUrl
      };
    },
  };
  </script>
  