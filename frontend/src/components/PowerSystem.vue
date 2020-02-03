<template>
  <links-page>
    <card title="M. Tech (Specialization- Power Systems)">
      <ul class="list-group list-gr">
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/Power Systems/Faculty  for Power Systems.pdf">Faculty</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/Power Systems/PE and POS of PS.pdf">PEOS/POS</a></li>
        <li><a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/Power Systems/Curricula and Syllabus of PS.pdf">Curricula and Syllabus</a></li>
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
