<template>
  <links-page>
    <card title="National Board of Accreditation">
      <ul class="list-group list-gr">
        <li v-for="nba in nbas">
          <a class="list-group-item" target="new" :href="nba.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ nba.date }} </span>&nbsp; {{ nba.title }}
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
