<template>
  <div class="tab-pane fade notice-wrap" :class="classname" :id="'panel' + idn" role="tabpanel">
    <div class="notice-wrap-l2" v-if="noticelist">
      <div class="paginate-wrap">
        <paginate-links
          for="noticelist"
          :limit="2"
          :show-step-links="true"
        />
      </div>
      <paginate name="noticelist" :per="10" :list="noticelist" class="paginate-list list-gr list-group">
        <li v-for="notice in paginated('noticelist')">
          <a class="list-group-item" :href="notice.file" target="new">{{ notice.title }}</a>
        </li>
      </paginate>
    </div>
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

<style>
  .notice-wrap .paginate-wrap{
    text-align: center;
    width: 100%;
    padding: 30px 0px;
  }
  .notice-wrap li.left-arrow{
    background-color: #001333;
    color: #fff;
  }
  .notice-wrap li.right-arrow{
    background-color: #001333;
    color: #fff;
  }
  .notice-wrap li.left-arrow.disabled{
    opacity: 0.3;
  }
  .notice-wrap li.right-arrow.disabled{
    opacity: 0.3;
  }
  ul.paginate-links{
    margin-bottom:0px;
    padding-left:0px;
  }
  @media screen and (max-width: 600px){
    .paginate-links a{
      padding: 2px 12px!important;
    }
  }
  .paginate-links li{
    padding-bottom: 5px;
    padding-top: 5px;
    display: inline-block;
    background-color: #E0F7FA;
    border-radius: 2px;
    margin: 0 1px;
  }
  .paginate-links a{
    padding: 5px 15px;
  }
  .paginate-links li.active{
    background-color: #001333;
    color: #fff;
  }
</style>