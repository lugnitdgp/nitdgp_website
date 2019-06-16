<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card container-fluid">
      <a class="card-header white-text text-center">Logo Competition</a>
      <div class="card-body px-lg-5 pt-0">
        <form action="" method="" enctype="multipart/form-data" class="form-group" id="c_form" @submit.prevent="logo_data()">
          <input type="text" id="name" class="form-control" v-model="name" placeholder="Your Full Name" required="required">
          <input type="text" id="guardian" class="form-control" v-model="guardian" placeholder="Guardian Name" required="required">        
          <input type="email" id="email" class="form-control" v-model="email" placeholder="Valid Email Id" required="required">
          <input type="number" id="mob" class="form-control" v-model="mob" placeholder="Mobile Number" required="required">
          <span class="text-center" style="margin-left: 50px;">Choose your logo image</span>
          <input type="file" id="file" name="file" ref="file" class="form-control" v-on:change="processFile()" required="required">
          <div class="text-center">
            <input type="submit" class="btn btn-primary text-center complain" :class="{ disabled: inactive }" value="Submit" >
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL, backURL } from '@/common.js'

export default {
  name: 'Logocompetition',
  data() {
    return {
      name:'',
      guardian:'',
      email:'',
      mob:'',
      file:'',
      sizeflag: 0,
      typeflag: 0,
      inactive: false

    }
  },
  created () {    
    this.$emit('hideloader', true)
  },
  methods:{
    logo_data(){
      let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

      if(this.mob.length<10 || this.mob.length>11){
        alert("Incorrect Mobile Number")
        return false
      }

      if(!re.test(this.email)){
        alert("Incorrect Email Format")
        return false
      }     
      if(this.sizeflag == 1){
        alert("File Size More than 2 MB")
        return false
      }
      if(this.typeflag==1){
        alert("Invalid File Type. Select an Image file")
        return false
      }
      let data = new FormData()
      data.append('name',this.name)
      data.append('guardian',this.guardian)
      data.append('email',this.email)
      data.append('mobile',this.mob)
      data.append('logoimg',this.file)
      //this.inactive = true
      
      axios({
        method: 'post',
        //url: 'https://admin.nitdgp.ac.in/facilities/logocompetition/',
        url: 'http://localhost:8000/facilities/logocompetition/',
        headers:{
          'Content-Type':'multipart/form-data'
        },
        data: data,
      }).then(response => {
            let sms = response.data.message
            if(sms=='Already Register'){
              alert("Email Id Already Register!!")              
            }
            else{
              alert(sms)
              // location.reload(true)
              window.location.href = '/logocompetition'
            }
          })
          .catch(e => {
            alert(e)
          })
          
    },
    processFile(){
      this.file = this.$refs.file.files[0]
      if(this.file.size > 3000000)
      {
        this.sizeflag = 1
      }
      if(this.file.type =='image/jpeg' || this.file.type == 'image/png' || this.file.type == 'image/gif')
      {
        this.typeflag = 0
      }
      else{
        this.typeflag = 1
      }
      console.log(this.typeflag)
      console.log(this.file.type)
      console.log(this.file.size)
      
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
  input[type="text"], input[type="email"], input[type="number"], input[type="file"], input[type="url"],input[type="password"], select, textarea{
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
input[type="text"]:focus:not([readonly]), input[type="email"]:focus:not([readonly]), input[type="number"]:focus:not([readonly]), input[type="file"]:focus:not([readonly]), input[type="url"]:focus:not([readonly]),input[type="password"]:focus:not([readonly]), select:focus:not([readonly]), textarea:focus:not([readonly]){
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