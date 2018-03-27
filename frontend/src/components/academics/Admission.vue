<template>
  <links-page>
    <collapse-list>
      <card-collapse v-for="(courses, prog) in results" :title="prog" :key="courses.id">
        <ul class="pg_contents">
          <li v-for="course in courses" class="bot-margin no-style-list">
            <h4>{{ key = Object.keys(course)[0] }}</h4>
            <ul>
              <li v-for="link in course[key]">
                <a target="new" :href="link.file">
                  {{ link.title }}
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
import LinksPage from '@/components/LinksPage'
import CollapseList from '@/components/CollapseList'
import CardCollapse from '@/components/CardCollapse'

import axios from 'axios'

export default {
  name: "Admission",
  data () {
    return {
      results: {}
    }
  },
  created: function () {
    axios.get(genBackendURL('academics/admission'))
         .then(response => {
           console.log("Axios(GET[admission]): Success")
           this.results = response.data.admission
           this.$emit('hideloader', true)
         })
         .catch(e => {
           this.errors.push(e)
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
