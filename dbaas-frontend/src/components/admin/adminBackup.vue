<template>
    <adminLeftsidebar />
    <div>
        <div class="cluster p-4 sm:ml-64 mt-24    flex">
            <div class=" p-4 w-full bg-gray-100 flex">
                <div class="text-black font-semibold text-4xl">Backup and Restore</div>
            </div>
            <div class="ml-auto">


            </div>
        </div>

        <div class="w-full h-15 border-b-2 p-4 sm:ml-64 border-solid mt-10 flex items-center">
            <div class=" ">
                <div class="flex items-center px-5 py-6 bg-gray-100 rounded-md shadow-sm">
                    <div class="p-3 bg-indigo-600 bg-opacity-75 rounded-full">
                        <svg viewBox="64 64 896 896" focusable="false" data-icon="database" width="1em" height="1em"
                            fill="currentColor" class="w-6 h-6" aria-hidden="true">
                            <path
                                d="M832 64H192c-17.7 0-32 14.3-32 32v832c0 17.7 14.3 32 32 32h640c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32zm-600 72h560v208H232V136zm560 480H232V408h560v208zm0 272H232V680h560v208zM304 240a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0zm0 272a40 40 0 1080 0 40 40 0 10-80 0z">
                            </path>
                        </svg>
                    </div>


                </div>
            </div>

            <!-- Search Bar -->
            <div class="relative ml-4 mr-4">
                <input type="text"
                    class="pl-8 pr-3 py-2 border rounded-lg w-48 bg-white border-gray-400 focus:border-primary-500 focus:ring-primary-500"
                    placeholder="Search" />
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M21 21l-5.2-5.2M15 10.5a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z"></path>
                    </svg>
                </div>
            </div>
            <div class="ml-4">
                <!-- Project Dropdown -->
                <span class="font-extrabold "> Clusters: </span>
                <select class="rounded-md ">
                    <option value="">All Users</option>
                    <option>Ankit</option>
                    <option>Preeti</option>
                    <option>Aastha</option>
                </select>
            </div>
        </div>

        <!-- New Table  -->
        <div class="flex flex-col mt-8 sm:ml-64">
            <div class="py-2 -my-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">


                <div
                    class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
                    <table class="min-w-full">
                        <thead>
                            <tr>
                                <th
                                    class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                    User
                                </th>
                                <th
                                    class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                    Project
                                </th>
                                <th
                                    class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                    Cluster Name
                                </th>
                                <th
                                    class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                    Provider
                                </th>
                                <th
                                    class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                    Database Version
                                </th>
                                <th
                                    class="px-6 py-3 text-xs font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                                    Created On
                                </th>
                                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50"></th>
                            </tr>
                        </thead>

                        <tbody class="bg-white">
                            <tr>
                                <td class=" border-b border-gray-200 whitespace-nowrap">
                                    <div class="flex items-center">
                                        <div class="flex-shrink-0 ">
                                            <button
                                                class="flex mt-1 items-center justify-center h-6 w-20 bg-indigo-200 rounded-lg">
                                                <div class="text-sm font-medium leading-5 text-gray-900">
                                                Preeti
                                                </div>
                                            </button>
                                        </div>

                                        <div class="ml-4">
                                            <div class="text-sm font-medium leading-5 text-gray-900">
                                              
                                            </div>
                                            <div class="text-sm leading-5 text-gray-500">
                                                
                                            </div>
                                        </div>
                                    </div>
                                </td>

                                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                                    <div class="text-sm leading-5 text-gray-900">
                                        <span class="inline-flex px-2 text-xs font-semibold leading-5
                     text-green-800 bg-green-100 rounded-full"> test-1 </span>

                                    </div>

                                </td>

                                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                                    <span class="inline-flex px-2 text-xs  font-semibold leading-5
                    text-gray-500 rounded-full">demo </span>
                                </td>

                                <td
                                    class="px-6 py-4 text-sm leading-5 text-gray-500 border-b border-gray-200 whitespace-nowrap">
                                    <span>Kubernetes</span>
                                </td>

                                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                                    <span class="inline-flex px-2 text-xs font-semibold leading-5
                 text-yellow-500 bg-yellow-100 rounded-full">Postgres 15</span>
                                </td>
                                <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                                    <span class="inline-flex px-2 text-xs font-semibold leading-5
                 text-yellow-500 bg-yellow-100 rounded-full">2 days ago</span>
                                </td>


                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import adminLeftsidebar from '@/components/admin/adminLeftsidebar.vue'

export default {
    components: {
        adminLeftsidebar,
    }
};
</script>