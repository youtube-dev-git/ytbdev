<template>   
    <div>
     <h1>List Card</h1>
       <card v-for="event in events" :key="event.id" :event="event" ></card>
    </div>
</template>

<script>
// import eventservice from '@/services/event_service.js';
import axios from 'axios'
import card from '@/components/card.vue'
export default {
      data(){
      return{
        events:[]
      }
  },
    created(){
     axios
     .get('http://localhost:3000/posts')
     .then(response =>{
         this.events = response.data
         console.log(response.data)
     })
     .catch(error =>{
         console.log('error', error.response)
     })
   },
    components:{
        card
    }
}
</script>
<style scoped>
.link{
    text-decoration: none;
}
</style>