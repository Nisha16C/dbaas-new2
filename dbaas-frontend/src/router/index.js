import { createRouter, createWebHistory } from "vue-router";

import loginPage from "@/components/loginPage.vue";

import clusterCreate from "@/components/clusterCreate.vue";
import projects from "@/components/projects.vue";
import result from "@/components/result.vue";
import clusterSetting from "@/components/clusterSetting.vue";
import clusterProvider from "@/components/providerPage.vue";
import overviewPage from "@/components/overviewPage.vue";

import projectsManagement from "@/components/admin/projectManagement.vue";
import clustersManagement from "@/components/admin/clusterManagement.vue";
import usersManagement from "@/components/admin/userManagement.vue";
import Createuser from "@/components/admin/createUser.vue";
import roles from "@/components/admin/roles.vue";
// import RoleAssignmentModal from "@/components/admin/RoleAssignmentModal.vue";

import homeView from "@/views/HomeView.vue";
import AdminDashboard from "@/views/AdminView.vue"; 

const routes = [
  {
    name: "login",
    path: "/",
    component: loginPage,
  },
  {
    name: "providers",
    path: "/providers",
    component: clusterProvider,
  },
  {
    name: "result",
    path: "/result",
    component: result,
  },
  {
    name: "overviews",
    path: "/overview",
    component: overviewPage,
  },
  {
    name: "clusterCreate",
    path: "/clusterCreate",
    component: clusterCreate,
  },
  {
    name: "Createuser",
    path: "/Createuser",
    component: Createuser,
  },
  {
    name: "cluster-setting",
    path: "/cluster-setting",
    component: clusterSetting,
  },
  {
    name: "home",
    path: "/home",
    component: homeView,
  },
  {
    name: "AdminDashboard",
    path: "/AdminDashboard",
    component: AdminDashboard,
  },
  {
    name: "projects",
    path: "/projects",
    component: projects,
  },

  {
    name: "projectsManagement",
    path: "/projects-management",
    component: projectsManagement,
  },

  {
    name: "clustersManagement",
    path: "/cluster-management",
    component: clustersManagement,
  },
  {
    name: "usersManagement",
    path: "/users-management",
    component: usersManagement,
  },
  { path: '/user/:userId', name: "roles", component: roles, props: true },
  // { path: '/role-assign', name: "role-assign", component: RoleAssignmentModal, props: true },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: "dark:text-pink-400",
});

// Create the router guard
router.beforeEach((to, from, next) => {
  const allowedPaths = ["/"];

  if (allowedPaths.includes(to.path)) {
    next();
  } else {
    const user_id = sessionStorage.getItem("user_id");
    const username = sessionStorage.getItem("username");

    if (user_id || username) {
      next();
    } else {
      next("/");
    }
  }
});

export default router;
