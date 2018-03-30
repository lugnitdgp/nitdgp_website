<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <h1>There will be a list of cards for student clubs</h1>
    <div class="card">
      <a class="card-header white-text">Students</a>
      <div class="card-body">
	<div class="card-text">
	  <ul>
	    <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg" target="new">Application For Duplicates/ Transcripts/ Migration Certificate</a></li>
	    <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg" target="new">
	      Transcript Fee Slip</a></li>
	    <li><a href="http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf" target="new">
	      Verification of Education Qualification</a></li>
	    <li><a href="http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf" target="new">
	      Issuance of Academic Documents</a></li>
	  </ul>
	</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Students',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
