<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text text-center">Medical Unit</a>
      <div class="card-body">
        <div class="row newscaro">
          <div class="col-8 caro" style="width: 100%;margin: 0 auto;">
          <Carousel :slides="slides"></Carousel>
        </div>
        <div class="col-4 news">
          <Bulletin :notices="notices"></Bulletin>
        </div>
        </div>
        
        <div class="text-center medi-title">HOSPITAL</div>
        <div class="medi-text">
          <p class="text-center" style="font-size: 20px;font-weight: bold;">
            “Wherever the art of medicine is loved, there is also a love of humanity”-Hippocrates.
          </p>
          NIT Durgapur promotes healthy and fit lifestyle of the campus community and focuses on both physical
          and psychological well-being. The Medical Unit-cum-Hospital prioritizes intensive care and attentive treatment by catering to the needs of its employees and students. One of the most indispensable
          necessities in the college campus, the Medical Unit of the Institute is served by three resident doctors, three temporary doctors and other medical staff. Apart from morning and evening OPDs, there is also a provision for round the clock medical emergency services. Besides the regular doctors, specialist doctors from various domains of expertise visit the medical unit on certain days in a week. It has observatory beds, isolation ward for students and dressing room. Moreover, the unit has an outsourced pathological blood collection and reporting system from IQ city hospital. The institute is upgrading the old facilities in order to provide the students and the staff with efficient treatment. In case of any serious  illness, patients are referred to State Government Hospital, The Mission Hospital, IQ City Hospital and some other hospitals  with which it has specific tie-ups. The Medical unit has a help desk for insurance for different kinds of treatments.
        </div>                
        <div class="text-center medi-title">Facilities</div>
        <div class="medi-text">
          <ul>
            <li>Morning and Evening OPDs except sunday and holidays</li>
            <li>Round the clock medical emergencies</li>
            <li>Visiting Physicians of different fields on fixed days</li>
            <li>Pharmacy (24x7 Pharmacy Facility in the institute is under active consideration)</li>
            <li>24 Hrs. one ambulance service and one  stand-by vehicle</li>
            <li>Observatory Beds</li>
            <li>Isolation ward for the students</li>
            <li>Dressing Room</li>
            <li>Sample collection center for outsourced pathological laboratory (9.30 AM to 10.30 AM except sunday and holidays)</li>
            <li>Nebulization</li>
            <li>Insurance help desk for students</li>
          </ul>
        </div>
        <div class="text-center medi-title">Counselling Centre for Psychosocial Wellness</div>
        <div class="medi-text">
          <p>The Counselling Centre strives to improve mental health of the students by providing them psychological counselling to cope with emotional trauma and stress.</p>
          <p><h4>Objective :</h4></p>
          <ul>
            <li>To sensitize students about the symptoms and causes of sudden depression and anxiety and enable them to identify harmful effects of addiction</li>
            <li>To raise awareness among students about behavioural disorders and the ways to gain control over anger and revengeful attitude</li>
            <li>To help students learn stress management skills</li>
            <li>To offer professional help to victims and potential victims to overcome depression, distress, addiction and stressful conditions through individual counselling and medication</li>
          </ul>
          <p><h4>Services rendered :</h4></p>
          <ul>
            <li>Clinical and support services are offered by a team of professional psychiatrists and psychologists. Counselling by psychologists is available four days a week while psychiatric treatment by experts is available twice a week. For details, see the <a href="https://admin.nitdgp.ac.in/files/academics/notices/2018/09/07/Timeschedule_R1.pdf" target="_blank"><span style="color: red;">schedule</span></a></li>    
            <li>Occasional sensitization programmes are organized.</li>
          </ul>
        </div>        
        <div class="text-center medi-title">Mdeical Officers & Temporary Doctors</div>
        <div class="medi-text-flex">
          <div class="sub-mdei-div">
            <h5 class="text-center">
              <u>Mdeical Officers</u>
            </h5>
            <div>
              <table class="table table-responsive-md table-bordered">
                <thead class="mdb-color lighten-4">
                  <tr>
                    <th class="th-lg">Name</th>
                    <th class="th-lg">Designation</th>
                    <th class="th-lg">Mobile</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>DR. B.K. Sarkar</td>
                    <td>Senior Medical Officer</td>
                    <td>+91-9434788075</td>
                  </tr>
                  <tr>
                    <td>DR. (Mrs.) S. Patra</td>
                    <td>Medical Officer</td>
                    <td>+91-9434788076</td>
                  </tr>
                  <tr>
                    <td>DR.(Mrs.) G.Pravabhati</td>
                    <td>Medical Officer</td>
                    <td>+91-9434789029</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="sub-mdei-div">
            <h5 class="text-center"><u>Temporary Doctors</u></h5>
            <div>
              <p class="text-center">DR. Daisy Bhengra <br>DR. Arnab Saha <br> DR. Anisul Islam </p>
            </div>
          </div>          
        </div>
        <div class="text-center medi-title">Hospital Timings</div>
        <div class="medi-text">          
          <ul>
            <li>Monday to Saturday Morning and Evening OPD, Timings: Morning OPD:9 AM- 1 PM Evening OPD:5 PM- 9 PM</li> 
            <li>Round the clock emergency services on all days 24×7.</li>
            <li>Sunday and Institute Holidays- Outdoor facility is not available only emergency facilities available. </li>
          </ul>
        </div>
        <div class="text-center medi-title">List of Doctors & schedule</div>  <div class="medi-text">
          <table class="table table-responsive-md table-bordered">
            <thead class="mdb-color lighten-4">
              <tr>
                <th class="th-lg">Name of Doctors</th>
                <th class="th-lg">Timing</th>
              </tr>
            </thead>
            <tbody>
              <tr>                
                <td>Dr. Dipankar Chakraborty (Cardiology and Medicine)</td>
                <td>MON (5PM), WED (7PM), THU (5PM)</td>
              </tr>
              <tr>                
                <td>Dr. Sukesh Nath (Medicine)</td>
                <td>TUE (12 NOON)</td>
              </tr>
              <tr>                
                <td>Dr. Ishani Dasgupta (Gynaec & Obs.) </td>
                <td>TUE (6:30 PM)</td>
              </tr>
              <tr>                
                <td>Dr. Anita Chatterjee (Eye Specialist)</td>
                <td>FRI (10:00 AM)</td>
              </tr> 
              <tr>                
                <td>Dr. Subir Mukherjee (Dentist) </td>
                <td>TUE (5PM), THU (5PM), SAT (5PM)</td>
              </tr>
              <tr>                
                <td>Dr. Debashish Roy (ENT Specialist) </td>
                <td>WED (11AM)</td>
              </tr>
              <tr>                
                <td>Dr. Om Prakash Singh (Psychiatrist) </td>
                <td>SUN (9 AM) (ALTERNATE)</td>
              </tr>

            </tbody>
          </table>
        </div>
        <div class="text-center medi-title">List of TIE-UP Hospitals</div>
        <div class="medi-text-flex">
          <div class="sub-mdei-div">
            <h5 class="text-center"><u>Durgapur</u></h5>
            <ul>
              <li>The Mission Hospital</li>
              <li>IQ City Medical Collage Hospital</li>
              <li>Healthworld Hospital</li>
              <li>Vivekananda Hospital</li>
              <li>Gouri Devi Hospital & Research Institute</li>
              <li>City Hospital</li>
              <li>Disha Eye Hospital - Durgapur & Barrackpore</li>
            </ul>
          </div>
          <div class="sub-mdei-div">
            <h5 class="text-center"><u>Kolkata</u></h5>
            <ul>
              <li>Ruby General Hospital</li>
              <li>Peerless Hospital & Research Center</li>
              <li>AMRI Hospital</li>
              <li>B.P. poddar Hospital & Medical research Limited</li>
            </ul>
          </div>          
        </div>
        <div class="text-center medi-title"><strong>Contact Details</strong></div>
        <div class="medi-text-flex">          
          <div class="sub-mdei-div3">
            <strong>Dr. B. K. Sarkar (MBBS)</strong><br>
            Phone: +91-343-2757118<br>
            Mobile: +91-9434788075<br>
            Email: b.sarkar@admin.nitdgp.ac.in<br>
          </div>
          <div class="sub-mdei-div3">
            <strong>Dr. ( Mrs. )S. Patra (MBBS)</strong><br>
            Phone: +91-343-2757116<br>
            Mobile: +91-9434788076<br>
            Email: s.patra@admin.nitdgp.ac.in<br>
          </div>
          <div class="sub-mdei-div3">
            <strong>Dr. (Mrs.) G. Pravabhati (MBBS)</strong><br>
            Mobile: +91-9434789029<br>
            Email: g.prabhavathi@admin.nitdgp.ac.in<br>
          </div>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
  import Carousel from '../Carousel'
  import Bulletin from '../Bulletin'
  import { convertNewsfeed } from '@/common.js'
