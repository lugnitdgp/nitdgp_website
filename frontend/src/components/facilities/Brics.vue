<template>
  <links-page>
    <card title="BRICS">
      <notice-list :noticelist="bricslist" />
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
  name: "BRICS",
  data () {
    return {
      bricslist: [],
      paginate: ['bricslist']
    }
  },
  created () {
    axios.get(genBackendURL("activities/brics"))
         .then(response => {
           this.bricslist = response.data.results
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
