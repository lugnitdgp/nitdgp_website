<template>
  <links-page>
    <card title="TEQIP">
      <ul class="list-group list-gr">
        <li v-for="teqip in teqips">
          <a class="list-group-item" target="new" :href="teqip.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ teqip.date }} </span>&nbsp;{{ teqip.title }}
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
  name: "Teqips",
  data () {
    return {
      teqips: []
    }
  },
  created () {
    axios.get(genBackendURL('information/teqip'))
         .then(response => {
           this.teqips = response.data.results
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
