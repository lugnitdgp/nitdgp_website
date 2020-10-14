<template>
  <links-page>
  	<div class="col-12 caro">
        <Carousel :slides="slides"></Carousel>
    </div><br>
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
import Carousel from '@/components/Carousel'
import NoticeList from '@/components/NoticeList'
import { genBackendURL } from '@/common.js'

export default {
  name: "Covidinfo",
  data () {
    return {
 	  slides:{},
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
    axios.get(genBackendURL('activities/coecarousel'))
         .then(response => {
          let coecarousels = response.data.coecarousels
          this.slides = coecarousels.COVID
          
          })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    Carousel,
    NoticeList
  }
}
</script>
