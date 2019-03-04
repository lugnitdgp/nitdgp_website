<template>
  <div class="l3-fac">
    <sp-card containerclass="l3-card">
      <div slot="header">
        <p class="tile-title-text">
          <a class="white-text">
            Computer Center
          </a>
          <span v-if="!general" @click="general = true">
            - Show
          </span>
        </p>
      </div>
      <div class="container-fluid fac-sm">
        <div class="row">
          <div class="list-group" 
            :class="extraNavClasses.concat([getClassNav()])"
            :style="{ top: popUpTop + 'px' }">
            <a class="dropdown-item active"  data-toggle="list" href="#li1" role="tab">About Us</a>
            <a class="dropdown-item"  data-toggle="list" href="#li2" role="tab">People</a>
            <a class="dropdown-item"  data-toggle="list" href="#li3" role="tab">Research Publications</a>
            <a class="dropdown-item"  data-toggle="list" href="#li4" role="tab">Projects</a>
            <a class="dropdown-item" data-toggle="list" href="#li5" role="tab">Facilities</a>
            <a class="dropdown-item" data-toggle="list" href="#li6" role="tab">HOD</a>
            <a class="dropdown-item" data-toggle="list" href="#li7" role="tab">Contact Us</a>
            <a class="dropdown-item" data-toggle="list" href="#li8" role="tab">Photo Gallery</a>
            <a class="dropdown-item" data-toggle="list" href="#li9" role="tab">CC Booking Form</a>          
          </div>
          <div class="downc tab-content" :class="getClassContent()">
            <button class="btn" type="button" @click="showNav($event)">
              <i class="fa fa-bars fa-2x"></i>
            </button>
            <div class="tab-pane fade show active big-list" id="li1" role="tabpanel">
              <h4 class="pane-title" align="center">About Us</h4>
              <hr>
              <p class="text-justify">
                The ‘Computer Centre’ provides central computing facilities for the students, scholars and the teachers of the whole Institute and also offers M.Tech. on ‘High Performance Computing’ and Ph.D. on 'Computer Science'.
                The Centre started as a server room in year 1986 to handle NIT Durgapur campus network. On November 11, 2002 additionally started working with new building as a central computing facility for the students, scholars, and the teachers of the whole Institute. In year 2014, started academic programs M.Tech. and Ph.D.
                The research specialisations are digital image processing, image compression, quality of images, color image processing, load forecasting, bio-informatics, software engineering and agent based computing. The department maintains research environment with the dedicated and knowledgeable faculties and the well equipped laboratories with updated computing systems.
                The Centre has necessary infrastructure like sufficient number of computer hardware, software, air-conditioned labs, and stabilized uninterrupted power supply. All these infrastructure are maintained by trained technical team members.
                The department has laboratories with a sizeable number of PCs and workstations running specialised engineering and scientific packages, like MATLAB, AUTOCad, STADD, IDEAS, PSpice, ANSYS, AFS, Sybase and PowerBuilder etc. 
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li2" role="tabpanel">
              <h4 class="pane-title" align="left">People</h4>
              <hr>
              <h6 class="red-text">Not Available at the moment </h6>
            </div>

            <div class="tab-pane fade big-list" id="li3" role="tabpanel">
              <h4 class="pane-title" align="left">Research Publications</h4>
              <hr>
              <p class="text-justify">               
                <span class="text-center"><h5><u>Journal Publications</u></h5></span>
                <ul>
                  <li>Contactless Palmprint Verification System using 2-D Gabor Filter and Principal Component Analysis</li>
                  <span style="font-size: 12px;">Satya Bhushan Verma, Saravanan Chandran, Contactless Palmprint Verification System using 2-D Gabor Filter and Principal Component Analysis, accepted for publication in International Arab Journal of Information Technology (IAJIT), www.iajit.org (SCI). </span>
                  <li>Touchless Palmprint Verification using Shock Filter, SIFT, I-RANSAC, and LPD</li>
                  <span style="font-size: 12px;">Saravanan Chandran, Satya Bhushan Verma, Touchless Palmprint Verification using Shock Filter, SIFT, I-RANSAC, and LPD, IOSR Journal of Computer Engineering, Vol.17, Iss.3, pp.1-8, 2015. e-ISSN: 2278-0661, p-ISSN: 2278-8727, http://www.iosrjournals.org/iosr-jce/papers/Vol17-issue3/Version-3/A017330108.pdf </span>
                  <li>Novel Design of Full Adder/ Subtractor by Less Complexity Multiplexers of Reversible Gates</li>
                  <span style="font-size: 12px;">Shefali Mamataj, Biswajit Das, Saravanan Chandran, Novel Design of Full Adder/ Subtractor by Less Complexity Multiplexers of Reversible Gates, Journal of Engineering Science and Technology, accepted for publication, ISSN: 1823-4690, http://jestec.taylors.edu.my/ </span>
                </ul>

                <span class="text-center"><h5><u>Conference Publications</u></h5></span>
                <ul>
                  <li>Performance Analysis of LSB, DCT, and DWT for Digital Watermarking Application using        Steganography</li>
                  <span style="font-size: 12px;">Saravanan Chandran, Koushik Bhattacharyya, Performance Analysis of LSB, DCT, and DWT for Digital Watermarking Application using Steganography, International Conference on Electrical, Electronics, Signals, Communication and Optimization (IEEE-EESCO – 2015), Visakhapatnam, Andhra Pradesh, India, Issue 1, pp..244-248, 24-25, Jan-2015, ISBN 978-1-4799-7678-2, Ranked 49 out of 600 papers. http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7253657<br>
                  Authors: Saravanan Chandran, Koushik Bhattacharyya<br>
                  Conference date: 24 Jan - 25 Jan 2015<br>
                  Conference: International Conference on Electrical, Electronics, Signals, Communication and Optimization (EESCO) - 2015<br>
                  Publication:Year 2015, Issue 1, Pages 244-248, Publisher IEEE<br>
                  Google Scholar Profile: Saravanan Chandran<br>
                  Google Scholar Profile: Koushik Bhattacharyya<br>
                  Download link at Research Gate</span>
                  <li>A Novel Steganography Technique for Securing User’s Digitized Handwritten Signature for Public      Authentication Systems</li>
                  <span style="font-size: 12px;">C Saravanan and R K Thakur, A Novel Steganography Technique for Securing User’s Digitized Handwritten Signature for Public Authentication Systems, First International Conference on Computing, Communication, Electrical, Electronics, Devices & Signal Processing, Machillipatinam, Andhra Pradesh, India, 28-30, March 2015.<br>
                  Authors: Chandran Saravanan, Ramesh Kumar Thakur
                  Conference date: 28 March - 30 March, 2015
                  Conference: First International Conference on Computing, Communication, Electrical, Electronics, Devices & Signal Processing - 2015
                  Publication:Not Available
                  Google Scholar Profile: Saravanan Chandran
                  Google Scholar Profile: Ramesh Kumar Thakur
                  Download link is not available</span>
                  <li>An Approach for Designing an Optimized Reversible Parallel Multiplier by Reversible Gates</li>
                  <span style="font-size: 12px;">Shefali Mamataj, Biswajit Das, Saravanan C., An Approach for Designing an Optimized Reversible Parallel Multiplier by Reversible Gates, ICCACCS, Kolkata, Springer, ISSN: 1876-1100, 30-10-2014 to 01-11-2014, ISSN – 1876-1100, Springer. </span>
                  <li>An Approach for Designing of Sequence Generator by Counter and Multiplexer of Reversible Gates</li>
                  <span style="font-size: 12px;">Shefali Mamataj, Biswajit Das, Saravanan C., An Approach for Designing of Sequence Generator by Counter and Multiplexer of Reversible Gates, IC3I-IEEE, 27-29, Nov. 2014, Mysuru, India, ISBN: 978-1-4799-66295.</span> 
                  <li>Automated Road Extraction From High Resolution Satellite Images</li>
                  <span style="font-size: 12px;">Jose Hormese and C. Saravanan, Automated Road Extraction From High Resolution Satellite Images, International Conference on Emerging Trends in Engineering, Science, and Technology (ICETEST - 2015), 9-11, December 2015, Govt. Engg. College, Thrissur, Kerala, India. </span>
                  <li>Modified Execution Time based Resource Reservation (METRR) Algorithm</li>
                  <span style="font-size: 12px;">Shubham Kumar and Saravanan Chandran, Modified Execution Time based Resource Reservation (METRR) Algorithm, ICBIM 2016, 9-11, January 2016, ISBN: 978-1-5090-1228-2, NIT Durgapur, INDIA.</span> 
                  <li>Extraction of Tumours in Medical Images using Region of Interest</li>
                  <span style="font-size: 12px;">Debarpita Chaudhuri, Saravanan Chandran, Extraction of Tumours in Medical Images using Region of Interest, Accepted for presentation in an 4th International Conference on Complex Dynamical Systems and Applications, NIT Durgapur, India, 15-17, February 2016.</span>
                  </ul> 


              </p>
            </div>

            <div class="tab-pane fade big-list" id="li4" role="tabpanel">
              <h4 class="pane-title" align="left">Projects</h4>
              <hr>
              <h6 class="red-text">Not Available at the moment </h6>
            </div>

            <div class="tab-pane fade big-list" id="li5" role="tabpanel">
              <h4 class="pane-title" align="left">Facilities</h4>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#panell1" role="tab">Software</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#panell2" role="tab">Hardware</a>
                </li>                
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="panell1" role="tabpanel">
                  <div class="row">
                    <div class="col">
                      <h5><strong>Details of Licensed Softwares</strong></h5>
                      <ul>                        
                        <li>MATLAB R14a</li>
                        <li>ANSYS 5 users, license server on blade8 (win2K3)</li>
                        <li>ASPEN PLUS, 5 users network license / Single in standalone (license on Intel Server)</li>
                        <li>AUTOCAD Mechanical, Civil 40, 10 users license , on blade server 8</li>
                        <li>CATIA (license server on management server of blade server rack)</li>
                        <li>Pro Engineer (license on 2nd Server)</li>
                        <li>Microsoft Campus License</li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade page-type-links" id="panell2" role="tabpanel">
                  <h5><strong>Details of Hardwares</strong></h5>
                  
                  <div class="table-wrapper-2 table-bordered">
                    <table class="table table-responsive-md">
                      <thead class="mdb-color lighten-4">
                        <tr>
                          <th class="th-lg">LAB Name</th>
                          <th class="th-lg">Details</th>
                          <th class="th-lg">Number of Computers</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>LAB-1</td>
                          <td>Lenovo (ThinkCentre) M58p - Intel Dual Core (3.0 GHz), 2 GB RAM<br>Dell Optiplex 755 Core2 Duo : 1.80GHz, 1 GB RAM ( + 1GB later)<br>Dell Optiplex 755 Core2 Vpro : 3.0 GHz, 2 GB RAM 
                          </td>
                          <td>17 nos<br><br> 13 nos <br><br>07 nos</td>
                        </tr>
                        <tr>
                          <td>LAB-2</td>
                          <td>Lenovo Thinkcentre Core i5 Vpro ( 3.3 GHz; 2GB RAM )</td>
                          <td>30 nos</td>
                        </tr>
                        <tr>
                          <td>LAB-3</td>
                          <td>Lenovo Thinkcentre Core i5 Vpro ( 3.3 GHz; 2GB RAM ) </td>
                          <td>30 nos</td>
                        </tr>
                        <tr>
                          <td>LAB-4</td>
                          <td>HP Elite Desk 800G – Intel core i5; 3.5 GHz; 4 GB RAM </td>
                          <td>30 nos</td>
                        </tr>
                        <tr>
                          <td>LAB for M. Tech (High Performance Computing)</td>
                          <td>HP Elite Desk 800G – Intel core i5; 3.5 GHz; 4 GB RAM</td>
                          <td>17 nos</td>
                        </tr>
                        <tr>
                          <td>LAB for Research Scholars</td>
                          <td>HP Elite Desk 800G – Intel core i5; 3.5 GHz; 4 GB RAM </td>
                          <td>13 nos</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <h3>Server</h3>

                    <ul>
                        <li>Blade server system :- (rack mounted)
                          <ul type="square">
                          <li>Management Server : Model-HP proliant ML350 Intel Xeon CPU</li>
                          <li>Second intel server in the rack Model-hp proliant ML350, Intel Xeon CPU</li>
                          <li>Eight nos. of blade server</li>
                          <li>HP Storage : Modular Smart Array 1000 SCSI array of 146.8 GB x 10</li>
                          <li>Redundant power supply system</li>
                          </ul>
                      </li>
                          <li>Dell Server- power edge Model:R720:- (rack mounted)</li>                        
                  </ul>

                <h3>Printer& Scanner</h3>
                  <ul>
                    <li>HP Laser jet 1566</li>
                    <li>A0 Colour Plotter : HP Design Jet 500 PS; Model: C7770C</li>
                    <li>HP Laserjet 9040dn</li>
                    <li>A0 Scanner : Vidar Nova XP36</li>
                    <li>A3 Scanner : Epson GT15000</li>
                  </ul>
                </div> 
                <div class="tab-pane fade page-type-links" id="panell3" role="tabpanel">
                  <h5><strong>Details of Syllabus/Programmes in PhD</strong></h5>
                </div>
              </div>
            </div>

            <div class="tab-pane fade big-list" id="li6" role="tabpanel">
              <h4 class="pane-title" align="left">HOD</h4>
              <hr>
              <div class="col testimonial">
                <div class="card testimonial-card text-center">
                  <div class="card-up">
                  </div>
                  
                  <div align="center">
                    <img src="https://admin.nitdgp.ac.in/files/faculty/Goutam%20Sanyal/sanyal.jpg" class="avatar mx-auto rounded-circle img-fluid">
                  </div>
                  <div class="card-body-in">
                    <p class="card-title">
                      <strong>
                        <a class="blue-text notranslate" href="https://nitdgp.ac.in/faculty/3b5e8096-d92d-4e01-bccf-37fb83a07091" target="_blank">
                          Dr. Goutam Sanyal
                        </a>
                      </strong>
                    </p>
                    
                    <h6 class="black-text">Professor<br>Department of Computer Science and Engineering,<br>NIT Durgapur, India</h6>
                    <hr>
                    <p class="min-profile">
                    <i class="fa fa-envelope"></i>&nbsp;&nbsp;&nbsp; goutam.sanyal@cse.nitdgp.ac.in, nitgsanyal@gmail.com<br>
                    <i class="fa fa-phone"></i> &nbsp;&nbsp;&nbsp;91-9434788006
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade big-list" id="li7" role="tabpanel">
              <h4 class="pane-title" align="left">Contact Us</h4>
              <hr>
              <p class="text-justify">
                Department of Computer Centre NIT Durgapur,<br>
                Mahatma Gandhi Avenue,<br>
                Durgapur - 713209,<br>
                West Bengal,<br>
                India.<br>
                Office Phone no. - +91-343-2752126
              </p>
            </div>
            <div class="tab-pane fade big-list" id="li8" role="tabpanel">
              <h4 class="pane-title" align="left">Photo Gallery</h4>
              <hr>
              
            </div>
            <div class="tab-pane fade big-list" id="li9" role="tabpanel">
              <h4 class="pane-title" align="left">CC Booking Form</h4>
              <hr>
              
            </div>
          </div>
          
        </div>
      </div>
    </sp-card>
    <div v-show="nav" id="fade" class="black_overlay"></div>
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL, backURL } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import SpCard from '@/components/SpCard'
import CardTestimonial from '@/components/CardTestimonial'

