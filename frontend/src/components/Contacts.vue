<template>
  <links-page>
    <collapse-list>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Director'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Director Office'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Registrar'" :key="groupname.id" title="Registrar">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Registrar Office'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Dean'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Associate Dean'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" v-if="details.designation=='Associate Dean (Academic & Examination)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;background-color: #e0f7fa;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
            </div>
            <div v-for="details in list" v-if="details.designation=='Associate Dean (Alumni & Outreach)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;background-color: #e0f7fa;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
            </div>
            <div v-for="details in list" v-if="details.designation=='Associate Dean (Research & Consultancy)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;background-color: #e0f7fa;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
            </div>
            <div v-for="details in list" v-if="details.designation=='Associate Dean (Student Welfare)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;background-color: #e0f7fa;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
            </div>
            <div v-for="details in list" v-if="details.designation=='Associate Dean (Training & Placement)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;background-color: #e0f7fa;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
            </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Training and Placement'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='HOD'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in sortedHOD" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Academic Qualification Verification'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Computer Center'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Library'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Workshops'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <!-- <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Officers'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse> -->
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Officers'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" v-if="details.designation=='Deputy Registrar (Academic & Examinations)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Deputy Registrar (Establishment)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Deputy Registrar (Finance & Accounts)'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Deputy Registrar(Procurement)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Assistant Registrar (Establishment)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Assistant Registrar(Internal Audit)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>

              <div v-for="details in list" v-if="details.designation=='Assistant Registrar (Registrar Secretariat, Legal Affairs & CPIO)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Assistant Registrar (Student Welfare)'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Executive Engineer'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Liason Officer, SC-ST Cell'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Medical Officers'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Nodal Officer of DASA - 2015'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Security Officer'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Staff Grievance Officer'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
      <card-collapse v-for="list,groupname,i in groups" v-if="groupname=='Warden'" :key="groupname.id" :title="groupname">
        <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" v-if="details.designation=='Chief Warden'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Associate Chief Warden'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Netaji Subhas Chandra Bose Hall of Residence (Hall-1)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Jagadish Chandra Bose Hall of Residence (Hall-2)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Rabindra Nath Tagore Hall of Residence (Hall-3)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='C V Raman Hall of Residence (Hall-4)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Swami Vivekananda Hall of Residence (Hall-5)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Rishi Aurobindo Hall of Residence (Hall-6)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Sister Nivedita Hall of Residence (Hall-7)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Preetilata Waddader Hall of Residence (Hall-8)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Satyendra Nath Bose Hall of Residence (Hall-9)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Mother Teresa Hall of Residence (Hall-10)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Meghnad Saha Hall of Residence (Hall-11)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='A.P.J. Abdul Kalam International Hostel (Hall-12)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Sarojini Naidu Hall of Residence (Hall-13)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
            </div>
          </ul>
        </div>
      </card-collapse>
    </collapse-list>
  </links-page>
</template>
<script>
import LinksPage from '@/components/LinksPage'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'
import axios from 'axios'
import { genBackendURL } from '@/common.js'


export default {
  name: 'Contacts',
  created () {
    axios.get(genBackendURL("dashboard/contacts"))
  	 .then(response => {
  	   this.groups = response.data.groups
       this.hodlist = this.groups['HOD']

  	   this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
    this.$emit('hideloader', true)
  },
  data () {
    return {
      groups: {},
      hodlist: {}
    }
  },
  computed: {
    sortedHOD: function() {
      function compare(a, b) {
        if (a.designation < b.designation)
          return -1;
        if (a.designation > b.designation)
          return 1;
        return 0;
      }

      return this.hodlist.sort(compare)
    }
  },
  components: {
    LinksPage,
    CollapseList,
    CardCollapse
  }
}
</script>
<style >
  .list-gr .contact-col{
    min-width: 33%;
    max-width: 33%;
    padding-bottom: 15px;
  }
  @media screen and (max-width: 1200px){
    .list-gr .contact-col{
      min-width: 50%;
      max-width: 50%;
    }
  }
  @media screen and (max-width: 800px){
    .list-gr .contact-col{
      min-width: 100%;
      max-width: 100%;
    }
  }
</style>
