import control from '@/classes/class_control.js';
export default {
     data(){
       return{
        names:'',
        email:'',
        phone:'',
        img:'no_pic.img',
        sex:'',
        password:'',
        password2:'',
        statut:''
       }
     },
      validate(name,mail,phone,sex,password,password2){
        this.names=name,
        this.email=mail,
        this.phone=phone,
        this.sex=sex,
        this.password=password,
        this.password2=password2,

      //  console.log(this.names,this.email,this.phone,this.sex,this.password,this.password2)
       control.verification(this.names,this.email,this.phone,this.sex,this.password,this.password2)
    },
  
}

