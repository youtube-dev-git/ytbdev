<template>

  <header>
      <nav>
        <div class="logo">
            <img src="../../src/assets/Logo_2.png" alt="">
            <h1>Youtube Dev</h1>
        </div>
        <div>
            <ul class="main_nav">
                <li><router-link :to="{name: 'Home'}" class="link">Home</router-link></li>
                <li><router-link :to="{name: 'Login'}" class="link">Categories</router-link></li>
                <li><router-link :to="{name: 'Login'}" class="link">Se Connecter</router-link></li>
                <li><router-link :to="{name: 'Register'}" class="link">S'inscrire</router-link></li>
                <li>
                    <div class="search">
                        <div class="icon"></div>
                        <div class="input">
                            <input v-model="search" type="text" placeholder="Rechercher Cours">
                        </div>
                    </div>
                </li>
            </ul>
        </div>
      </nav>
  </header>
</template>

<script>
export default {
    data () {
      return {
          search:''
      }
      
    },
    methods: {}
}
</script>

<style lang="scss">
header{
    width: 100%; 
    font-family: Arial, Helvetica, sans-serif;
}
nav{
    display: flex;
    justify-content: center;
    align-items: center;
    justify-content: space-between;
}
.logo{
    display: flex;
    align-items: center;
}
.logo img{
    width: 95px; height: 95px;
    margin-left: 15px;margin-right: 15px;
}
.logo h1{
    color: rgb(68, 66, 66);
    font-size: 30px;
    text-transform: uppercase;
    font-weight: 550;
}
.link{
    color: rgb(73, 72, 70);
    font-size: 21px;
}
.main_nav{
float: right;
list-style: none;
padding-right: 20px;
display: flex;
justify-content: center;
align-items: center;
}
.main_nav li{
    display: inline-block;
    margin-left: 25px;
}
.main_nav li .link:link,
.main_nav li .link:visited {
    padding: 10px 0;
    text-decoration: none;
    color: rgba(90, 86, 86, 0.979);
    letter-spacing: 1.1px;
    border-bottom: 2px solid transparent;
    transition: border-bottom 0.25;
}
.main_nav li .link::after {
    content: '';
    display: block;
    width: 0;
    border-bottom: 2px solid orangered;
    transition: width .9s;
}
.main_nav li .link:hover::after {
    width: 100%;
    color: orangered;
}
.main_nav li .link:hover{
    color: orangered;
}
.search{
    position: relative;
    width: 30px; height: 30px;
    border-radius: 60px;
    background-color: white;
    transition: 0.5s;
    box-shadow: 0 0 0 2px rgb(211, 208, 208);
    overflow: hidden;
}
.search .icon{
    position: absolute;
    top: 0;
    left: 0;
    width: 30px; height: 30px;
    background-color: white;
    border-radius: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    cursor: pointer;
}
.search .icon::before{
    content: '';
    position: absolute;
    width: 10px;height: 10px;
    border: 3px solid rgb(78, 76, 76);
    border-radius: 50%;
}
 .search:hover{
    width: 220px;
}
.search .input{
    position: relative;
    width: 165px;
    height: 25px;
    left: 35px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.search .input input{
    position: absolute;
    top: 0;
    width: 100%;height: 100%;
    border: none;
    outline: none;
}
</style>