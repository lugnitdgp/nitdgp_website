<template>
  <links-page>
    <card title="ICC">
      <ul class="list-group list-gr">
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/information/Internal%20Complaint%20Committee/Office%20Order%20Regarding%20Internal%20Complaints%20Committee..pdf">
            Internal Complain Committee
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
  name: "Icc",
  data () {
    return {
      // iccs: []
    }
  },
  created () {
    axios.get(genBackendURL('information/nba'))
         .then(response => {
           this.iccs = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log("Axios(GET[information]): Error: " + e)
         })
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
