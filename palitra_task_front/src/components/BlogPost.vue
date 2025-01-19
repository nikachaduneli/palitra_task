<template>
  <div>
    <h1>{{ blog.title }}</h1>
    <p>{{ blog.content }}</p>
  </div>
</template>

<script>
export default {
  props: ['blog'],
};
</script>
