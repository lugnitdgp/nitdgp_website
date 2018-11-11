<template>
  <sp-card containerclass="card-news">
    <span slot="header" class="tile-title-text">
      
      NEWSFEED
      
    </span>
    <div>
      <!--Slides-->
      <div>
        <div>
          <a href="http://nitdgp.ac.in/liveconvocation" target="new"  class="row card news-row">
            <div class="col date-col" style="background: #D81B60;">
              <div align="center" class="date-div">
                <strong class="white-text">
                  <h3>11</h3>
                  <h6 style="font-size: 15px;"> Sep 2018</h6>
                </strong>
              </div>
              <div class="news-title" style="color: #fff;font-weight: bold;text-align: center;">14th Convocation will Streaming Live at 9 AM</div>
            </div>
          </a>
        </div>
      </div>
      <div>
        <div>
          <a href="http://nitdgp.ac.in/AllPDF/14th_Convocation_Notice.pdf" target="new"  class="row card news-row">
            <div class="col date-col" style="background: #D81B60;">
              <div align="center" class="date-div">
                <strong class="white-text">
                  <h3>27</h3>
                  <h6 style="font-size: 15px;"> Sep 2018</h6>
                </strong>
              </div>
              <div class="news-title" style="color: #fff;font-weight: bold;text-align: center;">Notice for 14th Convocation </div>
            </div>
          </a>
        </div>
      </div>
      <!-- End of Slides-->
     
    </div>
  </sp-card>
</template>

<script>
import SpCard from './SpCard'

export default {
  name: 'Newsfeed',
  props: [
    'notices'
  ],
  components: {
    SpCard
  }
}
</script>
<style>
.news-row{
  margin-bottom: 5px;margin-top: 5px;min-height: 72px;
}
.news-row .date-col{
  margin-left:0px;padding:5px;
}
.news-row .date-div{
  height: 60px!important;width: 70px!important;border-radius:5px!important;border:solid 2px #001333!important;background-color:#001333!important;
}
@media screen and (min-width: 1920px)  {
  .news-title{
    margin-top: -4.0em!important;margin-left: 4.8em!important;font-size: 100%!important;
  }
}
.news-title{
  margin-top: -5.2em;margin-left: 6em;font-size: 80%;
  text-align: left!important;
}
.news-row .date-div h3{
  margin-top: -7px !important;
}
.news-row .date-div h6{
  margin-top: -16px !important;
}
.card-news .tile-title-text{
  letter-spacing: 2px;font-weight: bold;
  margin-top: -1.8em;
}
.card-news .card-body{
  margin-top: -1em!important;
}
.card-news .card-body .indiwrap{
  position: relative;margin-top: -10px;
}
.card-news .card-body .newsc-indi .active{
  background-color: #ECEFF1;
}
.card-news .card-body .newsc-indi li{
  background-color: #001333;
}
.card-news .tile-title-text .btn-sm{
  background-color: #ECEFF1!important;
}
.card-news .tile-title-text .fa{
  padding: 0px!important;margin: 0px!important;color: #001333;
}
.card-news .tile-title{
  background-color: #001333;
  height: 60px!important;
  padding-top: 0px!important;
}
#newscarowrap{
  height: 200px!important;
}
.card-news {
  height: 400px;padding-top: 1%;
  background: linear-gradient(#001333,#039BE5);
}
/* card-title color*/
.card-news div.tile-title{
  border: solid #ECEFF1 1px;
}
/* small-tile bg-color*/
.card-news div.tile-small{
  background-color: #4A148C;
}
/* small-tile-text color*/
.card-news div.tile-content{
  color: #ffffff;
}
</style>
