import { createStore } from 'vuex'
import axios from 'axios';

export default createStore({
  state: {
    currentTicket: "None",
    current_ticket: "None",
    status: false,
    currentOutput: "",
    currentParser: "Choose a Parser",
    stored_input: "",
    spinner: false,
    calls: [" N/A ", " N/A ", " N/A ", " N/A ", " N/A "],
    dropdown_flag: false,
    dropdown_parse: "Choose a Parser",
    additional_info: {
      ticket_status: "None",
      parser: "None",
      time_created: "None",
      time_finished: "None",
    }
  },
  mutations: {
    setDropdown(state, payload){
      state.dropdown_flag = payload.flag
      // state.currentParser = payload.parsei
      state.dropdown_parse = payload.parse
      state.currentParser = payload.parse
      console.log(state.currentParser)
      console.log(state.dropdown_flag)
      state.dropdown_flag = true
      state.stored_input = payload.parse
    }, 
    setCurrentTicket(state, payload) {
      console.log(payload.ticket)
      state.currentTicket = payload.ticket;
      console.log(state.currentTicket)
      state.calls.unshift(state.currentTicket);
      if(state.calls.length > 5){
        state.calls.pop()
      }
      console.log(state.calls)
    },  
    async setOutput(state) {
      console.log("going")
      console.log(state.currentTicket)

      try {
        let isCompleted = false;
        while (!isCompleted) {
          const response = await axios.get("http://localhost:8000/api/status/", { params: { ticket_number: state.currentTicket } });
          console.log(response.data);
          state.additional_info.parser = state.currentParser
          state.additional_info.time_created = response.data.time_created
          if (response.data.status === "Completed") {
            state.additional_info.ticket_status = response.data.status;
            state.currentOutput = JSON.stringify(response.data.p_output);
            state.additional_info.time_finished = response.data.time_finished
            state.spinner = false;
            state.status = true;
            isCompleted = true;  
          } else {
            state.additional_info.ticket_status = response.data.status;
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
      state.dropdown_flag = false
    }
  },
  actions: {
  },
  modules: {
  }
})
