<template>
  <links-page>
    <card title="Departmental Promotion">
      <ul class="list-group list-gr">
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Circular_cancellation .pdf">Cancellation of Circular No. NITD/Estt./2301/2019 Date - 4th July 2019 </a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/reservation_roster2019.pdf">Reservation Roster of 31.03.2019 </a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Notification_updated.pdf">Notification Regarding Departmental Promotion</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Recruitment_Rules_updated.pdf">Recruitment Rules 2017 (Non-Teaching )</a>
        </li>
        <!--<li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Education Qualification DPC.pdf">Education Qualifications Requirment for the Employee Apointed Before 05.02.2014 </a>
        </li>-->
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/Application_form_updated.pdf">Application Form ( PDF ) </a>
        </li>
        <!--<li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/DP/DPC Application Form.doc">Application Form ( DOC ) </a>
        </li>-->
        
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
