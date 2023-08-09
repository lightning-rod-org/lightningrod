<template>
<div class="dropdown mb-1">
    <label for="formFileLg" class="control-label form-label"></label>

  <button class="btn btn-outline-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    {{$store.state.currentParser}}
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li v-for="(item, index) in this.items" :key="index">
        <!-- @click="$store.state.currentParser = 'deez'" -->
        <a class="dropdown-item" href="#" @click="setParse(item)" >{{item}}</a>
    </li>
    <!-- <li><a class="dropdown-item" href="#" @click="$store.state.currentParser = 'deez'">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li> -->
  </ul>
</div>
</template>
<script>
import axios from 'axios';
import store from '@/store/index.js';

export default {    
    name: 'Dropdown',
    data(){
        return{
            items: ['deez', 'deez', 'deez'],
            i : ""
        }
    },
    props: {},
    methods: {
        setParse(item){
            let tflag = true;
            // store.state.currentParser = item
            // store.state.dropdown_flag = true;
            console.log(item)
            store.commit('setDropdown', {flag: tflag, parse: item });
            this.i = item
            this.$emit('select', { data: this.i  });
            
        },
  async parsers() {
    try {
      const res = await axios.get('http://localhost:8000/api/parsers/');
      const data = res.data; // Assuming the API response is already in JSON format
      this.items = data.parsers; // Assign the 'parsers' array to 'this.items'
    } catch (e) {
      console.log(e);
    }
  },
  
  // Other methods
},
    created() {
        this.parsers()
    }
}
</script>