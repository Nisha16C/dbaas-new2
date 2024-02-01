<template>
    <leftSidebar />
      <div class="flex fixed h-screen  ml-[230px]">          
         
        <div :class="['h-screen pb-5 flex-1 flex flex-col overflow-hidden w-[1690px]']">           
       
       <div class="flex-1 overflow-x-hidden overflow-y-auto " style="margin-bottom: 20px;">
        <embed  width="100%"    height="100%" :src="embedUrl" frameborder="0" allowfullscreen class="m-5" >
             
          </div>
         </div>
        </div>
     
    </template>
     
     
         
        
    <script>
    import { ref, computed } from 'vue';
    import leftSidebar from '@/components/leftSidebar.vue'
     
    export default {
      components: {
        leftSidebar,
      },
      setup() {
        const embedUrl = computed(() => {
          return `http://172.16.1.54:3000/d/08/postgresql-for-other-users?orgId=1&refresh=10s&from=1706705270228&to=1706705570229&theme=light`;
        });
        
        return {
          embedUrl
        };
      },
    };
    </script>
    