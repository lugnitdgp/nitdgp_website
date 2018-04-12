<template>
  <links-page>
    <card title="Deans">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row" v-for="i in range(1, deans.length+1, 6)">
            <div class="col" v-for="j in range(i, i+6 < (deans.length+1) ? i+6 : (deans.length+1))">
              <card-testimonial :image="deans[j-1].image" :name="deans[j-1].name"
                :desig="deans[j-1].role + ' ' + deans[j-1].designation">
                <i class="fa fa-envelope"></i><br>
                <strong>{{ deans[j-1].email }}</strong><br>
                <i class="fa fa-address-book"></i><br>
                <strong>+91-343-{{ deans[j-1].phone }}</strong></br>
                <strong>+91-{{ deans[j-1].alternate_phone }}</strong></br>
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
  name: "Deans",
  data () {
    return {
      deans: {}
    }
  },
  created () {
    console.log(range(3))
    axios.get(genBackendURL("administration/deans"))
         .then(response => {
           this.deans = response.data.results
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
