<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card container-fluid">
      <a class="card-header white-text">Prevent Caste Based Discrimination</a>
      <div class="card-body row">
        <div class="col-12">
          <ul class="nav md-pills nav-justified pills-secondary ulbackground">
            <li class="nav-item">
              <a class="nav-link active" data-toggle="tab" href="#panell1" role="tab">Complaint Form</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-toggle="tab" href="#panell2" role="tab">All Complaints</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-toggle="tab" href="#panell3" role="tab">Admin Login</a>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade in show active" id="panell1" role="tabpanel">      
              <div class="col-12 form-wrapper">
                <div class="card pcbdlogin">
                  <h5 class="card-header info-color white-text text-center py-4">
                    <strong>Complaint Form</strong>
                  </h5>
                  <!--Card content-->
                  <div class="card-body px-lg-5 pt-0">
                    <form action="" method="" class="form-group" id="c_form" @submit.prevent="pcbd_data()">
                        <input type="text" id="c_no" class="form-control" v-model="c_no" readonly="readonly">
                        <input type="text" id="stdname" class="form-control" v-model="stdname" placeholder="Your Full Name" required="required">
                        <input type="email" id="email" class="form-control" v-model="email" placeholder="Valid Email Id" required="required">
                        <input type="number" id="mob" class="form-control" v-model="mob" placeholder="Mobile Number" required="required">
                        <span class="text-center" style="margin-left: 50px;">Select Your Category</span>
                        <select class="form-control" v-model="cat" id="cat">
                          <option value="sc">SC</option>
                          <option value="st">ST</option>
                          <option value="obc">OBC</option>
                          <option value="pc">PC (Physically Challenged)</option>
                        </select>
                        <textarea class="form-control addr" cols="30" rows="35" id="address" placeholder="Address" v-model="address" required="required"></textarea>
                        <textarea class="form-control compl" cols="30" rows="10" id="compl" placeholder="Lodge Complaint" v-model="compl" required="required"></textarea><br>
                        <div class="text-center">
                          <input type="submit" class="btn btn-primary text-center complain" :class="{ disabled: inactive }" value="Submit">
                        </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade page-type-links" id="panell2" role="tabpanel">
            <p class="text-center" style="font-size: 25px;font-weight: bold;font-family: Courier New, Courier, monospace ;font-style: oblique;"> All Complaints</p>
            <table class="table table-bordered table-responsive-md">
              <thead class="mdb-color lighten-4">
                <th class="text-center th-lg"><strong>Complaint Number</strong></th>
                <th class="text-center th-lg"><strong>Name</strong></th>
                <th class="text-center th-lg"><strong>Email</strong></th>
                <th class="text-center th-lg"><strong>Mobile</strong></th>
                <th class="text-center th-lg"><strong>Category</strong></th>
                <th class="text-center th-lg"><strong>Address</strong></th>
                <th class="text-center th-lg"><strong>Complaint</strong></th>
                <th class="text-center th-lg"><strong>Reply</strong></th>
                <th class="text-center th-lg"><strong>Reply File (If any)</strong></th>
              </thead>
              <tbody>
                <tr v-for="(complaint, i) in allcomplnt">
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">{{ complaint.c_number }}</td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">{{ complaint.name }}</td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">{{ complaint.email }}</td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">{{ complaint.mobile }}</td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">{{ complaint.cat }}</td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;"><span v-html="counterCmplnt(complaint.address)"></span></td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;"><span v-html="counterCmplnt(complaint.complaint)"></span><button class="btn btn-rounded btn-warning" :id="i" style="background: #32fcd4;cursor: pointer;" @click.prevent="spanDetails(complaint.complaint)">Detalis</button></td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">
                    <span v-if="complaint.replytxt!=''" v-html="complaint.replytxt"></span>
                    <span v-else style="color:red;">Not Available</span>
                  </td>
                  <td style="font-family: Courier New, Courier, monospace ;font-style: oblique;">
                    <span v-if="complaint.replyurl!=null"><a :href="complaint.replyurl" target="_blank" style="color: green;"> PDF</a> </span>
                    <span v-else style="color:red;">Not Available</span>
                  </td>
                </tr>
              </tbody>
            </table>
            </div>
            <div class="tab-pane fade page-type-links" id="panell3" role="tabpanel">
              
              <!-- Material form login -->
                <div class="card pcbdlogin">
                  <h5 class="card-header info-color white-text text-center py-4">
                    <strong>Admin Login Form</strong>
                  </h5>
                  <!--Card content-->
                  <div class="card-body px-lg-5 pt-0">
                    <!-- Form -->
                    <form class="text-center" style="color: #757575;">
                      <!-- Email -->
                      <input type="email" id="email" class="form-control" placeholder="Valid Email Id" required="required">
                      <!-- Password -->
                      <input type="password" id="password" class="form-control" placeholder="Admin Password" required="required">
                      <br>
                      <!-- Sign in button -->
                      <button class="btn btn-primary btn-rounded loginbtn" type="submit">Sign in</button>
                      
                    </form>
                    <!-- Form -->

                  </div>

                </div>
                <!-- Material form login -->
            </div>
          </div>
        </div>
        <hr class="seperation">
        
        
        </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL, backURL } from '@/common.js'

