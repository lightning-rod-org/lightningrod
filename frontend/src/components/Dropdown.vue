<template>
<div class="dropdown mb-1">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    {{$store.state.currentParser}}
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#" @click="$store.state.currentParser = 'deez'">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
</template>
<script>
import axios from 'axios';

export default {    
    name: 'Dropdown',
    data(){
        return{
            items: ['deez', 'deez', 'deez']
        }
    },
    methods: {
        async parsers() {
    try {
      const res = await axios.get('http://localhost:8000/api/parsers/')
        console.log("yep")
      this.items = res.parsers
    } catch (e) {
        console.log(e)
    }
  }
        // function()
        // axios.get("http://localhost:8000/api/instantParse/", { params: { ticket_number: state.currentTicket } });
    },
    created() {
        this.parsers()
    }
}
</script>