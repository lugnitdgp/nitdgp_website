<template>
	<div class="l1 page-type-links faci">
		<!-- CONTENT -->
		<div class="card">
		  <a class="card-header white-text">NIT Durgapur Post Office</a>
		  <div class="card-body">
		    <div style="text-align: center;">
		      <img style="max-height:300px;width: 500px;max-width: 100%" src="http://www.nitdgp.ac.in/images/hostel/1.jpg" width="100%"><br>
		    </div>
		  </div>
		</div>
	</div>
</template>
<script>
	export default {
		name: 'Po',
		created () {
			this.$emit('hideloader', true)
		}
	}
</script>