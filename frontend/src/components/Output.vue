<template>
    <div>
        <div class="row w-100 justify-content-left"> 
          <div class="card shadow-sm rounded">
            <div class="card-body mb-2 p-4">
                <div class=""> 
                <h3 class="text-start text-primary">Output</h3> 
              </div>
                <div class="col-12"> 
                  <textarea v-model="jsonstr" class="form-control bg-light" id="exampleFormControlTextarea1" rows="3"></textarea>
            </div>
            </div>
          </div>
    </div>
    </div>
  </template>
   <script>
   export default {
     name: 'Output',
     data(){
      return {
        jsonstr: '{"id":1,"name":"A green door","price":12.50,"tags":["home","green"]}'
      }
     },
     props: {
     },
     methods: {}
   }
   </script>