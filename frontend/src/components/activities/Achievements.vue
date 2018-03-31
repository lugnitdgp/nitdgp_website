<template>
  <links-page>
    <card title="Achievements, Honours and Recognitions">
      <h1>May include a photo carousel here</h1>
      <ul>
	<li v-for="ach in achievements">
          <a :href="ach.file" target="new">{{ ach.title }}</a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from '@/components/Card.vue'
import LinksPage from '@/components/LinksPage.vue'

export default {
  name: 'Achievements',
  data () {
    return {
      achievements: [
        {
          title: "Achievement detail here",
          file: "http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_application_form.jpg"
        },
        {
          title: "Achievement detail here",
          file: "http://nitdgp.ac.in/all_pdf17/transcript_notice/transcript_fee_slip.jpg"
        },
        {
          title: "Achievement detail here",
          file: "http://nitdgp.ac.in/all_pdf17/Verification%20of%20Education%20Qualification..pdf"
        },
        {
          title: "Achievement detail here",
          file: "http://nitdgp.ac.in/all_pdf17/ISSUANCE%20OF%20ACADEMIC%20DOCUMENTS..pdf"
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
