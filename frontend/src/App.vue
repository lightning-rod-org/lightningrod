<template>
  <div> 
    <div>
      <Navbar></Navbar>
  </div>
  <div class="row">
    <div class="col-2 side-col">    
      <Sidebar></Sidebar>
    </div>
    <div class="col-10"> 
    <Home></Home>
    </div>
    </div>
  </div>
</template>
<script>
import Home from './components/Home.vue'
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar.vue'
export default {
  name: 'App',
  props: {

  },
  components: {
    Home,
    Navbar,
    Sidebar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.side-col{
/* padding-right: 200; */
padding-left: 0;
height: 100vh}

</style>
