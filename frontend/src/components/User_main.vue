<template>
  <div>
    <div class="home_intro">
        <h1>Un large sylabus de cours a votre disposition</h1>
        <p>Choisissez parmi nos vidéos de cours celle qui vous convient.. </p>
    </div>
    <div class="tabset">
        <!-- Tab 1 -->
        <input type="radio" name="tabset" id="tab1" aria-controls="tabpanel_1" checked>
        <label for="tab1">Html & Css</label>
        <!-- Tab 2 -->
        <input type="radio" name="tabset" id="tab2" aria-controls="tabpanel_2">
        <label for="tab2">JavaScript</label>
        <!-- Tab 3 -->
        <input type="radio" name="tabset" id="tab3" aria-controls="tabpanel_3">
        <label for="tab3">PHP & Mysql</label>
        <!-- Tab 4 -->
        <input type="radio" name="tabset" id="tab4" aria-controls="tabpanel_4">
        <label for="tab4">dev</label>

        <div class="tab-panels">
            <section id="tabpanel_1" class="tab-panel">
             <div class="sylab">
               <div v-for="sylab in html_filter" :key="sylab.id" class="sylab_info">
                 <router-link :to="{name: 'Course', params: {id:sylab.id } }" class="link">
                  <img v-bind:src="require('../../src/assets/' + sylab.img)" alt="">
                  <div class="sylab_item">
                    <h1>{{sylab.title}}</h1>
                    <p>{{sylab.expert}} | <span>Voir info</span> </p>
                    <div class="sylab_star">
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                    </div>
                    <div class="sylab_link">
                      <p>Frontend</p>
                    </div>
                  </div>
                 </router-link>
               </div>
             </div>
            </section>
            <section id="tabpanel_2" class="tab-panel">
              <div class="sylab">
               <div v-for="sylab in js_filter" :key="sylab.id" :sylab="sylab" class="sylab_info">
                  <router-link :to="{name: 'Course', params: {id:sylab.id } }" class="link">
                    <img v-bind:src="require('../../src/assets/' + sylab.img)" alt="">
                    <div class="sylab_item">
                    <h1>{{sylab.title}}</h1>
                    <p>{{sylab.expert}} | <span>Voir info</span> </p>
                    <div class="sylab_star">
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                    </div>
                    <div class="sylab_link">
                      <p>Backend</p>
                    </div>
                  </div>
                  </router-link>
               </div>
             </div>
            </section>
            <section id="tabpanel_3" class="tab-panel">
            <h2>6C. tabpanel_3 Bock</h2>
            </section>
            <section id="tabpanel_4" class="tab-panel">
            <h2>6C. phpk</h2>
            </section>
        </div>
    </div>
    <h1>Tous nos Syllabus</h1>
    <div class="all_sylab">
       <div class="sylab_all">
               <div v-for="sylab in db_sylab" :key="sylab.id" class="sylab_info">
                 <router-link :to="{name: 'Course', params: {id:sylab.id } }" class="link">
                  <img src="../../src/assets/Course.png" alt="">
                  <div class="sylab_item">
                    <h1>{{sylab.title}}</h1>
                    <p>Dr Youtube | <span>Voir info</span> </p>
                    <div class="sylab_star">
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                      <i class="las la-star"></i>
                    </div>
                    <div class="sylab_link">
                      <p>Web</p>
                    </div>
                  </div>
                 </router-link>
               </div>
        </div>
    </div>
    <div class="home_ctg">
        <h1><i class="las la-tags"></i> Nos Categories</h1>
        <div class="ctg_items">
            <div class="ctg_item">
             <img src="@/assets/frontend.png" alt="">
             <p>Frontend</p>
            </div>
            <div class="ctg_item">
             <img src="@/assets/backend.png" alt="">
             <p>Backend</p>
            </div>
            <div class="ctg_item">
             <img src="@/assets/design.png" alt="">
             <p>Design</p>
            </div>
            <div class="ctg_item">
             <img src="@/assets/data_science.png" alt="">
             <p>Data Sciences</p>
            </div>
            
        </div>
    </div>
  </div>
