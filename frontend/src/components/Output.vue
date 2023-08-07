<template>
    <div>
        <div class="row w-100 justify-content-left"> 
          <div class="card shadow-sm rounded">
            <div class="card-body mb-2 p-4">
                <div class=""> 
                  <div class="row"> 
                    <div class="col-2">
                <h3 class="text-start text-primary">Output</h3> 
              </div>
              <div class="col-2"> 
                <button class="btn mb-5 btn-light" @click="getOut()">Request JSON</button>
              </div>
              </div>
              </div>
                <div class="col-12"> 
                  <div v-if="$store.state.spinner" class="spinner-border spin text-primary" role="status">
                  <span class="sr-only"></span>
                </div>
                  <textarea v-model="$store.state.currentOutput" class="form-control bg-light" id="exampleFormControlTextarea1" rows="15"></textarea>
            </div>
            </div>
          </div>
    </div>
    </div>
  </template>
   <script>

import store from '@/store/index.js';

  export default {

     name: 'Output',
     data(){
      return {
        // jsonstr: '{"id":1,"name":"A green door","price":12.50,"tags":["home","green"]}'
      }
     },
     props: {
     },
     methods: {
      async getOut(){
        store.commit('setOutput', {})

      }

     },
     watch: {
        

  },
}
   </script>

<style scoped>
.spin{
  position:fixed;
}
</style>