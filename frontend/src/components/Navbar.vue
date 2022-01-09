<template>

  <header>
      <nav>
        <div class="logo">
            <img src="../../src/assets/Logo_2.png" alt="">
            <h1>Youtube Dev</h1>
        </div>
        <div>
            <ul class="main_nav">
                <li><a href="">Home</a></li>
                <li><a href="">Categories</a></li>
                <li><a href="">Se connecter</a></li>
                <li><a href="">S'inscrire</a></li>
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
      <hr class="dashed">
       <div class="slider">
           <button @click="prev" class="btn btn-left">
               <img src="../../src/assets/left.png" class="icone">
           </button>
           <div class="container-slides">
               <div class="item-slider">
                   <div class="item-container">
                       <div class="item-txt">
                           <h1>{{slides_title[current].title_val}}</h1>
                           <p>{{slides_txt[current].txt_val}}</p>
                       </div>
                       <div class="item-pic">
                           <img v-bind:src="require('../../src/assets/' + slides_pic[current].pic_val)">
                       </div>
                   </div>
               </div>
           </div>
           <button @click="next" class="btn btn-right" type="button">
               <img src="../../src/assets/right.png" class="icone">
           </button>
             
       </div> 
  </header>

</template>

<script>
export default {
    data () {
      return {
        current: 0,
        index: 0,
        transitionName: "fade",
        show: false,
        slides_title: [
          { title_val: "Apprentissage Gratuit" },
          { title_val: "Des Experts a votre disposition" },
        ],
        slides_txt: [
          { txt_val: "Formez vous des aujourd'hui de facon structuré, détaillé, grace a notre plateforme Youtube Dev" },
          { txt_val: "Nos experts du monde entier sélectionne les meilleurs vidéos d'apprentissage, pour vous offrir les outils et les compétences." },
        ],
        slides_pic: [
          { pic_val: "header_slide_1.png" },
          { pic_val: "header_slide_2.png" },
        ],
        search: '',
        name: 'TestOne',
      }
    },
    methods: {
        next(){
          var len = this.slides_txt.length-1;
          console.log(len);
          if(this.current === len){
              this.current = 0;
          }
          else{
              this.current ++;
          }
        },
        prev(){
          var len = this.slides_txt.length-1;
          console.log(len);
          if(this.current === 0){
              this.current = len;
          }
          else{
              this.current --;
          }
        }
    }
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
    width: 75px; height: 75px;
    margin-left: 15px;margin-right: 15px;
}
.logo h1{
    color: rgb(68, 66, 66);
    font-size: 27px;
    font-weight: 550;
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
.main_nav li a{
    text-decoration: none;
    color: rgba(90, 86, 86, 0.979);
    font-size: 17.5px;
    letter-spacing: 1.1px;
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
hr.dashed {
  margin-top: 35px;
  border-top: 1px dashed #bbb;
}
.slider{
    width: 100%;
    height: auto;
    overflow: hidden;
 
    position: relative;
}
.container-slides{
    display: flex;
}
.item-container{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-left: 75px;margin-right: 75px;
}
.item-slider{
    width: 100%;
    height: auto;
}
.item-txt{
    background-color: white;
    width: 650px;
    padding-left: 25px;

    border-radius: 5px;
    box-shadow: 2px 1px 1px 1px rgb(219, 215, 215);
    font-size: 17.2px;
    color: rgb(107, 104, 104);
}
.item-txt h1{
    color: rgb(51, 49, 49);
    text-transform: uppercase;
}
.item-pic img{
    width: 330px;
}
.btn{
    outline: none;
    border: none;
    width: 50px;height: 50px;
    border-radius: 50%;
    display: block;
    position: absolute;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
.btn-left{
    top: 50%;
    transform: translateY(-50%);
}
.btn-right{
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}
.icone:hover{
    transform: scale(1.3);
}
.icone{
    width: 25px;
}

</style>