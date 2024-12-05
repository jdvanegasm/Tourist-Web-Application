import { createApp } from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';
import './assets/tailwind.css';

const app = createApp(App);

axios.defaults.baseURL = 'http://127.0.0.1:8000/api';
app.config.globalProperties.$axios = axios;

const toastOptions = {
  position: 'top-right',
  timeout: 3000,
  closeOnClick: true,
  pauseOnHover: true,
};

app.use(Toast, toastOptions);
app.use(router);
app.mount('#app');
