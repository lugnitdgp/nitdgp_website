<template>
  	<div class="l1 page-type-links">
	    <!-- CONTENT -->
	    <div class="card">
	      <a class="card-header white-text">Placement Activities</a>
	      	<div class="card-body">
				<div class="card-text">
				  <ul class="list-group list-gr">
				    <li><a class="list-group-item" target="new" href="#">Placement Statistics</a></li>
				  </ul>
				</div>
	    	</div>
	    </div>
   	</div>
</template>
<script>
export default {
  name: 'Placement',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>