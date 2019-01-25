<template>
  <links-page>
    <card title="Curriculum and Syllabus">
      <ul class="list-group list-gr">
        <li>
          <a class="list-group-item" href="http://nitdgp.ac.in/AllPDF/COMPILED 2017 admission - FOR PROSPECTUS.pdf" target="_blank">
            Curriculum of 2017-18 Undergraduate Admission Batch
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import { genBackendURL } from '@/common.js'

export default {
  name: "Curriculmn",
  data () {
    return {
      curriculmn: {}
    }
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
