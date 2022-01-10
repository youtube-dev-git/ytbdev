import axios from 'axios'

const apiclient = axios.create({
    baseURL: 'http://localhost:3000',
    withCredentials: true,
    headers:{
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    getInfo(){
        return apiclient.get('/posts')
    },
    createInfo(names){
        return apiclient.post('/Register', {
         name:names   
        })
    },
    showuserInfo(){
        return apiclient.get('/Register')
    },
    getInfo_id(id){
        return apiclient.get('/posts/' + id)
    }
}