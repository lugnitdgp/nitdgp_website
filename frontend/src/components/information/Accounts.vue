<template>
  <links-page>
    <card title="Annual Accounts">
      <ul class="list-group list-gr">
        <li v-for="account in accounts">
          <a class="list-group-item" target="new" :href="account.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ account.date }} </span>&nbsp; {{ account.title }}
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
