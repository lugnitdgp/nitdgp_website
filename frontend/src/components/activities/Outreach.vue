<template>
  <div class="l1 page-type-links">
    <nav class="navbar navbar-expand-lg" style="background: #001333;">
  <!-- Collapse button -->
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#submenuItem"
	    aria-controls="submenuItem">
	    <i class="fa fa-bars fa-1x" style="color: white;"></i><span style="padding-left: 10px;color: white;">Menu</span>
	  </button>

  <!-- Collapsible content -->
  <div class="collapse navbar-collapse" id="submenuItem">

    <!-- Links -->
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active dropdown">
        <a class="nav-link dropdown-toggle" id="atcivitipopup" data-toggle="dropdown" aria-haspopup="true"
          aria-expanded="false">Activities</a>
          <div class="dropdown-menu submenu" aria-labelledby="atcivitipopup">
          <a class="nav-link" href="#">Short Term Courses</a>
          <a class="nav-link" href="#">Visit</a>
        </div>
      </li>
      <li class="nav-item active dropdown">
        <a class="nav-link dropdown-toggle" id="reseachpopup" data-toggle="dropdown" aria-haspopup="true"
          aria-expanded="false">Research</a>
          <div class="dropdown-menu submenu" aria-labelledby="reseachpopup">
          <a class="nav-link" href="#">Project</a>
          <a class="nav-link" href="#">Publication</a>
          <a class="nav-link" href="#">Product</a>
        </div>
      </li>
      <li class="nav-item active dropdown">
        <a class="nav-link dropdown-toggle" id="peoplepopup" data-toggle="dropdown" aria-haspopup="true"
          aria-expanded="false">People</a>
          <div class="dropdown-menu submenu" aria-labelledby="peoplepopup">
          <a class="nav-link" href="#">Faculty</a>
          <a class="nav-link" href="#">Collaborations</a>
          <a class="nav-link" href="#">PhD Scholar</a>
          <a class="nav-link" href="#">Alumni</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Contact</a>
      </li>

    </ul>
    <!-- Links -->

  </div>
  <!-- Collapsible content -->

</nav>
<!--/.Navbar-->
<br><br><br><br>
</div>
</template>
<script>
import axios from 'axios'
import TableRenderer from '@/components/TableRenderer'
import { genBackendURL, stripDesc, convertNewsfeed } from '@/common.js'

export default {
  name: 'Outreach',
	data() {
		return {
			outreach: {}
		}
	},
  created () {
		/*axios.get(genBackendURL("activities/outreach"))
         .then(response => {
					 this.outreach = response.data.outreach
					 console.log(this.outreach)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })*/
         this.$emit('hideloader', true)
	},
	methods: {
    genBackendURL: genBackendURL,
	},
	components: {
    TableRenderer
  }
}
</script>
<style scoped="scoped">
.navbar-nav .nav-item{
	color: #fff;
	font-size: 20px;
	font-weight: bold;
}
.navbar-nav .nav-link{
	text-decoration: none;
	color: #fff;
}
.navbar .nav-item .nav-link {
    display: block;
    padding-right: 4rem;
}
..navbar-nav .nav-item .nav-link{
	color: #fff;
}
.navbar .nav-item .nav-link .dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    z-index: 1000;
    display: none;
    float: left;
    width: 120%;
    padding: .5rem 0;
    margin: .125rem 0 0;
    margin-top: 0.125rem;
    font-size: 1rem;
    color: #212529;
    text-align: left;
    background-color: #cad;
    border: 1px solid rgba(0,0,0,.15);
    border-radius: .25rem;
}
.navbar .nav-item .nav-link .dropdown-menu ul li a{
	color: #fff;
}
.nav-link .submenu{
	background: rgb(0, 19, 51);
	color: #fff;
}
.nav-link .submenu a{
	color: #fff;
}
</style>
