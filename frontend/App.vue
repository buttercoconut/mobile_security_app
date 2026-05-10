# frontend/App.vue
<template>
  <div id="app">
    <h1>Mobile Security Dashboard</h1>
    <SecurityStatus />
  </div>
</template>

<script>
import SecurityStatus from './components/SecurityStatus.vue'
export default {
  components: { SecurityStatus }
}
</script>
