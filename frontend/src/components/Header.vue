<template>
  <header class="container-fluid">
    <nav v-show="header" class="navbar navbar-expand-lg container-fluid navbar-dark darken-2" id="nav-below">
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
            <p class="navbar-text-small">
              An Institute of National Importance under Government of India,<br>
              Ministry of Human Resource Development
            </p>
          </div>
        </div>
        <img class="navbar-img-big"  src="/static/img/emblem.png">
      </div>
    </nav>
    <nav class="mb-1 navbar fixed-top navbar-expand-sm" id="top-nav-wrap">
      <span class="top-nav-container-left">
        <a v-if="$route.path != '/'" href="/" class="top-nav-link">
          <i class="fa fa-home fa-lg fa-2x" aria-hidden="true"></i> |
        </a>
        <a class="top-nav-link" @click="toggleHeader()">H</a>
        <div style="display:inline-block">
        <a class="top-nav-link" href="http://nitdgp.ac.in/alumni/index.php">Alumni</a>
        <a class="top-nav-link" href="https://mail.google.com/a/nitdgp.ac.in">Webmail</a>
        <a class="top-nav-link" href="/contacts">Contacts</a>
        </div>
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
      header: true,
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
    width: 45%;
  }
  #navbarSupportedContent-4{
    padding-top: 6em;margin-top: -2em;
  }
  .navbar-brand {
    height: 90px;
    margin-top: -20px;
    margin-bottom: -20px;
  }
  .navbar-img-big{
    padding-left: 5px;
    height: 70px;
  }
  .navbar-img-small{
    height: 0px;
  }
  @media screen and (max-width: 1010px) {
    .navbar-brand {
      height: 70px;
      padding-top: 15px;
    }
    .navbar-text {
      margin-left: 0px;
    }
    .navbar-img-small {
      height: 50px;
      padding-top: 10px;
      margin-left: 3px;
    }
    .navbar-img-big {
      padding-left: 5px;height: 0px;
    }
  }
  .navbar-text-small{
    font-size: 65%;
  }
</style>
