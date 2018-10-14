<template>
  <links-page>
    <collapse-list>
      <card-collapse v-if="bogs" title="Board of Governors" :show="true">
        <div class="row">
          <card-testimonial v-for="(person, i) in bogs" :key="i"
            class="black-text"
            :image="person.image"
            :name="person.name"
            :desig="person.role">
            <strong>{{ person.designation }}</strong></br>
            {{ person.address }}</br>
          </card-testimonial>
        </div>
      </card-collapse>
      <card-collapse v-if="bog_agendas" title="Agenda of BOG Meetings">
        <notice-list :noticelist="bog_agendas" />
      </card-collapse>
    </collapse-list>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import CardCollapse from '@/components/CardCollapse'
import CollapseList from '@/components/CollapseList'
import CardTestimonial from '@/components/CardTestimonial'
import NoticeList from '@/components/NoticeList'
import { range, genBackendURL } from '@/common.js'

export default {
  name: "Bog",
  data () {
    return {
      bogs: [],
      bog_agendas: [],
      paginate: ['bog_agendas']
    }
  },
  created () {
    let count_axios = 0
    axios.get(genBackendURL("administration/bog"))
         .then(response => {
           for (let k in response.data) {
             this.bogs = this.bogs.concat(response.data[k])
           }
           if (count_axios == 1) {
             this.$emit('hideloader', true)
           }
           count_axios++
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL("administration/bogagenda"))
         .then(response => {
           this.bog_agendas = response.data.result
           if (count_axios == 1) {
             this.$emit('hideloader', true)
           }
           count_axios++
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
    CardCollapse,
    CollapseList,
    CardTestimonial,
    NoticeList
  }
}
</script>
