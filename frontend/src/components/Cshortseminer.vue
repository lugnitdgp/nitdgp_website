<template>
  <links-page>
    <card title="Candidates Shortlisted for Seminar for Advertise No. NITD/Estt./02/07/2019 (Rolling), dated 22.07.2019">
      <ul class="list-group list-gr">
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Biotechnology.pdf"> Biotechnology (BT)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Chemical Engineering.pdf">Chemical Engineering (CH)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Chemistry.pdf">Chemistry(CY)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Civil Engineering.pdf"> Civil Engineering (CE)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Computer Science and Engineering.pdf"> Computer Science and Engineering (CS)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Earth and Environmental Studies.pdf"> Earth and Environmental Studies (EES)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Electrical Engineering .pdf"> Electrical Engineering (EE)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Humanities and Social Sciences.pdf">Humanities and Social Sciences(HSS)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Management Studies.pdf">Management Studies (MS)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Mathematics.pdf"> Mathematics (MA)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Mechanical Engineering.pdf"> Mechanical Engineering (ME)</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Metallurgical and Materials Engineering.pdf"> Metallurgical and Materials Engineering (MME))</a></li>
        <li><a class="list-group-item" target="new" href="http://admin.nitdgp.ac.in/files/candidateseminerlist/Physics.pdf">Physics (PH)</a></li>
      </ul>
      <br>
      <br>
      <div>
      <p style="font-size:18px; color:blue;">**Candidates shortlisted after the Seminar will only be called for an interview. </p > 
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
