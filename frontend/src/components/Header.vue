<template>
  <header class="container-fluid">

    <nav class="mb-1 navbar fixed-top navbar-expand-sm" id="nav-below">
      <div class="navbar-menu">
         <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-2x fa-bars" ></i></a>
          <div class="dropdown-menu" style="background-color: #001333">
              <a class="dropdown-item" href="/"><i class="fa fa-2x fa-home" ></i></a>
              <a class="dropdown-item" href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
              <a class="dropdown-item" href="http://nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb</a>
          </div>
      </div>
      <div class="navbar-home">
        <a href="/"><i class="fa fa-2x fa-home" ></i></a>
      </div>
      <div class="navbar-header">
        <div id="brand-logo-block" align="center">
          <a :class="$route.path == '/'" href="/">
            <img class="navbar-brand" src="/static/img/nitdgp_logo_white.png">
            <img class="line-img" src="/static/img/line.png">
            <img class="navbar-img-small" src="/static/img/emblem.png">
          </a>
        </div>
        <div id="brand-name-block" class="navbar-text white-text" align="center">
          <h4>National &nbsp;Institute &nbsp;of &nbsp;Technology, &nbsp;Durgapur</h4>
          <h4>राष्ट्रीय प्रौद्योगिकी संस्थान, दुर्गापुर</h4>
          <p class="navbar-text-small">
            An Institute of National Importance under Government of India,<br>
            Ministry of Human Resource Development
          </p>
        </div>
        <div id="brand-name-block-small" class="navbar-text white-text" align="center">
          <p class="navbar-text-small">
            <h6 ali>National Institute of Technology<br/>Durgapur</h6>
          </p>
        </div>
        <img class="navbar-img-big"  src="/static/img/emblem.png">
      </div>
      <div class="navbar-list">
        <a href="http://nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb </a>&nbsp;
        <a href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
        <div id="google_translate_element"></div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      menu: false,
      windowWidth: 1000
    }
  },
  created () {
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  methods: {
    updateWidth () {
      this.windowWidth = document.body.clientWidth
    }
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .navbar .dropdown-item{
    color: white!important;
  }
  .navbar-menu {
    display: none;
    background-color: #001333;
  }
  .navbar-menu a{
    color: white!important;
  }
  .navbar-menu a:hover{
    background-color: #001c50!important;
  }
  .navbar-list {
    margin-bottom: -4%;font-size: 120%;
    background-color: #001333;
    color: white;
  }
  .navbar-home {
    margin-top: -3%;
    background-color: #001333;
    color: white;
  }
  .navbar a{
    color: white;
  }
  .navbar-header {
    margin: 0px auto;
    padding-left: 100px;
  }
  .navbar-text {
    vertical-align: middle;
    margin-top: -10px;
    margin-bottom: -1.8em;
  }
  .navbar-text h4 {
    margin-top: -5px;
    margin-bottom: 2px;
    font-size: 135%;
    line-height: 35px;
  }
  #top-nav-wrap{
    height: 2em;
    background-color: #ECEFF1;
    padding: 0px;
    padding-left: 5px;
  }
  .top-nav-container-left{
    width: 60%;
    text-align: left;
  }
  .top-nav-container-right{
    width: 40%;
    text-align: right;
  }
  .top-nav-link {
    color: #000000;
    padding-left: 10px;
    padding-right: 10px;
    height: 100%;
    max-height: 100%;
    display: inline-block;
    font-size: 100%;
  }
  .top-nav-link:hover {
    color: #459;
  }
  #nav-below {
    background-color: #001333;
    margin-bottom: -50px;
  }
  #search-btn-nav{
    height: 1.8em;
    padding: 0px;
    padding-left: 2px;
    padding-right: 2px;
    border-radius: 4px;
    background-color: #ffffff;
    width: 100%;
  }
  #navbarSupportedContent-4{
    padding-top: 6em;margin-top: -2em;
  }
  .navbar-brand {
    height: 130px;
    margin-top: -20px;
    margin-bottom: -20px;
    margin-right: -10px;
  }
  .navbar-img-big{
    padding-left: 5px;
    height: 100px;
  }
  .navbar-img-small{
    height: 0px;
  }
  #brand-logo-block, #brand-name-block {
    display: inline-block;
  }
  #brand-name-block h4{
    font-size: 160%;
    letter-spacing: 4px;
    font-weight: bold;
  }
  .navbar-text-small{
    letter-spacing: 2px;
    font-weight: bold;
  }
  @media screen and (max-width: 540px) {
    .navbar-menu {
      margin-left: -2%;
      margin-top: -8%!important;
    }
    #brand-logo-block {
      display: block;
      padding: 0px;
      margin: 0 auto;
      margin-top: 10px;
    }
    #brand-name-block {
      display: none;
      padding: 0px;
      margin: 0 auto;
      margin-bottom: -40px;
      margin-top: 15px;
    }
    .navbar #brand-name-block-small{
      display: block;
      padding-top: 0px;
      padding-bottom: 0px;
    }
    #nav-below {
      padding-top: 0px;
      padding-bottom: 0px;
    }
  }
  @media screen and (max-width: 1010px) {
    .navbar-brand {
      height: 70px;
      margin-right: 16px;
    }
    .navbar-img-small {
      height: 50px;
      margin-left: 3px;
    }
    .navbar-img-big {
      height: 0px;
    }
  }
  .navbar-text-small {
    font-size: 90%;
  }
  #brand-name-block-small{
    display: none;
  }
  @media screen and (max-width: 1200px) {
    .navbar-header {
      padding-left: 0px!important;
    }
    .navbar-list {
      display: none;
    }
    .navbar-home {
      display: none;
    }
    .navbar-menu {
      margin-left: -2%;
      margin-top: -3%;
      display: block;
    }
  }
</style>