export default {
  name: 'Cc',
  data () {
    return {
      general: true,
      windowWidth: 1000,
      extraNavClasses: [],
      nav: false,
      popUpTop: 0,
      top: -1
    }
  },
  created () {
    this.$emit('hideloader', true)
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  mounted () {
    Array.from(document.getElementsByClassName('dropdown-item')).forEach(el => {
      el.addEventListener('click', this.hideNav)
    })
  },
  methods: {
    hideNav () {
      this.nav = false
      this.extraNavClasses = []
      this.popUpTop = 0
    },
    showNav (event) {
      this.extraNavClasses = ['lift', 'div-block']
      this.nav = true
      this.popUpTop = event.clientY + this.top
      console.log(this.popUpTop)
    },    
    getClassContent () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-8'
      else if (width > 900)
        return 'col-7'
      else if (width > 600) {
        this.top = -1
        return 'col-8'
      }
      else {
        this.top = 1
        return 'col-12'
      }
    },
    getClassNav () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-2'
      else if (width > 900)
        return 'col-3'
      else
        return 'div-none'
    },
    updateWidth () {
      this.windowWidth = document.body.clientWidth
    }
  },
  components: {
    TableRenderer,
    CardCollapse,
    SpCard,
    CardTestimonial
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<style scoped>
  .staffs {
    min-width: 200px !important;
    min-height: 300px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
  .list-group a, .list-group a:hover {
    white-space: pre-wrap;
  }
  .dropdown-item:hover{
    background-color: #001333!important;
    color: #fff!important;
  }
  .photo {
    text-align: center;
  }
  .downc {
    margin: 0 auto;
    padding: 10px;
  }
  .btn {
    background: #001333;
    width: 50px;
    padding: 10px;
    float: right;
    margin-left: auto;
    margin-bottom: 0px;
  }
  @media screen and (min-width: 909px) {
    .btn {
      display: none;
      height: 0px;
    }
  }
  .lift {
    position: absolute;
    left: 10%;
    width: 80%;
    background-color: white;
    z-index: 2;
    overflow: auto;
  }
  .black_overlay {
    position: absolute;
    top: 0%;
    left: 0%;
    bottom: 0%;
    width: 100%;
    height: 100%;
    z-index: 1;
    background-color: black;
    -moz-opacity: 0.8;
    opacity: .80;
    filter: alpha(opacity=80);
  }
  .dropdown-item.faculty-login {
    background-color: #8f8;
  }
  .dropdown-item.faculty-login:hover {
    background-color: #0f0!important;
  }
  .col.testimonial {
    min-width: 200px;
    min-height: 100px;
    max-width: 320px;
    max-height: 500px;
    padding: 7px;
  }
  .min-profile {
    font-size: 72% !important;
  }
  hr {
    margin-left: 2em !important;
    margin-right: 2em !important;
  }
  .card-body-in .card-title .notranslate {
    font-size: 88% !important;
  }
  .card-body-in h6{
    font-size: 80% !important;
  }
  .testimonial-card .desig{
    font-size: 100%;
  }
  .testimonial-card .card-title{
    font-size: 100%;
  }
  .testimonial-card {
    min-height: 100% !important;
    min-width: 100% !important;
  }
  .card-up {
    height: 80px !important;
  }
  .card-up {
    background: linear-gradient(to right,#001333,#324e7d) !important;
  }
  .avatar {
    height: 100px !important;
    width: 100px !important;
  }
</style>
