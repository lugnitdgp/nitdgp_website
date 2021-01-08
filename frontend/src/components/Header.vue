<template>
  <header class="container-fluid">
    <nav class="navbar navbar-expand-lg primary-color fixed-top">
      <div class="hm-btn">
        <a href="/home"><i class="fa fa-2x fa-home" ></i> Home</a>&nbsp;&nbsp;
        <a href="/nirf"></i> NIRF</a>&nbsp;&nbsp;
        <a href="/chanakya"><i class="fa fa-1x fa-tv"></i> Chanakya&nbsp;</a>
        <a href="/live-convocation-16"> <span style="color: red;font-weight: bold;">16th Convocation Live&nbsp;</span></a>
      </div>
      <div class="navbar-menu">
        <a class="nav-link dropdown-toggle" style="color:white;padding-left: 5px"
         data-toggle="dropdown">
          <i style="color: white" class="fa fa-2x fa-bars" ></i>
        </a>
        <div class="dropdown-menu" style="background-color: #001333;">
          <a class="dropdown-item" href="/home"><i class="fa fa-2x fa-home" ></i> Home</a>
          <a class="dropdown-item" href="/nirf"><i class="fa fa-1x fa-newspaper-o" ></i> NIRF</a>
          <a class="dropdown-item" href="/chanakya"><i class="fa fa-1x fa-tv" ></i> Chanakya</a>
          <a href="/live-convocation-16"> <span style="color: red;font-weight: bold;">16th  Convocation Live&nbsp;</span></a>
          <a class="dropdown-item" href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
          <!-- <a class="dropdown-item" href="/quicklinks"><i class="fa fa-1x fa-plus"></i> Quick Links</a> -->
          <a class="dropdown-item" href="https://old.nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb</a>
          <a class="dropdown-item" href="https://mail.google.com/a/nitdgp.ac.in"><i class="fa fa-1x fa-envelope"></i> Mail</a>
        </div>
      </div>
      <div class="navbar-content-cen container pb-sm-4">
        <div class="row nav-logo">
          <div class="col-1" v-bind:class="{ hide_logo: hideLogo }">
            <a class="navbar-brand" :class="$route.path == '/'" href="/home">
              <img alt="NIT Durgapur Logo" class="navbar-brand" height="80" src="/static/img/nitdgp_logo_white.png"><span class="nm-en-smm" style="color: white;font-weight: bold;visibility: hidden">NIT DURGAPUR</span>
            </a>
          </div>
          <div class="col-11">
            <div class="text-cont">
              <div class="row">
                <p>
                  <span class="nm-en-sm">
                    &nbsp;&nbsp;&nbsp;NATIONAL INSTITUTE OF TECHNOLOGY DURGAPUR
                  </span>
                  <span class="nm-hi">
                    राष्ट्रीय प्रौद्योगिकी संस्थान, दुर्गापुर
                    &nbsp;|&nbsp;
                  </span>
                  <span class="nm-en">
                    NATIONAL INSTITUTE OF TECHNOLOGY DURGAPUR<br>
                  </span>
                  <span class="nm-det" style="font-size: 13px;">
                    An Institute of National Importance under Ministry of Education, Government of India
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="row position-absolute d-inline d-sm-none w-100">
          <div class="col-12">
            <div class="searchbar searchbar_mobile mr-1 float-right" @mouseover="hideLogo = true" @mouseleave="hideLogo = false">
              <input class="search_input" name="" placeholder="Search..." type="search" v-model="query" v-on:keyup.13="search()">
              <span class="search_icon"><i class="fa fa-search" aria-hidden="true"></i></span>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-_links">
        <div class="searchbar mr-1 p-1">
          <input class="search_input" name="" placeholder="Search..."   type="search" v-model="query" v-on:keyup.enter="search()">
          <span class="search_icon"><i class="fa fa-search" aria-hidden="true" v-on:click="search()"></i></span>
        </div>
        <a href="https://mail.google.com/a/nitdgp.ac.in"><i class="fa fa-1x fa-envelope"></i> Mail&nbsp;</a>
        <a href="/contacts"><i class="fa fa-1x fa-phone"></i> Contact&nbsp;</a>
        <a href="https://old.nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> Old&nbsp;</a>
      </div>
    </nav>
    <div class="live-news-section">
        <marquee behavior="scroll" direction="left" onmouseover="this.stop();" onmouseout="this.start();">
            <a href="https://nitdgp.ac.in/AllPDF/d_msg/Director_Sir.mp4" target="_blank">Video Message from Director Sir</a>&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://nitdgp.ac.in/videos/Help_file_for_attending_online_classes.mp4" target="_blank">Help File for Attending Online Classes</a>&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://admin.nitdgp.ac.in/files/newsfeed/2020/12/02/PPT_from_SW_2.pdf" target="_blank">PPT presentation for first year students from the office of student welfare</a>&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://nitdgp.ac.in/AllPDF/d_msg/To_the_Students.mp4" target="_blank">Director's Message for the students</a>&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://admin.nitdgp.ac.in/files/newsfeed/2020/04/15/PRANESH_NITDGP_website2.pdf" target="_blank">NIT Durgapur has developed an indigenous automated AMBU bag system, that can serve as a quick and temporary substitute for ventilators in emergency situations. AMBU stands for Artificial Manual Breathing Unit. The present system is automated and can be tuned for oxygen requirements. The system has been christened "Pranesh</a>
        </marquee>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      menu: false,
      windowWidth: 1000,
      query: '',
      hideLogo:false,
    }
  },
  created () {
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  methods: {
    updateWidth () {
      this.windowWidth = document.body.clientWidth
    },
    search() {
      this.$router.push({ path: '/search', query: { q: this.query } })
    }
  },
  watch: {
    '$route' (to, from) {
      if(from.query.q && to.query.q){
        this.$router.go()
      }
    }
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Kosugi|Open+Sans+Condensed:300|PT+Sans');
  header {
    padding-bottom: 1%;
  }
  @media screen and (max-width: 1200px)  {
    .nm-det{
      display: none
    }
    .text-cont{
      font-size: 80%
    }
    
  }
  @media screen and (max-width: 800px){
    .navbar-menu{
      display: block!important
    }
    .hm-btn{
      display: none
    }
    .nav-_links{
      display: none!important
    }
    .navbar-brand{
      height: 50px;
    }
    .text-cont .nm-hi{
      display: none
    }
  }
  @media screen and (max-width: 540px){
    .nm-en{
      display: none;
    }
    .nm-en-sm{
      display: block!important
    }
    .live-news-section{
      top: 50px;
    }
  }
  @media screen and (max-width: 530px){
    .nm-en-sm{
      display: none!important;
    }
    .nm-en-smm{
      visibility: visible!important;
    }
    .live-news-section{      
      top: 50px;
      color: #fff;
    }

  }
  .navbar{
    background-color: #001333!important;padding: 0px;padding-right:0px;
  }
  .navbar-menu{
    display: none;
    position: absolute;top: 0;
  }
  .navbar .hm-btn{
    position: absolute;bottom: 0;
  }
  .navbar .hm-btn i{
    color: white
  }
  .navbar .hm-btn a{
    color: white
  }
  .navbar-content-cen{
    z-index: -1000;
    text-align: center;
  }
  .navbar .nav-logo{
    text-align: center;margin: 0 auto;
  }
  .nav-logo .navbar-brand{
    padding: 0px;margin:0px;
  }
  .nav-logo .col-11 {
    margin: auto;
    padding: 0px;
  }
  .col-1 {
    padding: 0px;
  }
  .nav-logo .col-11 .text-cont{
    height: 100%;margin: 0 auto
  }
  .nav-logo .text-cont p{
    color: white;text-align: center;margin: 0;
  }
  .text-cont .nm-en{
    font-size: 150%;
    letter-spacing: 2px;
    font-family: 'Open Sans Condensed', sans-serif;
    font-weight: bold;
  }
  .text-cont .nm-en-sm{
    font-size: 100%;
    letter-spacing: 2px;
    font-family: 'Open Sans Condensed', sans-serif;
    font-weight: bold;
    display: none;
  }
  .text-cont .nm-en-sm2{
    font-size: 100%;
    letter-spacing: 2px;
    font-family: 'Open Sans Condensed', sans-serif;
    font-weight: bold;
    display: none;
  }
  .text-cont .nm-hi{
    font-size: 180%;
  }
  .text-cont .nm-det{
    text-align: center;
  }
  .lang-tr{
    position: absolute;top: 0;right: 0
  }
  .nav-_links{
    position: absolute;bottom: 0;right: 0;font-size: 120%
  }
  .nav-_links a{
    color: white!important;
  }
  .dropdown-menu .dropdown-item{
    color:white!important;
  }
  .dropdown-menu a:hover{
    color: white!important;
    background-color: #001388!important;
  }
  .searchbar{
    display: inline;
    border-radius: 30px;
  }
  .search_input{
    color:  #001333;
    border:none !important;
    outline: 0 !important;
    -webkit-box-shadow:none !important;
    box-shadow:none !important;
    background: none;
    width: 0 ;
    caret-color:transparent;
    font-size: 0.9rem;
    font-weight: 300 !important;
    margin-bottom:0;
    transition:  width 0.4s linear;
    -webkit-transition: width 0.4s linear;
  }
  .searchbar:hover{
    background:white;
  }
  .searchbar:hover > .search_input{
    padding: 0 10px;
    width: 150px;
    caret-color: #001333;
    transition: width 0.4s linear;
    outline:none !important;
    border:none !important;
  }
  @media screen and (max-width: 540px)
  {
    .searchbar:hover > .search_input{
      padding: 0 10px;
      width: 200px;
      caret-color: #001333;
      transition: width 0.4s linear;
      outline:none !important;
      border:none !important;
    }
  }
  .searchbar:hover > .search_icon{
    color:  #001333 !important;
  }
  .search_icon{
    display: inline;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    color:white;
    background: transparent;
    padding:0 2px;
    cursor: pointer;
  }
  .hide_logo{
    opacity: 0;
    transition: opacity 0.3s linear;
  }
  .live-news-section{
    position: relative;
    height: 60px;
    background-color: #ca2367;
    top: 90px;
    color: #fff;
    font-weight: bold;
    font-size: 22px;
    margin: 0 auto;
    text-align: center;
    padding-top: 14px;
  }
  .live-news-section a{
    color: #fff;
    text-decoration: none;
  }
</style>
