<template>
  <links-page>
    <card title="Tenders">
      <notice-list :noticelist="tenderslist" />
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import NoticeList from '@/components/NoticeList'
import { genBackendURL } from '@/common.js'

export default {
  name: "Tenders",
  data () {
    return {
      tenderslist: [],
      paginate: ['tenderslist']
    }
  },
  created () {
    axios.get(genBackendURL("information/tenders"))
         .then(response => {
           this.tenderslist = response.data.tenders
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    NoticeList
  }
}
</script>
