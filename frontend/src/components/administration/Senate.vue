<template>
  <links-page>
    <card title="Senate">
      <notice-list :noticelist="meetings" />
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
  name: "Senate",
  data () {
    return {
      meetings: [],
      paginate: ['meetings'],
    }
  },
  created () {
    axios.get(genBackendURL("administration/senate"))
         .then(response => {
           this.meetings = response.data.results
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
