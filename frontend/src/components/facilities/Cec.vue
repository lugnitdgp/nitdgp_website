<template>
	<div class="l2-srcc container-fluid">
		<sp-card containerclass="l2-card" bodyclass="text-center">
			<p slot="header" class="tile-title-text">
				<a href="#" class="white-text sh-dex">Continuing Education Cell </a>
				<a href="#" class="white-text sh-mob notranslate">CEC</a>
			</p>
			<div class="tabs-wrapper up-content mx-auto srcctab">
				<ul class="nav classic-tabs" role="tablist">
					<li class="nav-item">
						<a class="nav-link waves-light active" data-toggle="tab" href="#li1" role="tab" >CEC-Home</a>
					</li>
					<li class="nav-item">
						<a class="nav-link waves-light" data-toggle="tab" href="#" role="tab" v-on:click="teqipcall" >TEQIP</a>
					</li>
					<li class="nav-item">
						<a class="nav-link waves-light" data-toggle="tab" href="#li3" role="tab" >Guidelines</a>
					</li>
					<li class="nav-item">
						<a class="nav-link waves-light" data-toggle="tab" href="#li4" role="tab" >Different Forms</a>
					</li>
					<li class="nav-item">
						<a class="nav-link waves-light" data-toggle="tab" href="#li5" role="tab" >Members</a>
					</li>
					<li class="nav-item">
						<a class="nav-link waves-light" data-toggle="tab" href="#li6" role="tab" >Contact</a>
					</li>
				</ul>
			</div>
			<div class="tab-content card down-content">
				<div class="tab-pane fade show active big-list row newscaro" id="li1" role="tabpanel" aria-labelledby="li1-list">
					<div class="row">
						<div class="col-4 mobiledisplay" style="margin-top: 20px;">
							<div class="mpannel">
								<div class="mod-title">Programme</div>
								<div class="mod-body">
									<a href="#">National Conference on Recent Development in Chemistry, December 17-19, 2018 <span style="color: red;">[Closed]</span></a>
									<hr>
								</div> <br>
								<div class="mod-title">Downlods</div>
								<div class="mod-body">
									<a href="https://nitdgp.ac.in/nitdcec/files/forms/CEC Regulations.pdf" class="aligncenter">CEC All Forms</a>
									<hr>
								</div>
								<br>
								<div class="mod-title">Latest Updates</div>
								<div class="mod-body">
									<a href="https://nitdgp.ac.in/nitdcec/files/forms/CEC_WORKFLOW_15.5.18.pdf" class="aligncenter">CEC Workflow</a>
									<hr>
								</div>
							</div>
						</div>
						<div class="col-8 mobiledisplay">
							<Carousel :slides="slides"></Carousel>
							<br>							
						</div>
						<div class="mod-title">Welcome to Continuing Education Cell</div>
							<div class="mod-body">
								<p class="text-left" style="padding: 4px;">It is the cell through which all the short term courses, certificate courses, training programmes, students’ internship etc. and TEQIP III activities will be co-ordinated and will be monitored by Institute nominated committee. The nominated members of the committee will have tenure of two years. The monitoring committee constitutes the following members:
									<ul>
										<li>Chairman-CEC (Chairman)</li>
										<li>Dean (Academic), Member</li>
										<li>Dean (R & C), Member</li>
										<li>Two Senate members as nominated by Senate, Member</li>
										<li>Two non-Senate faculty members nominated by Director, Member</li>
										<li>Preceding Chairman of CEC (tenure of 1 year), Member</li>
									</ul>
								Any program to be organized will have a Co-ordinator/Organizing Secretary. The coordinator may propose the name of another faculty member, an academic staff member (at a grade equal to or above that of an Assistant Professor) to serve as a co–coordinator. The co– coordinator may be given financial powers only in the absence of the coordinator against a written request from the coordinator.</p>
							</div>
					</div>
				</div>
				<div class="tab-pane fade big-list" id="li2" role="tabpanel" aria-labelledby="li2-list"></div>
				<div class="tab-pane fade big-list" id="li3" role="tabpanel" aria-labelledby="li3-list">
					<div class="mod-title">GENERAL GUIDELINES</div>
					<div class="mod-body" style="text-align: justify;padding: 5px 4px;">
						<ol>
							<li>All the programmes under CEC are necessarily to be planned well in advance. Any programme without prior approval would not be funded.</li>
							<li>The programmes (workshop/ short term courses/conferences/training) less than 20-25 external participants are not advisable to conduct and it can be postponed with due approval for better participation.</li>
							<li>Any faculty members wants to organize a Short Term Programme (STP) is required to apply in prescribed format on an invitation from CEC or as per terms and conditions of any external sponsored programme. Interval of invitation for STP under TEQIP III will be normally six months and any application without invitation under TEQIP III would not be accepted.</li>
							<li>The applications received for different activities will be screened and approved as applicable.</li>
							<li> Norms of expenditure for activities under TEQIP III may vary time to time as per requirement.</li>
							<li>Presently, the fees for programme co-ordinator will be Rs. 15,000/- for 3 days programme and Rs. 20,000/- for 5 days programme (which includes remuneration for delivering lectures also) but not 10% of estimated expenditure of the said programme.</li>
						</ol>
					</div>
				</div>
				<div class="tab-pane fade big-list" id="li4" role="tabpanel" aria-labelledby="li4-list">
					<div class="mod-title">Fees Details</div>
					<div class="mod-body">
					In the case of self-financed courses, conceived and proposed by the Coordinator, he will fix the course fee taking into consideration the duration of the course, the intended quality of instruction and facilities provided to the participants. The fee structure set by the agencies of the Govt. of India (DOPT, AICTE etc.) may serve as the lower limit in fixing the course fees. Boarding and lodging expenses may or may not be included in the gross course fee at the discretion of the Coordinator. The fee structure for participants from academic, Government or charitable institutions and alumni of the Institute may be different from that for participants from industry. The fee payable by participants from abroad may also be different from that by students from India.</div><br>
					<div class="mod-title">Forms Section</div>
					<div class="mod-body">
						<ul class="listdisplay list-group list-gr">
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/CEC_form1.pdf" target="_new">Application Format for Short Term Course</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/CEC_form2.pdf" target="_new">Approval Format of Short Term Course</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/p10.pdf" target="_new">Application Format for the Request for Seed Money Loan</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/p11.pdf" target="_new">Format for Reimbursement for Expenditure</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="files/forms/CEC_form3.pdf" target="_new">Format for Remuneration for Institute Employees</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/CEC_form4.pdf" target="_new">Format for Remuneration paid to Guest Lecturer (Outside NITD)</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/p16.pdf" target="_new">Format for Transfer the Funds to Departmental Development Fund</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/p17.pdf" target="_new">Format for Final Report and Payment of Co-ordinator’s fee</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/p18.pdf" target="_new">Format for Receipt of cheque by Co-ordinator</a></li>
							<li class="liststyle"><a class="linkancher list-group-item" href="https://nitdgp.ac.in/nitdcec/files/forms/p19.pdf" target="_new">Format for Short Term Course Certificate</a></li>
						</ul>
					</div>
				</div>
				<div class="tab-pane fade big-list" id="li5" role="tabpanel" aria-labelledby="li5-list">
					<links-page>
						<card title="Members">
							<div class="row">
								<card-testimonial v-for="(person, i) in members" :key="i" :name="person.name" :image="person.image">
									{{person.designation}}<br>
									{{ person.email }}
								</card-testimonial>
							</div>
						</card>
					</links-page>
				</div>
				<div class="tab-pane fade big-list" id="li6" role="tabpanel" aria-labelledby="li5-list">
					<links-page>
						<card title="Members">
							<div class="row">
								<card-testimonial v-for="(person, i) in contacts" :key="i" :name="person.name" :image="person.image">
									{{person.designation}}<br>
									{{ person.email }}
								</card-testimonial>
							</div>
						</card>
					</links-page>
				</div>
				<div class="tab-pane fade big-list" id="li7" role="tabpanel" aria-labelledby="li7-list"></div>
				<div class="tab-pane fade big-list" id="li8" role="tabpanel" aria-labelledby="li8-list"></div>
				<div class="tab-pane fade big-list" id="li9" role="tabpanel" aria-labelledby="li9-list"></div>
				<div class="tab-pane fade big-list" id="li10" role="tabpanel" aria-labelledby="li10-list"></div>
			</div>
		</sp-card>
	</div>
