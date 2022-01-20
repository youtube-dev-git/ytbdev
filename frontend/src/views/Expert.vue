<template>
<div class="expert">
    <div class="exp_nav">
        <h1>Youtube Dev</h1> 
        <ul>
            <li>expert_name</li>
            <li>expert_statut</li>
            <li>deconnecter</li>
        </ul>
    </div>
<div class="contains">
    <div class="sidebar">
        <div class="sub_menu">
                  <ul class="side_menu">
                      <li><h1>Menu</h1></li>
                       <li class="menu_items"><p><i class="las la-angle-right"></i>  Sylabus</p> 
                                <ul>
                                    <li class="menu_item"><i class="las la-arrow-right"></i>   Ajouter Sylabus</li>
                                    <li class="menu_item"><i class="las la-arrow-right"></i>   Tous les sylabus</li>
                                </ul>
                        </li>
                        <li class="menu_items"><p><i class="las la-edit"></i>  Modifier Sylabus</p></li>
                        <li class="menu_items"><p><i class="las la-angle-right"></i>  Expert</p> 
                           <ul>
                                <li class="menu_item"><i class="las la-arrow-right"></i>   Voir Info</li>
                                <li class="menu_item"><i class="las la-arrow-right"></i>   Voir Statut</li>
                           </ul>
                        </li>
                        <li class="menu_items"><p><i class="las la-sign-out-alt"></i> Deconnexion</p></li>
                  </ul>
        </div>
    </div>
    <div class="exp_page">
      <div class="exp_home">
          <div class="home_submenu">
              <div class="sub_home">
                  <i class="las la-award"></i>
                  <div class="sub_txt">
                      <h1>Sylabus</h1>
                      <p>00</p>
                  </div>
              </div>
              <div class="sub_home">
                  <i class="las la-book-open"></i>
                  <div class="sub_txt">
                      <h1>Lecon</h1>
                      <p>00</p>
                  </div>
              </div>
              <div class="sub_home">
                  <i class="las la-play-circle"></i>
                  <div class="sub_txt">
                      <h1>Video</h1>
                      <p>00</p>
                  </div>
              </div>
          </div>
          <div class="home_graph">

          </div>
      </div>
    </div>
</div>
</div>

</template>

<script>


export default {
  components: {

  }
}
</script>

<style lang="scss">
.expert{
    position: relative;
}
.exp_nav{
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    margin-top: -5px;margin-bottom: 2px;
    width: 100%;
    color: white;
    height: 55px;
background-color: rgb(53, 54, 54);
   padding: 8px;
   display: flex;
   justify-content: space-between;
}
.exp_nav ul{
    display: flex;
}
.exp_nav ul li{
    list-style: none;
    margin-right: 25px;
    font-size: 20px;
    cursor: pointer;
    color: whitesmoke;
}
.contains{
    display: flex;
    justify-content: space-between;
}
.sidebar{
    width: 20%;
    height: 100vh;
    background-color: rgb(53, 54, 54);
}

.menu_items{
    margin-bottom: 35px;
}

.sub_menu ul{
    color: whitesmoke;
}
.sub_menu ul li{
    margin-top: 15px;
    list-style: none;
    font-size: 20px;
}

.exp_page{
    width: 75%;
    position: absolute;
    top: 140px;left: 25%;
}
.sub_home{
    background-color: rgb(230, 223, 223);
    width: 29%;
    padding-left: 20px;padding-right: 20px;
    margin-right: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.sub_home h1{
    font-size: 23px;
    color: rgb(38, 38, 39);
}
.sub_home p{
    font-size: 20px;
}
.sub_home i{
    font-size: 85px;
}
.sub_txt{
    display: flex;
    flex-direction: column;
    text-align: center;
}
.home_submenu{
    display: flex;
    justify-content: center;
}
.home_graph{
    display: flex;
    justify-content: center;
    margin-top: 85px;
}
.graph_H{
    background-color: rgb(62, 63, 65);
    width: 55%;
    margin-right: 20%;
}
.graph_H h1{
    font-size: 22px;
}
.menu_item{
    font-size: 17px !important;
    color: rgb(190, 185, 185);
}
</style>




