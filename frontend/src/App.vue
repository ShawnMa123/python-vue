<template>
  <div id="app">
    <header>
      <h1>{{ message }}</h1>
    </header>
    <main>
      <form @submit.prevent="checkService">
        <input type="text" v-model="serviceUrl" placeholder="Enter service URL" required>
        <button type="submit">Check Service</button>
      </form>
      <div v-if="serviceStatus" :class="{'status-up': serviceStatus === 'up', 'status-down': serviceStatus === 'down', 'status-error': serviceStatus === 'error'}">
        <p>Service Status: {{ serviceStatus }}</p>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: 'Service Status Checker',
      serviceUrl: '',
      serviceStatus: ''
    };
  },
  methods: {
    checkService() {
      axios.post('http://127.0.0.1:5000/api/check_service', { url: this.serviceUrl })
        .then(response => {
          this.serviceStatus = response.data.status;
        })
        .catch(error => {
          console.error("There was an error!", error);
          this.serviceStatus = 'error';
        });
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

#app {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
  text-align: center;
}

header {
  margin-bottom: 20px;
}

header h1 {
  margin: 0;
  font-size: 24px;
  color: #333;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.status-up {
  color: green;
}

.status-down {
  color: red;
}

.status-error {
  color: orange;
}

div[v-if="serviceStatus"] {
  margin-top: 20px;
  font-size: 18px;
}
</style>
