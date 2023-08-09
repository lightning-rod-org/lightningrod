<template>
    <nav class="navbar navbar-dark bg-dark shadow-sm">
  <div class="container-fluid mb-2 mt-2">
        <span class="navbar-brand mb-0 h1">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightning-fill" viewBox="0 0 16 16">
  <path d="M5.52.359A.5.5 0 0 1 6 0h4a.5.5 0 0 1 .474.658L8.694 6H12.5a.5.5 0 0 1 .395.807l-7 9a.5.5 0 0 1-.873-.454L6.823 9.5H3.5a.5.5 0 0 1-.48-.641l2.5-8.5z"/>
</svg>
            LightningRod</span>
      </div>
</nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
  },
  methods: {}
}
</script>
<style scoped>
.navbar {
  position: relative;
  z-index: 65;
  /* background-color: #2D3436; */
  /* box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
  width: 240px;
  z-index: 3; */
}
</style>