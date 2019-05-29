<template>
  <links-page>
    <h3 class="font-weight-bold text-center mb-2 mt-4">Search results</h3>
    <div v-if="notices.length||faculty.length">
      <ul class="nav nav-tabs ">
        <li class="nav-item">
          <a v-bind:class="{ 'active': notices.length }" class="nav-link" data-toggle="tab" href="#panel1" role="tab">Notices</a>
        </li>
        <li class="nav-item">
          <a v-bind:class="{ 'active':!notices.length&&faculty.length }" class="nav-link" data-toggle="tab" href="#panel2" role="tab">Faculty</a>
        </li>
      </ul>
      <div class="tab-content card">
        <div v-bind:class="{ 'in show active': notices.length }" class="tab-pane fade" id="panel1" role="tabpanel">
          <notice-list :noticelist="notices" />
        </div>
        <div v-bind:class="{ 'in show active': !notices.length&&faculty.length }" class="tab-pane fade" id="panel2" role="tabpanel">
          <div class="container-fluid mt-2">
            <div class="row">
              <card-testimonial v-for="(person, i) in faculty" :key="i"
                class="staffs"
                :name="person.name"
                :image="person.image"
                :desig="person.designation">
              <!--<strong>
                <span>Laboratory Experience {{ person.experience }}</span>
              </strong><br>-->
              <i class="fa fa-envelope" />&nbsp;&nbsp;&nbsp;
              <strong>{{ person.email }}</strong><br>
              <i class="fa fa-phone" />&nbsp;&nbsp;&nbsp;
              <strong>+91-{{ person.mobile }}</strong></br>
              <strong>
                <span class="blue-text">Joined the Institute in {{ convertYear(person.joining_year) }}</span>
              </strong>
            </card-testimonial>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="container text-center pt-2">
      No results found. Please search again.
    </div>
  </links-page>
</template>

<script>
import NoticeList from '@/components/NoticeList'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import axios from 'axios'
import { backURL } from '@/common.js'

export default {
  name: 'SearchResults',
  data() {
    return {
      notices: [],
      faculty: []
    }
  },
  created () {
    axios.all([
      axios.get(backURL+'/search/notice/?q='+this.$route.query.q),
      axios.get(backURL+'/search/faculty/?q='+this.$route.query.q)
    ]).then(axios.spread((notice_results, faculty_results) => {
            this.notices=notice_results.data.results;
            this.faculty=faculty_results.data.results;
            this.$emit('hideloader', true)
      }))
      .catch(e => {console.log(e)})
  },
  methods: {
    convertYear: function (year) {
      return year == 1959 ? "N/A" : year
    }
  },
  components: {
    NoticeList,
    LinksPage,
    Card,
    CardTestimonial
  }
}
</script>
<style scoped>
  .nav-tabs {
    padding: 0px;
  }
</style>
