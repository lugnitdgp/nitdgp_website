<template>
  <links-page>
    <card title="Right to Information">
      <ul class="list-group list-gr">
        <li v-for="rti in rtis">
          <a class="list-group-item" target="new" :href="rti.file">
            {{ rti.title }}
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
  name: "Rti",
  data () {
    return {
      rtis: []
    }
  },
  created () {
    axios.get(genBackendURL('information/rti'))
         .then(response => {
           this.rtis = response.data.results
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
