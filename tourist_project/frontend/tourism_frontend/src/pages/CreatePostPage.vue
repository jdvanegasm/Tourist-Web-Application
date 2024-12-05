<template>
    <div class="flex items-center justify-center min-h-screen bg-darkblue text-light">
      <div class="text-center space-y-6">
        <!-- Título principal -->
        <h1 class="text-6xl font-bold text-highlight">¡Ups! 🚧</h1>
        <p class="text-2xl font-semibold text-highlight-light">Estamos trabajando duro para que puedas crear posts increíbles.</p>
  
        <!-- Imagen decorativa -->
        <div class="flex justify-center">
          <img 
            src="https://www.oziozi.com/cdn/shop/products/custom-logo-maker-for-barber-shops-with-line-art-1153e_2000x.png?v=1579310168" 
            alt="Coming Soon" 
            class="max-w-md rounded-lg shadow-lg"
          />
        </div>
  
        <!-- Mensaje divertido -->
        <p class="text-lg text-secondary-light">
          Nuestro equipo de mapaches está trabajando día y noche 🦝💻. 
          ¡Vuelve pronto para ver la magia en acción! ✨
        </p>
  
        <!-- Botón para regresar al inicio -->
        <router-link
          to="/"
          class="inline-block mt-6 px-6 py-3 text-dark bg-highlight rounded-lg shadow-md hover:bg-highlight-light transition"
        >
          Volver al inicio
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ComingSoonPage",
  };
  </script>
  
  <style scoped>
  /* Estilos personalizados */
  .bg-darkblue {
    background-color: #01161E;
  }
  .text-light {
    color: #EFF6E0;
  }
  .text-highlight {
    color: #AEC3B0;
  }
  .text-highlight-light {
    color: #D0E2C6;
  }
  .text-secondary-light {
    color: #598392;
  }
  .bg-highlight {
    background-color: #124559;
  }
  .bg-highlight-light {
    background-color: #598392;
  }
  .transition {
    transition: all 0.3s ease-in-out;
  }
  .shadow-lg {
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3);
  }
  .rounded-lg {
    border-radius: 0.5rem;
  }
  </style>  