<template>
  <links-page>
    <collapse-list>
      <card-collapse v-if="members" title="Senate Members" :show="true">
        <div class="row bgcustom">
          <card-testimonial v-for="(person, i) in members" :key="i"
            class="black-text"
            :image="person.image"
            :name="person.name"
            :desig="person.designation">
            <strong>{{ person.role }}</strong></br>
            {{ person.address }}</br>
          </card-testimonial>
        </div>
      </card-collapse>
      <card-collapse title="Senate" :show="true">
        <notice-list :noticelist="meetings" />
      </card-collapse>
    </collapse-list>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardCollapse from '@/components/CardCollapse'
import CollapseList from '@/components/CollapseList'
import CardTestimonial from '@/components/CardTestimonial'
import NoticeList from '@/components/NoticeList'
import { genBackendURL } from '@/common.js'

export default {
  name: "Senate",
  data () {
    return {
      members: [],
      meetings: [],
      paginate: ['meetings'],
    }
  },
  created () {
    axios.get(genBackendURL("administration/senate"))
         .then(response => {
           this.meetings = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })

    axios.get(genBackendURL("administration/allmember"))
        .then(response=> {
          this.members = response.data.senatemem
          this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    CardCollapse,
    CollapseList,
    CardTestimonial,
    NoticeList
  }
}
</script>
<style scoped="scoped">
  .bgcustom{
    background: #f2f2f2 !important;
  }
</style>
