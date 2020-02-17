<template>
  <links-page>
    <card title="Shortlisted candidates for Seminar under Special Recruitment Drive for SC/ST/OBC/PWD for Faculty Positions – Remaining Four Departments">
      <ul class="list-group list-gr">
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Civil Engineering.pdf">Civil Engineering</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Electronics & Communication Engineering.pdf">Electronics and Communication Engineering</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Mechanical Engineering.pdf">Mechanical Engineering</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/rsltdriver/Metallurgical and Materials Engineering.pdf">Metallurgical and Materials Engineering</a></li> 
      </ul>
      
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"
import axios from 'axios'
import { genBackendURL } from '@/common.js'

export default {
  name: "ResultDriverRest",
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
