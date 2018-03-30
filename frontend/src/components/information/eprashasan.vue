<template>
	<div class="l1 page-type-links">
		<!-- CONTENT -->
		<div class="card">
		  <a class="card-header white-text">e-Prashasan@NITDGP</a>
		  <div class="card-body">
		      <div class="card-text">
		        <p>For Intranet users <strong><a href="http://172.16.5.56:8080/Campus/" target="_blank">Login</a></strong></p>
		        <strong>Objective :</strong><br>
		        We should be able to perform all of our necessary office tasks from a laptop or a Desktop Computer at office or anywhere with the help of Information Communication Technology (ICT). ICT is the tool which can deliver the job quickly, transparently, with accountability and reliability. The job can also be performed at anytime, anywhere, precisely by 24x7. It can perform more jobs in less time when it compares with manual operation.
		        <br>
		        <strong>Software Overview:</strong><br>
		        The Institute Automation Software of National Institute of Technology Durgapur e- Prashasan having two ends operation, one is Front End another is Back End operation.<br><br>
		        <ul>
		          <li>Academics</li>
		          <li>HRMS</li>
		          <li>Purchase</li>
		          <li>Accounts</li>
		          <li>Maintainance</li>
		          <li>Despatch</li>
		          <li>Academics</li>
		          <li>HRMS</li>
		          <li>Purchase</li>
		          <li>Accounts</li>
		          <li>Maintainance</li>
		          <li>Despatch</li>
		        </ul>
		        In Back end, Administrator module is to be used by the Administrator i.e. who will be maintaining the e-Prashasan, the name of the module: Administrator.
		      </div>
		  </div>
		</div>
	</div>
</template>
<script>
export default {
  name: 'Eprashasan',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
