<template>
  <links-page>
    <card title="Annual Accounts">
      <ul>
        <li v-for="account in accounts">
          <a target="new" :href="account.file">
            {{ account.title }}
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
  name: "Accounts",
  data () {
    return {
      accounts: []
    }
  },
  created () {
    axios.get(genBackendURL('information/accounts'))
         .then(response => {
           this.accounts = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
