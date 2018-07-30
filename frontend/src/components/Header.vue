<template>
  <header class="container-fluid">
    <nav class="navbar navbar-expand-lg navbar-dark darken-2" id="nav-below">
      <div class="container-fluid" >
        <div class="navbar-header">
          <a :class="$route.path == '/' ? 'disabled' : ''" href="/">
            <img class="navbar-brand" src="/static/img/nitdgp_logo_white.png">
          </a>
          <img class="line-img" src="/static/img/line.png">
          <img class="navbar-img-small" src="/static/img/emblem.png">
          <div class="navbar-text white-text">
            <div align="left">
              <h6>National Institute of Technology Durgapur</h6>
              <h6> राष्ट्रीय प्रौद्योगिकी संस्थान दुर्गापुर </h6>
              <p class="navbar-text-small">(An Institute of National Importance under Government of India,<br> Ministry of Human Resource Development)</p>
            </div>
          </div>
          <img class="navbar-img-big"  src="/static/img/emblem.png">
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-4" aria-controls="navbarSupportedContent-4" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon" style="margin-left: -10px;"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent-4">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link waves-effect waves-light navbar-link" href="http://nitdgp.ac.in/alumni/index.php"><i class="fa fa-plane"></i>Alumni</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-effect waves-light navbar-link" href="https://mail.google.com/a/nitdgp.ac.in"><i class="fa fa-tasks"></i>Webmail</a>
            </li>
            <li class="nav-item">
              <a class="nav-link waves-effect waves-light navbar-link" href="/contacts"><i class="fa fa-address-book"></i>Contacts</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <nav class="mb-1 navbar fixed-top navbar-expand-sm" id="top-nav-wrap">
      <span class="top-nav-container-left">
        <a v-if="$route.path != '/'" href="/" class="black-text">
          <i class="fa fa-home fa-lg fa-2x" aria-hidden="true"></i>
        </a>
      </span>
      <span class="top-nav-container-right">
        <input id="search-btn-nav" type="text" name="" placeholder=" Search">
        <a href="http://nitdgp.ac.in" class="top-nav-link">Old website</a>
      </span>
    </nav>
  </header>
</template>

<script>
 export default {
     name: 'Header',
     data () {
         return {
             msg: 'Welcome to Your Vue.js App'
         }
     }
 }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #navbar-link {
    font-size: 90%;
  }
  .navbar-header{
    margin-top: 1.7em;
  }
  .navbar-text {
    text-align: center;vertical-align: middle;line-height: 18px;margin-left: -25px;margin-top: -2px;margin-bottom: -1.8em;
  }
  #top-nav-wrap{
    height: 2em;
    background-color: #ECEFF1;
    padding: 0px;
    padding-left: 5px;
  }
  .top-nav-container-left{
    width: 10%;
    text-align: left;
  }
  .top-nav-container-right{
    width: 90%;
    text-align: right;
  }
  .top-nav-link{
    color: #000000;
    padding-left: 10px;
    font-size: 90%;
  }
  .top-nav-link:not(:nth-child(4))::after {
    padding: 0 0.2em;
    content: '>';
  }

  .top-nav-link:nth-child(4) {
    padding-right: 0.5em;
  }
  #nav-below{
    background-color: #001333;
  }
  #search-btn-nav{
    height: 1.8em;
    padding: 0px;
    padding-left: 2px;
    padding-right: 2px;
    border-radius: 4px;
    background-color: #ffffff;
    width: 30%;
  }
  #navbarSupportedContent-4{
    padding-top: 6em;margin-top: -2em;
  }
  .navbar-brand {
    height: 90px;margin-top: -20px;margin-bottom: -20px;
  }
  .navbar-img-big{
    padding-left: 5px;height: 70px;
  }
  .navbar-img-small{
    height: 0px;
  }
  .navbar-text-small{
    font-size: 65%;
  }
</style>
