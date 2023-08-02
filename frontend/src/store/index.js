import { createStore } from 'vuex'
import axios from 'axios';

export default createStore({
  state: {
    currentTicket: "",
    status: false,
    currentOutput: "",
    currentParser: ""
  },
  mutations: {
    setCurrentTicket(state, payload) {
      console.log(payload)
      state.currentTicket = payload.ticket;
      console.log(state.currentTicket)
      // let x = state.currentTicket
    },  
    setOutput(state) {
      console.log("going")
      console.log(state.currentTicket)
      axios.get("http://localhost:8000/api/instantParse/", { params: { ticket_number: state.currentTicket } })
          .then(function (response) {
            //handle success
            console.log(response)
            state.currentOutput = JSON.stringify(response.data.p_output)
          })
          .catch(function (response) {
            //handle error
            console.log(response);
          });
    },
    setParse(state, payload){
      state.currentParser = payload.parser
    }
  },
  actions: {
  },
  modules: {
  }
})
