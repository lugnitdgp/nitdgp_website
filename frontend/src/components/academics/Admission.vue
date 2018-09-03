<template>
  <links-page>
    <collapse-list>
      <card-collapse v-for="(degree, i) in degrees" :title="degree.name" :show="i == 0" :key="i">
        <ul class="pg_contents">
          <li v-for="(programme, j) in degree.programmes" class="bot-margin no-style-list" :key="j">
            <h4>{{ programme.name }}</h4>
            <ul class="list-group list-gr">
              <li v-for="doc in programme.documents">
                <a v-if="doc.file" class="list-group-item" target="new" :href="doc.file">
                  {{ doc.title }}
                </a>
                <a v-else class="list-group-item" target="new" :href="doc.link">
                  {{ doc.title }}
                </a>
              </li>
            </ul>
          </li>
        </ul>
      </card-collapse>
    </collapse-list>
  </links-page>
</template>

<script>
import axios from 'axios'

import LinksPage from '@/components/LinksPage'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'

import { genBackendURL } from '@/common.js'

export default {
  name: "Admission",
  data () {
    return {
      degrees: []
    }
  },
  created: function () {
    axios.get(genBackendURL('academics/admission'))
         .then(response => {
           this.degrees = response.data.results
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log("Axios(GET[admission]): Error: " + e)
         })
  },
  components: {
    LinksPage,
    CollapseList,
    CardCollapse
  }
}
</script>

<style>
  .no-style-list {
    list-style: none;
  }

  .bot-margin {
    margin-bottom: 20px;
  }
</style>
