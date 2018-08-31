<template>
	<links-page>
    <card title="Overview">
      <div>
        Since its inception in 1960, Regional Engineering College, Durgapur, as it was known then, strove to inculcate the spirit of academic
        fervour and excel in different domains of knowledge.<br>
        It has been elevated to the status of a National Institute of Technology and has since crossed the milestone of its first fifty years of
        existence as an Institute of National Importance. It has tried to instil in the students the enthusiasm of the past as well as the impulse
        to reach beyond. With this insignia of excellence, the institute has expanded its horizons and now the students propel themselves to achieve g
        reat academic feats with a focus on innovation.<br>
        National Institute of Technology, Durgapur the only one of its kind in West Bengal has surpassed many milestones and created an ambience of
        academic excellence.<br>
        Normally the placements in NITD commence in the beginning of the final year (Seventh Semester) i.e. in the month of July. Prior to this,
        an invitation is sent to all previous recruiters in the month of May. Along with the invitation a form is provided seeking the company
        profile & information ( CPI Form). After getting the willingness from the companies, the CPI Form is displayed in the notice Board.
        On the allotted day the company visits the campus, makes pre-placement talk, conducts tests and interviews of the willing candidates and
        selects the best . The students follow the placement policy of the institute which is available in the placement Portal.<br>
        The industries which approach the institute can be broadly categorized as :
        <br><br></p>
        <ul class="list">
          <li>Core Engineering industries</li>
          <li>Software / IT Industries</a></li>
          <li>Manufacturing Industries</li>
          <li>Consultancy Firms</li>
          <li>Management Organizations</a></li>
          <li>Management Organizations</li>
          <li>R &amp; D laboratories etc</li>
          <li>Public Sector Undertakings</li>
          <li>Academic Institute</li>
        </ul>
        The Placement Office is assisted by a committee comprising of representatives of students from the under-graduate and post-graduate streams.
        <br><br>The internship is looked after by Faculty -in-charge (Training) </a>
      </div>
    </card>
    <card title="Placement Activities and Statistics">
      <div>
        <ul class="list-group list-gr">
          <li v-for="link in docs">
            <a class="list-group-item" v-if="link.file" :href="link.file" target="new">
              {{ link.title }}
            </a>
            <a class="list-group-item" v-if="link.url" :href="link.url" target="new">
              {{ link.title }}
            </a>
          </li>
        </ul>
      </div>
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import axios from 'axios'
import { backURL, genBackendURL } from '@/common.js'

export default {
  name: 'Research',
  data () {
    return {
      docs: [],
      backURL: backURL
    }
  },
  created () {
    axios.get(genBackendURL('activities/placement-links'))
         .then(response => {
           this.docs = this.docs.concat(response.data.results)
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL('activities/placement'))
         .then(response => {
           this.docs = this.docs.concat(response.data.results)
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
