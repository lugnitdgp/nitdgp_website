<template>
  <links-page>
    <card title="Advanced Material (AM)">
    	<div style="border: 2px solid #01576A;border-radius: 12px;margin-bottom: 5px;text-align: justify;" class="descbox">
        <h2 style="color: #FFF;width: 100%;">Introduction</h2>
          <p style="padding: 10px;">
            The Centre of Excellence in Advanced Materials at NIT Durgapur has been established as a joint venture between the departments of Physics & Metallurgical & Materials Engineering, in 2013 through a generous grant of the MHRD, Govt. Of India under its Technical education quality improvement (TEQIP-II) program. The grant was received in response to a proposal prepared by its two principal investigators, Dr. A. K. Chakraborty and Prof. D. K. Mondal with the help of several other faculty members under the active guidance of the Dean (R&C) and the honourable Director. Since inception, the centre has been run by the able leadership of the two coordinators which has resulted in the recruitment of six PhD students and procurement of several state of the art equipment including a field emission scanning electron microscope, atomic force microscope, solar simulator etc. The centre has also organised one international conference and a few national short courses.
        </p>
      </div>
      <div style="border: 2px solid #01576A;border-radius: 12px;margin-bottom: 5px;text-align: justify;" class="descbox">
        <h2 style="color: #FFF;width: 100%;">Research</h2>
          <p style="padding: 10px;">
            The centre's research is focused on the following main areas: 
            <ul>
              <li>Carbon nanotube and graphene for development of advanced supercapacitors, photovoltaic cells, gas  sensors and lightweight polymer based composites.</li>

              <li>Multiferroic materials </li>

              <li>Photonic materials</li>

              <li>Nanocomposites synthesis and applications</li>

              <li>Aluminium alloy based Nanocomposites</li>

            <li> Molecular dynamics simulation of alloy based composites.</li>
           </ul> 
          The centre's aim is to establish its identity in the region for providing state of the art infrastructure for advance material research.
        </p>
      </div>
      <div style="border: 2px solid #01576A;border-radius: 12px;margin-bottom: 5px;text-align: justify;" class="descbox">
        <h2 style="color: #FFF;width: 100%;">Facilities</h2>
          <p style="padding: 10px;">
            The CoE Synthesis Lab is engaged in the synthesis of nano-particles and subsequent design of nanocomposites for diverse. The CoE Synthesis Lab is under construction and houses the following facilities:-
          </p>
          <p><u><h3 class="text-center">CoE Synthesis Lab</h3></u></p>
          <div class="text-center">
            <img src="http://nitdgp.ac.in/AllPDF/spincoater.jpg" class="img img-responsive text-center" style="height:250px;width: 50%;margin-left: 2%;">
            <p class="text-center">Spin Coater</p>
          </div>
          <div class="text-center">
            <img src="http://nitdgp.ac.in/AllPDF/glovebox.jpg" class="img img-responsive img-thumbnails text-center" style="height:250px;width: 50%;margin-left: 2%;">
            <p class="text-center">Glove Box</p>
          </div>
          <div class="text-center">
            <img src="http://nitdgp.ac.in/AllPDF/rotaryvacum.jpg" class="img img-responsive img-thumbnails text-center" style="height:250px;width: 50%;margin-left: 2%;">
            <p class="text-center">Rotary Vacuum Evaporator</p>
          </div>
          <div class="text-center">
            <ul>
              <li>Stirrer Hot Plate</li>
              <li>CVD ( yet to be installed)</li>
              <li>Thermal Evaporator ( yet to be installed)</li>
              <li>Semi Micro Balance ( yet to be installed)</li>
            </ul>
          </div>
          <p><u><h3 class="text-center">CoE Characterization Lab</h3></u></p>
          <p style="padding: 10px;">
            The Lab is currently under construction and it will be mostly engaged in characterizing the surface profile of thin films, electrochemical and electrical properties of nanocomposites for the purpose of energy harvesting and storage. The main objective is to develop an energy application centre at NIT Durgapur. The Lab presently has the following facilities
          </p>
          <div class="text-center">
            <img src="http://nitdgp.ac.in/AllPDF/atomicforce.jpg" class="img img-responsive text-center" style="height:250px;width: 50%;margin-left: 2%;">
            <p class="text-center">Atomic Force Microscopy</p>
          </div>
          <div class="text-center">
            <img src="http://nitdgp.ac.in/AllPDF/galvanostar.jpg" class="img img-responsive img-thumbnails text-center" style="height:250px;width: 50%;margin-left: 2%;">
            <p class="text-center">Potentiostat/ Galvanostat</p>
          </div>
          
          <div class="text-center">
            <ul>
              <li>FESEM ( Yet to be installed)</li>
              <li>Li Ion Battery Fabrication & Testing Unit (yet to be installed)</li>
              <li>Solar Simulator (Yet To be Installed)</li>
              <li>LCR Meter (Yet To be Installed)</li>
              <li>Gas Sensor System ( yet to be installed)</li>
            </ul>
          </div>
        </div>
        <!--<div style="border: 2px solid #01576A;border-radius: 12px;margin-bottom: 5px;text-align: justify;" class="descbox">
        <h2 style="color: #FFF;width: 100%;">Members</h2>
          <p style="padding: 10px;">

          </p>
      </div>-->
    </card>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
// import CollapseList from '@/components/CollapseList'
// import CardCollapse from '@/components/CardCollapse'


export default {
  name: 'Am',
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