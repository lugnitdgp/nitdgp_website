<template>
  <header class="container-fluid">
    <!--Navbar-->
<nav class="navbar navbar-expand-lg primary-color fixed-top" style="background-color: #001333!important;padding: 0px;padding-right:0px;display:none;">

 <div class="container" style="margin: 0px;padding:0px!important;min-width: 100%">
  <div class="navbar-menu" style="margin-top: -50px;">
     <a class="nav-link dropdown-toggle" style="color:white;padding-left: 5px"
     data-toggle="dropdown">
      <i style="color: white" class="fa fa-2x fa-bars" ></i></a>
      <div class="dropdown-menu" style="background-color: #001333;">
          <a class="dropdown-item" href="/"><i class="fa fa-2x fa-home" ></i></a>
          <a class="dropdown-item" href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
          <a class="dropdown-item" href="http://nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb</a>
      </div>
  </div>
  <div class="row">
    <div class="col collapse navbar-collapse justify-content-center font-weight-bold" id="basicExampleNav" style="margin-left: -20px;min-width: 100%">
      <h4 style="margin:0;margin-bottom:0em;margin:0px;font-size: 150%;
      letter-spacing: 2px;
      font-family: 'Open Sans Condensed', sans-serif;
      font-weight: bold;
      color: white;text-align: center;">NATIONAL INSTITUTE OF TECHNOLOGY DURGAPUR</h4>
      <a class="navbar-brand" style="padding: 0px;margin:0px" :class="$route.path == '/'" href="/">
        <img class="navbar-brand" style="padding: 0px;margin:0px;" height="80" src="/static/img/nitdgp_logo_white.png">
      </a>
      <h4 style="margin:0;margin-bottom:0em;font-size: 200%;
      letter-spacing: 1px;
      color: white;
      text-align: center;">राष्ट्रीय प्रौद्योगिकी संस्थान, दुर्गापुर</h4>
    </div>
    <div class="col collapse navbar-collapse justify-content-center font-weight-bold" id="basicExampleNav" style="margin-left: 20px;min-width: 100%">
      <h6 style="margin:0;
      letter-spacing: 2px;
      color: white;
      text-align: center;">
      An Institute of National Importance under Government of India,<br>
      Ministry of Human Resource Development
      </h6>
    </div>
  </div>
  <div id="google_translate_element">
    <div id=":0.targetLanguage" class="goog-te-gadget-simple" style="white-space: nowrap;">
      <span style="vertical-align: middle;">
        <a aria-haspopup="true" class="goog-te-menu-value" href="javascript:void(0)"></a>
     </span>
    </div>
  </div>
 </div>
</nav>
<!--/.Navbar-->
      <!-- <div class="navbar-menu">
         <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-2x fa-bars" ></i></a>
          <div class="dropdown-menu" style="background-color: #001333">
              <a class="dropdown-item" href="/"><i class="fa fa-2x fa-home" ></i></a>
              <a class="dropdown-item" href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
              <a class="dropdown-item" href="http://nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb</a>
          </div>
      </div>
        <a href="/"><i class="fa fa-2x fa-home" ></i></a>
          <a :class="$route.path == '/'" href="/">
            <img class="navbar-brand" src="/static/img/nitdgp_logo_white.png">
          </a>
          <h4>NATIONAL &nbsp;INSTITUTE &nbsp;OF &nbsp;TECHNOLOGY &nbsp;DURGAPUR</h4>
          <h4>राष्ट्रीय प्रौद्योगिकी संस्थान, दुर्गापुर</h4>
            An Institute of National Importance under Government of India,<br>
            Ministry of Human Resource Development
            National Institute of Technology<br/>Durgapur</h6>
        <a href="http://nitdgp.ac.in"><i class="fa fa-1x fa-globe"></i> OldWeb </a>&nbsp;
        <a href="/contacts"><i class="fa fa-1x fa-phone"></i> Contacts</a>
        <div id="google_translate_element"></div> -->
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
  .dropdown-menu a{
    color:white!important;
  }
  .dropdown-menu a:hover{
    background-color: #001333;
  }
</style>
