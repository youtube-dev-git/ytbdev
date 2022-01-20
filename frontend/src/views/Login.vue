<template>
<div class="login">
    <div class="login_img">
        <h1>Youtube Dev</h1>
      <img src="../../src/assets/login.png" alt="">
     </div>
    <div class="container">
     <div class="login-title">
        <h1>Se Connecter</h1>
     </div>

         <form @submit="login">
        <div class="login-control ">
          <input type="text" v-model="email" id="email" required>
          <label>Email</label>
        </div>
        <div class="login-control">
          <input type="password" v-model="password" id="password" required >
          <label>Password</label>
        </div>
        <button class="btn-login">Se connecter</button>
            <router-link to="/">cc</router-link>
        <p class="login-txt test">Aucun compte ? 
        <a href="#">S'inscrire</a></p>
    </form>
    </div>

</div>

</template>

<script>
import axios from 'axios'
export default {
    created(){
              axios.get('http://localhost:3000/Register/' + 1)
        .then(response =>{
         this.tab = response.data
         console.log(this.tab) 
     }) 

    },
    data () {
      return {
        email:null,
        password:null,
        taille: '',
        tab:[]
      }
    },
    methods: {  
        test: function(){
            var personne ={
                nom:['jean']
            };
            personne.nom[0];
            this.testss = personne.nom[0];
            console.log(personne.nom[0]);
            console.log(this.testss);
            
         },
        showError: function(input, message){
            const formcontrol = input.parentElement;
            formcontrol.className = 'login-control error'; 
            const small = formcontrol.querySelector('small');
            small.innerText = message;
        },
    login(e){
                     this.taille=this.tab.name
         console.log(this.tab.length)
        if(this.email && this.password){
            alert('Connexion reussi')

        }        
        e.preventDefault()
    }
      
    },

}
</script>


<style lang="scss">

.login{
  position: relative;
  background-color: steelblue;
  border-radius: 5px;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  height: 100vh;width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
//   flex-direction: column;
  overflow: hidden;
  margin: 0;
}
.login_img{
    margin-right: 250px;
}
.login_img img{
width: 350px;
}
.login_img h1{
    text-align: center;
    font-size: 45px;
    text-transform: uppercase;
    font-weight: 700;
}
.login-title{
    font-weight: 500;
    font-size: 15px;
}
.login-txt{
    text-align: center;
}
.container{
    background-color: rgba(0, 0, 0, 0.4);
    padding: 20px 40px;
    border-radius: 5px;
}
.container h1{
    text-align: center;
}
.container a{
    text-decoration: none;
    color: lightblue;
}
 .login-control {  
  position: relative;  
  margin: 35px 0 40px;  
  width: 300px;  
 }  
 .login-control input {  
  background-color: transparent;  
  border: 0;  
  border-bottom: 2px #fff solid;  
  display: block;  
  width: 100%;  
  padding: 12px 0;  
  font-size: 18px;  
  color: #fff;   
 }  
 .login-control input:focus,  
 .login-control input:valid {  
  outline: 0;  
  border-bottom-color: lightblue;  
 }  
 .login-control label {  
  position: absolute;  
  top: 20px;  
  left: 0;  
  pointer-events: none;  
 }  
 .login-control label  {  
  display: inline-block;  
  font-size: 20px;  
  min-width: 5px;   
 }  
 .login-control input:valid + label ,  
 .login-control input:focus + label  {  
  color: lightblue;  
  transform: translateY(-33px);  
 }

.btn-login{
    cursor: pointer;
    display: inline-block;
    width: 100%;
    background: lightblue;
    padding: 10px;
    color: rgb(48, 46, 46);
    font-size: 16px;
    border: 0;
    border-radius: 5px;
}
.btn-login:focus{
    outline: 0;
}
.btn-login:hover{
    transform: scale(1.1);
}
</style>




