<template>
  <links-page>
    <card title="Festivals">
      <div class="row">
        <card-testimonial v-for="(club, i) in clubs" :key="i"
          :image="club.image"
          :name="club.name">
          <span v-html="stripDesc(club.description)"></span><br>
          <strong><a :href="club.link">{{ club.link }}</a></strong><br>
        </card-testimonial>
      </div>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import { genBackendURL,stripDesc } from '@/common.js'

export default {
  name: "Students",
  data () {
    return {
      clubs: {}
    }
  },
  methods: {
    stripDesc: stripDesc
  },
  created () {
    axios.get(genBackendURL("activities/festivals"))
         .then(response => {
           this.clubs = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    CardTestimonial
  }
}
</script>
