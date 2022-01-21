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
          .post("http://127.0.0.1:8000/register", credentials)
          .then(({ data }) => {
              console.log("user data is:", data);
          })
          .catch((error) => {
              console.log("There was an error: " + error.response);
          });
  },
  login({commit}, credentials){
    return axios
        .post("http://127.0.0.1:8000/login", credentials)
        .then(({ data }) => {
            console.log("user data is:", data);
        });
},
add_sylab({commit}, credentials){
  return axios
      .post("http://127.0.0.1:8000/syllabus", credentials)
      .then(({ data }) => {
          console.log("user data is:", data);
      });
}
  },
  modules: {
  }
})
