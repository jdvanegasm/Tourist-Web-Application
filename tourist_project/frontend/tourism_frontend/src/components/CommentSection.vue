<template>
  <div class="mt-8">
    <h2 class="text-2xl font-bold text-light mb-4">Comentarios</h2>

    <!-- Mostrar comentarios -->
    <div v-if="comments.length > 0">
      <div v-for="comment in comments" :key="comment.comment_id" class="bg-dark p-4 mb-4 rounded-lg shadow-md">
        <p class="text-light font-semibold">{{ comment.user_name }}</p>
        <p class="text-light text-sm">{{ comment.comment_date }}</p>
        <p class="text-light mt-2">{{ comment.content }}</p>
      </div>
    </div>
    <p v-else class="text-light">No hay comentarios todavía.</p>

    <!-- Formulario para agregar nuevo comentario -->
    <div class="mt-6">
      <textarea
        v-model="newComment"
        class="w-full p-3 bg-light rounded-lg shadow-md text-dark"
        rows="4"
        placeholder="Escribe tu comentario..."
      ></textarea>
      <button
        @click="submitComment"
        class="mt-4 bg-highlight text-dark px-6 py-2 rounded-lg shadow-md hover:bg-highlight-light transition"
      >
        Publicar comentario
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CommentSection",
  props: {
    postId: {
      type: Number,
      required: true,
    },
    initialComments: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      comments: this.initialComments,
      newComment: "",
    };
  },
  methods: {
    async submitComment() {
      if (!this.newComment.trim()) return;

      try {
        // Obtener el nombre del usuario desde el localStorage (si existe), o asignar "Anónimo"
        const userName = localStorage.getItem("user_name") || "Anónimo";

        // Enviar el comentario al servidor sin token de autenticación
        const response = await axios.post(
          `http://localhost:8000/api/comments/`, 
          {
            post_id: this.postId,  // El ID del post al que pertenece el comentario
            content: this.newComment, // El contenido del comentario
            user_name: userName,  // Asignar el nombre del usuario o "Anónimo"
          }
        );

        // Agregar el nuevo comentario al array (optimización en el frontend)
        this.comments.push(response.data);
        this.newComment = ""; // Limpiar el campo de texto
      } catch (error) {
        console.error("Error al publicar el comentario:", error);
        alert("Hubo un error al publicar tu comentario. Intenta nuevamente.");
      }
    },
  },
};
</script>

<style scoped>
/* Estilos generales para comentarios */
.bg-dark {
  background-color: #01161E; /* Fondo oscuro */
}

.text-light {
  color: #EFF6E0; /* Texto claro */
}

.text-dark {
  color: #01161E; /* Texto oscuro */
}

.bg-light {
  background-color: #AEC3B0; /* Fondo claro para comentarios */
}

.bg-highlight {
  background-color: #124559; /* Color de fondo para el botón */
}

.bg-highlight-light {
  background-color: #598392; /* Color de fondo cuando se pasa el mouse */
}

/* Estilos para el área de texto */
.textarea {
  resize: vertical;
}

textarea {
  background-color: #AEC3B0; /* Fondo claro */
  color: #01161E; /* Texto oscuro */
  border: none;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Botón */
button {
  background-color: #124559;
  color: #EFF6E0;
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #598392;
}
</style>