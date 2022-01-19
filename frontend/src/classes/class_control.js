
export default {

      verification(name,pseudo,email,phone,sex,password,password2){
          if(!name){
            document.getElementById("name").style.borderColor ="red"
          }else{
            document.getElementById("name").style.borderColor ="#2ecc71"
          }
<<<<<<< HEAD
=======
          if(!pseudo){
            document.getElementById("pseudo").style.borderColor ="red"
          }else{
            document.getElementById("pseudo").style.borderColor ="#2ecc71"
          }
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
          if(!email){
            document.getElementById("mail").style.borderColor ="red"
          }else{
            document.getElementById("mail").style.borderColor ="#2ecc71"
          }
          if(!phone){
            document.getElementById("phone").style.borderColor ="red"
          }else{
            document.getElementById("phone").style.borderColor ="#2ecc71"
          }
          if(!sex){
            document.getElementById("sex").style.borderColor ="red"
          }else{
            document.getElementById("sex").style.borderColor ="#2ecc71"
          }
          if(!password){
            document.getElementById("sign_password").style.borderColor ="red"
          }else{
            document.getElementById("sign_password").style.borderColor ="#2ecc71"
          }
          if(!password2){
            document.getElementById("sign_password2").style.borderColor ="red"
          }else{
            document.getElementById("sign_password2").style.borderColor ="#2ecc71"
          }
<<<<<<< HEAD
          if(password != password2){
=======
          if(password !=password2){
>>>>>>> e7b8036f20a8054b30f93c4be35a1cba4217e434
            document.getElementById("sign_password").style.borderColor ="red"
            document.getElementById("sign_password2").style.borderColor ="red"
          }else{
            document.getElementById("sign_password").style.borderColor ="#2ecc71"
            document.getElementById("sign_password2").style.borderColor ="#2ecc71"
          }
          

      }
}

