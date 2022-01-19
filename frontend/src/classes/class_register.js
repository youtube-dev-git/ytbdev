import control from '@/classes/class_control.js';
export default {
     data(){
       return{
        names:'',
        pseudo:'',
        email:'',
        phone:'',
        img:'no_pic.img',
        sex:'',
        password:'',
        password2:'',
        statut:''
       }
     },
      validate(name,pseudo,mail,phone,sex,password,password2,statut){
        this.names=name,
        this.pseudo=pseudo,
        this.email=mail,
        this.phone=phone,
        this.sex=sex,
        this.password=password,
        this.password2=password2,
        this.statut=statut
       console.log(this.names,this.pseudo,this.email,this.phone,this.sex,this.password,this.password2,this.statut)
       control.verification(this.names,this.pseudo,this.email,this.phone,this.sex,this.password,this.password2,this.statut)
    },
  
}

