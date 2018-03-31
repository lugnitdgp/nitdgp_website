<template>
	<h1>
		<a href="http://nitdgp.ac.in/BOG.php">Link to old web</a>
	</h1>
</template>
<script>
export default {
  name: 'Bog',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>