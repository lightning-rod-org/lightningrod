<template>
    <div>
      <button type="button" class="btn btn-light">{{ticket_name}}</button>
  </div>  
</template>
<script>
  export default {
    name: 'Item',
    props: ['ticket_name'],
    methods: {
      pressed() {

      }
    }
  }
  </script>