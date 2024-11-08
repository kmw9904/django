<template>
  <li>{{ props.item.id }} / {{ props.item.name }}</li>
</template>

<script setup>
const props = defineProps(["item"]);
</script>

<style scoped></style>
