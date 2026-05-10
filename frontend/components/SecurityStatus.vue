# frontend/components/SecurityStatus.vue
<template>
  <div class="security-status">
    <button @click="fetchStatus">Refresh Status</button>
    <pre>{{ status }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const status = ref('Loading...')
const fetchStatus = async () => {
  try {
    const res = await $axios.get('http://localhost:8000/events')
    status.value = JSON.stringify(res.data, null, 2)
  } catch (e) {
    status.value = 'Error fetching status'
  }
}
fetchStatus()
</script>
