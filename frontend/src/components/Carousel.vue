<template>
  <div class="card card-cascade narrower card-pic">
    <div class="card-body">
      <!-- Carousel Wrapper -->
      <div id="carousel-home" class="carousel slide caro-wrap" data-ride="carousel" data-interval="6000">
        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li v-for="(slide,index) in slides" data-target="#carousel-home" :data-slide-to="index" :class="{ active: (index == 0) }"></li>
        </ol>
        <!-- End of Indicators -->
        <!-- Slides -->
        <div class="carousel-inner" role="listbox">
          <div v-for="(slide,index) in slides" class="carousel-item anim1" :class="{ active: (index == 0) }">
            <div class="view hm-black-light">
              <img class="d-block" :src="slide.image" :alt="['Slide ' + (index+1)]"/>
              <div class="mask"></div>
            </div>
            <div class="carousel-caption">
              <h5 class="h5-responsive">
                <span class="cap-text" v-if="slide.primary_caption">
                {{ slide.primary_caption }}
                </span>
                <span class="cap-text" v-if="slide.title">
                {{ slide.title }}
                </span>
                <!-- {{ slide.secondary_caption }} -->
              </h5>
            </div>
          </div>
        </div>
        <!-- End of Slides -->
        <a class="carousel-control-prev" href="#carousel-home" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carousel-home" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Carousel',
  props: ['slides']
}
</script>
<style>
  .d-block {
    height: 600px;
  }
  @media screen and (max-width: 800px) {
    .card-pic{
      height: 180px!important;
    }
    .card-pic .caro-wrap{
      height: 160px!important;
    }
  }
  .card-pic {
    height: 400px;
    background: linear-gradient(#001333,#039BE5);
  }
  .card-pic .card-body{
    padding-left: 10px!important;padding-right: 10px!important;padding-top: 10px!important;
  }
  .card-pic .caro-wrap{
    height: 380px;
    background: linear-gradient(#03A9F4,#039BE5,#039BE5,#039BE5);
  }
  .card-pic .carousel-indicators{
    margin-bottom: -0.2em!important;
  }
  .card-pic .carousel-inner{
    height: 100%;
  }
  .card-pic .view{
    height: 100%;margin: 0!important;padding: 0!important;
  }
  .card-pic .carousel-item{
    height: 100%;
  }
  .card-pic .carousel-caption{
    margin-bottom: -2em!important;
  }
  .card-pic .carousel-caption .cap-text{
    background-color: #ECEFF1;
    color:#000;
    font-weight: bold;
    padding: 5px;
    border-radius: 10px;
  }
  .card-pic img{
    min-width: 100% !important;
    margin: 0 auto;
    margin-top: -150px;
  }
</style>
