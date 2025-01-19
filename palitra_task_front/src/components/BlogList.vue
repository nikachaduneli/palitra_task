<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Loop through blogs -->
    <div
        v-for="blog in blogs"
        :key="blog.id"
        class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300"
    >
      <!-- blog Image -->
      <img
          :src="blog.main_image"
          :alt="blog.title"
          class="w-full h-64 object-cover rounded-lg mb-4"
      />

      <h2 class="text-2xl font-semibold text-gray-800">{{ blog.title }}</h2>
      <p class="text-gray-600 mt-2 line-clamp-3">{{ blog.description }}</p>
      <router-link
          :to="'/blog/' + blog.id"
          class="inline-block mt-4 text-blue-500 hover:underline"
      >
        Read more
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlogList",
  props: {
    blogs: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
/* Tailwind line-clamp to limit description length */
@import "tailwindcss/utilities";

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
