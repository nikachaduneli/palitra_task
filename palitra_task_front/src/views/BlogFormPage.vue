<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="bg-white p-10 rounded-lg shadow-md w-full max-w-4xl">
      <h2 class="text-2xl font-bold mb-4 text-center">{{ blogId ? 'Edit Blog' : 'Create Blog' }}</h2>
      <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
        <div class="mb-6">
          <label for="title" class="block text-sm font-semibold text-gray-700">Title</label>
          <input
              v-model="title"
              type="text"
              id="title"
              class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
              placeholder="Enter blog title"
          />
        </div>

        <div class="mb-6">
          <label for="description" class="block text-sm font-semibold text-gray-700">Description</label>
          <TinyMCE v-model="description"/>
        </div>

        <div class="mb-6">
          <label for="mainImage" class="block text-sm font-semibold text-gray-700">Main Image</label>
          <input
              type="file"
              id="mainImage"
              @change="handleMainImageChange"
              class="w-full text-sm file:border file:border-gray-300 file:rounded-md file:px-4 file:py-2"
          />
        </div>

        <div class="mb-6">
          <label for="category" class="block text-sm font-semibold text-gray-700">Category</label>
          <select
              v-model="category"
              id="category"
              class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
          >
            <option value="" disabled>Select a category</option>
            <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
          </select>
        </div>

        <div class="mb-6">
          <label for="tags" class="block text-sm font-semibold text-gray-700">Tags</label>
          <select
              v-model="tags"
              id="tags"
              multiple
              class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          >
            <option v-for="tag in tagsList" :key="tag.id" :value="tag.id">{{ tag.title }}</option>
          </select>
        </div>

        <div class="mb-6 text-center">
          <button
              type="submit"
              class="w-full bg-blue-500 text-white py-3 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
          >
            {{ blogId ? 'Update Blog' : 'Create Blog' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import TinyMCE from "@/components/TinyMCE.vue";

export default {
  name: 'BlogFormPage',
  components: {
    TinyMCE
  },
  data() {
    return {
      title: '',
      description: '',
      mainImage: null,
      publishDate: '',
      author: 'Logged-in user',
      blogId: this.$route.params.blogId || null,
      category: '',
      tags: [],
      categories: [],
      tagsList: [],
    };
  },
  mounted() {
    this.loadCategories();
    this.loadTags();

    if (this.blogId) {
      this.loadBlogData(this.blogId);
    }
  },
  methods: {
    loadCategories() {
      fetch('http://localhost:8000/blog/categories/')
          .then((response) => response.json())
          .then((data) => {
            this.categories = data;
          })
          .catch((error) => {
            console.error("Error loading categories:", error);
          });
    },
    loadTags() {
      fetch('http://localhost:8000/blog/tags/')
          .then((response) => response.json())
          .then((data) => {
            this.tagsList = data;
          })
          .catch((error) => {
            console.error("Error loading tags:", error);
          });
    },
    handleMainImageChange(event) {
      this.mainImage = event.target.files[0];
    },
    loadBlogData(blogId) {
      fetch(`http://localhost:8000/blog/blogs/${blogId}`)
          .then((response) => response.json())
          .then((data) => {
            this.title = data.title;
            this.description = data.description;
            this.publishDate = data.publish_date;
            this.author = data.author;
            this.category = data.category.id;
            this.tags = data.tags.map(tag => tag.id);
          })
          .catch((error) => {
            console.error("Error loading blog data:", error);
          });
    },
    handleSubmit() {
      const formData = new FormData();

      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('main_image', this.mainImage);
      formData.append('category', this.category);

      this.tags.forEach(tagId => formData.append('tags', tagId));
      const url = this.blogId ? `http://localhost:8000/blog/blogs/${this.blogId}/` : `http://localhost:8000/blog/blogs/`;

      const method = this.blogId ? 'PUT' : 'POST';

      const token = localStorage.getItem("access_token");

      fetch(url, {
        method: method,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData,
      })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              alert(`${this.blogId ? 'Blog updated' : 'Blog created'} successfully`);
              if (!this.blogId) {
                this.$router.push("/blogs");
              }
            } else {
              alert("Failed to save the blog");
            }
          })
          .catch((error) => {
            console.error("Error submitting blog data:", error);
            alert("An error occurred while submitting the blog.");
          });
    },
  },
};
</script>

<style scoped>
</style>
