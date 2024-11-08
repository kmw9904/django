<template>
  <div>
    <h1>{{ props.msg }}</h1>
  </div>
</template>

<script setup>
const props = defineProps(["msg"]);
</script>

<style scoped></style>
