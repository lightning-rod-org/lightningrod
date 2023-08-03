<template>
    <nav
       id="sidebarMenu"
       class=" d-lg-block sidebar h-100 bg-light"
       >
    <div class="bg-light">
      <div class="list-group list-group-flush mx-5">
        <a
           href="#"
           class="list-group-item bg-light list-group-item-action py-3 ripple"
           aria-current="true"
           >
          <i class="fas fa-tachometer-alt fa-fw me-2"></i>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="black" class="bi bi-house-fill" viewBox="0 0 20 20">
          <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/>
          <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z"/>
          </svg>
            <span class="text-dark">Home</span>
        </a>
        <a
           href="http://localhost:8000/admin"
           class="list-group-item bg-light list-group-item-action py-3 ripple "
           >
          <i class="fas fa-chart-area fa-fw me-2 "></i
            ><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="black" class="bi bi-lock-fill" viewBox="0 0 20 20">
  <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/>
</svg><span class="text-dark" href="http://google.com">  Admin</span>
        </a>
        <a
           href="#"
           class="list-group-item bg-light list-group-item-action py-3 ripple"
           ><i class="fas fa-lock fa-fw me-2 "></i><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-key-fill" viewBox="0 0 20 20">
  <path d="M3.5 11.5a3.5 3.5 0 1 1 3.163-5H14L15.5 8 14 9.5l-1-1-1 1-1-1-1 1-1-1-1 1H6.663a3.5 3.5 0 0 1-3.163 2zM2.5 9a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
</svg><span class="text-dark">Password</span></a
          >
          </div>
      </div>
  </nav>
</template>
<script>
export default {
  name: 'Sidebar',
  props: {
  }
}
</script>
<style scoped>
.sidebar {
  position: relative;
  height: 100vh;
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
}
.body {
    height: 100%;
}
</style>