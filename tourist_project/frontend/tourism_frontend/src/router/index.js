import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../pages/HomePage.vue';
import RegisterPage from '../pages/RegisterPage.vue';
import LoginPage from '../pages/LoginPage.vue';
import PostPage from '../pages/PostPage.vue';
import CreatePostPage from '../pages/CreatePostPage.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/post/:id',
    name: 'Post',
    component: PostPage,
    props: true,
  },
  {
    path: '/create-post',
    name: 'CreatePost',
    component: CreatePostPage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;