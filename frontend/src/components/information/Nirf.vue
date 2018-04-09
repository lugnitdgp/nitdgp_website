<template>
  <links-page>
    <card title="NIRF">
      <ul>
        <li v-for="nirf in nirfs">
          <a target="new" :href="nirf.file">
            {{ nirf.title }}
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
  name: "Nirf",
  data () {
    return {
      nirfs: []
    }
  },
  created () {
    axios.get(genBackendURL('information/nirf'))
         .then(response => {
           this.nirfs = response.data.results
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
