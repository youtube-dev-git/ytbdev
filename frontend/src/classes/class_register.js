import control from '@/classes/class_control.js';
export default {
     data(){
       return{
        names:'',
<<<<<<< HEAD
=======
        pseudo:'',
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
        email:'',
        phone:'',
        img:'no_pic.img',
        sex:'',
        password:'',
        password2:'',
        statut:''
       }
     },
<<<<<<< HEAD
      validate(name,mail,phone,sex,password,password2){
        this.names=name,
=======
      validate(name,pseudo,mail,phone,sex,password,password2,statut){
        this.names=name,
        this.pseudo=pseudo,
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
        this.email=mail,
        this.phone=phone,
        this.sex=sex,
        this.password=password,
        this.password2=password2,
<<<<<<< HEAD

       console.log(this.names,this.email,this.phone,this.sex,this.password,this.password2)
       control.verification(this.names,this.email,this.phone,this.sex,this.password,this.password2)
=======
        this.statut=statut
       console.log(this.names,this.pseudo,this.email,this.phone,this.sex,this.password,this.password2,this.statut)
       control.verification(this.names,this.pseudo,this.email,this.phone,this.sex,this.password,this.password2,this.statut)
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
    },
  
}

