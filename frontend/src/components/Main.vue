<template>
  <div>
    <div class="row d-flex justify-content-center"> 
    <div class="col-md-4 card shadow-lg rounded">
          <div class="card-body p-4">
            <div class="container">
              <div class="row d-flex justify-content-center"> <!-- Modified parent div -->
                <div class="col-auto"> <!-- Modified class for SVG -->
                  <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-lightning d-inline" viewBox="0 0 16 16">
                    <path d="M5.52.359A.5.5 0 0 1 6 0h4a.5.5 0 0 1 .474.658L8.694 6H12.5a.5.5 0 0 1 .395.807l-7 9a.5.5 0 0 1-.873-.454L6.823 9.5H3.5a.5.5 0 0 1-.48-.641l2.5-8.5zM6.374 1 4.168 8.5H7.5a.5.5 0 0 1 .478.647L6.78 13.04 11.478 7H8a.5.5 0 0 1-.474-.658L9.306 1H6.374z"/>
                  </svg>
                </div>
                <div class="col-auto"> <!-- Modified class for header text -->
                  <h2>Lightning Rod</h2>
                </div>
              </div>
            </div>
            <h3 class="text-start p-1 text-primary">Parser</h3>
            <div class="mb-2 col-3">
              <input v-model="pack" type="username" class="form-control" id="exampleInputPassword1">
            </div>
            <div class="container p-2">
              <div class="row">
                <div class="col-auto">
                  <button type="button" class="btn btn-outline-primary" @click="post()">Go</button>
                </div>
                <div class="col-auto"> 
                  <button type="button" class="btn btn-primary" :disabled="isButtonDisabled" @click="modalShow()">Show JSON</button>
                </div>
              </div>
            </div>
          </div>
        </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
  props: {
  },
  methods: {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- <style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style> -->
