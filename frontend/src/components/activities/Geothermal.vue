<template>
  <div class="l3-fac">
    <sp-card containerclass="l3-card">
      <div slot="header">
        <p class="tile-title-text">
          <a class="white-text">
            GEOTHERMAL HELIUM EARTHQUAKE PRECURSOR
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
            <a class="dropdown-item"  data-toggle="list" href="#li2" role="tab">Brief History</a>
            <a class="dropdown-item"  data-toggle="list" href="#li3" role="tab">Members</a>
            <a class="dropdown-item"  data-toggle="list" href="#li4" role="tab">Research Activities</a>
            <a class="dropdown-item" data-toggle="list" href="#li5" role="tab">Equipment</a>
            <a class="dropdown-item" data-toggle="list" href="#li6" role="tab">Field Visit Report</a>
            <a class="dropdown-item" data-toggle="list" href="#li8" role="tab">Publications</a>
            <a class="dropdown-item" data-toggle="list" href="#li7" role="tab">Seminar</a>
            <a class="dropdown-item" data-toggle="list" href="#li9" role="tab">Photo gallery</a> 
            <a class="dropdown-item" data-toggle="list" href="#li10" role="tab">Contact Us</a> 
          </div>
          <div class="downc tab-content" :class="getClassContent()">
            <button class="btn" type="button" @click="showNav($event)">
              <i class="fa fa-bars fa-2x"></i>
            </button>
            <div class="tab-pane fade show active big-list" id="li1" role="tabpanel">
              <h4 class="pane-title" align="center">About Us</h4>
              <hr>
              <p class="text-justify">
                The research focus of Center of Helium and Geothermal Research at NIT Durgapur is namely three fold 
                <ul>
                  <li>harnessing helium gas from geothermal resources (hot springs)</li>
                  <li>exploration of geothermal power</li>
                  <li>monitoring of earthquake precursory signals.</li>
                </ul>
                Helium consumption in India is approximately 0.15 billion cubic feet, about 2.3% of global helium consumption, most of which is imported from USA. Poland and Qatar are among the countries that produce helium, but have till the date limited export capability. India is entirely dependent on USA for tapping helium. USA is already turning off helium supplies to the outside world. The immediate implication is the serious consequences on our space, defense and atomic energy programme along with a whole host of other areas such as MRI’s medical equipment that will plunge into despair and come to a grinding halt. The switch off also implies serious problems to our R&D programme in the Indian laboratories. In the light of this, we have far too long taken the Micawberish attitude that something will turn up to save the situation. However, no comprehensive effort has been undertaken so far to map and extract helium in the country in a large scale. It is essential therefore for India to seriously initiate its own programme to produce helium in a large scale, in order to be reasonably self-reliant. British geologist identified more than three hundred hot springs in India. Out of over 300 hot springs scattered throughout the country many release gases enriched with helium (concentration > 1.0 vol.% ). On the other hand all the known natural petroleum gas fields in India are lean in helium (0.05 vol.% in average). And to recover helium from natural petroleum gas, a host of allied factors need to be taken into account including the natural petroleum gas well life-time, before a helium extraction unit can be set-up. As an alternate measure, exploring helium extraction from geothermal areas appears promising because of higher helium concentrations (1.0 vol% in average in hot spring gases, 20 times higher than helium concentration in natural petroleum gases) available for virtually inexhaustible time-scale durations (geological time scale). It is always economical to recover helium from a gas source having high helium content with high flow rate.<br>
                These hot springs may also be utilized as a source of geothermal power - a vital source of energy (green energy) still completely ignored in India. The thermal energy of the solid earth originates from the primordial heat locked up within its interiors during the formation of the planet, along with subsequent heat generated during geologic time on account of the radioactive decay of the isotopes in the elements of Uranium and Thorium series. High temperature and pressure within the earth cause rocks to melt. This is known as magma. Because it is lighter than rock, magma rises up and heats the rocks above. This is a heat source. It is known as geothermal energy. Geothermal energy is more easily accessible in areas where there are hot springs.However, no comprehensive effort has been undertaken so far to map and harness geothermal energy in the country. It is thus essential and timely for India to seriously initiate its own programme to generate geothermal power in a large scale. Geothermal electricity is grid interactive and has no dependence on meteorological parameters unlike wind or solar energy. Geothermal resources can sustain for long time. The most important aspect is that environmental impact of the geothermal power plant is negligible. The geothermal zones of India have a moderate to high geothermal gradient (47-1000 C) and heat flux (78-468 mW/m2). There are vast regions in the country that are characterised with high geothermal gradient (> 600 C) and high heat flux (> 200 mW/m2) and these geothermal zones could well utilized for generation of green power.<br>
                In this context a three year R&D project has been taken up by NIT Durgapur for detailed investigation towards large scale extraction of helium and geothermal energy at the Bakreswar-Tantloi geothermal region lying across the border districts of Birbhum in West Bengal and Dumka in Jharkhand.Both the idea of “extraction of helium in large scale” and “geothermal power” at Bakreswar-Tantloi geothermal area is complementary to each other. Helium and geothermal heat is coupled to each other. Both of them are produced from common source of uranium and thorium, present in the crustal rock and also in mantle. Hot spring with sizeable helium content in the emanating natural gas should in principal lead to large natural heat source not too far away from the surface of the earth. This is a fact especially so if one compares the depth to which one has to drill in areas where there is no hot spring with escaping natural gas. Therefore, a common deep drilling (~300-800 m deep) at Bakreswar-Tantloi geothermal area could be used to tap both the helium sources and geothermal resources.<br>
                Apart from this, the center is also actively involved in research on monitoring of earthquake precursory signals through geochemical and geophysical techniques. So far four monitoring laboratories are operated by NIT Durgapur at different corners of the country. Themonitoring stations are placed in dissimilar geological environments and in different seismic zones of the country.The names and locations of the laboratories are as
                <ul>
                  <li>Thermal spring site at Bakreswar, Birbhum, West  Bengal</li>
                  <li>Thermal spring site at Tantloi, Dumka, Jharkhand</li>
                  <li>Thermal spring site at TattaPani, Rajouri, Jammu & Kashmir</li>
                  <li>The mud volcano at Baratangisland, Andaman & Nicobar islands</li>
                </ul>
                And the data analysis centre is situated at Dept. of Physics, NIT Durgapur, Durgapur, West Bengal Different kind of instruments such as gas chromatograph, radon monitor, seismometer etc. is installed at the said laboratories to collect the geochemical and geophysical data.The recorded data are sent to the data analysis centre through VSAT internet connectivity for further analysis. 
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li2" role="tabpanel">
              <h4 class="pane-title" align="left">Brief History</h4>
              <hr>
              <p class="text-justify">
                Serious search for large-scale helium in India began during the first years of the 1970’s by the legendary S. N. Bose, FRS, National Professor of Physics. Professor Bose had the foresight to recognize that India would need substantial quantities of helium gas in future to feed its emergent requirements in crucial scientific areas. And this supply must essentially come out of its own natural resources. Accordingly, he started off a ‘Helium Recovery’ project at the Indian Association for the Cultivation of Science (IACS) at Jadavpur, Kolkata, during 1971. The entire task of planning and execution of this project was entrusted to the well-known experimental physicist, Professor S. D. Chatterjee, one of the distinguished students of Professor Bose. Prof. Chatterjee noted the presence of helium in the hot spring (72oC) gas emissions at Bakreswar, near Santiniketan, West Bengal. The helium content of the Bakreswar gas was about 1.8 volume percent. The helium recovery pilot plant (helium recovery from hot spring gas) built by Prof. Chatterjee and his colleagues at Bakreswar was a remarkable breakthrough. It immediately attracted the attention of Department of Science and Technology (DST) and Department of Atomic Energy (DAE). And therefore, in 1977 at the insistence of Dr. H. N. Sethna, the then Chairman, Atomic Energy Commission (AEC) along with Dr. A. S. Divatia, Project Manager, Variable Energy Cyclotron Centre (VECC), Kolkata the work concerning helium recovery done at IACS was transferred to VECC from March 1978. The related field work was taken charge of by the Atomic Mineral Directorate (AMD) of DAE. This part was also subsequently transferred to VECC in 1982. Around 1984, Prof. Bikash Sinha came to VECC from BARC and he got interested in the project, especially after meeting Professor S.D. Chatterjee who had extraordinarily original and innovative ideas and was greatly admired by Dr. Raja Ramanna and Prof. Sinha. Meanwhile, helium extraction from the nearby geothermal field at Tantloi (Jharkhand) also started through a joint venture of DST, VECC and Saha Institute of Nuclear Physics (SINP), Kolkata. A purification plant was installed improving recovered helium purity to 99.99 per cent purity level. In the year 2009 a prototype helium extraction plant was also installed at natural gas field at Kuthalam, Tamilnadu by VECC, SINP in collaboration with DST and Oil and Natural Gas Corporation (ONGC) to extract helium from natural gas having feeble helium concentration of 0.05 volume percent. It was demonstrated for the first time in the country that it is very much possible to recover helium from natural petroleum gases having feeble helium content (0.05 vol.%). Moreover that extreamly low concentration helium bearing natural petroleum gas was purified using Pressure Swing Adsorption (PSA) technique to produce a high grade helium (99.0 vol.% pure helium). The installation and commissioning of the PSA helium pilot plant (helium recovery from natural petroleum gas) along with purification unit (99.0 vol.% pure helium) was a remarkable breakthrough.  <br>
                Prof. Bikash Sinha in his capacity as Homi Bhabha Professor of DAE along with some young colleagues continued the programme, which was funded by Ministry of Earth Sciences (MoES). Prof. Bikash Sinha and his group performed geochemical and geophysical research activities at Bakreswar-Tantloi geothermal region, West Bengal and in Jharkhand. The work brought to light two vital conclusions:
              <ul>
                  <li>The entire Bakreswar-Tantloi geothermal area is sitting on a huge reservoir of helium existing within the crust not far beneath from the top soil. The surface expression of helium, as seen at hot spring bubble gas, figures only but a tiny fraction of this reservoir. This region hosts almost 60 hot springs within 2500 square km area. These hot springs are enriched with high concentration of helium (1.88-2.77 vol.%.). Indeed, this fact was surmised and mentioned long time ago by Professor S. D. Chatterjee to Prof. Bikash Sinha. We wish to explore the entire topology and the extent of the helium reservoir.</li>
                  <li>The high geothermal heat outflow (230 mW/m2), geothermal gradient (90 0C/km) is seen in this area. Also high concentration of helium and radon (radioactive gas) are emanating from the hot springs of this zone. These data indicates the presence of a potential geothermal resource in the area. This area will be ideal for setting up a “geothermal” energy reactor - a vital source of energy (green energy) still completely ignored in India.</li>
                </ul>
                Presently the entire programme is operated from NIT Durgapur. A high level scientific community is monitoring and supervising the said activity. 
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li3" role="tabpanel">
              <h4 class="pane-title" align="left">Members</h4>
              <hr>
              <p class="text-justify">
                <ul type="A">                  
                  <li>Faculty and Scientists
                    <ul type="1">
                      <li><strong>Dr. H. Chaudhuri</strong>
                        <p>Project Manager, Helium and Geothermal Project & Assistant Professor,<br> Physics Department, NIT Durgapur<br> <strong>Physicist</strong></p>
                      </li>
                      <li><strong>Prof. T. Kumar  </strong>
                        <p>Director, NIT Durgapur<br> <strong>Petroleum Engineer</strong></p>
                      </li>
                      <li><strong>Prof. N. K. Roy</strong>
                        <p>Professor, Electrical Engineering Department, NIT Durgapur<br> <strong>Electrical Engineer</strong></p>
                      </li>
                      <li><strong>Prof. A. Gangopadhyaya</strong>
                        <p>Professor, Earth & Environmental StudiesDepartment, NIT Durgapur<br> <strong>Geologist</strong></p>
                      </li>
                      <li><strong>Dr. Kalyan Adhikari</strong>
                        <p>Associate Professor, Earth & Environmental Studies Department, NIT Durgapur<br> <strong>Geologist</strong></p>
                      </li>
                    </ul>
                  </li>
                  <li>Advisor
                    <ul type="1">
                      <li><strong>Prof. Bikash Sinha,</strong><p>Emeritus Professor at NIT Durgapur and INSA Eminent Scientist and Former Chairperson BOG, NIT Durgapur and Former Director, SINP, Kolkata & VECC, Kolkata <br><strong>Physicist</strong></p></li>
                      <li><strong>Prof. Amalendu Bhushan Bhattacharyya</strong>
                        <p>Chairperson BOG, NIT Durgapur and Former Faculty Department of Physics, IIT Delhi, Delhi and Former Director, Institute of Technology and Management, Gurgaon andFormer Director, VLSI Design Programme, GOA University.<br><strong>Physicist</strong></p></li>
                    </ul>
                  </li>
                  <li>Technical staff members
                    <div class="table-wrapper-2 table-bordered">
                    <table class="table table-responsive-md">
                      <thead class="mdb-color lighten-4">
                        <tr>
                          <th class="th-lg">SL. NO. </th>
                          <th class="th-lg">Name Of The Employee</th>
                          <th class="th-lg">Designation</th>
                          <th class="th-lg">Location</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>1</td>
                          <td>Mr. Prithwijit Roy</td>
                          <td>Technician</td>
                          <td>Tantloi Site (Jharkhand)</td>
                        </tr> 
                        <tr>
                          <td>2</td>
                          <td>Mr. Sumit Khajuria</td>
                          <td>Technician</td>
                          <td>TattaPani (Jammu & Kasmir)</td>
                        </tr>
                        <tr>
                          <td>3</td>
                          <td>Mr. Dhavinder Kumar</td>
                          <td>Attendant</td>
                          <td>TattaPani (Jammu & Kasmir)</td>
                        </tr> 
                        <tr>
                          <td>4</td>
                          <td>Mr. Suresh Kumar</td>
                          <td>Watch Man</td>
                          <td>TattaPani (Jammu & Kasmir)</td>
                        </tr> 
                        <tr>
                          <td>5</td>
                          <td>Mr. Galib Hussain</td>
                          <td>Watch Man</td>
                          <td>TattaPani (Jammu & Kasmir)</td>
                        </tr>
                        <tr>
                          <td>6</td>
                          <td>Mr. Filix Ekka</td>
                          <td>Technician</td>
                          <td>Baratang(Andaman&Nicobar)</td>
                        </tr> 
                        <tr>
                          <td>7</td>
                          <td>Mr. Kamil Baa</td>
                          <td>Attendant</td>
                          <td>Baratang(Andaman&Nicobar)</td>
                        </tr> 
                        <tr>
                          <td>8</td>
                          <td>Mr. Sudhir Kandulana</td>
                          <td>Watch Man</td>
                          <td>Baratang(Andaman&Nicobar)</td>
                        </tr>
                        <tr>
                          <td>9</td>
                          <td>Mr. Prakul Minj</td>
                          <td>Watch Man</td>
                          <td>Baratang(Andaman&Nicobar)</td>
                        </tr>                        
                      </tbody>
                    </table>
                  </div>
                  </li>
                  <li>Research students</li>
                </ul>
              </p>
              
            </div>

            <div class="tab-pane fade big-list" id="li4" role="tabpanel">
              <h4 class="pane-title" align="left">Research Activities</h4>
              <hr>
            </div>

            <div class="tab-pane fade big-list" id="li5" role="tabpanel">
              <h4 class="pane-title" align="left">Equipment</h4>
              <hr>
            </div>

            <div class="tab-pane fade big-list" id="li6" role="tabpanel">
              <h4 class="pane-title" align="left">Field Visit Report</h4>
              <hr>
              
            </div>
            <div class="tab-pane fade big-list" id="li7" role="tabpanel">
              <h4 class="pane-title" align="left">Seminar</h4>
              <hr>
              
            </div>
            <div class="tab-pane fade big-list" id="li8" role="tabpanel">
              <h4 class="pane-title" align="left">Publications</h4>
              <hr>
              
            </div>
            <div class="tab-pane fade big-list" id="li9" role="tabpanel">
              <h4 class="pane-title" align="left">Photo Gallery</h4>
              <hr>
              
            </div>
            <div class="tab-pane fade big-list" id="li10" role="tabpanel">
              <h4 class="pane-title" align="left">Contact Us</h4>
              <hr>
              <div class="col testimonial">
                <div class="card testimonial-card text-center">
                  <div class="card-up">
                  </div>
                  
                  <div align="center">
                    <img src="https://admin.nitdgp.ac.in/files/faculty/Hirok%20Chaudhuri/55.JPG" class="avatar mx-auto rounded-circle img-fluid">
                  </div>
                  <div class="card-body-in">
                    <p class="card-title">
                      <strong>
                        <a class="blue-text notranslate" href="https://nitdgp.ac.in/faculty/bed09767-49b2-4ed9-a5d8-aaefbeea9a40">
                          Dr. Hirok Chaudhuri
                        </a>
                      </strong>
                    </p>
                    
                    <h6 class="black-text">Project Manager, Helium and Geothermal Project & Associate Professor, Department of Physics <br>National Institute of Technology Durgapur <br>Mahatma Gandhi Avenue, Durgapur-713209 <br>West Bengal, India</h6>
                    <hr>
                    <p class="min-profile">
                      <i class="fa fa-envelope"></i>&nbsp;&nbsp;&nbsp;hirok.chaudhuri@phy.nitdgp.ac.in , chaudhuri_hirok@yahoo.co.in<br>
                      <i class="fa fa-phone"></i>&nbsp;&nbsp;&nbsp+91 343 2546808 (Office) , +91 9434789019
                                   , +91 9830076271
                    </p>
                  </div>
                </div>
              </div>
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
  name: 'Geothermal',
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
