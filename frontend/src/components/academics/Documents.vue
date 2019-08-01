<template>
  <links-page>
    <card title=" Verification and Issuance of Academic Documents">
      <div v-for="(links, doctype) in docs">
        <div style="border: 1px solid #000;padding: 5px 6px;">
          <p class="text-justify" style="color:#000;">
            For all academic verification related mails are to be directed to -<br>
            Deputy Register (Academic and Examination),<br>
            Email: <strong>draca@admin.nitdgp.ac.in.</strong>
          </p>
        </div>
        <h3>Releated Notices</h3>
        <ul class="list-group list-gr">
          <li v-for="link in links">
            <a class="list-group-item" :href="backURL + link.filename" target="new">
              {{ link.title }}
            </a>
          </li>
        </ul>
      </div>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import axios from 'axios'
import { backURL, genBackendURL } from '@/common.js'

export default {
  name: 'Documents',
  data () {
    return {
      docs: {},
      backURL: backURL
    }
  },
  created () {
    axios.get(genBackendURL('academics/document'))
         .then(response => {
           this.docs = response.data.documents
           this.$emit('hideloader', true)
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
