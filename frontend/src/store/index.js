import { createStore } from 'vuex'
import axios from 'axios'
export default createStore({
  state: {
    user:null
  },
  mutations: {
    SET_USER_DATA (state, userData){
      state.user = userData
      localStorage.setItem('user', JSON.stringify(userData))
      axios.defaults.headers.common['Authorization'] = `Bearer ${userData.token}` 
    }
  },
  actions: {
    register({commit}, credentials){
      return axios
      .post('http://localhost:3000/Register', credentials)
      .then(({data})=>{
          console.log('user data is:', data)
      })
  },
  login({commit}, credentials){
    return axios
    .post('http://localhost:3000/Login', credentials)
    .then(({data})=>{
        console.log('user data is:', data)
    })
},
add_sylab({commit}, credentials){
  return axios
  .post('http://localhost:3000/Sylab', credentials)
  .then(({data})=>{
      console.log('user data is:', data)
  })
}
  },
  modules: {
  }
})