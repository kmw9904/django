<template>
  <ul>
    <ListItemComponent v-for="fruit in props.fruits" :key="fruit.id" :item="fruit" />
  </ul>
</template>

<script setup>
import ListItemComponent from "@/components/ListItemComponent.vue";
const props = defineProps(["fruits"]);
</script>

<style scoped></style>
