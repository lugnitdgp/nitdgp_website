<template>
  <links-page>
    <card title="More Information">
      <ul>
        <li v-for="link in links">
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
  name: "Moreinfo",
  data () {
    return {
      links: []
    }
  },
  created () {
    axios.get(genBackendURL('information/more'))
         .then(response => {
           console.log(response)
           this.links = response.data.results
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
