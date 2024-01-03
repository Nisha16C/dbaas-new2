<template>
   <leftSidebar />

   <div class="pt-24 ml-64 main_content w-full h-[100vh]">
      <div class="container px-3 mx-auto flex flex-wrap flex-col md:flex-row items-center">
         <!--Left Col-->
         <div :class="{ 'zoom-in': zoomIn }"
            class="flex flex-col w-full md:w-2/5 justify-center items-start text-center md:text-left">
            <p class="uppercase tracking-loose w-full text-white">What business we are?</p>
            <h1 class="my-4 text-4xl font-bold leading-tight text-white">
               Empower Your Data Journey with BitBlast!!
            </h1>
            <p class="leading-normal text-2xl mb-8 text-white">
               Experience the transformational power of BitBlast as it propels your data journey forward!
            </p>


            <router-link to="clusterCreate"  class="
               relative inline-flex items-center  justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-full
               group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500
                  hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300
                  dark:focus:ring-blue-800">
                     <span
                        class="relative px-6 text-lg py-2.5 transition-all ease-in duration-75 text-black bg-white  group-hover:bg-opacity-0">
                        Create New Cluster
                     </span>
            </router-link>

         </div>
         <!--Right Col-->
         <div class="w-full md:w-3/5 py-6 text-center">
            <img class="w-full md:w-4/5 z-50" src="@/assets/static/frontPagesvg2.svg " />
         </div>
      </div>
   </div>

   
</template>
 
<script>
import leftSidebar from '@/components/leftSidebar.vue';
import fooTer from '@/components/fooTer.vue';

export default {
   components: {
      leftSidebar,
      fooTer,
   },
   data() {
      return {
         Username: '',
         zoomIn: false,
         zoomOut: false,
      };
   },
   created() {
      this.Username = sessionStorage.getItem("username");
   },
   mounted() {
      // Add the zoom-in class after a delay
      setTimeout(() => {
         this.zoomIn = true;
      }, 500);

      // Add the zoom-out class after a longer delay
      setTimeout(() => {
         this.zoomOut = true;
      }, 800);
   },
}

</script>
<style scoped>
.zoom-in {
   animation: zoomIn 1s;
}

.zoom-out {
   animation: zoomOut 1s;
}

@keyframes zoomIn {
   from {
      transform: scale(0.8);
      opacity: 0;
   }

   to {
      transform: scale(1);
      opacity: 1;
   }
}

@keyframes zoomOut {
   from {
      transform: scale(1);
      opacity: 1;
   }

   to {
      transform: scale(0.8);
      opacity: 0;
   }
}

.main_content {
   background: linear-gradient(90deg, #25316D 0%, #8b7c59 100%);

}</style>
 
 