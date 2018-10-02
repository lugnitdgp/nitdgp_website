<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Central Instruments Facilities</a>
      <div class="card-body">
	<div class="img-wrap">
	  <img src="/static/img/xray.jpg" width="100%">
	</div>
	<div>
	  <div align="justify">
	    <font>
	      <b> XRD Equipment:</b> PANalytical XPert Pro Basic X-ray Powder Diffraction Package with all accessories and soft wares. Offers Defect studies of Metallic Alloys including Rietveld Analsis, Phase Analysis, Chemical Analysis for both inorganic and organic specimen, Microstructural Parameters. Compatible for samples of solid flat specimens, solid powders, liquid specimen, thin films etc.
	    </font><br>
	    <font><br>
	      <b>SEM with EDS Equipment: SEM: </b>S-3000N, HITACHI-JAPAN, EDS : THERMO-NORAN-USA, SIX-NSS 200 with PC Monitor, Softwares etc. Offers morphological and surface studies of Metallic Alloys, semi-conducting, insulating and biological samples. Chemical analysis, Phase analysis, X-ray mapping etc. on the EDS.
	    </font>
	  </div>
	</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Cif',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
