<template>
  <div class="status">
    <p>Current Security Status: <strong>{{ status }}</strong></p>
    <ul>
      <li v-for="event in events" :key="event.id">{{ event.timestamp }} - {{ event.message }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useSecurityStore } from '../store'

const store = useSecurityStore()
const status = ref('unknown')
const events = ref([])

onMounted(async () => {
  await store.fetchStatus()
  status.value = store.status
  events.value = store.events
})
</script>

<style scoped>
.status { margin-top: 1rem; }
</style>
