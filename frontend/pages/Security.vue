<template>
  <div class="security-page">
    <h2>Security Dashboard</h2>
    <SecurityStatus />
    <SecuritySettings />
  </div>
</template>

<script setup>
import SecurityStatus from '../components/SecurityStatus.vue'
import SecuritySettings from '../components/SecuritySettings.vue'
</script>

<style scoped>
.security-page { padding: 1rem; }
</style>
