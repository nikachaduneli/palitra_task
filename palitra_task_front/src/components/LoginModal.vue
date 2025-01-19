<template>
  <div class="fixed inset-0 flex justify-center items-center bg-black bg-opacity-50 z-50">
    <div class="bg-white p-8 rounded-lg shadow-md w-96 relative">
      <h2 class="text-2xl font-bold mb-4 text-center">Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label for="username" class="block text-sm font-semibold text-gray-700">Username</label>
          <input
              v-model="username"
              type="text"
              id="username"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
              placeholder="Enter your username"
          />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-sm font-semibold text-gray-700">Password</label>
          <input
              v-model="password"
              type="password"
              id="password"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
              placeholder="Enter your password"
          />
        </div>
        <div class="mb-4 text-center">
          <button
              type="submit"
              class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
          >
            Login
          </button>
        </div>
      </form>
      <button @click="closeModal"
              class="absolute top-2 right-5 text-gray-600 hover:text-red-500 font-bold text-xl transition-all">
        &times;
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginModal",
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async handleLogin() {
      const apiBaseUrl = process.env.VUE_APP_API_BASE_URL;
      const loginEndpoint = `${apiBaseUrl}/users/token/`;

      try {
        const response = await fetch(loginEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });

        if (response.status === 200) {
          const data = await response.json();
          localStorage.setItem('access_token', data.access);
          localStorage.setItem('refresh_token', data.refresh);
          alert('Login successful!');
          this.closeModal();
        } else {
          const errorData = await response.json();
          alert(`Error: ${errorData.detail || 'Login failed'}`);
        }
      } catch (error) {
        console.error('Error during login:', error);
        alert('An error occurred. Please try again later.');
      }
    },
    closeModal() {
      this.$emit("close-modal");
    }
  }
};
</script>
