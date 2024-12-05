<template>
  <header class="bg-darkblue text-light py-6 shadow-md border-b border-highlight relative z-50">
    <div class="container mx-auto flex items-center justify-between">
      <!-- Logo de la empresa -->
      <router-link to="/" class="flex items-center space-x-2 no-underline hover:no-underline">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-8 w-8 text-highlight"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path d="M10 2a8 8 0 100 16 8 8 0 000-16zM6.83 10H4a6 6 0 1111.88 0h-2.83a4.002 4.002 0 00-6.22 0zM10 14a3 3 0 01-2.83-2h5.66A3 3 3 0 0110 14z" />
        </svg>
        <h1 class="text-3xl font-extrabold text-highlight tracking-wide">
          Happy Fly <span class="text-highlight-light">Tours</span>
        </h1>
      </router-link>

      <!-- Barra de búsqueda -->
      <div class="hidden md:flex items-center relative w-1/3">
        <SearchBar />
      </div>

      <!-- Botones de acción -->
      <div class="flex items-center space-x-4">
        <!-- Botón Crear Post -->
        <button
          class="flex items-center bg-secondary hover:bg-secondary-light text-light px-4 py-2 rounded-full shadow-md focus:outline-none focus:ring-2 focus:ring-highlight transition"
          @click="goToCreatePost"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 mr-2"
            viewBox="0 0 24 24"
            fill="currentColor"
          >
            <path
              d="M12 4a1 1 0 011 1v6h6a1 1 0 110 2h-6v6a1 1 0 11-2 0v-6H5a1 1 0 110-2h6V5a1 1 0 011-1z"
            />
          </svg>
          Crear un Post
        </button>

        <!-- Menú de usuario -->
        <div class="relative">
          <button
            class="flex items-center bg-secondary hover:bg-secondary-light text-light px-4 py-2 rounded-full shadow-md focus:outline-none focus:ring-2 focus:ring-highlight transition"
            @click="toggleMenu"
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="24" height="24" fill="none">
              <circle cx="50" cy="50" r="48" stroke="#124559" stroke-width="4" fill="#EFF6E0" />
              <circle cx="50" cy="35" r="15" fill="#124559" />
              <path d="M35 60 Q50 75 65 60 Q65 50 35 50 Z" fill="#124559" />
            </svg>
          </button>
          <div
            v-if="menuOpen"
            class="absolute right-0 mt-2 w-48 bg-light text-darkblue rounded-lg shadow-lg py-2 z-50"
          >
            <a
              href="#"
              class="block px-4 py-2 hover:bg-highlight-light rounded transition"
              v-if="!isAuthenticated"
              @click="goToLogin"
            >
              Iniciar Sesión
            </a>
            <a
              href="#"
              class="block px-4 py-2 hover:bg-highlight-light rounded transition"
              v-if="!isAuthenticated"
              @click="goToRegister"
            >
              Registrarse
            </a>

            <a
              href="#"
              class="block px-4 py-2 hover:bg-highlight-light rounded transition"
              v-if="isAuthenticated"
              @click="logout"
            >
              Cerrar Sesión
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { useToast } from "vue-toastification";
import SearchBar from "../components/SearchBar.vue"; // Importar el componente SearchBar

export default {
  components: {
    SearchBar,
  },
  data() {
    return {
      menuOpen: false,
      isAuthenticated: false,
    };
  },
  mounted() {
    this.checkAuthentication();
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    goToCreatePost() {
      const toast = useToast();
      if (!this.isAuthenticated) {
        toast.warning("Por favor inicia sesión para crear un post.", {
          timeout: 3000,
          position: "top-right",
        });
        this.$router.push("/login");
      } else {
        this.$router.push("/create-post");
      }
    },
    goToLogin() {
      this.$router.push("/login");
    },
    goToRegister() {
      this.$router.push("/register");
    },
    logout() {
      const toast = useToast();
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      this.isAuthenticated = false;
      toast.success("Sesión cerrada correctamente.", {
        timeout: 3000,
        position: "top-right",
      });
      this.$router.push("/");
    },
    checkAuthentication() {
      const token = localStorage.getItem("accessToken");
      this.isAuthenticated = !!token;
    },
  },
};
</script>

<style scoped>
.bg-darkblue {
  background-color: #01161e;
}
.bg-secondary {
  background-color: #124559;
}
.bg-secondary-light {
  background-color: #598392;
}
.text-light {
  color: #eff6e0;
}
.text-highlight {
  color: #aec3b0;
}
.text-highlight-light {
  color: #d0e2c6;
}
.focus\\:ring-highlight {
  --tw-ring-color: #aec3b0;
}
.transition {
  transition: all 0.3s ease-in-out;
}
.z-50 {
  z-index: 50;
}
</style>