<template>
	<div class="page-type-person">
	  <h1 class="name-title" align="center"> MEET OUR REGISTRAR </h1>
	  <div class="card testimonial-card">
      <div class="card-up">
        <!-- <img src="/static/img/nitdgp_logo.png" > -->
      </div>
      <div class="card-body">
        <h3 class="mt-1 white-text">
          <strong>Shri Soumya Sen Sharma</strong>
        </h3>
        <h4 class="desig cyan-text">Registrar</h4>
        <hr class="hr-grey">
        <p class="white-text" align="center">
        <i class="fa fa-map-marker fa-1x"></i><br>
        National Institute of Technology,<br>
        Mahatma Gandhi Avenue,<br>
        Durgapur, West Bengal, India,<br>
        PIN – 713209.<br>
        <i class="fa fa-envelope fa-1x"></i><br>
        registrar@admin.nitdgp.ac.in<br>
        <i class="fa fa-phone fa-1x"></i><br>
        Phone :+91-343-2545290 (O)<br>
        Fax :+91-343-2546406<br>
        <a href="#" class="white-text">*MoreInfo*</a>
        </p>
      </div>
	  </div>
  </div>
</template>
<script>
export default {
  name: 'Registrar',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
