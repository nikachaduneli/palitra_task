<template>
  <div id="app">
    <Header @open-login-modal="openLoginModal"
            @open-register-modal="openRegisterModal"
    />
    <router-view/>

    <LoginModal v-if="isLoginModalOpen" @close-modal="closeLoginModal"/>
    <RegisterModal v-if="isRegisterModalOpen" @close-modal="closeRegisterModal"/>
  </div>
</template>

<script>
import Header from '@/components/HeaderComponent.vue';
import LoginModal from '@/components/LoginModal.vue';
import RegisterModal from "@/components/RegisterModal.vue";

export default {
  name: 'App',
  components: {
    RegisterModal,
    Header,
    LoginModal
  },
  methods: {
    openLoginModal() {
      this.isLoginModalOpen = true;
    },
    closeLoginModal() {
      this.isLoginModalOpen = false;
    },
    openRegisterModal() {
      this.isRegisterModalOpen = true;
    },
    closeRegisterModal() {
      this.isRegisterModalOpen = false;
    },
  },
  data() {
    return {
      isLoginModalOpen: false,
      isRegisterModalOpen: false,
    }
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  line-height: 1.6;
}
</style>
