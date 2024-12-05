<template>
  <div id="app">
    <template v-if="$route.name === 'Register'">
      <HeaderRegister />
    </template>
    <template v-else>
      <MainHeader />
    </template>
    <router-view />
    <MainFooter />
  </div>
</template>

<script>
import MainHeader from "@/components/MainHeader.vue";
import MainFooter from "@/components/MainFooter.vue";
import HeaderRegister from "@/components/HeaderRegister.vue";

export default {
  components: {
    MainHeader,
    MainFooter,
    HeaderRegister,
  },
};
</script>
