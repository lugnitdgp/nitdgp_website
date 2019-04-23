<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text text-center">HOSPITAL</a>
      <div class="card-body">
        <div style="text-align: center;">
          <img style="max-height:300px;max-width: 100%;margin-bottom: 10px;" src="https://nitdgp.ac.in/AllPDF/medical.jpg" width="100%"><br>
        </div>
        <div class="medi-text">
          <p class="text-center" style="font-size: 20px;font-weight: bold;">
            “Wherever the art of medicine is loved, there is a love of humanity”-Hippocrates
          </p>
          One of the most indispensable necessities in the college campus, the <b>Medical Unit</b> of our Institute is served by three resident doctors, three temporary doctors and other medical staff. With Morning and Evening OPDs, there is also a provision of <b>round the clock medical emergency services</b>. Apart from the regular doctors, specialist doctors of <b>various fields visit the medical unit</b> on fixed days of a week. It has observatory beds, isolation ward for students and dressing room. Moreover, the unit has an <b>outsourced pathological blood collection and reporting system from IQ city hospital</b>. The institute is upgrading the old facilities in order to provide the students and the staff with efficient treatment. In case of any serious sickness, patients are referred to State Government Hospital, The Mission Hospital, IQ City Hospital and <b>some other hospitals with tie up</b>. The Medical unit has a help desk for insurance for these kinds of treatments.
        </div>        
          <div class="text-center medi-title">Mdeical Officers</div>
        <div class="medi-text">
          <table class="table table-responsive-md table-bordered">
            <thead class="mdb-color lighten-4">
              <tr>
                <th class="th-lg">Name</th>
                <th class="th-lg">Designation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>DR. B.K. Sarkar</td>
                <td>Senior Medical Officer</td>
              </tr>
              <tr>
                <td>DR. (Mrs.) S. Patra</td>
                <td>Medical Officer</td>
              </tr>
              <tr>
                <td>DR. (Mrs.) G. Pravabhati</td>
                <td>Medical Officer</td>
              </tr>
            </tbody>
          </table>
        </div>  
          <div class="text-center medi-title">Temporary Doctors</div>
        <div class="medi-text">
          <p class="text-center">DR.Daisy Bhengra <br>DR. Arnab Saha <br> DR. Anisul Islam </p>
        </div>
        <div class="text-center medi-title">HOSPITAL TIMINGS</div>
        <div class="medi-text">          
          <ul>
            <li>Monday to Saturday Morning and Evening OPD, Timings: MOPD:9 AM- 1 PM EOPD:5 PM- 9 PM</li> 
            <li>Round the clock emergency services on all days 24×7.</li>
            <li>Sunday and Institute Holidays- Outdoor facility is not available only emergency facilities available. </li>
          </ul>
        </div>
        <div class="text-center medi-title">List of Doctors</div>  <div class="medi-text">
          <table class="table table-responsive-md table-bordered">
            <thead class="mdb-color lighten-4">
              <tr>
                <th class="th-lg">Name Of Doctors</th>
                <th class="th-lg">Timing</th>
              </tr>
            </thead>
            <tbody>
              <tr>                
                <td>Dr.Dipankar Chakraborty(Cardiology and Medicine)</td>
                <td>MON (5PM),WED (7PM),THU (5PM)</td>
              </tr>
              <tr>                
                <td>Dr.Sukesh Nath(Medicine)</td>
                <td>TUE (12 NOON)</td>
              </tr>
              <tr>                
                <td>Dr.Ishani Dasgupta(Gynaec& Obs.) </td>
                <td>TUE (6:30 PM)</td>
              </tr>
              <tr>                
                <td>Dr.Anita Chatterjee(Eye Specialist)</td>
                <td>FRI (10:00 AM)</td>
              </tr> 
              <tr>                
                <td>Dr.Subir Mukherjee(Dentist) </td>
                <td>TUE (5PM),THU (5PM), SAT (5PM)</td>
              </tr>
              <tr>                
                <td>Dr.Debashish Roy(ENT Specialist) </td>
                <td>FRI (11AM)</td>
              </tr>
              <tr>                
                <td>Dr.Om Prakash Singh(Psychiatrist) </td>
                <td>SUN (9 AM) (ALTERNATE)</td>
              </tr>

            </tbody>
          </table>
        </div>
        <div class="text-center medi-title"><strong>Contact Details</strong></div>
        <div class="medi-text">          
          <p>
            <strong>Dr. B. K. Sarkar ( MBBS )</strong><br>
            Phone: +91-343-2757118<br>
            Mobile: +91-9434788075<br>
            Email: b.sarkar@admin.nitdgp.ac.in<br>
            <strong>Dr. ( Mrs. )S. Patra ( MBBS )</strong><br>
            Phone: +91-343-2757116<br>
            Mobile: +91-9434788076<br>
            Email: s.patra@admin.nitdgp.ac.in<br>
          </p>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Mu',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
<style scoped="scoped">
  .medi-text{
    border: 1px solid #007;
    padding: 8px 10px;
    text-align: justify;
  }
  .medi-title{
    background: #007;
    color: #fff;
    width: 100%;
    min-height: 30px;
    line-height: 30px;
    margin-top: 10px;

  }
</style>
