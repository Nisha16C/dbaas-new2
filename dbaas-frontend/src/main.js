import './assets/style.css';
import 'flowbite';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import store from './stores/index.js';

const app = createApp(App);

// Add an event listener to the document for the contextmenu event
// document.addEventListener('contextmenu', (event) => {
//   // Prevent the default context menu
//   event.preventDefault();

//   // Display an alert message
//   alert('Right-click is disabled for security reasons.');
// });

app.config.devtools = false;
app.config.productionTip = false;

app.use(createPinia());
app.use(router);
app.use(store);

app.mount('#app');
