<template>
  <links-page>
    <card title="Officers">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <card-testimonial v-for="(officer,i) in officers" :key=i
              class="black-text"
              :image="officer.photo"
              :name="officer.name"
              :desig="officer.designation">
              <i class="fa fa-envelope"></i><br>
              <strong>{{ officer.email }}</strong><br>
              <i class="fa fa-address-book"></i><br>
              <strong>+91-{{ officer.mobile }}</strong></br>
            </card-testimonial>
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
  name: "Officers",
  data () {
    return {
      officers: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/officers"))
         .then(response => {
           this.officers = response.data.results
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
