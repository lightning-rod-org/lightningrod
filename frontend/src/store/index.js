import { createStore } from 'vuex'
import axios from 'axios';

export default createStore({
  state: {
    currentTicket: "",
    status: false,
    currentOutput: "",
    currentParser: "Choose a Parser",
    spinner: false,
  },
  mutations: {
    setCurrentTicket(state, payload) {
      console.log(payload)
      state.currentTicket = payload.ticket;
      console.log(state.currentTicket)
    },  
    async setOutput(state) {
      console.log("going")
      console.log(state.currentTicket)

      try {
        let isCompleted = false;
        while (!isCompleted) {
          const response = await axios.get("http://localhost:8000/api/instantParse/", { params: { ticket_number: state.currentTicket } });
          console.log(response.data);
          
          if (response.data.status === "Completed") {
            state.currentOutput = JSON.stringify(response.data.p_output);
            state.spinner = false;
            state.status = true;
            isCompleted = true; // Exit the loop
          } else {
            state.status = false;
            state.spinner = true;
            await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for 1 second before the next check
          }
        }
      } catch (error) {
        // handle error
        console.log(error);
      }
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
