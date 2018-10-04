<template>
  <footer v-if="footer" class="page-footer center-on-small-only">
    <div class="container" id="footer-container">
      <div class="container-fluid" align="center">
        <div class="row quick-links-row quick-links-container">
          <div v-for="link in links" class="container-fluid">
            <div v-if="link.name == 'MHRD'">
              <div class="modal fade" :id="'mhrdModal'" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 style="color:black;" class="modal-title" id="mhrdModal">You are leaving www.nitdgp.ac.in</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                    <div class="modal-body" style="color:black;">
                      Are you sure you want to go to {{link.name}}
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-primary" data-dismiss="modal">Stay Here</button>
                      <a :href="link.href" class="btn btn-danger">Go There</a>
                    </div>
                  </div>
                </div>
              </div>
              <a href="#" data-toggle="modal" :data-target="'#mhrdModal'" class="container-fluid logo-container">
                {{link.name}}
              </a>
            </div>
            <quick-links v-else-if="link.name == 'Quick Links'">
              
            </quick-links>
            <div v-else>
              <a :href="link.href">{{ link.name }}</a>
            </div>
          </div>
        </div>
        <div class="row">
          <div v-for="(logo, index) in logos" class="modal fade" :id="'basicExampleModal'+index" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 style="color:black;" class="modal-title" id="exampleModalLabel">You are leaving www.nitdgp.ac.in</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body" style="color:black;">
                  Are you sure you want to go to <img :src="['/static/img/' + logo.name + '.png']" :alt="logo.name">
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-primary" data-dismiss="modal">Stay Here</button>
                  <a :href="logo.href" class="btn btn-danger">Go There</a>
                </div>
              </div>
            </div>
          </div>
          <a v-for="(logo,index) in logos" data-toggle="modal" :data-target="'#basicExampleModal'+index"
            class="container-fluid logo-container">
            <img :src="['/static/img/' + logo.name + '.png']" :alt="logo.name">
          </a>
        </div>
      </div>
    </div>
    <div class="footer-copyright" id="footer-copyright">
      <div class="row">
        <div class="container-fluid ftr-1">
          <span class="copyright-txt">
            Last updated: {{ footer.last_updated.slice(0,10) }}
          </span>
        </div>
        <div class="container-fluid ftr-2">
          <span class="copyright-txt">© 2018 Copyright: <a href="https://www.nitdgp.ac.in"> nitdgp.ac.in </a></span>
        </div>
        <div class="container-fluid ftr-3">
          <span class="copyright-txt">Visitors Count: {{ footer.hits }} </span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import axios from 'axios'
import { genBackendURL } from '@/common.js'
import QuickLinks from '@/components/QuickLinks'

export default {
  name: 'Footer',
  data() {
    return {
      footer: undefined,
      logos: [{name: 'govlogo1', href:"https://www.india.gov.in/"},
              {name: 'govlogo2', href:"https://www.mygov.in/"},
              {name: 'govlogo3', href:"http://dial.gov.in/"},
              {name: 'govlogo4', href:"http://digitalindia.gov.in/"},
              {name: 'govlogo5', href:"https://evisitors.nic.in/"},
              {name: 'govlogo6', href:"http://www.nvsp.in/"},
              {name: 'govlogo7', href:"https://data.gov.in/"},
              {name: 'govlogo8', href:"http://rti.gov.in/"},
              {name: 'govlogo9', href:"http://electronicsindia.co.in/"},
              {name: 'govlogo10', href:"http://swachhbharatmission.gov.in"}],
      links: [{name: "Quick Links", href: "#"},
              {name: "Holidays", href: "/holidays"},
              {name: "Notices@NITD", href: "/notices/general"},
              {name: "Careers@NITD", href: "/careers"},
              {name: "Tenders@NITD", href: "/tenders"},
              {name: "MHRD", href: "/mhrd"},
              {name: "Webteam", href: "/webteam"},
              {name: "Archives", href: "/archives"},
              // {name: "Policies", href: "/policies"},
              {name: "Downloads", href: "/downloads"}]
    }
  },
  created () {
    axios.get(genBackendURL("dashboard/footer"))
         .then(response => {
           this.footer = response.data
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components:{
    QuickLinks
  }
}
</script>

<style>
  footer {
    width: 100%;
    min-height: 170px;
    bottom: 0;
  }
  #footer-container > .container-fluid > .row:last-child {
    padding: 3px;
    margin-top: 20px;
    background-color: #fff;
    border-radius: 10px;
  }
  @media screen and (max-width: 600px){
    .ftr-1{
      display: none;
    }
    .ftr-3{
      display: none;
    }
  }
</style>
