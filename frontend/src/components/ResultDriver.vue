<template>
  <links-page>
    <card title="Shortlisted candidates for Seminar under Special Recruitment Drive for SC/ST/OBC/PWD for Faculty Positions">
      <ul class="list-group list-gr">
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Biotechnology.pdf"> Biotechnology (BT)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Chemical Engineering.pdf">Chemical Engineering (CH)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Chemistry.pdf">Chemistry(CY)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Computer Science and Engineering.pdf"> Computer Science and Engineering (CS)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Earth and Environmental Studies.pdf"> Earth and Environmental Studies (EES)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Electrical Engineering.pdf"> Electrical Engineering (EE)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Humanities and Social Sciences.pdf">Humanities and Social Sciences(HSS)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Management Studies.pdf">Management Studies (MS)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Mathematics1.pdf"> Mathematics (MA)</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Physics.pdf">Physics (PH)</a></li>
      </ul>
      <br>
      <br>
      <div>
      <p style="font-size:18px; color:#000;">**Candidates shortlisted after the Seminar will only be called for interview. </p > 
    </div>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: "ResultDriver",
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
