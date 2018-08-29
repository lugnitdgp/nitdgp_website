<template>
  <links-page>
    <card v-for="(report, header) in reports"
      :title="header + ' Reports'" :key="report.id">
      <ul class="list-group list-gr">
        <li v-for="link in report">
          <a class="list-group-item" target="new" :href="link.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ link.date }} </span>&nbsp; {{ link.title }}
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
           this.reports = response.data.reports
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
