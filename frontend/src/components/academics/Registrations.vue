<template>
  <links-page>
    <card title="Registrations">
      <ul>
        <li v-for="reg in registrations">
          <a :href="reg.file" target="new">
            {{ reg.title }}
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

export default {
  name: 'Registrations',
  data () {
    return {
      registrations: {}
    }
  },
  created () {
    axios.get(genBackendURL("academics/registration"))
         .then(response => {
           this.registrations = response.data.results
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
