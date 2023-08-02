import { createStore } from 'vuex'

export default createStore({
  state: {
    currentTicket: "",
    status: false,
    currentOutput: ""
  },
  mutations: {
    setCurrentTicket(state, payload) {
      console.log(payload)
      state.currentTicket = payload.ticket;
      console.log(state.currentTicket)
      
    },  
  },
  actions: {
  },
  modules: {
  }
})
