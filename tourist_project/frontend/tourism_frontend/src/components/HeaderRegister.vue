<template>
  <header class="bg-darkblue text-light py-6 shadow-md border-b border-highlight">
    <div class="container mx-auto flex items-center justify-center">
      <!-- Logo de la empresa con redirección -->
      <h1 
        class="text-4xl font-bold text-highlight tracking-wide cursor-pointer hover:text-highlight-light transition"
        @click="goToHome"
      >
        Happy Fly <span class="text-highlight-light">Tours</span>
      </h1>
    </div>
  </header>
</template>

<script>
export default {
  name: "HeaderRegister",
  methods: {
    goToHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.bg-darkblue {
  background-color: #01161e;
}
.text-highlight {
  color: #aec3b0;
}
.text-highlight-light {
  color: #d0e2c6;
}
.py-6 {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.cursor-pointer {
  cursor: pointer;
}
.hover\:text-highlight-light:hover {
  color: #d0e2c6;
}
.transition {
  transition: all 0.3s ease-in-out;
}
/* Nueva línea para el borde */
.border-b {
  border-bottom-width: 1px;
}
.border-highlight {
  border-color: #aec3b0;
}
</style>