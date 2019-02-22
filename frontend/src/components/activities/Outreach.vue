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
<ul class="nav nav-tabs md-tabs" id="myTabMD" role="tablist">
  <li class="nav-item active">
	<a class="nav-link active dropdown-toggle" id="atcivitipopup" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Activities</a>
		<div class="dropdown-menu submenu" aria-labelledby="atcivitipopup">
			<a class="nav-link active" id="home-tab-md" data-toggle="tab" href="#home-md" role="tab" aria-controls="home-md"      aria-selected="true">Short Term Courses</a>
			<a class="nav-link" href="#">Visit</a>
		</div>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="profile-tab-md" data-toggle="tab" href="#profile-md" role="tab" aria-controls="profile-md"
      aria-selected="false">Profile</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="contact-tab-md" data-toggle="tab" href="#contact-md" role="tab" aria-controls="contact-md"
      aria-selected="false">Contact</a>
  </li>
</ul>
<div class="tab-content card pt-5" id="myTabContentMD">
  <div class="tab-pane fade" id="home-md" role="tabpanel" aria-labelledby="home-tab-md">
    <p>Raw denim you probably haven't heard of them jean shorts Austin. Nesciunt tofu stumptown aliqua,
      retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica.
      Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry
      richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american
      apparel, butcher voluptate nisi qui.</p>
  </div>
  <div class="tab-pane fade" id="profile-md" role="tabpanel" aria-labelledby="profile-tab-md">
    <p>Food truck fixie locavore, accusamus mcsweeney's marfa nulla single-origin coffee squid.
      Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko
      farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip
      jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna
      delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan
      fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry
      richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus
      tattooed echo park.</p>
  </div>
  <div class="tab-pane fade" id="contact-md" role="tabpanel" aria-labelledby="contact-tab-md">
    <p>Etsy mixtape wayfarers, ethical wes anderson tofu before they sold out mcsweeney's organic lomo
      retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer,
      iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony.
      Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles
      pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of
      them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
  </div>
</div>
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
