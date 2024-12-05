import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router';
import './assets/tailwind.css';

const app = createApp(App);

axios.defaults.baseURL = 'http://127.0.0.1:8000/api';
app.config.globalProperties.$axios = axios;

app.use(router);
app.mount('#app');
