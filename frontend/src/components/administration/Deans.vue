<template>
  <links-page>
    <card title="Deans">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <div class="col" v-for="dean in deans">
              <div class="card testimonial-card">
                <div class="card-up">
                </div>
                <div class="avatar mx-auto">
                  <img :src="dean.image" class="rounded-circle img-responsive">
                </div>
                <div class="card-body-in">
                  <h4 class="card-title mt-1"><strong>{{ dean.name }}</strong></h4>
                  <hr>
                  <strong> {{ dean.role }} {{ dean.designation }} </strong><br>
                  <p class="min-profile">
                    <i class="fa fa-envelope"></i><br>
                    <strong>{{ dean.email }}</strong><br>
                    <i class="fa fa-address-book"></i><br>
                    <strong>+91-343-{{ dean.phone }}</strong></br>
                    <strong>+91-{{ dean.alternate_phone }}</strong></br>
                  </p>
                </div>
              </div>
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
import { genBackendURL } from '@/common.js'

export default {
  name: "Deans",
  data () {
    return {
      deans: {}
    }
  },
  created () {
    axios.get(genBackendURL("administration/deans"))
         .then(response => {
           this.deans = response.data.results
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
