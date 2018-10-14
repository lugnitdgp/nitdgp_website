<template>
  <links-page>
    <div class="col black-text" v-for="(club,index) in clubs">
      <div class="modal fade" :id="'basicExampleModal'+index" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 style="color:black;" class="modal-title" id="exampleModalLabel">{{club.name}}</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" v-html="club.description" style="color:black;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <card title="Student Clubs">
      <div class="carousel-inner person-list" role="listbox">
        <div class="carousel-item active">
          <div class="row">
            <card-testimonial v-for="(club, i) in clubs" :key="i"
              class="black-text"
              :image="club.image"
              :name="club.name">
              <strong>Description</strong><br>
              <a style="font-weight:normal!important;" data-toggle="modal" :data-target="'#basicExampleModal'+i" v-html="stripDesc2(club.description)"></a><br>
              <i class="fa fa-globe"></i><br>
              <strong><a :href="club.link">{{ club.link }}</a></strong><br>
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
import { genBackendURL,stripDesc2 } from '@/common.js'

export default {
  name: "Students",
  data () {
    return {
      clubs: {}
    }
  },
  methods: {
    stripDesc2: stripDesc2
  },
  created () {
    axios.get(genBackendURL("activities/student-clubs"))
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
