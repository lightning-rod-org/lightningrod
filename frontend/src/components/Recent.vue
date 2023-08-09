<template>
    <div>
        <div class="row w-100 justify-content-left">

            <div class="card shadow-sm rounded">
                <div class="card-body ">
                    <div>
                        <h3 class="text-start p-1 text-primary">Recent Calls</h3>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item text"><a>{{$store.state.calls[0]}}</a></li>
                            <li class="list-group-item text"><a>{{$store.state.calls[1]}}</a></li>
                            <li class="list-group-item text"><a>{{$store.state.calls[2]}}</a></li>
                            <li class="list-group-item text"><a>{{$store.state.calls[3]}}</a></li>
                            <li class="list-group-item text"><a>{{$store.state.calls[4]}}</a></li>
                        </ul>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  <script>
import store from '../store';

  export default {
    name: 'Recent',
    props: {
    },
    data(){
        return{
            items: store.state.calls,
            i : ""
        }
    },
    methods: {
        recent(){
            console.log("im gay")
        }
    }
  }
  </script>
  <!-- <style-scoped>
  .text {

  }
  </style> -->