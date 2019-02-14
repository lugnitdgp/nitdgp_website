<template>
  <links-page>
    <card title="Reservation Rosters">
    	<div style="border: 2px solid #001333;padding: 10px;text-align: justify;">
    		All concerned are hereby requested to take into consideration the institute level reservation rosters of 31-Dec-2017 and 31-Dec-2018. Errors and omissions if any, may be brought to the notice of the Deputy Registrar (Establishment) by 18-Feb-2019 with proper justification.

    		</div><br>
      <ul class="list-group list-gr">
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/roster/ROSTER_2017(amended).pdf">Reservation Roster of 31.12.2017</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/roster/ROSTER_2018.pdf">Reservation Roster of 31.12.2018</a>
        </li>
        
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: "Rroster",
  data () {
    return {
      
    }
  },  
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
