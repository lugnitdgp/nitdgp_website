<template>
  <links-page>
    <card title="Officers">
      <div class="card-text">
          <ul class="list-group list-gr">
            <div class="row">
              <div v-for="details in list" v-if="details.designation=='Joint Registrar (Academic & Examinations)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Joint Registrar (Establishment)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Joint Registrar (Finance & Accounts)'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Joint Registrar (Hostel Section)'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Joint Registrar (Procurement)- Addl. Charge'" class="col contact-col ">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Assistant Registrar (Hostels)'" class="col contact-col ">
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
              <div v-for="details in list" v-if="details.designation=='Assistant Registrar (SRCC)'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Technical Officer & Joint Registrar SRCC(Addl. Charge)'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Security Officer & I/C Estate'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Executive Engineer (Civil)'" class="col contact-col">
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
              <div v-for="details in list" v-if="details.designation=='Senior Medical Officer'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Medical Officer'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>
              <div v-for="details in list" v-if="details.designation=='Nodal Officer of DASA'" class="col contact-col">
                <li class="list-group-item disabled" style="height: 100%;">
                  <h4>{{ details.name }}</h4>
                  <h5 style="font-weight: bold" v-if="details.designation">
                    {{ details.designation }}
                  </h5>
                  <span v-html="details.contact"/>
                </li>
              </div>              
              <div v-for="details in list" v-if="details.designation=='Assistant Librarian'" class="col contact-col">
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
      </card>
  </links-page>
</template>


<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import { range, genBackendURL } from '@/common.js'

export default {
  name: "Officers",
  data () {
    return {
      list: {}
    }
  },
  created () {
    axios.get(genBackendURL("dashboard/contacts"))
         .then(response => {
           this.list = response.data.groups['Officers']
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    CardTestimonial
  }
}
</script>
<style scoped="scoped">
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