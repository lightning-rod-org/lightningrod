<template>
    <div>
      <div class="container-fluid">
        <div class="row">
          <div class="col-5 h-25">
            <!-- Main Content -->
            <div class="mt-3 w-100">
              <!-- <h1 class="d-flex justify-content-start">Dashboard</h1> -->
              <!-- <h1 class="text-left">Dashboard</h1> -->
              <Main></Main>
            </div>
          </div>
          <div class="col-4">
            <div class="mt-3 w-100">
              <NewParser></NewParser>
            </div>
          </div>
          <div class="col-3">
            <div class="mt-3 w-100">
              <Recent></Recent>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-9">
            <Output></Output>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script>
import Main from './Main.vue'
// import Navbar from './Navbar.vue'
// import Sidebar from './Sidebar.vue'
import NewParser from './NewParser.vue'
import Recent from './Recent.vue'
import Output from './Output.vue'

export default {
name: 'Home',
props: {
},
components: {
    Main,
    NewParser,
    Recent,
    Output
  }
}
</script>
<style scoped>

/* .nav {
z-index: 600;
}
.side-col{
/* padding-right: 200; */
/* padding-left: 0;
height: 100vh} */ 

</style>