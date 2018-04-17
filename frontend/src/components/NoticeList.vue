<template>
  <div v-if="noticelist" class="tab-pane fade" :class="classname" :id="'panel' + idn" role="tabpanel">
    <paginate name="noticelist" :per="10" :list="noticelist" class="paginate-list">
      <li v-for="notice in paginated('noticelist')">
        <a :href="notice.file" target="new">{{ notice.title }}</a>
      </li>
    </paginate>
    <center>
      <paginate-links for="noticelist" :limit="5" :show-step-links="true"/>
    </center>
  </div>
</template>

<script>
export default {
  name: "NoticeList",
  props: {
    noticelist: {
      required: true
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
  data () {
    return {
      paginate: ['noticelist']
    }
  }
}
</script>

<style scoped>
  ul {
    list-style-type: none;
    padding: 0px;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  .paginate-list {
    margin: 0 auto;
    text-align: left;
    li {
      display: block;
      &:before {
        content: '⚬ ';
        font-weight: bold;
        color: slategray;
      }
    }
  }

  .left-arrow {
    width: 20px;
  }

  .paginate-links.noticelist {
    a {
      cursor: pointer;
    }
    li.active a {
      font-weight: bold;
    }
    li.next:before {
      content: ' | ';
      margin-right: 13px;
      color: #ddd;
    }
    li.disabled a {
      color: #ccc;
      cursor: no-drop;
    }
  }
</style>
