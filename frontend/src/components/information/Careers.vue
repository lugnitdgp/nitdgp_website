<template>
	<div class="l1 page-type-links">
    <div class="card">
      <a class="card-header white-text">Career @ NIT DGP</a>
      <div class="card-body content">
        <ul>
          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg" target="new">Application For Duplicates/ Transcripts/ Migration Certificate</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg" target="new">
          Transcript Fee Slip</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf" target="new">
          Verification of Education Qualification</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf" target="new">
          Issuance of Academic Documents</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg" target="new">Application For Duplicates/ Transcripts/ Migration Certificate</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg" target="new">
          Transcript Fee Slip</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf" target="new">
          Verification of Education Qualification</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf" target="new">
          Issuance of Academic Documents</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg" target="new">Application For Duplicates/ Transcripts/ Migration Certificate</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg" target="new">
          Transcript Fee Slip</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf" target="new">
          Verification of Education Qualification</a></li>
          <li><a href="http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf" target="new">
          Issuance of Academic Documents</a></li>
        </ul>
        <div id="selector">
          <ul class="pagination justify-content-center">
            <li class="page-item">
              <a class="page-link" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
                <span class="sr-only">Previous</span>
              </a>
            </li>

            <li class="page-item active" ><a class="page-link" data-toggle="tab" href="#li1" role="tab">1</a></li>
            <li class="page-item"><a class="page-link" data-toggle="tab" href="#li2" role="tab">2</a></li>
            <li class="page-item"><a class="page-link" data-toggle="tab" href="#li3" role="tab">3</a></li>
            <li class="page-item"><a class="page-link" data-toggle="tab" href="#li4" role="tab">4</a></li>
            <li class="page-item">
              <a class="page-link" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
                <span class="sr-only">Next</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: 'Careers',
  created () {
    this.$emit('hideloader', true)
  },
  components: {
  	LinksPage,
  	Card
  }
}
</script>
