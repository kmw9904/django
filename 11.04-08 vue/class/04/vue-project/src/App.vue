<template>
  <div>
    <!-- 텍스트 보간법 {{ 반응형 변수 }} -->
    <h1>{{ message }}</h1>
    <p>첫 댓글이네요</p>
    <!-- 기본적으로 HTML에서는 대소문자를 구분하지 않는다 -->
    <!-- 요소의 속성으로 원하는 데이터를 전달 -->
    <ChileComponent msg="안녕하세요" />

    <ChileComponent v-bind:msg="message" />

    <ListComponent :fruits="items" />
  </div>
</template>

<script setup>
// @ : src 폴더의 경로
import ChileComponent from "@/components/ChileComponent.vue";
import ListComponent from "@/components/ListComponent.vue";
import { ref } from "vue";
const message = ref("안녕하세요!");

let idx = 1;
const items = ref([
  { id: idx++, name: "사과" },
  { id: idx++, name: "딸기" },
  { id: idx++, name: "바나나" },
]);
</script>

<style scoped>
h1 {
  color: blue;
}
</style>
