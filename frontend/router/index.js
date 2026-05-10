import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Security from '../pages/Security.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/security', name: 'Security', component: Security },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
