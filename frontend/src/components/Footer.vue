<template>
  <footer class="page-footer center-on-small-only" >
    <div class="container" id="footer-container" >
      <div class="container-fluid" align="center" >
        <div class="row">
          <div v-for="logo in logos" class="container-fluid logo-container">
            <a :href="logo.href"><img :src="['/static/img/' + logo.filename]"></a>
          </div>
        </div>
        <hr class="style4">
        <div class="row quick-links-row">
          <div v-for="link in links" class="container-fluid quick-links-container">
            <a :href="link.href">{{ link.name }}</a>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-copyright" id="footer-copyright" >
      <div class="row">
        <div class="container-fluid" >
          <span class="copyright-txt" >Last updated: {{ last_updated }} </span>
        </div>
        <div class="container-fluid" >
          <span class="copyright-txt">© 2018 Copyright: <a href="https://www.nitdgp.ac.in"> nitdgp.ac.in </a></span>
        </div>
        <div class="container-fluid" >
          <span class="copyright-txt">Visitors Count: {{ visitors }} </span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
    name: 'Footer',
    data() {
      return {
        visitors: 12312,
        last_updated: "1/12/18 12:12 PM",
        logos: [{name: 'govlogo1', filename: 'govlogo1.png', href:"#!"},
                {name: 'govlogo2', filename: 'govlogo2.png', href:"#!"},
                {name: 'govlogo3', filename: 'govlogo3.png', href:"#!"},
                {name: 'govlogo4', filename: 'govlogo4.png', href:"#!"},
                {name: 'govlogo5', filename: 'govlogo5.png', href:"#!"},
                {name: 'govlogo6', filename: 'govlogo6.png', href:"#!"},
                {name: 'govlogo7', filename: 'govlogo7.png', href:"#!"},
                {name: 'govlogo8', filename: 'govlogo8.png', href:"#!"}],
        links: [{name: "Holidays", href:"#!"},
                {name: "Archives", href:"#!"},
                {name: "Policies", href:"#!"},
                {name: "Webteam", href:"#!"}]
      }
    }
}
</script>

<style scoped>
  #footer-container > .container-fluid > .row:first-child {
    background-color: #fff;
    padding:5px;
    border-radius: 10px;
  }
  .logo-container:nth-child(6) a img {
    padding-top: 10%;
  }
</style>
