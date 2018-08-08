<template>
  <header class="container-fluid">
    <nav class="navbar navbar-expand-lg container-fluid navbar-dark darken-2" id="nav-below">
      <div class="navbar-header">
        <div id="brand-logo-block">
          <a :class="$route.path == '/' ? 'disabled' : ''" href="/">
            <img class="navbar-brand" src="/static/img/nitdgp_logo_white.png">
          </a>
          <img class="line-img" src="/static/img/line.png">
          <img class="navbar-img-small" src="/static/img/emblem.png">
        </div>
        <div id="brand-name-block" class="navbar-text white-text" align="center">
          <h4>National Institute of Technology, Durgapur</h4>
          <h4>राष्ट्रीय प्रौद्योगिकी संस्थान, दुर्गापुर</h4>
          <p class="navbar-text-small">
            An Institute of National Importance under Government of India,<br>
            Ministry of Human Resource Development
          </p>
        </div>
        <img class="navbar-img-big"  src="/static/img/emblem.png">
      </div>
    </nav>
    <nav class="mb-1 navbar fixed-top navbar-expand-sm" id="top-nav-wrap">
      <span class="top-nav-container-left">
        <a v-if="$route.path != '/'" href="/" class="top-nav-link">
          <i class="fa fa-home fa-lg fa-2x" aria-hidden="true"></i>
        </a>
        <div v-if="windowWidth < 720" style="display:inline-block">
          <a @click="menu = !menu" class="top-nav-link"><i class="fa fa-bars fa-lg fa-2x"></i></a>
        </div>
        <div v-show="windowWidth >= 720 || menu"
          :class="windowWidth >= 720 && !menu ? 'div-inline-block' : 'menu-div'">
          <a v-show="menu" class="red white-text" @click="menu = !menu" href="javascript:void(0)">
            Close dialog
          </a><hr v-show="menu">
          <a class="top-nav-link" href="http://nitdgp.ac.in/alumni/index.php">
            Alumni
          </a><hr v-show="menu">
          <a class="top-nav-link" href="https://mail.google.com/a/nitdgp.ac.in">
            Webmail
          </a><hr v-show="menu">
          <a class="top-nav-link" href="/contacts">
            Contacts
          </a><hr v-show="menu">
          <a class="top-nav-link" href="http://nitdgp.ac.in">
            Old website
          </a><hr v-show="menu">
          <a v-show="menu" class="top-nav-link" href="/notices">
            Notices
          </a>
        </div>
        <div v-show="menu" id="fade" class="black_overlay"></div>
      </span>
      <span class="top-nav-container-right">
        <input id="search-btn-nav" type="text" name="" placeholder=" Search">
      </span>
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
    if (window.localStorage["header"] !== undefined)
      this.header = window.localStorage.getItem("header") == "true"
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  methods: {
    toggleHeader() {
      this.header = !this.header
      window.localStorage.setItem("header", this.header)
    },
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
  .navbar-header {
    padding-top: 20px;
    margin: 10px auto;
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
    height: 90px;
    margin-top: -20px;
    margin-bottom: -20px;
    margin-right: -10px;
  }
  .navbar-img-big{
    padding-left: 5px;
    height: 70px;
  }
  .navbar-img-small{
    height: 0px;
  }
  #brand-logo-block, #brand-name-block {
    display: inline-block;
  }
  @media screen and (max-width: 540px) {
    #brand-logo-block {
      display: block;
      padding: 0px;
      margin: 0 auto;
      margin-top: 10px;
    }
    #brand-name-block {
      display: block;
      padding: 0px;
      margin: 0 auto;
      margin-bottom: -40px;
      margin-top: 15px;
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
  .menu-div {
    position: absolute;
    left: 10%;
    width: 80%;
    background-color: white;
    z-index: 2;
    overflow: auto;
  }
  .black_overlay {
    position: absolute;
    top: 0%;
    left: 0%;
    bottom: 0%;
    width: 100%;
    height: 2000%;
    z-index: 1;
    background-color: black;
    -moz-opacity: 0.8;
    opacity: .80;
    filter: alpha(opacity=80);
  }
  .menu-div a {
    color: blue;
    text-decoration: none;
    display: block;
    width: 100%;
    text-align: center;
    padding-top: 7px;
    padding-bottom: 7px;
  }
  .menu-div hr {
    width: 95%;
    color: #aaa;
    padding: 0px;
    margin: 0 auto;
  }
</style>
