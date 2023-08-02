<template>
    <div>
        <div class="row w-100 justify-content-left"> 
           <div class="card shadow-sm rounded">
            <div class="card-body mb-2">
                <div class="col-12"> 
                <h3 class="text-start text-primary">Set Parser</h3>
                <label for="formFileLg" class="control-label form-label">Enter Parser</label>

                <input v-model="parse" type="username" class="form-control" id="exampleInputPassword1">
                <div class="mt-3"> 
                <button type="button" class="btn btn-outline-primary">Set</button>
            </div>
              </div>
                
            </div>
          </div>
    </div>
    </div>
  </template>
  <script>
  import store from '@/store/index.js';

  export default {
    name: 'NewParser',
    data() {
      return{
        parse: ""
      }
    },
    props: {
    },
    methods: {
      setParse(){
        store.commit('setParse', {parser: this.parse });

      }
    }
  }
  </script>