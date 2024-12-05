<template>
  <div class="min-h-screen bg-darkblue">
    <div class="flex items-center justify-center py-12">
      <div class="bg-light p-8 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-2xl font-bold text-darkblue mb-6 text-center">Regístrate</h2>

        <!-- Mensaje de error -->
        <p v-if="errorMessage" class="text-red-500 text-sm text-center mb-4">{{ errorMessage }}</p>

        <form @submit.prevent="handleSubmit">
          <!-- Nombre -->
          <div class="mb-4">
            <label for="name" class="block text-darkblue font-semibold mb-2">Nombre</label>
            <input
              type="text"
              id="name"
              v-model="form.name"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-highlight focus:border-highlight transition-shadow"
              required
            />
          </div>

          <!-- Correo -->
          <div class="mb-4">
            <label for="email" class="block text-darkblue font-semibold mb-2">Correo Electrónico</label>
            <input
              type="email"
              id="email"
              v-model="form.email"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-highlight focus:border-highlight transition-shadow"
              required
            />
          </div>

          <!-- Contraseña -->
          <div class="mb-4">
            <label for="password" class="block text-darkblue font-semibold mb-2">Contraseña</label>
            <input
              type="password"
              id="password"
              v-model="form.password"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-highlight focus:border-highlight transition-shadow"
              required
            />
          </div>

          <!-- Confirmar Contraseña -->
          <div class="mb-6">
            <label for="confirmPassword" class="block text-darkblue font-semibold mb-2">Confirmar Contraseña</label>
            <input
              type="password"
              id="confirmPassword"
              v-model="form.confirmPassword"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-highlight focus:border-highlight transition-shadow"
              required
            />
          </div>

          <!-- Botón de Registro -->
          <button
            type="submit"
            class="w-full bg-highlight text-darkblue font-bold py-3 rounded-lg shadow-md hover:bg-highlight-light transition"
          >
            Registrarse
          </button>
        </form>

        <!-- Enlace para iniciar sesión -->
        <p class="mt-6 text-center text-sm text-darkblue">
          ¿Ya tienes una cuenta? 
          <span
            class="text-darkhipblue font-semibold cursor-pointer hover:underline"
            @click="$router.push('/login')"
          >
            Inicia sesión aquí
          </span>.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useToast } from "vue-toastification";

export default {
  name: "RegisterPage",
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: "",
        confirmPassword: "",
      },
      errorMessage: "",
    };
  },
  methods: {
    async handleSubmit() {
      const toast = useToast();

      if (this.form.password !== this.form.confirmPassword) {
        toast.error("Las contraseñas no coinciden.");
        return;
      }

      try {
        const response = await axios.post("http://localhost:8000/api/register/", {
          name: this.form.name,
          email: this.form.email,
          password: this.form.password,
        });
        console.log("Usuario registrado:", response.data.message);

        toast.success("¡Registro exitoso! Redirigiendo...");
        
        setTimeout(() => {
          this.$router.push("/login");
        }, 1000);

      } catch (error) {
        toast.error(
          error.response?.data?.detail || "Ocurrió un error en el registro."
        );
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
.focus\\:ring-highlight {
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
.focus\\:border-highlight {
  border-color: #aec3b0;
}
.transition-shadow {
  transition: box-shadow 0.2s ease-in-out, border-color 0.2s ease-in-out;
}
</style>