</template>

<script>
	import axios from 'axios'
	import SpCard from '@/components/SpCard'
	import { genBackendURL, convertNewsfeed } from '@/common.js'
	import CardTestimonial from '@/components/CardTestimonial'
	import Carousel from '../Carousel'
	import LinksPage from '../LinksPage'
	import Card from '../Card'
	export default {
		name: "Cec",
		data () {
			return {
				slides:[
				{primary_caption:"Director's Speech",secondary_caption:"Director's Speech",image:"https://nitdgp.ac.in/nitdcec/images/Directors_Speech1.JPG"}
				],
				members: [
					{name:"Dr. Kartik Chandra Ghanta", email:"kartik.ghanta@che.nitdgp.ac.in", designation:"+91-9434788020", image:"https://nitdgp.ac.in/nitdcec/images/members/kartik_chandra_ghanta.jpg"},
					{name:"Dr. Indrajit Basak", email:"indrajit.basak@me.nitdgp.ac.in", designation:"+91-9434788109",image:"https://nitdgp.ac.in/nitdcec/images/members/i_basak.jpg" },
					{name:"Dr. Ajit Kumar Meikap", email:"ajit.meikap@phy.nitdgp.ac.in" ,designation:"+91-9434788060", image:"https://nitdgp.ac.in/nitdcec/images/members/ajit_kumar.jpg"},
					{name:"Dr. Susmita Dutta", email:"susmita.dutta@che.nitdgp.ac.in" ,designation:"+91-9434788120", image:"https://nitdgp.ac.in/nitdcec/images/members/susmita_dutta.jpg"},
					{name:"Dr. Jayati Dey", email:"deybiswasjayati@gmail.com" ,designation:"+91-9434788173", image:"https://nitdgp.ac.in/nitdcec/images/members/jayati_dey.jpg"},
					{name:"Dr. Bibhash Sen", email:"bibhash.sen@cse.nitdgp.ac.in" ,designation:"+91-9434788161", image:"https://nitdgp.ac.in/nitdcec/images/members/b_sen.jpg"},
					{name:"Dr. Nirmal Kumar Roy", email:"nirmalkumar.roy@ee.nitdgp.ac.in" ,designation:"+91-9434788042", image:"https://admin.nitdgp.ac.in/files/faculty/Nirmal%20Kumar%20Roy/nirmal_kumar.jpg"}
				],
				contacts:[
				{name:"Dr. Kartik Chandra Ghanta", email:"kartik.ghanta@che.nitdgp.ac.in", designation:"+91-9434788020", image:"https://nitdgp.ac.in/nitdcec/images/members/kartik_chandra_ghanta.jpg"}
				]
			}
		},
		created () {
			this.$emit('hideloader', true)
		},
		methods:{
			teqipcall:function(){
				window.location.href='https://nitdgp.ac.in/teqip'
			}
		},
		components: {
			SpCard,
			Carousel,
			LinksPage,
			Card,
			CardTestimonial
		}
	}
