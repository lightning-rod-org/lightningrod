<template>
    <div>
        <div class="row w-100 justify-content-left"> 
           <div class="card shadow-sm rounded">
            <div class="card-body">
                <div class="col-12"> 
                <h3 class="text-start text-primary">Set Parser</h3>
                <label for="formFileLg" class="control-label form-label">Selected Parser:</label>
                <div class="row"> 
                  <div class="col-3">

                  </div>
                 <div class="col-6"> 
                <!-- <input v-model="parse" type="username" class="form-control" id="exampleInputPassword1"> -->
                <a v-if="parser_set == false"> None</a>
                <a v-else class="text-success">{{ this.parse }} </a>
              </div>
              <div class="col-1">
                <button type="button" class="btn btn-outline-primary" @click="setParse()">Set</button>
              </div>
              </div>
                <div class="mt-3"> 
                <Dropdown @select="handleChange"></Dropdown>
                
            </div>
              </div>
                
            </div>
          </div>
    </div>
    </div>
  </template>
  <script>
  // import { useToast } from "vue-toastification";
  import store from '@/store/index.js';
  import Dropdown from './Dropdown.vue';
  import axios from 'axios';
  import { mapState } from 'vuex';

  export default {
    name: 'NewParser',
    components: {
      Dropdown
    },
    data() {
      return{
        parse: "",
        items: [],
        flag: false,
        parser_set: false
      }
    },
    computed: {
    ...mapState(['dropdown_parse']), // Add other state properties here if needed
  },
  dropdown_flag() {
    this.parse = "dsafa"
    },
    props: {
    },
    methods: {
      async parsers() {
    try {
      const res = await axios.get('http://localhost:8000/api/parsers/');
      const data = res.data; // Assuming the API response is already in JSON format
      this.items = data.parsers; // Assign the 'parsers' array to 'this.items'
    } catch (e) {
      console.log(e);
    }
  },
      async setParse(){
        // const toast = useToast();
        this.parser_set = true
        store.state.dropdown_parse = store.state.currentParser
        console.log(this.parse)
        await this.parsers()
        console.log("yooo")
        store.commit('setParse', {parser: this.parse })
        },
        handleChange(eventData) {
          this.parse =  eventData.data;
        }
    },

       
    }
  
  </script>