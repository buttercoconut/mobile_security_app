import { createRouter, createWebHistory } from 'vue-router';
import SecuritySettings from '../components/SecuritySettings.vue';
import SecurityStatus from '../components/SecurityStatus.vue';

const routes = [
  { path: '/', component: SecurityStatus },
  { path: '/settings', component: SecuritySettings },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
