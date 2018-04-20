<template>
	<links-page>
    <card title="Research Activities">
      <div>
        <ul class="list-group list-gr">
          <li v-for="link in docs">
            <a class="list-group-item" v-if="link.file" :href="link.file" target="new">
              {{ link.title }}
            </a>
            <a class="list-group-item" v-if="link.url" :href="link.url" target="new">
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
  name: 'Research',
  data () {
    return {
      docs: {},
      backURL: backURL
    }
  },
  created () {
    axios.get(genBackendURL('activities/research'))
         .then(response => {
           this.docs = response.data.results
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