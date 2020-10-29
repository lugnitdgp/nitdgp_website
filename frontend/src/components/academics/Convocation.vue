<template>
  <links-page>
    <card title="Convocation and Special Events">
      <collapse-list>
        <card-collapse title="16th Convocation Preparatory Documents" show="true">
          <ul class="list-group list-gr">
            <li v-for="convocation in convocations">
              <a v-if="convocation.file" class="list-group-item" :href="convocation.file">
                <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ convocation.updated_at.substring(0,10) }} </span>&nbsp;{{ convocation.title }}
                </a>
              <a v-else class="list-group-item" :href="convocation.url">
                <span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ convocation.updated_at.substring(0,10) }} </span>&nbsp;{{ convocation.title }}
              </a>
            </li>
          </ul>
      </card-collapse>

      <card-collapse title="Convocation Archivals">  
        <ul class="list-group list-gr">
            <li v-for="con_ar in convarc">
              <a v-if="con_ar.file" class="list-group-item" :href="con_ar.file">
                {{ con_ar.title }}
                </a>
              <a v-else class="list-group-item" :href="con_ar.url">
                {{ con_ar.title }}
              </a>
            </li>
          </ul>
      </card-collapse>
    </collapse-list>
    </card>
  </links-page>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'
import { genBackendURL } from '@/common.js'

export default {
  name: "Convocations",
  data () {
    return {
      convocations: {},
      convarc: {}
    }
  },
  created () {
    axios.get(genBackendURL("academics/convocation"))
         .then(response => {
           this.convocations = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
    axios.get(genBackendURL("/archives/"))
     .then(response => {
           let archives = response.data           
           this.convarc = archives.convocation
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    CollapseList,
    CardCollapse
  }
}
</script>
