<template>
  <links-page>
    <card title="Departmental Promotion">
      <ul class="list-group list-gr">
        <li v-for="promotion in promotions">
          <a class="list-group-item" target="new" :href="promotion.file">{{ promotion.title}}</a>
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
  name: "Dpromotion",
  data () {
    return {
      promotions: []
    }
  },
  created () {
    axios.get(genBackendURL('information/promotion'))
         .then(response => {
           this.promotions = response.data.results
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
