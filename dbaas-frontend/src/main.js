import './assets/style.css';
import 'flowbite';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import store from './stores/index.js';

const app = createApp(App);

app.config.devtools = false;
app.config.productionTip = false;

app.use(createPinia());
app.use(router);
app.use(store);

app.mount('#app');
