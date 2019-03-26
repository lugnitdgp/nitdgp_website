<template>
  <links-page>
    <card title="Intellectual Property Policy">
      <div class="col-12 caro">
        <Carousel :slides="slides"></Carousel>
      </div>
      <br>
      <div class="mtitle">Introduction</div>
          <div class="mbody">
            National Institute of Technology Durgapur (NITD), an institute of national importance is dedicated to excellence in teaching and research over the years. Excellence in research and education, exchange, and dissemination of knowledge are guiding principles of NITD. These activities may lead to generation of Intellectual Property (IP), which needs to be protected, developed, transferred and commercialized for the benefit of the society. Our country will highly be benefited socioeconomically due to commercial exploitation of such IPs.National Institute of Technology Durgapur, therefore, encourages due recognition, protection and utilization of such inventions through patenting and subsequent technology transfer to potential organizations for commercial exploitation. This is expected to yield economic benefits to the Institute thereby strengthening financial support base for research activities and economic incentive to the inventors. This will eventually ignite the passions for research and innovations and contribute to maintain the country’s growth trajectory in innovation and to improve India’s ranking in Global Innovation Index (GII). The policy laid down in this document is expected to fulfill the commitment of the Institute for constant encouragement towards innovation and appreciation of the innovators. It will also enable the Institute to make beneficial use of such developed intellectual property for the greatest possible benefit to the public, the Institute, and the creators/inventors involved. 

      </div><br>
      <div class="mtitle">Important Informations of Intellectual Property Management</div>
      <div class="mbody">
        <ul class="list-group list-gr">
          <li><a class="list-group-item" href="http://nitdgp.ac.in/AllPDF/IPR/Committee_IPR.pdf" target="new">Intellectual Property Management Committee (IPMC)</a></li>
          <li><a class="list-group-item" href="http://nitdgp.ac.in/AllPDF/IPR/FORMS_IPR.pdf" target="new">Forms for Patent related Applications</a></li>
          <li><a class="list-group-item" href="http://nitdgp.ac.in/AllPDF/IPR/IP_POLICY_2018_NITD.pdf" target="new">Intellectual Property Policy and Guidelines</a></li>
        </ul>
      </div>
      
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'


export default {
  name: 'Ipr',
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
<style scoped="scoped">
  .list-gr .contact-col{
    min-width: 100%;
    max-width: 100%;
    padding-bottom: 15px;
    color: #fff;
  }
  .col {
    -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -ms-flex-positive: 1;
    flex-grow: 1;
    max-width: 100%;
  }
  .mtitle{
    background-color: #001333;
    color: #fff;
    padding: 10px;
    text-align: center;
    border: .25px solid #001333;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
  }
  .mbody{
    border: 2px solid #001333;
    padding: 10px;
    text-align: justify;
  }
  @media screen and (max-width: 1200px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
  @media screen and (max-width: 800px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
</style>