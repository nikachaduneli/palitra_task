<template>
  <header class="bg-gray-800 text-white shadow-md sticky top-0 z-50">
    <div class="container mx-auto flex justify-between items-center p-4">
      <div class="logo text-2xl font-semibold">
        <router-link to="/" class="hover:underline">My Blog</router-link>
      </div>
      <nav>
        <ul class="flex space-x-6">
          <li>
            <router-link to="/" class="hover:underline">Home</router-link>
          </li>
          <li v-if="!isLoggedIn">
            <button @click="openLoginModal" class="hover:underline">Login</button>
          </li>
          <li v-if="!isLoggedIn">
            <button @click="openRegisterModal" class="hover:underline">Register</button>
          </li>
          <li v-if="isLoggedIn">
            <button @click="logout" class="hover:underline">Logout</button>
          </li>
          <li v-if="isLoggedIn">
            <router-link to="/profile" class="hover:underline">Profile</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('access_token');
    }
  },
  methods: {
    openLoginModal() {
      this.$emit("open-login-modal");
    },
    openRegisterModal() {
      this.$emit("open-register-modal");
    },
    logout() {
      localStorage.removeItem('access_token');
      this.$router.push('/');
    },
  }
}
</script>
