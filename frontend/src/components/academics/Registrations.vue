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
    axios.get("http://172.16.20.3:8000/academics/registration?format=json")
         .then(response => {
           this.registrations = response.data.results
         })
         .catch(e => {
           this.errors.push(e)
           console.log(errors)
         })
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
