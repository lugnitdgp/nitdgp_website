<template>
	<div class="l1 page-type-links">
		<!-- CONTENT -->
		<div class="card">
		  <a class="card-header white-text">Achievements, Honours &amp; Recognitions </a>
		  <div class="card-body">
		      <div class="card-text">
		        <h1>May include a photo carousel here</h1>
		        <ul>
		          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg" target="new">Achievement detail here</a></li>
		          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg" target="new">
		          Achievement detail here</a></li>
		          <li><a href="http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf" target="new">
		          Achievement detail here</a></li>
		          <li><a href="http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf" target="new">
		          Achievement detail here</a></li>
		        </ul>
		      </div>
		  </div>
		</div>
	</div>
</template>
<script>
	export default {
		name: 'Achievements',
		created () {
			this.$emit('hideloader', true)
		}
	}
</script>