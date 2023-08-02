<template>
  <div>
    <div class="row w-100 justify-content-left"> 
      <div class="card shadow-sm rounded">
        <div class="card-body mb-2">
          <h3 class="text-start text-primary">Parse File</h3>
          <div class="col-9">
            <div>
              <label for="formFileLg" class="control-label form-label">Choose a File</label>
              <input class="form-control form-control" id="formFileLg" type="file" ref="fileInput" @change="previewFiles">
            </div>   
          </div>
          <div class="mt-3 align-conten-end">
            <button type="button" class="btn btn-outline-primary" @click="uploadFile">Go</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.control-label{
    text-align: start;
}
</style>

<script>
import axios from 'axios';
import store from '@/store/index.js';

export default {
  name: 'Main',
  data() {
    return {
      file: null,
      content: null,
      formData: null,
      parser: 'ifconfig'
    }
  },
  methods: {
      previewFiles(event) {
      console.log(event.target.files);
      this.file =  event.target.files[0];
      console.log(this.file)
      // this.$store.commit('setCurrentTicket', {  });

            // formData = new FormData();
      // formData.append('file', this.file); // Append the file to the form data
      // formData.append('parser', 'ifconfig'); // Append your parser value
      // console.log(JSON.stringify(formData))
   },
  
    async uploadFile() {
      var formData = new FormData()
      formData.append('file', this.file)
      formData.append('parser', "ifconfig")
      const headers = { 'Content-Type': 'application/json, text/plain, */*' }
      axios.post("http://localhost:8000/api/submit/", formData, headers)
          .then(function (response) {
            //handle success
            console.log(response.data.ticket_number);
            // var x = response;
            var x = response.data.ticket_number;
            store.commit('setCurrentTicket', {ticket: x });

          })
          .catch(function (response) {
            //handle error
            console.log(response);
          });
    },
}}
</script>
