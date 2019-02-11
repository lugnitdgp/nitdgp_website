<template>
  <links-page>
    <card title="National Academic Depository (NAD)">
    	<div style="border: 2px solid #001333;padding: 10px;text-align: justify; color: #000;">
		      <p>National Academic Depository (NAD) is an important initiative of Government of India facilitated by Ministry of Human Resource Development to facilitate issuance and storage of academic awards to students in an online depository system on the pattern of Securities Depository.</p>
		      <p>The vision of National Academic Depository (NAD) is to provide an online storehouse of all academic awards. National Academic Depository (NAD) is a 24X7 online storehouse of all academic awards viz.certificates, diplomas, degrees, mark-sheets etc. duly digitized and lodged by academic Institutions / Boards / Eligibility Assessment Bodies. NAD not only ensures easy access to and retrieval of an academic award but also validates and guarantees its authenticity and safe storage.</p>
		      <p>National Academic Depository comprises of two interoperable digital depositories viz. CDSL Ventures Limited (CVL) and NSDL Database Management Limited (NDML). These digital depositories have ensured hardware, network facilities, and software of prescribed quality for smooth and secured operationalization of NAD.</p>
		      <p>This is an initiative of Government of India under “Digital India” program to empower the students with online, permanent access. The certificates are digital and verifiable and hence are easily trusted by all users. NAD is a significantly beneficial initiative for students.</p>
		      <span style="color: green;">For more details related to student registration, certificate verification etc. please log on to -</span>
		      <ul>
		      	<li><a href="http://nad.gov.in/" target="_blank">http://nad.gov.in/</a></li>
		      	<li><a href="https://nad.ndml.in/" target="_blank">https://nad.ndml.in/</a></li>
		      </ul>
		  </div><br>
      <div style="border: 2px solid #001333;padding: 10px;text-align: justify;color: #000;">
      	<ul class="list-group list-gr">
           <li>
            <a class="list-group-item" target="new" href="http://nitdgp.ac.in/AllPDF/NAD FAQs.pdf">NAD FAQs</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/1n0Erc4cFPf8vHIwGKOyUvjLvr2dN8gT7/view">National Academic Depository - Introduction</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/1ySuwF9P9xgt_rSN4H3VPhdRNoyeCo_gA/view">STUDENT-Registration Aadhaar Based</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/1-FA4gJHzy0H_ZVolH3xyVacHV6fhUXeI/view">Student-Registration NAD ID Based</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/11sJAK3-c42xvgqUVZHbucJSTKB-5mm9F/view">Student-Login and Sharing a Certificate</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/1Yw41bExPJe4lID-poMlrzn4QgaayooxU/view">Verifier- Placing a Verification Request</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/1KkSpgl4Ng2z_weHFESuCjYAVBMukWnnn/view">Student- Verification Request Approval</a>
           </li>
           <li>
            <a class="list-group-item" target="new" href="https://drive.google.com/file/d/1fxopBT0YpiHAhmxP-WvkZv2pOlg_M-HY/view">Verifier- Viewing Certificate Post Student Approval</a>
           </li>
        </ul><br><br>
		<span style="color: green;">For more information please send email to -</span> egov@nitdgp.ac.in
      </div>
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'



export default {
  name: 'Nad',
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
<style >
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
  h2{
    height: 40px;
    background: #01576A;
    display: block;
    width: 100%;
    font-size: 20px;
    color: #FFF;
    text-align: center;
    line-height: 40px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
   .descbox:hover{
    background: #C7ECF5;

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