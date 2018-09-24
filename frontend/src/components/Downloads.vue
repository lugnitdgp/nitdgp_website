<template>
  <links-page>
    <card title="Downloads">
      <ul class="list-group list-gr">
        <li v-for="file in files">
          <a class="list-group-item" target="new" :href="file.file">
            {{file.title}}
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
  name: "Downloads",
  data () {
    return {
      files: []
    }
  },
  created () {
    axios.get(genBackendURL('dashboard/downloads'))
         .then(response => {
           this.files = response.data.results
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

