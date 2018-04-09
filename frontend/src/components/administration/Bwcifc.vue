<template>
	<links-page>
    <card title="Minutes of IFC Meeting">
      <ul>
        <li v-for="i in ifc_docs"><a :href="i.file" target=_blank>{{ i.title }}</a></li>
      </ul>
    </card>
    <card title="Minutes of BWC Meeting">
      <ul>
        <li v-for="b in bwc_docs"><a :href="b.file" target=_blank>{{ b.title }}</a></li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import { genBackendURL } from '@/common.js'

export default {
  name: "Calendar",
  data () {
    return {
      bwc_docs: [],
			ifc_docs: []
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
    Card
  }
}
</script>
