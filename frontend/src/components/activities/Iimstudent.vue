<template>
  <div class="l3-fac">
    <sp-card containerclass="l3-card">
      <div slot="header">
        <p class="tile-title-text">
          <a class="white-text">
            IIM Student Chapter
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
            <a class="dropdown-item active"  data-toggle="list" href="#li1" role="tab">Home</a>
            <a class="dropdown-item"  data-toggle="list" href="#li2" role="tab">About us</a>
            <a class="dropdown-item"  data-toggle="list" href="#li3" role="tab">Executive committee</a>
            <a class="dropdown-item"  data-toggle="list" href="#li4" role="tab">Activities</a>
            <a class="dropdown-item" data-toggle="list" href="#li5" role="tab">Membership</a>
            <a class="dropdown-item" data-toggle="list" href="#li6" role="tab">Notice</a>
            <a class="dropdown-item" data-toggle="list" href="#li7" role="tab">Gallery</a>
            <a class="dropdown-item" data-toggle="list" href="#li8" role="tab">Press release</a>
            <a class="dropdown-item" data-toggle="list" href="#li9" role="tab">Downloads</a>
            <a class="dropdown-item" data-toggle="list" href="#li10" role="tab">Contact Us</a>
            <a class="dropdown-item" data-toggle="list" href="#li11" role="tab">Follow us on</a>
            <a href="https://nitdgp.ac.in/department/MM" style="margin-left:24px;" role="tab">MME Department Page</a>
          </div>
          <div class="downc tab-content" :class="getClassContent()">
            <button class="btn" type="button" @click="showNav($event)">
              <i class="fa fa-bars fa-2x"></i>
            </button>
            <div class="tab-pane fade show active big-list" id="li1" role="tabpanel">
              <h4 class="pane-title" align="center">Home</h4>
              <hr>
              <div class="container-fluid">
                <div class="row newscaro">
                  <div class="col-8 caro">
                    <Carousel :slides="slides"></Carousel>
                  </div>
                  <div class="col-4 news">
                    <Newsfeed :notices="notices"></Newsfeed>
                  </div>
                </div>
              </div>              
            </div>

            <div class="tab-pane fade big-list" id="li2" role="tabpanel">
              <h4 class="pane-title" align="left">About Us</h4>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#panell1" role="tab">About IIM</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#panell2" role="tab">About Student Chapter</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#panell3" role="tab">About Department of MME</a>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="panell1" role="tabpanel">
                  <p class="text-justify">
                    The idea of formation of an Indian Institute for metallurgists was conceived as early as in 1945. This was possible by the efforts of a few metallurgists, who realised the need for an adequate body for professional metallurgists in India. During that time many of the technical informations were not easily available in India. Communications with other countries were difficult because of the war. The ordnance factories and many other industries involved in manufacture of various products for the war efforts were greatly handicapped because of the non-availability of technical information on metallurgy. The Inspectorate of Metals in the ordnance factory was the only reliable organisation who could undertake investigations on metal products.
