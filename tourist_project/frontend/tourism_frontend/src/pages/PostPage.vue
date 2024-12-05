<template>
  <div class="container mx-auto py-8">
    <div class="max-w-full mx-auto bg-primary p-8 rounded-lg shadow-lg">
      <h1 class="text-4xl font-bold text-light mb-4">{{ post.title }}</h1>
      <p class="text-sm text-secondary-light mb-2">
        Publicado en <span class="font-semibold">{{ formattedDate }}</span>
      </p>
      <p class="text-md text-highlight-light mb-6">
        {{ post.city?.name }}, {{ post.city?.country?.name }}
      </p>
      <p class="text-light leading-relaxed mb-6">{{ post.description }}</p>

      <div v-if="post.images && post.images.length > 0" class="flex justify-center mb-6">
        <img
          v-for="(image, index) in post.images"
          :key="index"
          :src="image"
          alt="Imagen del post"
          class="rounded-lg shadow-md object-contain object-center w-full max-h-screen"
        />
      </div>

      <div v-if="post.tags && post.tags.length > 0" class="mt-6">
        <h3 class="text-lg font-semibold text-light mb-2">Etiquetas:</h3>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="(tag, index) in post.tags"
            :key="index"
            class="px-3 py-1 bg-highlight text-dark rounded-full text-sm font-semibold shadow-md"
          >
            {{ tag }}
          </span>
        </div>
      </div>

      <router-link
        to="/"
        class="mt-6 inline-block bg-highlight text-dark px-6 py-3 rounded-lg shadow-md hover:bg-highlight-light transition"
      >
        Volver al inicio
      </router-link>

      <!-- Agregar la sección de comentarios -->
      <CommentSection :postId="post.id" :initialComments="post.comments" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CommentSection from "@/components/CommentSection.vue"; // Importar el componente

export default {
  name: "PostPage",
  components: {
    CommentSection,
  },
  data() {
    return {
      post: {},
    };
  },
  computed: {
    formattedDate() {
      if (this.post.creation_date) {
        return new Date(this.post.creation_date).toLocaleDateString("es-ES", {
          year: "numeric",
          month: "long",
          day: "numeric",
        });
      }
      return "";
    },
  },
  async created() {
    try {
      const postId = this.$route.params.id;
      const response = await axios.get(`http://localhost:8000/api/posts/${postId}/`);
      this.post = response.data;
    } catch (error) {
      console.error("Error al cargar el post:", error);
      this.$router.push("/"); // Redirigir al inicio si hay un error
    }
  },
};
</script>

<style scoped>
/* Colores alineados a la paleta */
.bg-primary {
  background-color: #01161e; /* Fondo principal */
}
.text-light {
  color: #eff6e0; /* Texto principal */
}
.text-secondary-light {
  color: #598392; /* Resaltados secundarios */
}
.text-highlight-light {
  color: #aec3b0; /* Resaltados secundarios */
}
.bg-highlight {
  background-color: #124559; /* Botones y destacados */
}
.bg-highlight-light {
  background-color: #598392; /* Hover en botones */
}
.text-dark {
  color: #01161e; /* Texto oscuro */
}
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.object-contain {
  object-fit: contain; /* Asegura que la imagen no se estire */
}
.object-center {
  object-position: center; /* Centra la imagen */
}
.w-full {
  width: 100%; /* Asegura que la imagen ocupe todo el ancho disponible */
}
.max-h-screen {
  max-height: 100vh; /* Asegura que la imagen no se desborde verticalmente */
}
</style>