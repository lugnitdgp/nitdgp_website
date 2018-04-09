<template>
  <links-page>
    <card title="National Board of Accreditation">
      <ul>
        <li v-for="nba in nbas">
          <a target="new" :href="nba.file">
            {{ nba.title }}
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
  name: "Nba",
  data () {
    return {
      nbas: []
    }
  },
  created () {
    axios.get(genBackendURL('information/nba'))
         .then(response => {
           this.nbas = response.data.results
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