It was in this background that about a dozen young metallurgists met informally in Calcutta and discussed the issue at the residence of Dr. Dara P. Antia, who was then Chief Metallurgist of Indian Aluminium Co. It was unanimously agreed that an institute of metallurgists in India should be formed. Later, various metallurgists holding senior positions in India were approached for their support. Also, a large number of people in high positions in Government and Industries were approached. At the same time a Memorandum and Articles of Association were drafted after studying the memorandum and articles of various other bodies. The Iron and Steel Institute, UK and Institute of Metals, UK also welcomed the idea and suggested formation of a single institute and not various separate institutes such as Metals, Iron and Steel, etc. Accordingly the Memorandum and Articles were finalised and the Institute was registered at Calcutta. An Organisational Council with Dr. Dara P. Antia who played a key role in establishing the Institute as President (see page 7 for full membership) was formed to manage the affairs till the election of the first Council. The House of Tatas provided office space in Calcutta.
The first Organisational meeting was held on 24th February, 1946 at the residence of Mr. K. C. Sood in Calcutta. Later, four more meetings were held within two months. These meetings were mostly attended by M/s Dara P. Antia, V. Rama Iyer, R. N. Kapoor, R. Krishnasamy, P. K. Paul, B.A. Rao, D.V. Reddy, C.J. Shah, S. Sircar and K.C. Sood. The Institute was inaugurated by Hon’ble Dr. Shyama Prasad Mukherjee, Minister for Industry and Supply on Monday, 29th December 1947 at the Royal Asiatic Society Hall, Calcutta. Sri Jahangir J. Gandhy became the first President and Dr. Dara P. Antia the first Honorary Secretary of the Institute. The following were elected as the first council members.
Since then the growth of the Institute has been phenomenal. Starting with a modest membership of 42, the IIM Membership now (1999) stands more than 10,000 drawn from various fields of metallurgical activity. Membership requirements are rigid to maintain the highest professional standards. The Institute has grown into a reputed Institution devoted to promotion and advancement in the study, practice and research of Metallurgical Science and Technology. The Indian Institute of Metals is now recognised throughout the world as one of the premier metallurgical organisations.
The scope of the Institute activities includes mineral beneficiation, extraction, fabrication, heat treatment, finishing as well as practical and theoretical aspects of metallurgy of all ferrous and non-ferrous metals and alloys. Ceramics and other disciplines and technologies allied to metallurgical problems also come under the scope of the Institute.
The activities of the Institute include organising national and international technical conferences and programmes, research activities, publications, conducting qualifying examinations etc. Although there is a small permanent staff of the Institute, almost all the activities are carried out through the Honorary services of the Office-bearers, Council Members, Chapter Chairmen, Secretaries and Treasurers as well as a large number of Institute members.

