<template>
  <links-page>
    <card title="Events and Seminars">
      <h1> This may be notice-type page </h1>
      <ul>
        <li v-for="event in events">
          <a :href="event.file">{{ event.title }}</a>
        </li>
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
    </card>
  </links-page>
</template>
<script>
import Card from '@/components/Card'
import LinksPage from '@/components/LinksPage'

export default {
  name: 'Events',
  data () {
    return {
      events: [
        {
          file: "http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg",
          title: "Application For Duplicates/ Transcripts/ Migration Certificate"
        },
        {
          file: "http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg",
          title: "Transcript Fee Slip"
        },
        {
          file: "http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf",
          title: "Verification of Education Qualification"
        },
        {
          file: "http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf",
          title: "Issuance of Academic Documents"
        }
      ]
    }
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