export default {
  name: 'Mu',
  data(){
    return {
      notices:[],
      slides: [
        {primary_caption:"Medical Unit",secondary_caption:"Medical Unit",image:"http://nitdgp.ac.in/MU/Outside.jpg"},
        {primary_caption:"OPD of Medical Unit",secondary_caption:"OPD of Medical Unit",image:"http://nitdgp.ac.in/MU/outdoor.jpg"},
        {primary_caption:"Entrance & Lobby",secondary_caption:"Entrance & Lobby",image:"http://nitdgp.ac.in/MU/corridoor.jpg"},
        {primary_caption:"Dental OPD",secondary_caption:"Dental OPD",image:"http://nitdgp.ac.in/MU/dental_opd.jpg"},
        {primary_caption:"Counselling Centre for Wellness",secondary_caption:"Counselling Centre for Wellness",image:"http://nitdgp.ac.in/MU/councelling_center.jpg"},
        {primary_caption:"Resting Ward",secondary_caption:"Resting Ward",image:"http://nitdgp.ac.in/MU/watchroom.jpg"},
        {primary_caption:"Emergency Ward",secondary_caption:"Emergency Ward",image:"http://nitdgp.ac.in/MU/emergency_ward.jpg"},        
      ],
      buletins:[
        
      ]
    }
    
  },
  components: {
    Carousel,
    Bulletin
  },
  created () {
    this.notices = convertNewsfeed(this.buletins)
    this.$emit('hideloader', true)
  }
}
</script>
<style scoped="scoped">
  .card-pic img{
    margin-top: 0;
  }
  .medi-text{
    border: 1px solid #33b5e5;
    padding: 8px 10px;
    text-align: justify;
  }
  .medi-title{
    background: #33b5e5;
    color: #fff;
    width: 100%;
    min-height: 30px;
    line-height: 30px;
    margin-top: 10px;
    border-top-right-radius: 5px;
    border-top-left-radius: 5px;
  }
  .page-type-links .date-col .black-text {
    margin-left: 6.5em;
  }
  .medi-text-flex{
    border: 1px solid #33b5e5;
    padding: 8px 10px;
    text-align: justify;
    display: flex;
    flex-direction: row;
  }
  .sub-mdei-div{
    border: 1px solid #33b5e5;
    width: 100%;
    text-align: justify;
    margin-right: 3px;
  }
  .sub-mdei-div3{
    border: 1px solid #33b5e5;
    width: 33%;
    text-align: justify;
    margin-right: 3px;
  }
  tbody tr td{
    color: #000;
    font-weight: bold;
  }
@media screen and (max-width: 760px;){
  .col-8{
    width: 100%;
  }
}
</style>
