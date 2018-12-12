<template>
  <header class="container-fluid">
    <nav class="navbar navbar-expand-lg primary-color fixed-top">
      <div class="hm-btn">
        <a href="/home"><i class="fa fa-2x fa-home" ></i> Home</a>&nbsp;&nbsp;
        <a href="/chanakya"><i class="fa fa-1x fa-tv"></i> Chanakya&nbsp;</a>
      </div>
      <div class="navbar-menu">
        <a class="nav-link dropdown-toggle" style="color:white;padding-left: 5px"
         data-toggle="dropdown">
          <i style="color: white" class="fa fa-2x fa-bars" ></i>
        </a>
        <div class="dropdown-menu" style="background-color: #001333;">
          <a class="dropdown-item" href="/home"><i class="fa fa-2x fa-home" ></i> Home</a>          
          <a class="dropdown-item" href="/home"><i class="fa fa-1x fa-tv" ></i> Chanakya</a>          
          <a class="dropdown-item" href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
          <!-- <a class="dropdown-item" href="/quicklinks"><i class="fa fa-1x fa-plus"></i> Quick Links</a> -->
          <a class="dropdown-item" href="https://old.nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb</a>
          <a class="dropdown-item" href="https://mail.google.com/a/nitdgp.ac.in"><i class="fa fa-1x fa-envelope"></i> Mail</a>
        </div>
      </div>
      <div class="navbar-content-cen container">
        <div class="row nav-logo">
          <div class="col-1">
            <a class="navbar-brand" :class="$route.path == '/'" href="/home">
              <img alt="NIT Durgapur Logo" class="navbar-brand" height="80" src="/static/img/nitdgp_logo_white.png"><span class="nm-en-smm" style="color: white;font-weight: bold;visibility: hidden">NIT DURGAPUR</span>
            </a>
          </div>
          <div class="col-11">
            <div class="text-cont">
              <div class="row">
                <p>
                  <span class="nm-en-sm notranslate">
                    &nbsp;&nbsp;&nbsp;NATIONAL INSTITUTE OF TECHNOLOGY DURGAPUR
                  </span>
                  <span class="nm-hi">
                    राष्ट्रीय प्रौद्योगिकी संस्थान, दुर्गापुर
                    &nbsp;|&nbsp;
                  </span>
                  <span class="nm-en notranslate">
                    NATIONAL INSTITUTE OF TECHNOLOGY DURGAPUR<br>
                  </span>
                  <span class="nm-det" style="font-size: 13px;">
                    An Institute of National Importance under Government of India,
                    Ministry of Human Resource Development
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="lang-tr" style="display:none;">
        <div id="google_translate_element">
          <div id=":0.targetLanguage" class="goog-te-gadget-simple">
            <h5>अ|A</h5>
            <!-- <div class="goog-te-banner">
            <a id=":2.close" class="goog-close-link" href="javascript:void(0)" title="Close"><img alt="NIT Durgapur Logo" src="https://www.google.com/images/cleardot.gif" width="15" height="15" alt="Close" style="background-image:url(https://translate.googleapis.com/translate_static/img/te_ctrl3.gif);background-position:-28px 0px"></a>
            </div> -->
          </div>
        </div>
      </div>
      <div class="nav-_links">
        <a href="https://mail.google.com/a/nitdgp.ac.in"><i class="fa fa-1x fa-envelope"></i> Mail&nbsp;</a>
        <a href="/contacts"><i class="fa fa-1x fa-phone"></i> Contact&nbsp;</a>
        <a href="https://old.nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> Old&nbsp;</a>
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
  @import url('https://fonts.googleapis.com/css?family=Kosugi|Open+Sans+Condensed:300|PT+Sans');
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
  }
  @media screen and (max-width: 530px){
    .nm-en-sm{
      display: none!important;
    }
    .nm-en-smm{
      visibility: visible!important;
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
  .navbar .navbar-content-cen{
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
  .lang-tr #google_translate_element{
    margin: auto;
  }
  .lang-tr #google_translate_element .goog-te-gadget-simple{
    background-color: #001333;border: none;white-space:nowrap;
  }
  .lang-tr #google_translate_element .goog-te-gadget-simple h5{
    text-decoration: underline;margin: 0;font-weight: normal;color:white;padding-left: 2px;padding-right: 2px
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
</style>
