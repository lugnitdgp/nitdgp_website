<template>
  <links-page>
    <card title="Board of Governors">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div class="col black-text" v-for="person in bogs.chairperson">
              <card-testimonial :image="person.image" :name="person.name"
                :desig="person.role">
                <strong>-- {{ person.designation }} --</strong></br>
                {{ person.address }}</br>
              </card-testimonial>
            </div>
            <div class="col black-text" v-for="person in bogs.secratary">
              <card-testimonial :image="person.image" :name="person.name"
                :desig="person.role">
                <strong>-- {{ person.designation }} --</strong></br>
                {{ person.address }}</br>
              </card-testimonial>
            </div>
            <div class="col black-text" v-for="person in bogs.member">
              <card-testimonial :image="person.image" :name="person.name"
                :desig="person.role">
                <strong>-- {{ person.designation }} --</strong></br>
                {{ person.address }}</br>
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
import { range, genBackendURL } from '@/common.js'

export default {
  name: "Bog",
  data () {
    return {
      bogs: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/bog"))
         .then(response => {
           this.bogs = response.data
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  methods: {
    range: range
  },
  components: {
    LinksPage,
    Card,
    CardTestimonial
  }
}
</script>
