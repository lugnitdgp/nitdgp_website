<template>
  <div class="tab-pane fade" :class="classname" :id="'panel' + idn" role="tabpanel">
    <br>
    <ul v-if="noticelist">
      <li v-for="notice in noticelist">
        <a :href="notice.file" target="new">{{ notice.title }}</a>
      </li>
    </ul>
    <page-list v-if="noticelist"
      :num-of-pages="parseInt((noticelist.length-1)/10 + 1)">
    </page-list>
  </div>
</template>

<script>
import PageList from '@/components/PageList'

export default {
  name: "NoticeList",
  props: {
    noticelist: {
      required: true,
      default: []
    },
    idn: {
      type: String,
      required: false,
      default: ""
    },
    classname: {
      type: String,
      required: false,
      default: ""
    }
  },
  components: {
    PageList
  }
}
</script>
