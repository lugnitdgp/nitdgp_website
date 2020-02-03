<template>
  <links-page>
    <card title="M. Tech (Specialization- Power Electronics and Machine Drives)">
      <ul class="list-group list-gr">
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/PowerElectronics/Faculty  for Power Electronics.pdf">Faculty</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/PowerElectronics/PE and POS of PEMD.pdf">PEOS/POS</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/PowerElectronics/Curricula and Syllabus of PEMD.pdf">Curricula and Syllabus</a></li>
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
  name: "PowerSystem",
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
