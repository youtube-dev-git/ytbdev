import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Home_user from '../views/Home_user.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Course from '../views/Course.vue'
import Expert from '../views/Expert.vue'
import Expert_add from '../views/Expert_add.vue'
import Eventlist from '../views/event_list.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Home/user/:pseudo',
    name: 'Home_user',
    component: Home_user,
    props: true
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Expert',
    name: 'Expert',
    component: Expert
  },
  {
    path: '/Expert/add',
    name: 'Expert_add',
    component: Expert_add
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
