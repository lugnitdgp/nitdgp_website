<template>
	<div class="page-type-person">
	  <h1 class="name-title" align="center"> MEET OUR DIRECTOR </h1>
	  <div class="card testimonial-card">
      <div class="card-up">
        <img src="/static/img/director_image.jpg" >
      </div>
      <div class="card-body">
        <h3 class="mt-1 white-text">
          <strong>Prof. Anupam Basu</strong>
        </h3>
        <h4 class="desig cyan-text">Director</h4>
        <hr class="hr-grey">
        <p class="white-text" align="center">
        <i class="fa fa-map-marker fa-1x"></i><br>
        National Institute of Technology,<br>
        Mahatma Gandhi Avenue,<br>
        Durgapur, West Bengal, India,<br>
        PIN – 713209.<br>
        <i class="fa fa-envelope fa-1x"></i><br>
        director@admin.nitdgp.ac.in<br>
        <i class="fa fa-phone fa-1x"></i><br>
        Phone :+91 343 2546397 (O)<br>
        Fax :+91 343 2547375<br>
        <a href="#" class="white-text">*MoreInfo*</a>
        </p>
      </div>
	  </div>
	</div>
</template>
<script>
export default {
  name: 'Chairperson',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
