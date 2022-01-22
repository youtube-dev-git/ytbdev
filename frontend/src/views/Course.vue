<template>
    <div>
        <div class="course">
            <div class="course_header">
                <h1>{{course[id-1].title}} </h1>
                <p>Bienvenue sur notre page de cours dans la quelle nous vous offrons les meilleurs videos youtube .</p>
                <p>Nombre Lecon: <span>{{course[id-1].lessons.length}}</span></p>
                <div class="course_star">
                    <i class="las la-star"></i>
                    <i class="las la-star"></i>
                    <i class="las la-star"></i>
                    <i class="las la-star"></i>
                </div>
                <p>cree par : <span>Dr Youtube</span> | <span>Web Develop</span></p>
            </div>
            <h1 class="txt_title">Programme d'etudes</h1>
            <section class="course_container">
                <div class="course_items">
                   <div class="course_item">
                       <div class="course_descrip">
                          <div class="course_info">
                             <h1>Chapitre 1 :{{course[id-1].title}}</h1>
                             <p>Description: <span>Aucune....</span></p>
                         </div>
                      </div>

                       <div class="sub_menu">
                         <ul>
                            <li><button class="list_btn">Afficher Lecon</button>
                            <ul class="lst_lecons">
                                <li><p class="lecon_title">Lecon_1 : {{course[id-1].lessons[id-1].title}}</p> 
                                <ul>
                                    <li class="lecon_item">
                                      <div class="video_item">
                                          <iframe width="270" height="200"  src="https://www.youtube.com/embed/2r6zeeGIfoI"></iframe>
                                          <iframe width="270" height="200" v-bind:src="'https://www.youtube.com/embed/' + course[0].lessons[0].videos[0].videoId"></iframe>
                                      </div>
                                    </li>
                                    <li class="lecon_item"></li>
                                </ul>
                                </li>
                                <li><p class="lecon_title">Lecon_2 : CSS les bases</p> 
                                <ul>
                                    <li class="lecon_item"> video_1</li>
                                </ul> 
                                </li>
                            </ul>
                            </li>
                          </ul>
                       </div>
                   </div>
                </div>
                <div class="course_menu">
                    <h1>Categories</h1>
                  <div class="menu_items">
                     <div class="menu_item">
                         <p>HTML</p>
                         <span>01</span>
                     </div>
                    <div class="menu_item">
                         <p>CSS</p>
                         <span>00</span>
                     </div>
                  </div>
                </div>
            </section>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import axios from 'axios'
import Footer from '@/components/Footer.vue'
export default {
    props:['id'],
    components: {
    Footer
  },
  data(){
      return{
          url:"2r6zeeGIfoI",
          course:[]
      }
  },
  created(){
               axios.get('https://ng70hk.deta.dev/syllabus')
                    .then(response =>{
                this.course = response.data
                console.log(response.data)
            })
            .catch(error =>{
                console.log('error', error.response)
            })

  },
  methods:{
        tests: function(){
            const lecons = document.querySelectorAll('list_btn')
            const submenu = document.querySelectorAll('course_submenu')
            lecons.forEach(tab => {
            tab.addEventListener('click', () => {
                lecons.forEach(tab => {
                tab.classList.remove('active')
                })
                tab.classList.add('active')
            })
            })
        }
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
.txt_title{
    margin-top: 35px;padding-left: 35px ; 
}
.txt_title::after {
    content: '';
    display: block;
    width: 12%;
    padding-bottom: 7px;
    border-bottom: 3px solid orangered;
}
.course_container{
    display: flex;
    justify-content: space-between;
}
.course_items{
   padding: 10px;
   width: 55%;
   color: white;
   display: flex;
   flex-direction: column;
}
.course_item{
    margin-left: 25px;
    margin-bottom: 30px;
}
.course_info{
    padding: 10px;
    background-color: rgb(65, 63, 63);
}
.course_info p{
    color: rgb(224, 219, 219);
    font-size: 18px;
    line-height: 25px;
    width: 70%;
}
.sub_menu{
    margin-top: -13px;
}
.sub_menu ul{
    color: black;
}
.sub_menu ul li{
    list-style: none;
}
.sub_menu ul ul{
    display: none;
}
.sub_menu ul li:hover > ul{
    display: block;
}
.sub_menu ul ul ul{
    display: none;
}
.list_btn{
    cursor: pointer;
    background-color: rgb(65, 63, 63);
    font-size: 16px;
    color:white;
    padding: 4.5px;
    letter-spacing: .5px;
    border: none;
    outline: none;
    margin-top: -2px;
}
.list_btn:hover{
    background-color: white;
    color: black;
    border: 1px solid rgb(34, 33, 33);
}
.lst_lecons{
    background-color: white;
    padding-bottom: 17px;
}
.lst_lecons li{
    margin-bottom: 10px;padding-top: 7px;
}
.lecon_title{
    font-size: 20px;
    cursor: pointer;
}
.lecon_title:hover{
    background-color: rgb(58, 56, 56);
    color: white;
    padding: 2px;
}
.lecon_item{
    font-size: 19px;
    color: rgb(89, 91, 94);
    cursor: progress;
    margin-bottom: 8px;
}
.course_menu{
    background-color: rgb(41, 39, 39);
    height: 100vh;width: 20%;
    margin-top: -92px;
    color: whitesmoke;
    font-size: 18px;
    padding-left: 15px;
    width: 23%;
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
.video_item iframe{
    margin-right: 60px;
}
</style>