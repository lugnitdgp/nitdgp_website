<template>
  <links-page>
    <collapse-list>      
      <card-collapse title="Minutes of FC Meeting" :show="true">
        <notice-list :noticelist="ifc_docs" />
      </card-collapse>
      <card-collapse v-if="ifc_members" title="FC Members" :show="false">
        <div class="row bgcustom">
          <card-testimonial v-for="(person, i) in ifc_members" :key="i"
            class="black-text"
            :image="person.image"
            :name="person.name"
            :desig="person.designation">
            <strong>FC</strong></br>
            {{ person.address }}</br>
          </card-testimonial>
        </div>
      </card-collapse>
      <card-collapse title="Minutes of BWC Meeting" :show="false">
        <notice-list :noticelist="bwc_docs" />
      </card-collapse>
      <card-collapse v-if="bwc_members" title="BWC Members" :show="false">
        <div class="row bgcustom">
          <card-testimonial v-for="(person, i) in bwc_members" :key="i"
            class="black-text"
            :image="person.image"
            :name="person.name"
            :desig="person.designation">
            <strong>B&WC</strong></br>
            {{ person.address }}</br>
          </card-testimonial>
        </div>
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
  name: "Calendar",
  data () {
    return {
      bwc_members: [],
      ifc_members: [],
      bwc_docs: [],
      paginate: ['bwc_docs'],
      ifc_docs: [],
      paginate: ['ifc_docs']
    }
  },
  created () {
    let flag = false
    axios.get(genBackendURL("administration/bwc"))
         .then(response => {
           this.bwc_docs = response.data.results
           if (flag)
             this.$emit('hideloader', true)
           flag = true
         })
         .catch(e => {
           console.log(e)
         })
     axios.get(genBackendURL("administration/ifc"))
          .then(response => {
            this.ifc_docs = response.data.results
           if (flag)
              this.$emit('hideloader', true)
            flag = true
          })
          .catch(e => {
            console.log(e)
          })

     axios.get(genBackendURL("administration/allmember"))
        .then(response=> {
          this.bwc_members = response.data.bwcmem
          console.log(this.bwc_members)
          this.ifc_members = response.data.ifcmem
          console.log(this.ifc_members)
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