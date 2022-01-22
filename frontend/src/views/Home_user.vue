<template>
  <div class="home">
      <header>
      <nav>
        <div class="logo">
            <img src="../../src/assets/Logo_2.png" alt="">
            <h1>Youtube Dev</h1>
        </div>
        <div>
            <ul class="main_nav">
                <li><router-link :to="{name: 'Home_user'}" class="link">Home</router-link></li>
                <li><router-link :to="{name: 'Login'}" class="link">Categories</router-link></li>
                <li><router-link :to="{name: 'Home'}" class="link">Deconnecter</router-link></li>
                <li>
                    <div class="search">
                        <div class="icon"></div>
                        <div class="input">
                            <input v-model="user_search" type="text" placeholder="Rechercher Cours">
                        </div>
                    </div>
                </li>
                <li><h1 class="user_logo">{{user_logo}}</h1></li>
            </ul>
        </div>
      </nav>
  </header>
    <SlideOne></SlideOne>
     <UserMain></UserMain>
     <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import UserMain from '@/components/User_main.vue'
import Footer from '@/components/Footer.vue'
import SlideOne from '@/components/Carousel_1.vue'
export default {
  props:['pseudo'],
  name: 'Home_user',
  components: {
    SlideOne,
    UserMain,
    Footer
  },
  created(){
   console.log(this.pseudo)
   this.user_logo = this.pseudo.charAt(0)+this.pseudo.charAt(1)
  },
  data(){
      return{
          user_logo:'',
          user_search:null
      }
  },
  methods:{

  }
}
</script>
<style scoped>
.user_logo{
    text-transform: uppercase;
    background-color: rgb(70, 67, 67);
    color: white;
    padding: 8px;
    font-size: 19px;
    border-radius: 50%;
}
</style>