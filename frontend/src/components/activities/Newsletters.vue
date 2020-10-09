<template>
  <links-page>
    <card title="Newsletters">
      <notice-list :noticelist="newslettersList" />
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
  name: "Newsletters",
  data () {
    return {
      newslettersList: [],
      paginate: ['newslettersList']
    }
  },
  created () {
    axios.get(genBackendURL("activities/newsletters"))
         .then(response => {
           this.newslettersList = response.data.tenders
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