IIM Webpage: <a href="https://www.iim-india.net">https://www.iim-india.net/</a>
 
                  </p>
                </div>
                <div class="tab-pane fade in show" id="panell2" role="tabpanel">
                 <p class="text-justify">
                   The Student affiliated chapter of The Indian Institute of Metals was passed through council Meeting No: 342/III/2019-20 on Saturday,22nd November 2020 held at Kaladham Conference Hall, Vidyanagar in presence of president, Dr. U Kamachi Mudali [2019-20 Council Year] and other council members as per Point 6b resolution. On the 19th of September, 2020 NIT Durgapur, paced its first steps towards inducting the students’ chapter of Indian Institute of Metals into its working structure. The inaugural program, organized by the Metallurgical and Materials Engineering Department of NIT Durgapur, was long-sought and despite seeing some delays, the event was attended with much zeal and enthusiasm by all. Keeping in with the COVID-19 restrictions, the program was held entirely online via the Microsoft Teams platform and was also live-streamed on Facebook and YouTube simultaneously. The event saw over 250 registrations and was attended by a vast diaspora of proficient personalities of the Academic World that included eminent professors, research scholars, graduate and undergraduate students. Dr M.M. Ghosh, HoD of the Metallurgical and Materials (MME) Department commenced the inauguration by welcoming the guests. He lauded the efforts put in by everyone within the department and in the college to make this students’ chapter a success. He illuminated the department’s rich academic heritage and extended his support, willingness and devotion towards working in co-operation with the students’ chapter in organizing seminars and events throughout the year for the benefit of the students. He also encouraged more students to become a part of this organization and reap the benefits of being a member to the fullest. Mr. L. Badu, the Secretary, IIM – Local Chapter, Durgapur, commended the efforts put in by the faculty in-charges, and the interest shown by NIT, the college itself, towards the formation of this students’ branch. He emphasized on the harmonious and smooth working of IIM in association with NIT Durgapur and especially the MME Department, in a way that will be of advantage to all, in academics to research and eventually nation building. Prof. Biswajit Halder, Dean of Student Welfare, NIT Durgapur, recalled the glitches of paperwork that came in the way and despite all the difficulties and delays, he admired the unbreakable dedication and efforts put in by the HoD and the Faculty In-charge to help the students chapter take shape into reality. He wished luck and provided subtle guidance to the students associated with the chapter for the easy functioning of the branch within the college. The Director of NIT Durgapur, Prof. Anupam Basu welcomed and appreciated every one. Despite being a professor in Computer Science Engineering himself, he stated that he was familiar with the activities of IIM right from his college days in IIT Kharagpur. He appreciated the department for being proactive in several academic and research assignments and praised its efforts for introducing the students’ branch of IIM. He put forth a very thought-provoking suggestion for the newly inducted student members of IIM-Student’s Chapter, that is to interact with school students and encourage them to take up this field of study and acquaint them with the challenges ahead, in an effort that they may choose this as a career option out of passion. The Guest of Honor for the event, Prof. K. Chattopadhyay, who also happens to an eminent alumnus of NIT Durgapur and an ex-president of IIM, then addressed the event. He recalled that during his college days, the concept of a student chapter had not been given much attention. He detailed the benefits that students may gain from the organization, working together and learning from it. He laid importance on the fact of how powerful a tool virtual meetings could be. He suggested a joint venture wherein all the students’ chapters all across the country could organize virtual seminars and conferences. He also spoke briefly about an upcoming educational portal, which will launch soon and will assist students in learning and gathering more information about the subjects through its resources. His words of encouragement and inspiration were received well by everyone. Prof. A. Gokhale, the President of IIM and also the Chief Guest for the inaugural ceremony, stressed on different shortcomings of technical education and suggested ways to overcome them. As a nation with the highest number of Engineering graduates each year and a rich, resourceful reinforcement, he weighed upon the need for an inclusive effort from the Metallurgical, Mechanical and Chemical Engineers’ Society to work together for improving the current standards. He reminded all about our duty towards the environment at the same time. Speaking to the students, he said, IIM will provide the source of in-depth knowledge for the students and will also guide them in modeling a better perspective in their professional careers as over time, the students will get to interact with people in the Industries, Research and Development, and the people directly involved in Policy Making. The overwhelming exposure will come as a magnificent boon to the undergraduate students in the time to come. He also spoke at length about the future endeavors scheduled at IIM, the monthly magazine – IIM Metal News and the Platinum Jubilee of IIM. He appreciated the faculty in-charge and HoD for fulfilling all the requirements for opening a student chapter within a short time frame. Dr. Arup Kumar Mandal, the Faculty in-charge of IIM Student Chapter- NIT Durgapur, on behalf of the Organizing Committee, presented the vote of thanks and expressed his warm regards and gratitude towards the Chief Guest, the Guest of Honor, other distinguished guests and all the attendees of the online event. 
                 </p>
                </div>
                <div class="tab-pane fade in show" id="panell3" role="tabpanel">
                  <p class="text-justify">
                    The Department, which started its journey in the year 1960, presently offers B.Tech. (Metallurgical and Material Engineering), M.Tech. (Metallurgy and Materials Technology) and Ph.D Programme. The Department maintains high level of interactions with other academic institutes (IIT Kharagpur, Jadavpur University, IIEST (Shibpur) and NIFFT (Ranchi)), CSIR Laboratories, SAIL and other steel plants in India. At present, fifteen highly qualified and dedicated faculty members are serving this Department. The teaching at B.Tech level focuses on the fundamental knowledge base development in various areas of Metallurgical and Materials Engineering, such as, Extractive Metallurgy, Physical Metallurgy, Mechanical Metallurgy and Corrosion Science and Engineering. M.Tech level teaching emphasizes on advanced knowledge input in new material development and latest techno-scientific progress in Metallurgical Industry. The research activities of the Department are centered on B.Tech and M.Tech Projects, Ph.D Programmes and sponsored research projects. Many research papers have been published in reputed peer reviewed Journals. The vision of the department is the development of techno-scientific knowledge-base to impart quality education to students at all levels (UG, PG and PhD) with an augmented focus on research and innovation in various fields of Metallurgical and Materials Engineering so as to cater the need of Industry and society at large. 
                  </p>
                </div>
              </div>

            </div>

            <div class="tab-pane fade big-list" id="li3" role="tabpanel">
              <h4 class="pane-title" align="left">Executive committee</h4>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#ecomm1" role="tab">Present Committee</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#ecomm2" role="tab">Present Working Committe</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#ecomm3" role="tab">Past Committe</a>
                </li>                
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="ecomm1" role="tabpanel">
                  <p class="text-justify">
                    <links-page>
                      <card title="Present Committee">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in pemember" :key="i" :name="person.name" :image="person.image">
                            <strong>{{person.desig}}</strong><br><hr>
                            {{ person.edu }}<br>
                            {{ person.dept }}<br>
                            {{ person.addrs }}<br>
                            +91-{{ person.mobile }}<br>
                            {{ person.email }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    
                  </p>
                </div>
                <div class="tab-pane fade in show" id="ecomm2" role="tabpanel">
                  <p class="text-justify">
                    <links-page>
                      <card title="Present Working Committe">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in pwcmem" :key="i" :name="person.name" :image="person.image">
                            <strong>{{person.desig}}</strong><br><hr>
                            {{ person.edu }}<br>
                            {{ person.dept }}<br>
                            {{ person.addrs }}<br>
                            +91-{{ person.mobile }}<br>
                            {{ person.email }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    <br>
                    <links-page>
                      <card title="Media And Publication Cell">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in mpcmem" :key="i" :name="person.name" :image="person.image">
                            <strong>{{person.desig}}</strong><br><hr>
                            {{ person.edu }}<br>
                            {{ person.dept }}<br>
                            {{ person.addrs }}<br>
                            +91-{{ person.mobile }}<br>
                            {{ person.email }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    <br>
                    <links-page>
                      <card title="Event Management Cell">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in emcmem" :key="i" :name="person.name" :image="person.image">
                            <strong>{{person.desig}}</strong><br><hr>
                            {{ person.edu }}<br>
                            {{ person.dept }}<br>
                            {{ person.addrs }}<br>
                            +91-{{ person.mobile }}<br>
                            {{ person.email }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    <br>
                    <links-page>
                      <card title="Sponsorship Cell">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in scmem" :key="i" :name="person.name" :image="person.image">
                            <strong>{{person.desig}}</strong><br><hr>
                            {{ person.edu }}<br>
                            {{ person.dept }}<br>
                            {{ person.addrs }}<br>
                            +91-{{ person.mobile }}<br>
                            {{ person.email }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    
                  </p>
                </div>
                <div class="tab-pane fade in show" id="ecomm3" role="tabpanel">
                  <p class="text-justify">
                    -------
                  </p>
                </div>
              </div>
            </div>

            <div class="tab-pane fade big-list" id="li4" role="tabpanel">
              <h4 class="pane-title" align="left">Activities</h4>
              <hr>
              <ul class="nav md-pills nav-justified pills-secondary">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#activ1" role="tab">Upcoming Events</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#activ2" role="tab">Past Events</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#activ3" role="tab">Members achievements</a>
                </li>                
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade in show active" id="activ1" role="tabpanel">
                  <ul class="link-list">
                    <li><a href="http://nitdgp.ac.in/iimchapter/Doc-18-1.pdf" target="_new">Tough High-Carbon Mattenstite</a></li>
                    <li><a href="http://nitdgp.ac.in/iimchapter/Doc-18-2.pdf" target="_new">Accelerated development of high-performance magnetic materials for emerging technologies.</a></li>
                    <li><a href="http://nitdgp.ac.in/iimchapter/Doc-18-3.pdf" target="_new">Multiscale and multi-physics simulations of chemo-mechanical crystal plasticity problems for complex engineering materials using DAMASK</a></li>
                  </ul>
                </div>
                <div class="tab-pane fade in show" id="activ2" role="tabpanel">
                  <ul class="link-list">
                    <li><a href="http://nitdgp.ac.in/iimchapter/Doc-17.pdf" target="_new">Aluminum Superalloys for high-strength high-temperature applications.</a></li>
                  </ul>
                </div>
                <div class="tab-pane fade in show" id="activ3" role="tabpanel">
                  <strong>Shubhadip Paul</strong> – Awarded the Special Prize for oral presentation on the 10th International Seminar on Metallurgy and Material Science (Behind the Teacher’s Desk), organized by IIM, Jamshedpur Chapter in association with Tata Steel Ltd and CSIR-NML conducted on 28th August, 2020.
                </div>
                
              </div>
              
            </div>

            <div class="tab-pane fade big-list" id="li5" role="tabpanel">
              <h4 class="pane-title" align="left">Membership</h4>
              <hr>
              <p class="text-justify">
                <links-page>
                  <card title="New Membership">
                    <div class="row">
                      <ul class="link-list">
                        <li><a href="http://nitdgp.ac.in/iimchapter/Doc-21.pdf" target="_new">How to apply</a></li>
                        <li><a href="http://nitdgp.ac.in/iimchapter/Doc-22.pdf" target="_new">Membership form</a></li>
                        <li><a href="http://nitdgp.ac.in/iimchapter/Doc-23.pdf" target="_new">Membership form </a></li>
                        <li><a href="http://nitdgp.ac.in/iimchapter/Doc-24.pdf" target="_new">Contact for new membership</a></li>
                      </ul>
                    </div>
                  </card>
                </links-page>
                <br>
                <links-page>
                  <card title="Membership List">
                    <div class="row">
                      <table-renderer :theader="['Name','ID','Phone','Email','Academic Year','Department','Membership']" :table="memdir" />
                    </div>
                  </card>
                </links-page>
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li6" role="tabpanel">
              <h4 class="pane-title" align="left">Notices</h4>
              <hr>  
              <ul class="link-list">
                <li><a href="http://nitdgp.ac.in/iimchapter/Doc-25.pdf" target="_new">Notice for IIM Student Chapter</a></li>
              </ul>       
            </div>

            <div class="tab-pane fade big-list" id="li7" role="tabpanel">
              <h4 class="pane-title" align="left">Gallery</h4>
              <hr>
              <links-page>
                <card title="Photo Gallery">
                  <div class="row">             
                    <div class="text-justify gallery">
                      <img v-for="img in imggallery" :src="img.image" class="glry-item">
                    </div>
                  </div>
                </card>
              </links-page>
              <br>
              <links-page>
                <card title="Video Gallery">
                  <div class="row">             
                    <div class="text-justify gallery">
                      <video  v-for="videofile in videogallery" class="glry-item" width="320" height="240" controls>
                        <source :src="videofile.link" type="video/mp4">
                        Your browser does not support the video tag.
                      </video>
                    </div>
                  </div>
                </card>
              </links-page>
            </div>
            <div class="tab-pane fade big-list" id="li8" role="tabpanel">
              <h4 class="pane-title" align="left">Press Release</h4>
              <hr>
              -------
            </div>
            <div class="tab-pane fade big-list" id="li9" role="tabpanel">
              <h4 class="pane-title" align="left">Downloads</h4>
              <hr>
              <ul class="link-list">
                <li><a href="#">Annual Reports</a></li>
                <li><a href="http://nitdgp.ac.in/iimchapter/Doc-26.pdf">Rules & Regulations</a></li>
              </ul>
            </div>
            <div class="tab-pane fade big-list" id="li10" role="tabpanel">
              <h4 class="pane-title" align="left">Contact Us</h4> 
              <hr>            
              <p class="text-justify">
                IIM Students’ Chapter<br>
                Room Number MM01<br> 
                Department of Metallurgical and Materials Engineering <br>
                National Institute of Technology Durgapur-713209<br> 
                West Bengal <br>
                India<br> 
                Email: iimsc.nitdgp@gmail.com
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li11" role="tabpanel">
              <h4 class="pane-title" align="left">Follow us on</h4>
              <hr>             
              <div class="text-justify social-link">
                <a class="social-btn" href="https://www.linkedin.com/company/the-indian-institute-of-metals-nit-durgapur-chapter/?viewAsMember=true" target="_new"><i class="fa fa-linkedin"></i></a>
                <a class="social-btn" href="https://www.facebook.com/iimscnitdgp/" target="_new"><i class="fa fa-facebook"></i></a>
                <a class="social-btn" href="https://www.youtube.com/channel/UCJGEnFPupkLD_sgbEFTq7Dg/" target="_new"><i class="fa fa-youtube"></i></a>
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
import { convertNewsfeed, genBackendURL, backURL } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import SpCard from '@/components/SpCard'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import LinksPage from '@/components/LinksPage'
import Carousel from '../Carousel'
import Newsfeed from '../Newsfeed'

export default {
  name: 'Geothermal',
  data () {
    return {
      general: true,
      windowWidth: 1000,
      extraNavClasses: [],
      nav: false,
      popUpTop: 0,
      top: -1,
      notices:[],
      slides:[{primary_caption: "IIM Student Chapter", image: "http://nitdgp.ac.in/iimchapter/Pic-0.jpeg", secondary_caption: "IIM Student Chapter"}],
      news:[
        {title: "Shubhadip Paul – Awarded the Special Prize for oral presentation on the 10th International Seminar on Metallurgy and Material Science (Behind the Teacher’s Desk), organized by IIM, Jamshedpur Chapter in association with Tata Steel Ltd and CSIR-NML conducted on 28th August, 2020. ", file: "", date: "2020-08-28", url:""},
        ],
      imggallery:[
        {primary_caption:"Pic-11",primary_caption:"Pic-11",image:"http://nitdgp.ac.in/iimchapter/Pic-11 (1).jpeg"},
        {primary_caption:"Pic-12",primary_caption:"Pic-12",image:"http://nitdgp.ac.in/iimchapter/Pic-12.png"},
        {primary_caption:"Pic-13",primary_caption:"Pic-13",image:"http://nitdgp.ac.in/iimchapter/Pic-13.png"}
        ],
      videogallery:[
        {link:"http://nitdgp.ac.in/iimchapter/AGokhale.mp4"},
        {link:"http://nitdgp.ac.in/iimchapter/KChattopadhyay1.mp4"},
        ],
      pemember:[
        {name: "Dr. Arup kumar Mandal", desig: "Faculty-in-Charge", edu: "Assistant Professor", dept: "Department of Metallurgical and Materials Engineering", addrs: "National Institute of Technology Durgapur", mobile: "9434788110", email: "arup.mandal@mme.nitdgp.ac.in", image: "http://nitdgp.ac.in/iimchapter/Pic-1.jpg"},
        {name: "Dr. Satadal Ghorai", desig: "Associate Faculty-in-Charge", edu: "Assistant Professor", dept: "Department of Metallurgical and Materials Engineering", addrs: "National Institute of Technology Durgapur", mobile: "9470150674", email: "satadal.ghorai@mme.nitdgp.ac.in", image: "http://nitdgp.ac.in/iimchapter/Pic-2.jpg"}
      ],
      pwcmem:[
        {name:"Syed Abdur Rahman",desig : "Chairperson",edu: "B. Tech, 3rd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "7044666253",email: "sar18u10311@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-3.jpg"
        },
        {name:"Malobika Biswas",desig : "Vice Chairperson",edu: "B. Tech, 3rd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9732511949",email: "mb18u10495@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-4.jpg"
        },
        {name:"Shubhadip Paul",desig : "General Secretary",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "6290575323",email: "sp.19u10117@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-5.jpeg"
        },
        {name:"Debakshi Gupta",desig : "Treasurer",edu: "B. Tech, 3rd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9064268823",email: "dg18u10499@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-6.jpg"
        }
      ],
    mpcmem:[
        {name:"Sayan Majumder",desig : "Head",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "7001996145",email: "sm.19u10037@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-7.jpg"
        },
        {name:"Atul Pooniya",desig : "Member",edu: "B. Tech, 2nd Year ",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "8964867724",email: "ap.19u10270@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        },
        {name:"Vishal Jaiswal",desig : "Member",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9093219642",email: "vj.19u10140@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        },
        {name:"Amitabha Biswas",desig : "Member",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9330626914",email: "ab.19U10733@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        },
        {name:"Shyam Srinivas",desig : "member",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9177212755",email: "sss.19u10787@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        }
        
      ],
      emcmem:[
        {name:"Rabin Mondal",desig : "Head",edu: "B. Tech, 3rd Year ",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9883011157",email: "rm18u10392@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-8.png"
        },       
        {name:"Geddam Varnika Sri",desig : "Member ",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "9390193866",email: "gvs.19U10743@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        },       
        {name:"G. Sai Supraja",desig : "Member",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "7029329049",email: "gss.19U10663@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        },       
        {name:"Souvik Mukherjee",desig : "Member",edu: "B. Tech, 2nd Year",dept: "Department of Metallurgical and Materials Engineering",addrs: "National Institute of Technology, Durgapur",mobile: "8583050307",email: "sm.19U10141@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"
        }   
      ],
      scmem:[
        {name: "Trishikha Saha", desig: "Head", edu: "B. Tech, 3rd Year", dept: "Department of Metallurgical and Materials Engineering", addrs: "National Institute of Technology, Durgapur", mobile: "7063495918", email: "ts18u10500@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-9.jpg"},
        {name: "Durgesh Kumar Jha", desig: "Head", edu: "B. Tech, 3rd Year", dept: "Department of Metallurgical and Materials Engineering", addrs: "National Institute of Technology, Durgapur", mobile: "7816030097", email: "dkj18u10304@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/Pic-10.jpg"},
        {name: "Ankit Rai", desig: "Member", edu: "B. Tech, 2nd Year", dept: "Department of Metallurgical and Materials Engineering", addrs: "National Institute of Technology, Durgapur", mobile: "8777324733", email: "ar.19u10539@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"},
        {name: "Chelluboina Sravani", desig: "Member", edu: "B. Tech, 2nd Year", dept: "Department of Metallurgical and Materials Engineering", addrs: "National Institute of Technology, Durgapur", mobile: "9701369588", email: "cs.19u10799@btech.nitdgp.ac.in",image:"http://nitdgp.ac.in/iimchapter/img_avatar.png"}
        
      ],
      memdir:[
        {name:"ABRARUL HAQUE",mem_id: "58193", phone: "7059166797",email:"auh.19U10353@btech.nitdgp.ac.in",acad_year:"2nd Year", dept:"Chemical", mem_start:"01/09/2020"},
        {name:"AMITABHA BISWAS",mem_id:"58198",phone:"9330626914",email:"ab.19u10733@btech.nitdgp.ac.in",acad_year:"2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"ANKIT ADAK",mem_id:" 58177",phone:"7407681473",email:"aa18u10573@btech.nitdgp.ac.in",acad_year:"3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"Ankit Rai",mem_id:"58199",phone:"8777324733",email:"ar.19u19539@btech.nitdgp.ac.in",acad_year:"2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"ARPAN GHOSH",mem_id:"58161",phone:"9382760469",email:"ag18u10577@btech.nitdgp.ac.in",acad_year:"3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"Atul Pooniya",mem_id:" 58192",phone:"8964867724",email:"ap.19u10270@btech.nitdgp.ac.in",acad_year:"2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"BANAMALI KAR",mem_id:" 58171",phone:"8346023375",email:"bk.19u10230@btech.nitdgp.ac.in",acad_year:"2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"DEBAKSHI GUPTA",mem_id:" 58200",phone:"9064268823",email:"dg18u10499@btech.nitdgp.ac.in",acad_year:"3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"Durgesh Kumar Jha",mem_id:"58180",phone:"9010638500",email:"dkj18u10304@btech.nitdgp.ac.in",acad_year:"  3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"G. Chinni Sai Mohan Babu",mem_id:" 58223",phone:"7732099901",email:" gcsmb.19P10269@mtech.nitdgp.ac.in",acad_year:"2nd Year(PG)",dept:"MME",mem_start:"01/09/2020"},
        {name:"GANTA SAI SUPRAJA",mem_id:"58197",phone:"7029329049",email:"gss.19U10663@btech.nitdgp.ac.in",acad_year:" 2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"GEDDAM VARNIKA SRI",mem_id:" 58170",phone:"9390183866",email:"gvs.19U10743@btech.nitdgp.ac.in",acad_year:"   2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"GOMPA KIRANKUMAR",mem_id:" 58178",phone:"7661947016",email:"gkk18u10726@btech.nitdgp.ac.in",acad_year:"  3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"Kanneti. Eswar Reddy",mem_id:" 58179",phone:"8179896407",email:"ker18u10468@btech.nitdgp.ac.in",acad_year:"  3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"KONATHALA SM AEYSHOVARDHAN",mem_id:" 58181",phone:"7780459559",email:"ksma18u10510@btech.nitdgp.ac.in",acad_year:"   3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"MALOBIKA BISWAS",mem_id:"  58176",phone:"9732511949",email:"mb18u10495@btech.nitdgp.ac.in",acad_year:"   3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"RABIN MONDAL",mem_id:" 58191",phone:"8670952593",email:"rm18u10392@btech.nitdgp.ac.in",acad_year:"   3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SARATHI DEY",mem_id:"58182",phone:"8335075319",email:"sd18u10629@btech.nitdgp.ac.in",acad_year:" 3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SAYAN MAJUMDER",mem_id:" 58173",phone:"7001996145",email:"sm.19u10037@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SHALIN SRIVASTAVA",mem_id:"58194",phone:"7029775266",email:"ss.19u10702@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SHUBHADIP PAUL",mem_id:" 58169",phone:"6290575323",email:"sp.19u10117@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SOUVIK MUKHERJEE",mem_id:" 58241",phone:"8583050307",email:"sm.19u10141@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"ME ",mem_start:"01/09/2020"},
        {name:"SRAVANI CHELLUBOINA",mem_id:"  58163",phone:"9701369588",email:"cs.19U10799@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SREEJA VADIGA",mem_id:"  58187",phone:"9553908442",email:"vs.19U10680@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"SURISETTY SHYAM SRINIVAS",mem_id:" 58183",phone:"9177212755",email:"sss.19u10787@btech.nitdgp.ac.in",acad_year:" 2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"Syed Abdur Rahman",mem_id:"  58160",phone:"7044666253",email:"sar18u10311@btech.nitdgp.ac.in",acad_year:"  3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"Tirtharaj Paul",mem_id:" 58190",phone:"8017058704",email:"tp.19u10104@btech.nitdgp.ac.in",acad_year:"  2nd Year ",dept:"ME ",mem_start:"01/09/2020"},
        {name:"TRISHIKHA SAHA",mem_id:" 58165",phone:"7063495918",email:"ts18u10500@btech.nitdgp.ac.in",acad_year:" 3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"UNMESH ROY",mem_id:" 58164",phone:"8337843602",email:"ur18u10374@btech.nitdgp.ac.in",acad_year:" 3rd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"V.B.S.SIDDHARDHA",mem_id:" 58172",phone:"9676709639",email:"vbs.19u10248@btech.nitdgp.ac.in",acad_year:"   2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"VISHAL JAISWAL",mem_id:" 58189",phone:"9093219642",email:"vj.19u10140@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"},
        {name:"YASHWANTH POSHALA",mem_id:"  58195",phone:"9398441817",email:"py.19U10776@btech.nitdgp.ac.in",acad_year:"  2nd Year",dept:"MME",mem_start:"01/09/2020"}
      ]
    }
  },
  created () {
    this.$emit('hideloader', true)
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
    this.notices = convertNewsfeed(this.news)
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
    Card,
    Carousel,
    Newsfeed,
    CardTestimonial,
    LinksPage
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<style scoped>
  .social-link{
    padding: 10px;
  }
  .social-link a{
    text-decoration: none;
    font-size: 30px;
    padding: 10px 20px;
    border: 1px solid #0275d8;
  }
  .social-link a:hover{
    background: #0275d8;
    transition: 2s;
  }
  .social-link a:hover i{
    color: #fff;
    transition: 2s;
  }
  .link-list{
    list-style-type: none;
  }
  .link-list li{
    padding: 3px;
    background: #e0f7fa;
    margin: 3px auto;
  }
  .link-list li:hover{
    background: #001333;
  }
  .link-list li a{
    color: #000;
  }
  .link-list li:hover a{
    color: #fff;
  }
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
  .gallery{
    display: grid;
    grid-template-columns: auto auto auto;
    background-color: #2196F3;
    padding: 10px;  
  }
  .glry-item{
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid rgba(0, 0, 0, 0.8);
    padding: 20px;
    font-size: 30px;
    text-align: center;
    width: 100%;
    height: 400px;
  }
  .card-pic .caro-wrap {
    height: 380px;
    background: -webkit-gradient(linear,left top, left bottom,from(#03A9F4),color-stop(#039BE5),color-stop(#039BE5),to(#039BE5));
    background: linear-gradient(#03A9F4,#039BE5,#039BE5,#039BE5);
  }
  element {

}
.carousel-item {

    height: 100%;

}
.anim1 {
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-name: fadeIn;
    animation-name: fadeIn;
    -webkit-animation-delay: 0s;
    animation-delay: 0s;
    -webkit-animation-timing-function: initial;
    animation-timing-function: initial;
    -webkit-animation-iteration-count: initial;
    animation-iteration-count: initial;
    -webkit-animation-direction: initial;
    animation-direction: initial;
    -webkit-animation-fill-mode: initial;
    animation-fill-mode: initial;
    -webkit-animation-play-state: initial;
    animation-play-state: initial;
}
.carousel-item {
    display: none;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    width: 100%;
    transition: -webkit-transform .6s ease;
    -webkit-transition: -webkit-transform .6s ease;
    transition: transform .6s ease;
    transition: transform .6s ease, -webkit-transform .6s ease;
    transition: transform .6s ease,-webkit-transform .6s ease;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    perspective: 1000px;
}
.carousel, .carousel-inner, .carousel-item {
    position: relative;
}

  @media screen and (min-width: 909px) {
    .btn {
      display: none;
      height: 0px;
    }
    .geoimage{
      width: 100%;
    }
  }
  @media screen and (max-width: 512px) {
    .geoimage{
      width: 100%;
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
