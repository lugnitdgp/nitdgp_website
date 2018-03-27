<template>
  <div class="card card-cascade narrower card-pic">
    <div class="card-body">
      <!-- Carousel Wrapper -->
      <div id="carousel-home" class="carousel slide carousel-fade" data-ride="carousel" data-interval="6000">
        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li v-for="(slide,index) in slides" data-target="#carousel-home" :data-slide-to="index" :class="index == 0 ? 'active' : ''"></li>
        </ol>
        <!-- End of Indicators -->
        <!-- Slides -->
        <div class="carousel-inner" role="listbox">
          <div v-for="(slide,index) in slides" class="carousel-item anim1" :class="index == 0 ? 'active' : ''">
            <div class="view hm-black-light">
              <img class="d-block w-100" :src="slide.image" alt="['Slide ' + (index+1)]"/>
              <div class="mask"></div>
            </div>
            <div class="carousel-caption">
              <h3 class="h3-responsive">{{ slide.primary_caption }}</h3>
              <p>{{ slide.secondary_caption }}</p>
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
