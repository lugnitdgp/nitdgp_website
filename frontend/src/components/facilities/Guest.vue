<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Accommodation</a>
      <div class="card-body">
	National Institute of Technology, Durgapur is a residential Institute. There are seven hostels for boys and two hostels for girls to accommodate the admitted students. A canteen for the students and the staff is located near the main academic building and there is a second canteen at the rear exit of the main academic building of the Institute. The most of the teachers and the staff members reside in the residential quarters provided by the Institute. A modern Guest House beside the Director's Bungalow extends hospitality to the guests of the Institute. In the middle of the residential area there is a Shopping Complex which meets the daily requirement of the residents. A model co-educational higher secondary school has been set up for the wards of the employees of the Institute. Also there is a branch of State Bank of India, a branch of Canara Bank and a Post-Office within the Institute Campus.
      </div>
    </div>
    <div class="card">
      <a class="card-header white-text">Guest House</a>
      <div class="card-body">
	<div style="text-align: center;">
	  <img style="max-height:300px;width: 500px;max-width: 100%" src="/static/img/guest_house.jpg" width="100%"><br>
	</div>
	The Institute Guest House standing beside the Director's Bungalow serves to render hospitality to the Official and Non-official guests of the Institute. It is a unique double storied building with modern living facilities overlooking a beautiful garden and tall sal trees all around. The guests of faculty members and students are also accommodated there with advanced booking as per availability.
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Guest',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
