<template>
  <links-page>
    <card title="Tenders">
      <ul class="list-group list-gr">
        <li v-for="tender in tenders">
          <a class="list-group-item" :href="tender.file">{{ tender.title }}</a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import { genBackendURL } from '@/common.js'

export default {
  name: "Tenders",
  data () {
    return {
      tenders: {}
    }
  },
  created () {
    axios.get(genBackendURL("information/tenders"))
         .then(response => {
           this.tenders = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
