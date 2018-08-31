<template>
  <links-page>
    <card title="Minutes of IFC Meeting">
      <notice-list :noticelist="ifc_docs" />
    </card>
    <card title="Minutes of BWC Meeting">
      <notice-list :noticelist="bwc_docs" />
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
  name: "Calendar",
  data () {
    return {
      bwc_docs: [],
      paginate: ['bwc_docs'],
      ifc_docs: [],
      paginate: ['ifc_docs']
    }
  },
  created () {
		let flag = false
    axios.get(genBackendURL("administration/bwc"))
         .then(response => {
           this.bwc_docs = response.data.results
					 if (flag)
             this.$emit('hideloader', true)
           flag = true
         })
         .catch(e => {
           console.log(e)
         })
     axios.get(genBackendURL("administration/ifc"))
          .then(response => {
            this.ifc_docs = response.data.results
 					 if (flag)
              this.$emit('hideloader', true)
            flag = true
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
