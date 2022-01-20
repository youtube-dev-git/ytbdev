<template>
  <div class="carousel_1">
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
  </div>

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
          { title_val: "Des Experts à votre disposition" },
        ],
        slides_txt: [
          { txt_val: "Formez vous dès aujourd'hui dans divers domaines du developpement web en suivant des programmes structurés et détaillés, grace à notre plateforme Youtube Dev." },
          { txt_val: "Des experts du monde entier sélectionnent chaque jour les meilleurs vidéos d'apprentissage pour vous offrir le strict nécessaire pour votre formatiion.." },
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
.carousel_1{
    width: 100%; 
    font-family: Arial, Helvetica, sans-serif;
}

hr.dashed {
  margin-top: 25px;
  border-top: .5px dashed #bbb;
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