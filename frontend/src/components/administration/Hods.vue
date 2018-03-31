<template>
	<h1>
		<a href="http://www.nitdgp.ac.in/contact_us.php">Take the list of HODs from here</a>
	</h1>
</template>
<script>
export default {
  name: 'Hods',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>