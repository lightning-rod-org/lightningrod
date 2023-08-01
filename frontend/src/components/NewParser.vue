<template>
    <div>
        <div class="row w-100 justify-content-left"> 
           <div class="card shadow-sm rounded">
            <div class="card-body mb-2">
                <div class="col-9"> 
                <h3 class="text-start p-1 text-primary">Add Parsers</h3>
                <label for="formFileLg" class="control-label form-label">Enter new Parser</label>

                <input v-model="pack" type="username" class="form-control" id="exampleInputPassword1">
                <div class="p-1"> 
                <button type="button" class="btn btn-outline-primary">Go</button>
            </div>
              </div>
                
            </div>
          </div>
    </div>
    </div>
  </template>
  <script>
  export default {
    name: 'NewParser',
    props: {
    },
    methods: {}
  }
  </script>