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
        <div class="form_sylab">
                    <h1>Ajouter Sylabus</h1>
            <form action="" @submit.prevent="save_sylab">
                <div class="sign-control">
                    <label for="sylab_name">Titre Sylabus</label>
                    <input type="text" id="sylab_name" v-model="sylab_title" placeholder="Entrer titre" />
                    <small>Error message</small>
                </div>
                    <p>Lecon 1</p>
                    <div class="sign-control">
                    <label for="lecon_name">Titre Lecon</label>
                    <input type="text" id="lecon_name" v-model="lecon_title1" placeholder="Entrer titre" />
                    <small>Error message</small>
                  </div>
                        <div class="sign-control">
                            <label for="video">Lien video</label>
                            <input type="text" name="video" v-model="lien1"  >
                            <small>Error message</small>
                        </div>
                    <p>Lecon 2</p>
                    <div class="sign-control">
                    <label for="lecon_name">Titre Lecon</label>
                    <input type="text" id="lecon_name" v-model="lecon_title2" placeholder="Entrer titre" />
                    <small>Error message</small>
                  </div>
                    <div class="sign-control">
                        <label for="video">Lien video</label>
                        <input type="text" name="video" v-model="lien2" >
                        <small>Error message</small>
                    </div>
                <button>Enregistrer</button>
            </form>
        </div>
    </div> 
</div>
</div>
</template>
<script>
export default {
     data () {
      return {
        expert_id:"martins",
        sylab_title:null,
        lien1:null,
        lecon_title1:null,
        lien2:null,
        lecon_title2:null,
      }
    },
    methods:{
        save_sylab(){
            this.$store.dispatch('add_sylab', {
                expert_id: this.expert_id,
                sylabus:{
                   title:this.sylab_title,
                   lessons:[
                       {
                           title:this.lecon_title1,
                           videos:[
                               {
                                   link:this.lien1,
                               }
                           ]
                       },
                       {
                           title:this.lecon_title2,
                           videos:[
                               {
                                   link:this.lien2,
                               }
                           ]
                       }
                   ]
                 }
            })
            .then( () =>{
              console.log('Reussi')
            })
        }
    }
}
</script>
<style scoped>
.form_sylab{
    margin-top: -70px;
    width: 80%;
}
.form_sylab .contains{
    width: 60%;
}
</style>