<template>
  <div class="settings">
    <h3>Security Settings</h3>
    <button @click="toggleEncryption">Toggle Encryption ({{ encryptionEnabled ? 'On' : 'Off' }})</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const encryptionEnabled = ref(false)

async function toggleEncryption() {
  try {
    const res = await axios.post('/api/security/encrypt', { enable: !encryptionEnabled.value })
    encryptionEnabled.value = res.data.enabled
  } catch (e) {
    console.error(e)
  }
}
</script>

<style scoped>
.settings { margin-top: 2rem; }
button { padding: 0.5rem 1rem; }
</style>
