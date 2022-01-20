<template>
  <div class="home">
    <Navbar></Navbar>
    <SlideOne></SlideOne>
     <Main></Main>
     <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
import Main from '@/components/Home_main.vue'
import Footer from '@/components/Footer.vue'
import SlideOne from '@/components/Carousel_1.vue'
export default {
  name: 'Home',
  components: {
    Navbar,
    SlideOne,
    Main,
    Footer
  }
}
</script>
