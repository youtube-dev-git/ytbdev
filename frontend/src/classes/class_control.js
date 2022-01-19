
export default {

      verification(name,pseudo,email,phone,sex,password,password2){
          if(!name){
            document.getElementById("name").style.borderColor ="red"
          }else{
            document.getElementById("name").style.borderColor ="#2ecc71"
          }
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
          if(password != password2){
            document.getElementById("sign_password").style.borderColor ="red"
            document.getElementById("sign_password2").style.borderColor ="red"
          }else{
            document.getElementById("sign_password").style.borderColor ="#2ecc71"
            document.getElementById("sign_password2").style.borderColor ="#2ecc71"
          }
          

      }
}

