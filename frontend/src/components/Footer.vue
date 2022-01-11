<template>
    <div>
    <section class="blog_footer">
       <div class="blog_end-contain">
          <div class="blog_ends">
            <div class="blog-end-info">
              <h1><i class="lab la-youtube"></i> YOUTUBE<span> Dev</span></h1>
              <div class="blog-reseau">
                <i class="lab la-facebook-f"></i>
                <i class="lab la-github"></i>
                <i class="lab la-whatsapp"></i>
                <i class="lab la-google-plus-g"></i>
              </div>
              <p>copyright@2021 All right reserved this site made by <span>TP_INF3055</span></p>
            </div>
          </div>
       </div>
     </section>
    </div>
</template>
<style scoped>
/* footer */
.blog_footer{
    margin-top: 20px;
    width: 100%;
}
.blog_end-contain{
    width: 100%;
    display: flex;
    background-color: rgb(31, 31, 31);
    justify-content: center;
}
.blog-end-info{
    text-align: center;
    align-items: center;
    justify-content: center;
    margin-top: 15px;
}

.blog_ends{
    text-align: center;
    justify-content: center;
}
.blog-end-info h1{
    text-align: center;
    font-size: 28px;
    font-family: Arial, Helvetica, sans-serif;
    text-transform: uppercase;
    color: whitesmoke;
}
.blog-end-info small{
    text-align: center;
    font-size: 15px;
    letter-spacing: .8px;
    color: whitesmoke;
    margin-top: 13px;
    font-family: Arial, Helvetica, sans-serif;
}
.blog-end-info p{
    text-align: center;
    font-size: 12px;
    letter-spacing: .8px;
    color: whitesmoke;
    margin-top: 13px;
    font-family: Arial, Helvetica, sans-serif;
}
.blog-reseau i{
    /* display: flex; */
    margin-left: 17px;
    margin-top: 15px;
    font-size: 20px;
    color: rgb(196, 192, 192);
}
.blog-end-info span{
    font-size: 20px;
    font-weight: 500;
}
</style>