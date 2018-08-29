<template>
  <links-page>
    <card title="More Information">
      <ul class="list-group list-gr">
        <li v-for="link in links">
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
