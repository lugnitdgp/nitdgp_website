<template>
  <links-page>
    <card title="Convocation and Special Events">
      <ul class="list-group list-gr">
        <li v-for="convocation in convocations">
          <a v-if="convocation.file" class="list-group-item" :href="convocation.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ convocation.updated_at.substring(0,10) }} </span>&nbsp;{{ convocation.title }}
            </a>
          <a v-else class="list-group-item" :href="convocation.url">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ convocation.updated_at.substring(0,10) }} </span>&nbsp;{{ convocation.title }}
          </a>
        </li>
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
  name: "Convocations",
  data () {
    return {
      convocations: {}
    }
  },
  created () {
    axios.get(genBackendURL("academics/convocation"))
         .then(response => {
           this.convocations = response.data.results
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
