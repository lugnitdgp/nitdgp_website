<template>
  <links-page>
    <card v-for="(report, header) in reports"
      :title="header + ' Reports'" :key="report.id">
      <ul>
        <li v-for="link in report">
          <a target="new" :href="link.file">
            {{ link.title }}
          </a>
        </li>
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
  name: "Reports",
  data () {
    return {
      reports: []
    }
  },
  created () {
    axios.get(genBackendURL('information/reports'))
         .then(response => {
           this.reports = response.data.results[0].reports
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
