<template>
  <links-page>
    <card title="Departmental Promotion">
      <ul class="list-group list-gr">
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/DPC Notification 2019.pdf">Notification Regarding Departmental Promotion</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Revised_Recruitment_Rules_for_NonTeaching_in_NITs_20122017.pdf">Recruitment Rules 2017 (Non-Teaching )</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Education Qualification DPC.pdf">Education Qualifications Requirment for the Employee Apointed Before 05.02.2014 </a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/DPC Application Form.pdf">Application Form ( PDF ) </a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/DPC Application Form.doc">Application Form ( DOC ) </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: "Dpromotion",
  data () {
    return {
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
