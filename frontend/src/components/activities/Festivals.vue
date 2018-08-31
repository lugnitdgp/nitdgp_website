<template>
  <links-page>
    <card title="Festivals">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div v-if="club.name == 'GNU/Linux Users\' Group'" class="col black-text" v-for="club in clubs">
              <card-testimonial :image="club.image" :name="club.name">
                <strong>-- Description --</strong><br>
                <span v-html="stripDesc(club.description)"></span><br>
                <i class="fa fa-globe"></i><br>
                <strong><a :href="club.link">{{ club.link }}</a></strong><br>
              </card-testimonial>
            </div>
            <div v-if="(club.name != 'GNU/Linux Users\' Group') && (club.name != 'Centre for Cognitive Activities')" class="col black-text" v-for="club in clubs">
              <card-testimonial :image="club.image" :name="club.name">
                <strong>-- Description --</strong><br>
                <span v-html="stripDesc(club.description)"></span><br>
                <i class="fa fa-globe"></i><br>
                <strong><a :href="club.link">{{ club.link }}</a></strong><br>
              </card-testimonial>
            </div>
            <div v-if="club.name == 'Centre for Cognitive Activities'" class="col black-text" v-for="club in clubs">
              <card-testimonial :image="club.image" :name="club.name">
                <strong>-- Description --</strong><br>
                <span v-html="stripDesc(club.description)"></span><br>
                <i class="fa fa-globe"></i><br>
                <strong><a :href="club.link">{{ club.link }}</a></strong><br>
              </card-testimonial>
            </div>
          </div>
        </div>
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
