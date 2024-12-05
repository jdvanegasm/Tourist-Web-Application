<template>
  <div>
    <div class="min-h-screen bg-darkblue">
      <div class="flex items-center justify-center py-12">
        <div class="bg-light p-8 rounded-lg shadow-lg max-w-md w-full">
          <h2 class="text-2xl font-bold text-darkblue mb-6 text-center">
            Iniciar Sesión
          </h2>

          <!-- Mensaje de error -->
          <p v-if="errorMessage" class="text-red-500 text-sm text-center mb-4">
            {{ errorMessage }}
          </p>

          <!-- Formulario de inicio de sesión -->
          <form @submit.prevent="handleLogin">
            <!-- Email -->
            <div class="mb-4">
              <label
                for="email"
                class="block text-darkblue font-semibold mb-2"
                >Correo Electrónico</label
              >
              <input
                type="email"
                id="email"
                v-model="form.email"
                autocomplete="email"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-highlight focus:border-highlight transition-shadow"
                required
              />
            </div>

            <!-- Contraseña -->
            <div class="mb-6">
              <label
                for="password"
                class="block text-darkblue font-semibold mb-2"
                >Contraseña</label
              >
              <input
                type="password"
                id="password"
                v-model="form.password"
                autocomplete="current-password"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-highlight focus:border-highlight transition-shadow"
                required
              />
            </div>

            <!-- Botón de inicio de sesión -->
            <button
              type="submit"
              class="w-full bg-highlight text-darkblue font-bold py-3 rounded-lg shadow-md hover:bg-highlight-light transition"
            >
              Iniciar Sesión
            </button>
          </form>

          <!-- Enlace para registrarse -->
          <p class="mt-6 text-center text-sm text-darkblue">
            ¿No tienes una cuenta?
            <span
              class="text-darkhipblue font-semibold cursor-pointer hover:underline"
              @click="$router.push('/register')"
            >
              Regístrate aquí
            </span>.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useToast } from "vue-toastification"; // Importar toast

export default {
  name: "LoginPage",
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errorMessage: "", // Usado para mostrar errores en el template
    };
  },
  methods: {
    async handleLogin() {
      const toast = useToast(); // Inicializar el toast
      try {
        // Enviamos la solicitud al backend
        const response = await axios.post("http://localhost:8000/api/login/", {
          email: this.form.email,
          password: this.form.password,
        });

        // Si la respuesta tiene tokens, los guardamos
        if (response.data.access && response.data.refresh) {
          localStorage.setItem("accessToken", response.data.access);
          localStorage.setItem("refreshToken", response.data.refresh);

          // Mostrar mensaje de éxito con toast
          toast.success("Inicio de sesión exitoso. Redirigiendo...", {
            timeout: 3000,
            position: "top-right",
          });

          // Redirigir después de un corto retraso
          setTimeout(() => {
            this.$router.push("/");
          }, 1500);
        } else {
          // Mensaje genérico si no hay tokens
          this.errorMessage = "No se pudo iniciar sesión. Intenta nuevamente.";
        }
      } catch (error) {
        // Manejo de error básico
        this.errorMessage = "Ocurrió un error. Revisa tus credenciales o la conexión al servidor.";
      }
    },
  },
};
</script>

<style scoped>
.bg-darkblue {
  background-color: #01161e;
}
.bg-light {
  background-color: #eff6e0;
}
.text-darkblue {
  color: #01161e;
}
.text-darkhipblue {
  color: #0d3849;
}
.focus\:ring-highlight {
  --tw-ring-color: #aec3b0;
}
.bg-highlight {
  background-color: #aec3b0;
}
.bg-highlight-light {
  background-color: #d0e2c6;
}
.border-gray-300 {
  border-color: #d1d5db;
}
.focus\:border-highlight {
  border-color: #aec3b0;
}
.transition-shadow {
  transition: box-shadow 0.2s ease-in-out, border-color 0.2s ease-in-out;
}
</style>