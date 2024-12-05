<template>
  <div class="min-h-screen bg-darkblue text-light p-6">
    <h1 class="text-3xl font-bold text-highlight mb-6">Resultados de búsqueda</h1>
    <div v-if="posts.length === 0">
      <p class="text-lg">No se encontraron resultados para "{{ $route.query.q }}"</p>
    </div>
    <div v-else>
      <div v-for="post in posts" :key="post.post_id" class="bg-secondary p-4 rounded-lg shadow-md mb-4">
        <h2 class="text-2xl font-bold text-highlight">{{ post.title }}</h2>
        <p class="text-lg text-highlight-light">{{ post.description }}</p>
        <router-link :to="{ name: 'Post', params: { id: post.post_id } }" class="text-highlight underline">
          Ver más
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchResultsPage",
  data() {
    return {
      posts: [],
    };
  },
  async created() {
    await this.fetchPosts(); // Llamada inicial
  },
  watch: {
    // Escucha los cambios en el parámetro "q" de la URL
    "$route.query.q": {
      immediate: true, // Ejecuta al inicializar el componente también
      handler() {
        this.fetchPosts(); // Llama al método para buscar
      },
    },
  },
  methods: {
    async fetchPosts() {
      const query = this.$route.query.q;
      if (!query) return;

      try {
        const response = await axios.get("http://localhost:8000/api/search-prioritized", {
          params: { q: query },
        });
        this.posts = response.data.posts;
      } catch (error) {
        console.error("Error fetching search results:", error);
      }
    },
  },
};
</script>

<style scoped>
.bg-darkblue {
  background-color: #01161E;
}
.text-light {
  color: #EFF6E0;
}
.text-highlight {
  color: #AEC3B0;
}
.bg-secondary {
  background-color: #124559;
}
.text-highlight-light {
  color: #D0E2C6;
}
</style>