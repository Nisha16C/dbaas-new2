import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
// import Tables from "../views/Tables.vue";

import ClusterCreate from "../views/UserDashboard/Clusterinfo.vue";
import ClusterSetting from "../views/UserDashboard/ClusterSetting.vue";
import Clusterss from "../views/UserDashboard/Clusters.vue";
import Projectss from "../views/UserDashboard/Projects.vue";
import Providers from "../views/UserDashboard/Providers.vue";
import UserDashboard from "../views/UserDashboard/UserDashboard.vue";
import Result from "../views/UserDashboard/Result.vue";
import Delete from "../views/UserDashboard/delete.vue";


import ClustersManagement from "../views/Clusters.vue";
import ProjectManagement from "../views/Projects.vue";
import UserManagement from "../views/UserMgmt.vue";
import Signin from "../views/Signin.vue";
import Backup from "../views/Backup.vue";
import BackupForm from "../views/BackupForm.vue";
import Cconfiguration from "../views/UserDashboard/Dbconfig.vue";
import RestoreBackup from "../views/RestoreBackup.vue";
import BackupDetails from "../views/BackupDetails.vue";

import Profile from "../views/Profile.vue";
import ProjectSelect from "../views/UserDashboard/ProjectSelect.vue";
import ActivityLog from "../views/ActivityLog.vue";
import USER from "../views/USER.vue"; 

import BackupSchedule from "../views/BackupSchedule.vue";
// import BackupDetails from "../views/BackupDetails.vue";


const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/signin",
  },

  // Admin route

  {
    path: "/scheduled-backups",
    name: "Schedule Backup",
    component: BackupSchedule,
  },
  {
    path: "/admin-dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/Cconfiguration",
    name: "Cconfiguration",
    component: Cconfiguration,
  },
  {
    path: "/admin-backup",
    name: "Backup",
    component: Backup,
  },
  {
    path: "/admin-backup/form",
    name: "Create Backup",
    component: BackupForm,
  },
  {
    path: "/admin-backup/restore-backup",
    name: "Restore Backup",
    component: RestoreBackup,
  },
  {
    path: "/backup/:serverName",
    name: "BackupDetails",
    component: BackupDetails,
    props:true,
  }
,
  {
    path: "/User-dashboard",
    name: "User Dashboard",
    component: UserDashboard,
  },
  // {
  //   path: "/tables",
  //   name: "Tables",
  //   component: Tables,
  // },

  {
    path: "/Clusters-Management",
    name: "Clusters-Management",
    component: ClustersManagement,
  },

  {
    path: "/Cluster-Setting",
    name: "Cluster-Setting",
    component: ClusterSetting,
  },

  // User Route
  {
    path: "/Clusters",
    name: "Clusters",
    component: Clusterss,
  },
  {
    path: "/result",
    name: "Result",
    component: Result,
  },
  {
    path: "/delete",
    name: "Delete",
    component: Delete,
  },
  {
    path: "/Cluster-Create",
    name: "Cluster-Create",
    component: ClusterCreate,
  },
  {
    path: "/Projects",
    name: "Projects",
    component: Projectss,
  },

  {
    path: "/Provider",
    name: "Providers",
    component: Providers,
  },
  {
    path: "/User-Management",
    name: "User-Management",
    component: UserManagement,
  },
  {
    path: "/Project-Management",
    name: "Project-Management",
    component: ProjectManagement,
  },

  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/signin",
    name: "Signin",
    component: Signin,
  },
  {
    path: "/Project-Select",
    name: "Project Select",
    component: ProjectSelect,
  },

  {
    path: "/ActivityLog",
    name: "ActivityLog",
    component: ActivityLog,
  },
  {
    path: "/USER",
    name: "USER",
    component: USER,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
