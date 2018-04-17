<template>
  <footer class="page-footer center-on-small-only">
    <div class="container" id="footer-container">
      <div class="container-fluid" align="center">
        <div class="row quick-links-row quick-links-container">
          <a v-for="link in links" :href="link.href" class="container-fluid">
            {{ link.name }}
          </a>
        </div>
        <div class="row">
          <a v-for="logo in logos" :href="logo.href"
            class="container-fluid logo-container">
            <img :src="['/static/img/' + logo.filename]">
          </a>
        </div>
      </div>
    </div>
    <div class="footer-copyright" id="footer-copyright">
      <div class="row">
        <div class="container-fluid ftr-1">
          <span class="copyright-txt">Last updated: {{ last_updated }} </span>
        </div>
        <div class="container-fluid ftr-2">
          <span class="copyright-txt">© 2018 Copyright: <a href="https://www.nitdgp.ac.in"> nitdgp.ac.in </a></span>
        </div>
        <div class="container-fluid ftr-3">
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
      links: [{name: "Holidays", href: "/holidays"},
              {name: "Archives", href: "/archives"},
              {name: "Policies", href: "/policies"},
              {name: "Webteam", href: "/webteam"}]
    }
  }
}
</script>

<style scoped>
  #footer-container > .container-fluid > .row:last-child {
    padding: 3px;
    margin-top: 20px;
    background-color: #fff;
    border-radius: 10px;
  }
  @media screen and (max-width: 600px){
    .ftr-1{
      display: none;
    }
    .ftr-3{
      display: none;
    }
  }
</style>
