<template>
  <div>
    <h2>Security Status</h2>
    <button @click="checkMalware">Check Malware</button>
    <p v-if="malwareResult">Result: {{ malwareResult }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import api from '../services/api';

const malwareResult = ref('');

const checkMalware = async () => {
  const res = await api.post('/api/security/malware-check', { data: 'sample' });
  malwareResult.value = res.data.result;
};
</script>
