<template>
  <links-page>
    <card title="Academic Fees" class="list-group list-grations">
      <ul class="list-group list-gr">
        <li v-for="fee in fees">
          <a class="list-group-item" target="new" :href="fee.file">
            {{ fee.title }}
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: "Fees",
  data () {
    return {
      fees: []
    }
  },
  created () {
    axios.get(genBackendURL('academics/fee'))
         .then(response => {
           this.fees = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log("Axios(GET[academics/fees]): Error: " + e)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
