<template>
    <div>
        <div class="course">
            <div class="course_header">
                <h1>HTML et CSS : la formation ULTIME {{id}}</h1>
                <p>Testez et améliorez vos compétences en HTML & CSS grâce à 101 exercices HTML & CSS corrigés allant de débutant à avancé.</p>
                <p>Nombre Video: <span>00</span></p>
                <div class="course_star">
                    <i class="las la-star"></i>
                    <i class="las la-star"></i>
                    <i class="las la-star"></i>
                    <i class="las la-star"></i>
                </div>
                <p>cree par : <span>Nom_expert</span> | <span>Frontend</span></p>
            </div>
            <h1 class="txt_title">Contenu du Cours</h1>
            <div class="course_main">
                <div class="course_items">
                  <div class="item_course">
                     <div class="video_course">
                         <img src="@/assets/html_course_4.jpg" alt="">
                     </div>
                     <div class="video_info">
                         <h1>Introduction HTML & CSS</h1>
                         <p>Description</p>
                         <p>Autre information</p>
                     </div>
                  </div>
                </div>
                <div class="course_menu">
                  <h1>Categories</h1>
                  <div class="menu_items">
                     <div class="menu_item">
                         <p>Nom categorie </p>
                         <span>00</span>
                     </div>
                  </div>
                </div>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import Footer from '@/components/Footer.vue'
export default {
    props:['id'],
    components: {
    Footer
  }  
}
</script>
<style scoped>
.course_header{
     padding: 5px;
    padding-left: 35px ;

    background-color: rgb(46, 44, 44);
    color: white;
    border-radius: 5px;
    font-family: Arial, Helvetica, sans-serif;
}
.course_header p{
    font-size: 20px;
    width: 55%;
    letter-spacing: .5px;
    line-height: 24px;
}
.course_star i{
    color: orangered;
    margin-left: 2px;
}
.course_main{
padding-left: 35px ; 
display: flex;
justify-content: space-between;
}
.txt_title{
    margin-top: 35px;padding-left: 35px ; 
}
.course_items{
    display: flex;
    flex-direction: column;
    width: 60%;
    background-color: rgb(241, 237, 237);
    margin-bottom: 35px;
    border: white solid 2px;
    height: 150px;
}
.item_course{
    display: flex;
    align-items: center;
    height: 150px;
}
.video_course{
width: 175px;
height: 150px;
}
.video_course img{
width: 175px;
height: 150px;
}
.video_info{
    margin-left: 40px;
}
.course_menu{
    background-color: rgb(172, 169, 169);
    height: 100vh;width: 20%;
    margin-top: -90px;
    color: rgb(46, 43, 43);
    font-size: 18px;
}
.course_menu h1{
    font-size: 25px;
    margin-left: 15px;
    color: rgb(75, 76, 77);
}
.course_menu p{
    cursor: pointer;
}
.course_menu :hover{
    color: white;
    font-size: 19px;
}
.menu_item{
    padding-left: 25px;padding-right: 25px;
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 25px;
}
.menu_item span{
    background-color: rgb(66, 63, 63);
    border-radius: 5px;
    padding: 2px;
    color: whitesmoke;
}
</style>