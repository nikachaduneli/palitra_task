<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-md w-96">
      <h2 class="text-2xl font-bold mb-4 text-center">Profile</h2>
      <div class="mb-4">
        <label for="username" class="block text-sm font-semibold text-gray-700">Username</label>
        <p class="w-full px-4 py-2 border border-gray-300 rounded-md">{{ username }}</p>
      </div>
      <div class="mb-4">
        <label for="email" class="block text-sm font-semibold text-gray-700">Email</label>
        <p class="w-full px-4 py-2 border border-gray-300 rounded-md">{{ email }}</p>
      </div>
      <div class="mb-4">
        <label for="profilePicture" class="block text-sm font-semibold text-gray-700">Profile Picture</label>
        <div v-if="profileImage">
          <img :src="profileImageUrl" alt="Profile Picture" class="w-24 h-24 rounded-full object-cover">
        </div>
        <p v-else>No profile picture</p>
      </div>
      <div class="mb-4 text-center">
        <button
            @click="editProfile"
            class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
        >
          Edit Profile
        </button>
      </div>
      <div class="mb-4 text-center">
        <button
            @click="addBlog"
            class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
        >
          create new blog
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfilePage",
  data() {
    return {
      username: '',
      email: '',
      profileImage: null,
    };
  },
  computed: {
    profileImageUrl() {
      return this.profileImage ? `http://localhost:8000${this.profileImage}` : '';
    }
  },
  mounted() {
    this.loadProfileData();
  },
  methods: {
    loadProfileData() {
      const token = localStorage.getItem("access_token");
      fetch("http://localhost:8000/users/profile", {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      })
          .then(response => response.json())
          .then(data => {
            this.username = data.username;
            this.email = data.email;
            this.profileImage = data.profile_image;
          })
          .catch(error => console.error("Error loading profile data", error));
    },
    editProfile() {
      this.$router.push("/profile/edit");
    },
    addBlog() {
      this.$router.push({ name: 'BlogForm' });
    }
  }
};
</script>

<style scoped>
/* Add custom styles for the profile page if needed */
</style>
