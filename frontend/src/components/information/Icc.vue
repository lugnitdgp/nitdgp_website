<template>
  <links-page>
    <card title="ICC">
      <ul class="list-group list-gr">
        <li v-for="icc in iccs">
          <a v-if="icc.link" class="list-group-item" target="new" :href="icc.link">
           {{icc.title}}
          </a>
          <a v-else class="list-group-item" target="new" :href="icc.file">
            {{icc.title}}
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
      iccs: []
    }
  },
  created () {
    axios.get(genBackendURL('information/icc'))
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
