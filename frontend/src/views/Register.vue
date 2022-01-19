<template>
<div id="sign">
    <div class="user_type">
    <ul class="tabs">
        <li @click="tab_user" data-tab-target="#Apprenant" class="active tab">Apprenant</li>
        <li @click="tab_exp" data-tab-target="#Expert" class="tab">Expert</li>
        <li @click="tab_adm" data-tab-target="#Admin" class="tab">Admin</li>
    </ul>
    </div>
    <div class="sign_img">
        <h1>Youtube Dev</h1>
      <img v-bind:src="require('../../src/assets/' + signUp_pic[pos].val)">
     </div>
    <div class="sign_container">
      <form id="form" class="form" @submit.prevent="click">
           <h2>S'inscrire</h2>

            <div class="sign-control">
            <label for="name">Nom</label>
            <input type="text" id="name" v-model="name" placeholder="Entrer votre Nom" />
            <small>Error message</small>
            </div>
<<<<<<< HEAD
=======
            <div class="sign-control">
            <label for="pseudo">Pseudo</label>
            <input type="text" id="pseudo" v-model="pseudo" placeholder="Entrer votre Pseudo" />
            <small>Error message</small>
            </div>
        </div>
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
        <div class="contains">
            <div class="sign-control">
            <label for="mail">Email</label>
            <input type="text" id="mail" v-model="email" placeholder="Entrer votre Email" />
            <small>Error message</small>
            </div>
            <div class="sign-control">
            <label for="phone">Telephone</label>
            <input type="text" id="phone" v-model="phone" placeholder="Entrer votre numero" />
            <small>Error message</small>
            </div>
        </div>
         <div class="contains">
            <div class="sign-control">
                <label for="files">Image file</label>
                <input type="file" name="files"  id="files">
                <small>Error message</small>
            </div>
            <div class="sign-control">
                <label for="sex">sex</label>
                <select name="sex" id="sex" v-model="sex">
                    <option  value="M">M</option>
                    <option value="F">F</option>
                </select>
            </div>
         </div>
        <div class="sign-control">
          <label for="sign_password">Mot de Passe</label>
          <input type="password" id="sign_password" v-model="password" placeholder="Enter Mot de Passe" />
          <small>Error message</small>
        </div>
        <div class="sign-control">
          <label for="sign_password2">Confirm Password</label>
          <input type="password" id="sign_password2" v-model="password2" placeholder="Enter password again"/>
          <small>Error message</small>
        </div>
        <button type="submit" @click="submit">Submit</button>
      </form>
    </div>
</div>
</template>

