import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Course from '../views/Course.vue'
import Eventlist from '../views/event_list.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Event_list',
    name: 'Event_list',
    component: Eventlist
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/Course/:id',
    name: 'Course',
    component: Course,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