</template>
<script>
export default {
      props:{
        sylab: Object
    },
    created(){
           this.$store.dispatch('show_sylab')
                    .then(response =>{
                this.db_sylab = response.data
                console.log(response.data)
            })
            .catch(error =>{
                console.log('error', error.response)
            })
    },
    data(){
      return{
          sylabus: [
          {id:"0", title: "HTML et CSS : la formation ULTIME", img:"html_course_1.jpg", tags:"html", mark:"5", expert:"Dr Youtube " },
          {id:"1", title: "Apprendre à coder en HTML et CSS : Cours complet", img:"html_course_4.jpg", tags:"html", mark:"5", expert:"Dr Youtube " },
          {id:"2", title: "JavaScript : la formation ULTIME", img:"javascript_1.jpg", tags:"js", mark:"5", expert:"Dr Youtube " },
          {id:"3", title: "Apprendre à coder en JavaScript : Cours complet", img:"javascript_2.jpg", tags:"js", mark:"5", expert:"Dr Youtube " },
          {id:"4", title: "PHP & Mysql : la formation ULTIME", img:"php_1.jpg", tags:"php", mark:"5", expert:"Dr Youtube " },
        ],
        db_sylab:[],
        search:'frontend'
      }
    },
    computed:{
      html_filter(){
        return this.sylabus.filter((sylab) => {
          return sylab.tags.toLowerCase().includes('html')
        })
      },
      all(){
        return this.sylabus
      },
      js_filter(){
        return this.sylabus.filter((sylab) => {
          return sylab.tags.toLowerCase().includes('js')
        })
      }
    }
}
</script>
<style scoped>
.home_intro{
    color: rgb(32, 31, 31);
    margin-bottom: 30px;
}
.home_intro h1{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 30px;
}
.home_intro p{
    font-size: 19px;
}
/*
Tabs : debut
*/
.tabset > input[type="radio"] {
  position: absolute;
  left: -200vw;
}

.tabset .tab-panel {
  display: none;
}

.tabset > input:first-child:checked ~ .tab-panels > .tab-panel:first-child,
.tabset > input:nth-child(3):checked ~ .tab-panels > .tab-panel:nth-child(2),
.tabset > input:nth-child(5):checked ~ .tab-panels > .tab-panel:nth-child(3),
.tabset > input:nth-child(7):checked ~ .tab-panels > .tab-panel:nth-child(4),
.tabset > input:nth-child(9):checked ~ .tab-panels > .tab-panel:nth-child(5),
.tabset > input:nth-child(11):checked ~ .tab-panels > .tab-panel:nth-child(6) {
  display: block;
}

.tabset > label {
  position: relative;
  display: inline-block;
  padding: 12px 25px 20px;
  border-radius: 5px;
  font-size: 17px;
  border: 1px solid transparent;
  border-bottom: 0;
  cursor: pointer;
  font-weight: 300;
  color: rgb(26, 25, 25);
  text-transform: capitalize;

}

.tabset > label::after {
  content: "";
  position: absolute;
  left: 25px;
  bottom: 10px;
  width: 60%;
  height: 2.6px;
  background: #7a7a7a;
}

.tabset > label:hover,
.tabset > input:focus + label {
  color: #06c;
}

.tabset > label:hover::after,
.tabset > input:focus + label::after,
.tabset > input:checked + label::after {
  background: #06c;
}

.tabset > input:checked + label {
  border-color: #ccc;
  border-bottom: 1px solid #fff;
  margin-bottom: -1px;
}
.tab-panel {
  padding: 30px 0;
  border-top: 1px solid #ccc;
}
.tabset {
  width: 100%;
  font-family: Arial, Helvetica, sans-serif;
}
/* Tabs : fin */
.sylab{
    display: flex;  
}
.sylab_all{
display: flex;
flex-wrap: wrap;
overflow: hidden;
padding-bottom: 25px;
width: 100%;
}
.all_sylab{
  padding-bottom: 35px;padding-top: 25px;
}
.sylab_info{
    position: relative;
    cursor: pointer;
    width: 245px;
    background-color: white;
    /* border: .3px solid rgb(185, 182, 182); */
    border-radius: 5px;
    color: rgb(48, 47, 47);
    margin-left: 20px;margin-right: 20px;
    padding: 2px;
}
.sylab_info:hover{
    transform: scale(1.02);
    border: .3px solid rgb(117, 116, 116);
}
.sylab_info img{
    width: 100%;
    height: 135px;
}
.sylab_item{
 padding-left: 9px;padding-right: 9px;
}
.sylab_info h1{
    font-size: 15px;
}
.sylab_info p{
    font-size: 15px;
    color: rgb(87, 85, 85);
}
.sylab_star i{
    color:orangered
}
.sylab_link p{
    float: right;
    background-color: teal;
    color: white;
    margin-right: 10px;
    padding: 2.7px;
    border-radius: 2px;
}
.home_ctg{
    width: 100%;
    color: #363434;
    text-transform: uppercase;
    font-size: 15px;
}
.home_ctg h1{
  font-size: 20px;
}
.ctg_items{
    text-transform: capitalize;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    overflow: hidden;
}
.ctg_item{
  text-align: center;
    cursor: pointer;
    margin-right: 90px;margin-top: 35px;
}
.ctg_item:hover{
    transform: scale(1.1);
}
.ctg_item img{
    width: 200px;
}
</style>