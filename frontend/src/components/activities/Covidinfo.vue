<template>
  <links-page>
  	<card title = "Covid-19" class="text-justify">
  		
  	</card>
  	<br>
    <card title="Covid-19 Notifications">
      <notice-list :noticelist="covidList" />
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
  name: "Covidinfo",
  data () {
    return {
 
	  covidList: [],
      paginate: ['covidList']
    }
  },
  created () {
  	axios.get(genBackendURL("activities/covid"))
         .then(response => {
           this.covidList = response.data.results
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
