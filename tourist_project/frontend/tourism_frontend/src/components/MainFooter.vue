<template>
    <footer class="bg-primary text-light py-8">
      <div class="container mx-auto flex flex-col md:flex-row justify-between items-center">
        <!-- Sección de información -->
        <div class="text-center md:text-left mb-4 md:mb-0">
          <h4 class="text-lg font-bold">Happy Fly Tours</h4>
          <p class="text-sm">Explora el mundo con nosotros. Descubre y comparte experiencias.</p>
        </div>
  
        <!-- Links útiles -->
        <div class="flex space-x-6 mb-4 md:mb-0">
          <a href="#" class="text-sm hover:text-highlight transition">Sobre nosotros</a>
          <a href="#" class="text-sm hover:text-highlight transition">Contacto</a>
          <a href="#" class="text-sm hover:text-highlight transition">Políticas</a>
        </div>
  
        <!-- Redes sociales -->
        <div class="flex space-x-4">
          <a href="#" class="text-light hover:text-highlight transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24h21.351c.731 0 1.324-.593 1.324-1.324V1.325C24 .593 23.407 0 22.675 0zm-4.431 4.6h-2.175c-1.62 0-2.644 1.07-2.644 2.697v1.245h-2.22v2.456h2.22v6.436h2.682v-6.436h2.234l.353-2.456h-2.587V7.297c0-.709.198-1.193 1.217-1.193h1.416V4.6z"/>
            </svg>
          </a>
          <a href="#" class="text-light hover:text-highlight transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M24 4.56v15.08c0 .85-.69 1.54-1.54 1.54H1.54C.69 21.18 0 20.49 0 19.64V4.56c0-.85.69-1.54 1.54-1.54h20.92c.85 0 1.54.69 1.54 1.54zM9.54 17.8l8.94-5.8-8.94-5.8v11.6z"/>
            </svg>
          </a>
          <a href="#" class="text-light hover:text-highlight transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2.163c-5.271 0-9.524 4.253-9.524 9.524 0 4.292 2.89 7.926 6.783 9.242-.093-.814-.18-2.072-.053-2.967.124-.869.79-5.574.79-5.574s-.201-.403-.201-.996c0-.932.54-1.628 1.214-1.628.572 0 .849.429.849.944 0 .574-.367 1.432-.559 2.23-.159.672.337 1.222.998 1.222 1.198 0 2.121-1.264 2.121-3.082 0-1.609-1.158-2.738-3.146-2.738-2.139 0-3.459 1.604-3.459 3.256 0 .588.228 1.218.513 1.56.056.07.064.132.047.204-.051.223-.17.723-.195.824-.032.133-.103.162-.237.098-.88-.406-1.418-1.683-1.418-2.712 0-2.204 1.663-4.233 4.813-4.233 2.518 0 4.465 1.794 4.465 4.185 0 2.489-1.567 4.486-3.742 4.486-.732 0-1.419-.38-1.651-.828l-.449 1.707c-.162.618-.603 1.39-.898 1.86.683.21 1.401.325 2.153.325 5.271 0 9.524-4.253 9.524-9.524 0-5.271-4.253-9.524-9.524-9.524z"/>
            </svg>
          </a>
        </div>
      </div>
  
      <!-- Línea divisoria -->
      <div class="mt-8 border-t border-highlight opacity-50"></div>
  
      <!-- Derechos reservados -->
      <div class="text-center mt-4 text-xs">
        <p>&copy; 2024 Happy Fly Tours. Todos los derechos reservados.</p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'MainFooter',
  };
  </script>
  
  <style scoped>
  .bg-primary {
    background-color: #124559;
  }
  .text-light {
    color: #eff6e0;
  }
  .text-highlight {
    color: #aec3b0;
  }
  </style>  