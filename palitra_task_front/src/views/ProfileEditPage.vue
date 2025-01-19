<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-md w-96">
      <h2 class="text-2xl font-bold mb-4 text-center">Edit Profile</h2>
      <form @submit.prevent="handleProfileUpdate"  enctype="multipart/form-data">
        <div class="mb-4">
          <label for="email" class="block text-sm font-semibold text-gray-700">Email</label>
          <input
              v-model="email"
              type="email"
              id="email"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
              placeholder="Enter your email"
          />
        </div>
        <div class="mb-4">
          <label for="profilePicture" class="block text-sm font-semibold text-gray-700">Profile Picture</label>
          <input
              type="file"
              id="profilePicture"
              @change="handleProfilePictureChange"
              class="w-full text-sm file:border file:border-gray-300 file:rounded-md file:px-4 file:py-2"
          />
        </div>
        <div class="mb-4 text-center">
          <button
              type="submit"
              class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
          >
            Save Changes
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileEditPage",
  data() {
    return {
      email: '',
      profilePicture: null
    };
  },
  mounted() {
    this.loadProfileData();
  },
  methods: {
    loadProfileData() {
      const token = localStorage.getItem("access_token");
      fetch("http://localhost:8000/users/profile/", {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
          .then(response => response.json())
          .then(data => {
            this.email = data.email;
          })
          .catch(error => console.error("Error loading profile data", error));
    },
    handleProfileUpdate() {
      const token = localStorage.getItem("access_token");
      const formData = new FormData();
      formData.append('email', this.email);
      if (this.profilePicture) {
        formData.append('profile_image', this.profilePicture);
      }
      fetch("http://localhost:8000/users/profile/", {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData
      })
          .then(response => response.json())
          .then(() => {
              alert("Profile updated successfully");
          })
          .catch(error => {
            console.error("Error updating profile:", error);
            alert("An error occurred while updating the profile");
          });
    },
    handleProfilePictureChange(event) {
      this.profilePicture = event.target.files[0];
    }
  }
};
</script>

<style scoped>
</style>
