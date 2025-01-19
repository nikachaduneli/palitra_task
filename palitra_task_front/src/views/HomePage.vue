<template>
  <div class="bg-gray-100 min-h-screen p-6">

    <!-- Blogs List -->
    <div class="container mx-auto">
      <!-- Pass the blogs to the blogList component -->
      <BlogList :blogs="blogs" />
    </div>
  </div>
</template>

<script>
import BlogList from "@/components/BlogList.vue";

export default {
  name: "HomePage",
  components: {
    BlogList
  },
  data() {
    return {
      blogs: []
    };
  },
  async mounted() {
    const apiBaseUrl = process.env.VUE_APP_API_BASE_URL;
    const blogsEndpoint = `${apiBaseUrl}/blog/blogs`;

    try {
      const response = await fetch(blogsEndpoint, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        }
      });

      if (response.ok) {
        const data = await response.json();
        this.blogs = data.results;
      } else {
        console.error("Failed to fetch blogs:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching blog posts:", error);
    }
  }
};
</script>
