<template>
  <div class="notice-wrap" v-if="noticelist">
    <div class="paginate-wrap">
      <paginate-links
        for="noticelist"
        :limit="2"
        :show-step-links="true"
      />
    </div>
    <paginate name="noticelist" :per="10" :list="noticelist" class="paginate-list list-gr list-group">
      <li v-for="notice in paginated('noticelist')">
        <a class="list-group-item" :href="notice.file" target="new"><span style="background-color: #001333;color: white;padding: 5px"> &nbsp;{{ notice.date }} </span>&nbsp; {{ notice.title }}</a>
      </li>
    </paginate>
  </div>
</template>

<script>
export default {
  name: "NoticeList",
  props: {
    noticelist: {
      required: true
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
    padding: 7px 0px;
    padding-top: 3px;
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
      padding: 2px 10px!important;
    }
  }
  .paginate-links li{
    padding-bottom: 3px;
    padding-top: 3px;
    display: inline-block;
    background-color: #E0F7FA;
    border-radius: 2px;
    margin: 0 1px;
  }
  .paginate-links a{
    padding: 3px 12px;
  }
  .paginate-links li.active{
    background-color: #001333;
    color: #fff;
  }
</style>
