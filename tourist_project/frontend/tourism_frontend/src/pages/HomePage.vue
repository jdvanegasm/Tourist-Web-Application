<template>
  <div class="bg-darkblue text-light">
    <!-- Hero Section -->
    <section class="relative bg-darkblue text-center py-16">
      <div class="container mx-auto">
        <h1 class="text-4xl font-bold text-highlight mb-4">Explora el mundo con Happy Fly Tours</h1>
        <p class="text-lg text-highlight-light mb-8">
          Encuentra los destinos más emocionantes y comparte tus experiencias únicas.
        </p>
        <button
          class="bg-highlight hover:bg-highlight-light text-darkblue font-bold py-3 px-6 rounded-full shadow-md transition"
          @click="$router.push('/create-post')"
        >
          Explora un destino Aleatorio
        </button>
      </div>
    </section>

    <!-- Image Gallery -->
    <section class="py-16 bg-secondary">
      <div class="container mx-auto">
        <h2 class="text-3xl font-bold text-light mb-8 text-center">Galería de Destinos</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="relative">
            <img
              class="w-full h-60 object-cover rounded-lg shadow-md transition-transform transform hover:scale-105"
              src="https://www.chooseparisregion.org/sites/default/files/news/6---Tour-Eiffel_AdobeStock_644956457_1920_72dpi.jpg"
              alt="París"
            />
            <p class="absolute bottom-2 left-2 bg-darkblue bg-opacity-75 text-light text-sm px-2 py-1 rounded">
              París
            </p>
          </div>
          <div class="relative">
            <img
              class="w-full h-60 object-cover rounded-lg shadow-md transition-transform transform hover:scale-105"
              src="https://www.interviajesny.com/wp-content/uploads/central-park-nueva-york-3-1200x723.jpg"
              alt="Nueva York"
            />
            <p class="absolute bottom-2 left-2 bg-darkblue bg-opacity-75 text-light text-sm px-2 py-1 rounded">
              Nueva York
            </p>
          </div>
          <div class="relative">
            <img
              class="w-full h-60 object-cover rounded-lg shadow-md transition-transform transform hover:scale-105"
              src="https://cdn5.travelconline.com/images/fit-in/2000x0/filters:quality(75):strip_metadata():format(webp)/https%3A%2F%2Ftr2storage.blob.core.windows.net%2Fimagenes%2FCepFu9RAtqVN-YZCPyV6ulrjpeg.jpeg"
              alt="Tokio"
            />
            <p class="absolute bottom-2 left-2 bg-darkblue bg-opacity-75 text-light text-sm px-2 py-1 rounded">
              Tokio
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="py-16 bg-darkblue text-center">
      <div class="container mx-auto">
        <h2 class="text-3xl font-bold text-highlight mb-8">Testimonios de Nuestros Viajeros</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="p-6 bg-secondary-light rounded-lg shadow-md">
            <p class="text-lg text-darkblue italic">
              "Explorar París con Happy Fly Tours fue la mejor experiencia de mi vida. Todo fue perfecto."
            </p>
            <span class="block mt-4 font-bold text-highlight">- Camila R.</span>
          </div>
          <div class="p-6 bg-secondary-light rounded-lg shadow-md">
            <p class="text-lg text-darkblue italic">
              "Gracias a esta plataforma, descubrí lugares que nunca habría imaginado."
            </p>
            <span class="block mt-4 font-bold text-highlight">- Diego G.</span>
          </div>
          <div class="p-6 bg-secondary-light rounded-lg shadow-md">
            <p class="text-lg text-darkblue italic">
              "¡Excelente! El diseño es tan intuitivo que encontré mi destino ideal en minutos."
            </p>
            <span class="block mt-4 font-bold text-highlight">- Laura P.</span>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section class="py-16 bg-darkdiffblue text-center">
      <div class="container mx-auto">
        <h2 class="text-3xl font-bold text-light mb-4">¿Qué hacemos?</h2>
        <p class="text-lg text-light max-w-3xl mx-auto">
          Happy Fly Tours es la plataforma donde los viajeros descubren, comparten y conectan. Busca destinos, publica
          tus aventuras y encuentra la inspiración para tu próxima gran aventura.
        </p>
      </div>
    </section>

    <!-- Contact Us Section -->
    <section class="py-16 bg-secondary-light text-center">
      <div class="container mx-auto">
        <h2 class="text-3xl font-bold text-darkblue mb-4">Contáctanos</h2>
        <p class="text-lg text-darkblue mb-8">
          ¿Tienes preguntas o necesitas ayuda? Estamos aquí para ayudarte.
        </p>
        <button
          class="bg-darkblue hover:bg-secondary text-light font-bold py-3 px-6 rounded-full shadow-md transition"
          @click="$router.push('/contact')"
        >
          Contáctanos
        </button>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
.bg-darkblue {
  background-color: #01161e;
}
.bg-darkdiffblue {
  background-color: #1f4352;
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
.transition {
  transition: all 0.3s ease-in-out;
}
</style>
