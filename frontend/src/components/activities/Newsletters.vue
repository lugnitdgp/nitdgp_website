<template>
  <links-page>
  	<card title = "About Newsletters" class="text-justify">
  		The Institute Newsletter, a biannual publication, presents an account of the academic activities of the faculty members and accomplishments of the students along with the extra-curricular achievements of NIT Durgapur fraternity, during the relevant period. It also aims at reflecting the ambience of the institute and its social connectivity. It will serve as the medium of interaction among the faculty members, students and alumni, constituting a novel platform for looking beyond the boundary and networking with the academic institutions for achieving excellence.
  	</card>
  	<br>
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
 //      newslettersList: [      
	// 	{title:"Newsletters 2019", file:"https://admin.nitdgp.ac.in/files/newsfeed/2020/10/08/Compiled_Newsletter_9_compressed.pdf",date: "2020-10-08"},
	// 	{title:"NIT Durgapur Newsletter - Special issue on COVID-19", file:"https://admin.nitdgp.ac.in/files/newsfeed/2020/08/04/COVID_Special_Newsletter.pdf",date: "2020-08-02"}
	// ],
	  newslettersList: [],
      paginate: ['newslettersList']
    }
  },
  created () {
  	// this.$emit('hideloader', true)
    axios.get(genBackendURL("activities/newsletters"))
         .then(response => {
           this.newslettersList = response.data.results
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
