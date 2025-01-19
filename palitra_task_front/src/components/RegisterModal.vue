<template>
  <div class="fixed inset-0 flex justify-center items-center bg-black bg-opacity-50 z-50">
    <div class="bg-white p-8 rounded-lg shadow-md w-96 relative">
      <h2 class="text-2xl font-bold mb-4 text-center">Register</h2>
      <form @submit.prevent="handleRegister">
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
        <div class="mb-4">
          <label for="confirmPassword" class="block text-sm font-semibold text-gray-700">Confirm Password</label>
          <input
              v-model="confirmPassword"
              type="password"
              id="confirmPassword"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
              placeholder="Confirm your password"
          />
        </div>
        <div class="mb-4 text-center">
          <button
              type="submit"
              class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
          >
            Register
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
  name: "RegisterModal",
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    async handleRegister() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match");
        return;
      }

      const apiBaseUrl = process.env.VUE_APP_API_BASE_URL;
      const registerEndpoint = `${apiBaseUrl}/users/register/`;

      try {
        const response = await fetch(registerEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password,
            password2: this.confirmPassword,
          }),
        });

        if (response.status === 201) {
          const data = await response.json();
          alert('Registration successful!');
          this.closeModal();
        } else {
          const errorData = await response.json();
          alert(`Error: ${errorData.message || 'Registration failed'}`);
        }
      } catch (error) {
        console.error('Error during registration:', error);
        alert('An error occurred. Please try again later.');
      }
    },
    closeModal() {
      this.$emit("close-modal");
    }
  }
};
</script>
