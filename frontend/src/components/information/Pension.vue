<template>
  <links-page>
    <card title="Pensioners' Corner">
      <ul class="list-group list-gr">
        <li>
          <!--<a class="list-group-item" target="new" :href="nba.file">
            <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ nba.date }} </span>&nbsp; {{ nba.title }}
          </a>-->
          <a class="list-group-item" target="new" href="nitdgp.ac.in/AllPDF/Circular Dated 06.11.2015.pdf">Circular Dated 06.11.2015</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="nitdgp.ac.in/AllPDF/Life Certificate.pdf">Pensioner's/Family Pensioner's Life Certificate</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="nitdgp.ac.in/AllPDF/Pro Forma for Restoration of Commuted Portion of Pension After 15 Years from the Date of Commutation.pdf">Pro Forma for Restoration of Commuted Portion of Pension After 15 Years from the Date of Commutation</a>
        </li>
        <li>
          <a class="list-group-item" target="new" href="nitdgp.ac.in/AllPDF/Pro Forma for Additional Quantum of Pension.pdf">Pro Forma for Additional Quantum of Pension</a>
          <a class="list-group-item" target="new" href="nitdgp.ac.in/AllPDF/pensioner conner0001.pdf">FMA Undertaking Format </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: "Pension",
  data () {
    return {
      
    }
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
