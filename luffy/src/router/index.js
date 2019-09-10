import Vue from 'vue'
import Router from 'vue-router'
import Index from "@/components/Index";
import Course from "../components/Course";



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    }
  ]
})
