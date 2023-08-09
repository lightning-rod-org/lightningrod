<template>
    <div class="h-100">
        <div class="row w-100 justify-content-left">
            <div class="card shadow-sm rounded">
                <div class="card-body mb-1">
                    <div>
                        <h3 class="p-2 text-primary">Additional Info</h3>
                            <h4 class="">Status:</h4>
                            <a>{{$store.state.additional_info.ticket_status}}</a>
                            <h4>Parser:</h4>
                            <a>{{$store.state.additional_info.parser}}</a>
                            <h4>Time Created:</h4>
                            <a>{{$store.state.additional_info.time_created}}</a>
                            <h4>Time Finished:</h4>
                            <a>{{$store.state.additional_info.time_finished}}</a>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// import store from '../store';

export default {
    name: 'AdditionalInfo',
    props: {
    },
    methods: {}
  }
  </script>