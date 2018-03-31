<template>
	<h1>
		<a href="http://nitdgp.ac.in/deans.php">Deans are here</a>
	</h1>
</template>
<script>
export default {
  name: 'Deans',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>