<template>
	<h1>
		<a href="http://www.nitdgp.ac.in/information/senate_meetings.php">Link to the old web</a>
	</h1>
</template>
<script>
export default {
  name: 'Senate',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>