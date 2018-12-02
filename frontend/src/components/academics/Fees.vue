<template>
  <links-page>
    <card title="Academic Fees" class="list-group list-grations">
      <ul class="list-group list-gr">
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/Fee Structure for PhD programme at National Institute of Technology Durgapur for the admission year of 2018-2019.pdf">Fee structure for PhD programme at National Institute of Technology Durgapur for the admission year of 2018-19</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/Fee structure for B.Tech, B.Tech & M.Tech(Dual degree) programme at National Institute of Technology Durgapur for the admission year of 2018-2019.pdf">Fee structure for B.Tech, B.Tech & M.Tech(Dual degree) programme at National Institute of Technology Durgapur for the admission year of 2018-2019</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/Fee structure for Post-Graduate programme at National Institute of Technology Durgapur for the admission year of 2018-2019.pdf">Fee structure for Post-Graduate programme at National Institute of Technology Durgapur for the admission year of 2018-2019</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/FEE STRUCTURE FOR B.TECH, B.TECH & M.TECH (DUAL DEGREE), INTEGRATED M.SC PROGRAMME AT NIT DURGAPUR FOR THE ADMISSION YEAR OF 2017-2018.pdf">Fee Structure For B.TECH, B.TECH & M.TECH (Dual Degree), Integrated M.SC Programme At NIT Durgapur For The Admission Year Of 2017-2018</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/FEE STRUCTURE FOR POST-GRADUATE PROGRAMME AT NIT DURGAPUR FOR THE ADMISSION YEAR OF 2017-2018.pdf">Fee Structure For Post-Graduate Programme At NIT Durgapur For The Admission Year Of 2017-2018</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/FEE STRUCTURE FOR Ph.D PROGRAMME AT NIT DURGAPUR FOR THE ADMISSION YEAR OF 2017-2018.pdf">Fee Structure For Ph.D Programme At NIT Durgapur For The Admission Year Of 2017-2018</a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'

export default {
  name: "Fees",
  data () {
    return {
     
    }
  },
  created () {
    
        this.$emit('hideloader', true)        
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
