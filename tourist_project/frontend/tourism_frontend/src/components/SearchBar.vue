<template>
    <div class="relative w-full max-w-xl mx-auto">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Buscar destinos, países o ciudades..."
        class="w-full px-4 py-2 text-darkblue rounded-full shadow-md focus:outline-none focus:ring-2 focus:ring-highlight"
        @input="fetchSuggestions"
      />
      <div v-if="suggestions.length > 0" class="absolute bg-light rounded-lg shadow-lg mt-2 w-full z-50">
        <ul>
          <li
            v-for="(suggestion, index) in suggestions"
            :key="index"
            class="px-4 py-2 cursor-pointer hover:bg-highlight-light transition"
            @click="handleSuggestionClick(suggestion)"
          >
            {{ suggestion }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "SearchBar",
    data() {
      return {
        searchQuery: "",
        suggestions: [],
      };
    },
    methods: {
      async fetchSuggestions() {
        if (this.searchQuery.trim() === "") {
          this.suggestions = [];
          return;
        }
  
        try {
          const response = await axios.get("http://localhost:8000/api/search-suggestions/", {
            params: { q: this.searchQuery },
          });
          this.suggestions = [
            ...response.data.countries,
            ...response.data.cities,
            ...response.data.tags,
          ];
        } catch (error) {
          console.error("Error fetching suggestions:", error);
        }
      },
      handleSuggestionClick(suggestion) {
        this.searchQuery = suggestion;
        this.suggestions = [];
        // Redirigir a la página de resultados
        this.$router.push({ name: "SearchResults", query: { q: suggestion } });
      },
    },
  };
  </script>
  
  <style scoped>
  .bg-light {
    background-color: #000000;
  }
  .text-darkblue {
    color: #01161E;
  }
  .focus\\:ring-highlight {
    --tw-ring-color: #AEC3B0;
  }
  .bg-highlight-light {
    background-color: #598392;
  }
  </style>  