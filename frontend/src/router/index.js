import Vue from "vue";
import VueRouter from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import Home from "@/views/Home"

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
];

const router = new VueRouter({
  mode: "history",
  base: '/owner/',
  routes,
});

export default router;