export default {
  name: 'Pcbd',
  data() {
    return {
      ranvalue: '',
      dt:'',
      mnt:'',
      sec:'',
      day:'',
      c_no:'',
      stdname:'',
      email:'',
      mob:'',
      cat:'obc',
      address:'',
      compl:'',
      allcomplnt: [],
      inactive: false

    }
  },
  created () {
    this.ranvalue = Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000;
    this.dt = new Date();
    this.mnt = this.dt.getMonth()
    this.sec = this.dt.getSeconds()
    this.day = this.dt.getDay()
    this.c_no = 'NITD/PCBD/'+this.mnt+this.sec+this.day+'/'+this.ranvalue;
    this.inactive = false
    axios.get(genBackendURL("facilities/pcbd/"))
                .then(response => {
                  this.allcomplnt = response.data.results                  
                })
                .catch(e => {
                  console.log(e)
                })
    this.$emit('hideloader', true)
  },
  methods:{
    pcbd_data(){
      let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

      if(this.mob.length<10 || this.mob.length>11){
        alert("Incorrect Mobile Number")
        return false
      }

      if(!re.test(this.email)){
        alert("Incorrect Email Format")
        return false
      }
      let data = new FormData()
      data.append('c_number',this.c_no)
      data.append('name',this.stdname)
      data.append('email',this.email)
      data.append('mobile',this.mob)
      data.append('cat',this.cat)
      data.append('address',this.address)
      data.append('complaint',this.compl)
      this.inactive = true
      
      axios({
        method: 'post',
        url: 'https://admin.nitdgp.ac.in/facilities/pcbdcomplaint/',
        data: data,
      }).then(response => {
            let sms = response.data.message
            if(sms=='Already Register'){
              alert("Email Id Already Register!!")              
            }
            else{
              alert(sms)
              // location.reload(true)
              window.location.href = '/pcbd'
            }
            
            
          })
          .catch(e => {
            alert(e)
          })
    },
    counterCmplnt(c){
      if(c.length>100){
        return c.slice(0, 100)+'...'
      }
      else{
        return c
      }
    },
    spanDetails(msg){

      alert(msg)
    }
  }
}
</script>
<style scoped="scoped">
  select.form-control:not([size]):not([multiple]) {
    height: calc(2.25rem + 0px);
}
  .seperation{
    display: none;
  }
  .form-control{
    width: 90%;
    margin:0 auto;
    color: #000133;
    
  }
  .ulbackground{
    background: #001333;
    color: #fff;
  }
  .ulbackground li a{
    color: #fff;
  } 
  .pills-secondary .nav-link.active, .pills-secondary .show > .nav-link, .tabs-secondary {
    background-color: #fff !important;
}
.md-pills .nav-link.active {
    color: #000;
    background-color: #2bbbad;
}
  .addr{
    height: 150px;
    margin-top: 5px;
  }
  .compl{
    height: 250px;
    margin-top: 5px;
  }
  .mandatory{
    color: red;
    font-size: 2em;
  }
  .text-left{
    text-align: center;
    font-size: 1em;
  }
  #c_form{
    width: 100%;
    margin:0 auto;
    /*background-color:#d81b60!important*/
  }
  .pcbdlogin{
    margin-left: 5%;
    margin-right: 5%;
  }
  .loginbtn{
    width: 50%;
    margin: 0 auto;
  }
  .loginbtn:hover{
    background-color: #33b5e5 !important;
    color: #fff;
  }
  input[type="text"], input[type="email"], input[type="number"], input[type="time"], input[type="url"],input[type="password"], select, textarea{
    background-color: transparent;
    border: 1px solid #a2a2a2;
    border-radius: 0;
    outline: 0;
    height: 2.1rem;
    width: 90%;
    font-size: 1rem;
    margin-top: 5px;
    box-shadow: none;
    box-sizing: content-box;
    -webkit-transition: all .3s;
    transition: all .3s;
    display: block !important;
}
input[type="text"]:focus:not([readonly]), input[type="email"]:focus:not([readonly]), input[type="number"]:focus:not([readonly]), input[type="time"]:focus:not([readonly]), input[type="url"]:focus:not([readonly]),input[type="password"]:focus:not([readonly]), select:focus:not([readonly]), textarea:focus:not([readonly]){
  border: 1px solid #4285F4;
  box-shadow: 1px 1px 1px 1px #4285F4;
}
@media screen and (max-width: 900px)  {
    .col-10,.col-2{
      -ms-flex: 0 0 100%;
      -webkit-box-flex: 0;
      flex: 0 0 100%;
      max-width: 100%;
      padding-right: 0px;
      padding-left: 0px;  
    }
    .seperation{
      margin-top: 10px;
      border-bottom: 3px solid #d2d2d2;
      display: block;
    }
    .form-control{
    width: 90%;
    margin:0 auto;
    color: #000133;    
    }
    #c_form{
    width: 100%;
    margin:0 auto;
    /*background-color:#d81b60!important*/
    }
    .addr{
    height: 150px;
    margin-top: 5px;
  }
  .compl{
    height: 250px;
    margin-top: 5px;
    }
    .pcbdlogin{
    margin-left: 1%;
    margin-right: 1%;
  }
  }
</style>