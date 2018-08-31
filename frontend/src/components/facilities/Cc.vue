<template>
  <div class="l1 page-type-links">
    <div class="card">
      <a class="card-header white-text">Computer Center</a>
      <div class="card-body">
	<div class="card-text">
	  <ul>
	    <li><a href="http://nitdgp.ac.in/cc/" target="new">Link to the old webpg</a></li>
	  </ul>
	</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Cc',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