</script>
<style>
.card-test {
	min-width: 230px !important;
	min-height: 300px !important;
	max-width: 500px !important;
	max-height: 500px !important;
	padding: 10px !important;
}
.staffs {
	min-width: 200px !important;
	min-height: 300px !important;
	max-width: 500px !important;
	max-height: 500px !important;
	padding: 10px !important;
}
.l2-srcc .sh-mob{
	display: none;
}
.mpannel{

}
.mod-title{
	background: -moz-linear-gradient(left, #1583E0, #D9EEF9);
	background: -o-linear-gradient(left, #1583E0, #D9EEF9);
	background: -webkit-linear-gradient(left, #1583E0, #D9EEF9);
	border-top-left-radius: 8px;
	border-top-right-radius: 8px;
	width: 100%;
	font-size: 20px;
}
.shadow {
	box-shadow: -8px 4px 8px 0 rgba(0, 0, 0, 0.4), -4px 6px 20px 0 rgba(0, 0, 0, 0.4);
}
.mod-body{
	text-align: justify;
	border: 1px solid #1583E0;
	padding: 2px 2px;
}
.aligncenter{
	text-align: center !important;
	margin-left: 35%;
}
.listdisplay{
	display: -ms-flexbox;
	display: flex;
	-ms-flex-direction: column;
	flex-direction: column;
	padding-left: 0;
	margin-bottom: 0;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-orient: vertical;
	-webkit-box-direction: normal;
	-ms-flex-direction: column;
	flex-direction: column;
	padding-left: 0;
	margin-bottom: 0;
}
.liststyle{
	list-style: none;
	width: 100%;
}
.linkancher{
	color: #001333;
	background-color: #e0f7fa;
	margin: 5px 0;
	padding: 3px;
	width: 100%;
}
.linkancher:hover{
	background-color: #001333;
	color: #FFF;
}
.card-up {
	height: 80px !important;
	background: linear-gradient(90deg,#001333,#324e7d) !important;
}
.min-profile {
	font-size: 55%;
	padding-left: 5px;
	padding-right: 5px;
}
.col.testimonial {
	min-width: 200px;
	min-height: 100px;
	max-width: 320px;
	max-height: 500px;
	padding: 7px;
}
@media screen and (max-width: 750px){
	.l2-srcc .sh-mob{
		display: block!important;
	}
	.l2-srcc .sh-dex{
		display: none!important;
	}
	.mobiledisplay {
		-ms-flex: 0 0 100%;
		-webkit-box-flex: 0;
		flex: 0 0 100%;
		max-width: 100%;
	}
	.d-block{
		height: 400px;
	}
}
.l2-srcc {
	margin-top: 20px;
}
@media screen and (max-width: 600px){
	.l2-srcc .tab-content{
		padding-left:5px;
		padding-right:5px;
	}
}
.l2-srcc .l2-card .down-content .big-list .mb-0{
	font-size: 75%;
}
.l2-srcc .l2-card .down-content .tab-pane .tab-content{
	background: none;border:dotted 1px #ECEFF1;
}
.l2-srcc .l2-card {
	background: linear-gradient(#ECEFF1,#B0BEC5);
}
.l2-srcc .l2-card div.tile-title{
	background: #001333;
}
.l2-srcc .l2-card p.tile-title-text{
	color: #ffffff;
}
.l2-srcc .l2-card .down-content{
	background-color:#ffffff;
}
.l2-srcc .l2-card .down-content .pane-text{
	text-align: justify;
	color:#000000;
}
.l2-srcc .l2-card .down-content .pane-title{
	text-align: justify;
	color:#000000;
}
.l2-srcc{
	padding-top: 5em;
	padding-bottom: 1em;padding-right: 1.5%;padding-left: 1.5%;
}
.l2-srcc .card-body .down-content .caros .carousel-title{
	font-size: 180%;
}
.l2-srcc .card-body .down-content .carousel-item .col{
	width: 100%;margin: 5px;max-width: 500px ! important;min-width: 200px !important;
}
.l2-srcc .card-body .down-content #li7 .col{
	min-width: 100%;
}
.l2-srcc .card-body .up-content .classic-tabs .nav-link{
	font-size: 100%;
}
.l2-srcc .card-body .up-content .classic-tabs .nav-item{
	margin: 0;
}
.l2-srcc .card-body .up-content .classic-tabs .nav-item a{
	font-weight: bold;
	padding:10px;
}
.l2-srcc .card-body .down-content #li2 .accordion .card-header{
	border:solid 1px black;
}
.l2-srcc .card-body .down-content .table .th-lg{
	min-width: 5px;
}
.l2-srcc .card-body .down-content .table td{
	font-weight: bold;
}
.l2-srcc .card-body .down-content .table th{
	font-weight: bold;
}
.l2-srcc .card-body .down-content .carousel-inner .col{
	max-width: 20%;margin: 2px;
}
.l2-srcc .card-body .down-content .caros{
	margin-bottom: -45px !important;
}
.l2-srcc .card-body .down-content .min-profile{
	font-size:55%;
	padding-left: 5px;
	padding-right: 5px;
}
.l2-srcc .card-body .down-content #li4 h6{
	margin-top: -1em;
}
.l2-srcc .card-body .down-content .table-wrapper-2{
	display: block;
	max-height: 2500px;
	overflow-y: auto;
	-ms-overflow-style: -ms-autohiding-scrollbar;
}
.l2-srcc .card-body .down-content th{
	background-color: #E0E0E0;
	padding: 6px;
}
.l2-srcc .card-body .down-content td{
	background-color: #F5F5F5;
	padding: 5px;
}
.l2-srcc .card-body .down-content #li7 .tab-content{
	font-size: 80%;
}
.l2-srcc .card-body{
	margin-top: -0.5em;
	margin-bottom: -0.5em;
	margin-left: -0.5em;
	margin-right:-0.5em;
}
.l2-srcc .tile-title-text{
	letter-spacing: 2px;
	font-weight: bold;
	text-align: center;
	vertical-align: middle;
	line-height: 1px;
	color: #ffffff;
}
.l2-srcc .tile-title{
	height: 1px;
}
.l2-srcc .tile-small-text{
	font-size: 90%;font-weight: bold;
}
.l2-srcc .card-body .up-content .classic-tabs{
	background-color: #001333;
}
.l2-srcc .down-content .pills-secondary .nav-link.active{
	background-color: #001333 !important;
	color: #ECEFF1;
}
.l2-srcc .down-content .tab-pane .nav-link{
	background-color: #E0E0E0;
	color: #78909C;
}
.l2-srcc .card-body .down-content #li4 .carousel-indicators li{
	background-color: #001333;
}
.l2-srcc .card-body .down-content #li4 .carousel-indicators li.active{
	background-color: #001333;
}
.l2-srcc .card-body .down-content .carousel-title{
	font-weight: bold;letter-spacing: 2px;font-size: 150%;color:#000000;
}
.classic-tabs li a.active {
	border: 1px solid !important;
	border-radius: 5px;
	color: inherit !important;
}

</style>