<script>
import register from '@/classes/class_register.js';
export default {
    created(){
        
    },
    data () {
      return {
        signUp_pic: [
          { val: "login_user.png" },
          { val: "login_master.png" },
          { val: "login_admin.png" },
        ],
<<<<<<< HEAD
=======
        pseudo:null,
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
        name:null,
        email:null,
        phone:null,
        password:null,
        password2:null,
        statut:'Apprenant',
        img:'no_pic.png',
        sex:null,
        pos:0
      }
    },
    methods: {  
        test: function(){
            const tabs = document.querySelectorAll('[data-tab-target]')
            const tabContents = document.querySelectorAll('[data-tab-content]')
            tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const target = document.querySelector(tab.dataset.tabTarget)
                tabContents.forEach(tabContent => {
                tabContent.classList.remove('active')
                })
                tabs.forEach(tab => {
                tab.classList.remove('active')
                })
                tab.classList.add('active')
                target.classList.add('active')
            })
            })
        },
    tab_user(){
        const signUp_color = document.getElementById("sign")
        signUp_color.style.backgroundColor='steelblue'
          this.test();
          this.pos=0;
          this.statut='Apprenant';
      },
    tab_exp(){
        const signUp_color = document.getElementById("sign")
        signUp_color.style.backgroundColor='rgb(5, 55, 95)'
          this.test();
          this.pos=1;
          this.statut='Expert';
      },
    tab_adm(){
        const signUp_color = document.getElementById("sign")
        signUp_color.style.backgroundColor='rgb(52, 52, 53)'
          this.test();
          this.pos=2;
          this.statut='Admin';
    },
    click(){
<<<<<<< HEAD
        if(this.name && this.email && this.phone && this.sex  && this.password===this.password2 ){
            this.$store.dispatch('register', {
                 user:{
                  name: this.name,
                  email: this.email,
                  phone_num: this.phone,
                  password: this.password,
                  gender: this.sex,
                  photo: this.img,
                 },
                  statut: this.statut,
            })
            .then( () =>{
              
            })
              if(this.statut=='Apprenant'){
                 this.$router.push({name: 'Home_user', params: {pseudo:this.name }})
              }
                console.log('connexion reussi')     
        }
      register.validate(this.name,this.email,this.phone,this.sex,this.password,this.password2)
=======
        this.$router.push({name: 'Home_user', params: {pseudo:this.pseudo }})
        if(this.name && this.pseudo && this.email && this.phone && this.sex  && this.password==this.password2 ){
            this.$store.dispatch('register', {
                name: this.name,
                pseudo: this.pseudo,
                email: this.email,
                phone: this.phone,
                img: this.img,
                sex: this.sex,
                password: this.password,
                statut: this.statut,
            })
            .then( () =>{
              if(this.statut=='Apprenant'){
                 this.$router.push({name: 'Home', params: {name:this.name }})
              }
              
            })
                console.log('connexion reussi')     
        }
      register.validate(this.name,this.pseudo,this.email,this.phone,this.sex,this.password,this.password2,this.statut)
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
    }
},
}
</script>

<style lang="scss">
:root {
  --success-color: #2ecc71;
  --error-color: #e74c3c;
}
#sign{
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
.user_type{
    position: absolute;
    top: 0;
    left: 0;
    background-color: white;
    padding-bottom: 5px;
    border-bottom-right-radius: 5px;
    text-transform: uppercase;
}
.tabs {
  display: flex;
  justify-content: space-around;
  list-style-type: none;
  margin: 0;
  padding: 0;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 19px;
  color: rgb(26, 24, 24);
}

.tab {
  cursor: pointer;
  padding: 10px;
}

.tab.active {
  border-bottom: 2px solid ;
  border-bottom-color: orangered;
  color: orangered;
}

.sign_img{
    margin-right: 250px;
}
.sign_img img{
width: 350px;
}
.sign_img h1{
    text-align: center;
    font-size: 45px;
    text-transform: uppercase;
    font-weight: 700;
}
.sign-title{
    font-weight: 500;
    font-size: 15px;
}
.sign_container {
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  width: 450px;
}
.contains{
    display: flex;
    justify-content: center;
    align-items: center;
}
h2 {
    color: #000;
  text-align: center;
  margin: 0 0 20px;
}


.form {
  padding: 30px 20px;
}

.sign-control {
  margin-bottom: 10px;margin-right: 15px;
  padding-right: 20px;
  padding-bottom: 10px;
  position: relative;
}

.sign-control label {
  color: #777;
  display: block;
  margin-bottom: 5px;
}

.sign-control input {
  border: 2px solid #f0f0f0;
  border-radius: 4px;
  display: block;
  width:100%;
  padding: 10px;
  font-size: 14px;
}

.sign-control input:focus {
  outline: 0;
  border-color: #777;
}

.sign-control.success input {
  border-color: var(--success-color);
}

.sign-control.error input {
  border-color: var(--error-color);
}

.sign-control small {
  color: var(--error-color);
  position: absolute;
  bottom: 0;
  left: 0;
  visibility: hidden;
}

.sign-control.error small {
  visibility: visible;
}

.form button {
  cursor: pointer;
  background-color: #3498db;
  border: 2px solid #3498db;
  border-radius: 4px;
  color: #fff;
  display: block;
  font-size: 16px;
  padding: 10px;
  margin-top: 20px;
  width: 100%;
}

</style>