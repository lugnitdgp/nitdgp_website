<template>
  <div class="l1 page-type-links notices">
    <div class="card">
      <a class="card-header white-text">Tenders</a>
      <div class="card-body">
        <div class="notice-wrap-l2" v-if="tenderslist">
          <div class="paginate-wrap">
            <paginate-links
              for="tenderslist"
              :limit="2"
              :show-step-links="true"
            />
          </div>
          <paginate name="tenderslist" :per="10" :list="tenderslist" class="paginate-list list-gr list-group">
            <li v-for="tender in paginated('tenderslist')">
              <a class="list-group-item" :href="tender.file" target="new">{{ tender.title }}</a>
            </li>
          </paginate>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import LinksPage from '@/components/LinksPage'
import Card from '@/components/Card'
import NoticeList from '@/components/NoticeList'
import { genBackendURL } from '@/common.js'

export default {
  name: "Tenders",
  data () {
    return {
      tenderslist: [],
      paginate: ['tenderslist']
    }
  },
  created () {
    axios.get(genBackendURL("information/tenders"))
         .then(response => {
           this.tenderslist = response.data.tenders
           this.$emit('hideloader', true)
         })
         .catch(e => {
           console.log(e)
         })
  },
  components: {
    LinksPage,
    Card,
    NoticeList
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