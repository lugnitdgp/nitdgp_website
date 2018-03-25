<template>
  <div id="carousel-home" class="carousel slide carousel-fade" data-ride="carousel">
      <ol class="carousel-indicators">
        <li v-for="(slide,index) in slides" data-target="#homepage-carousel" :data-slide-to="index" :class="index == 0 ? 'active' : ''"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div v-for="(slide,index) in slides" :class="index == 0 ? 'carousel-item active' : 'carousel-item'">
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
      <a class="carousel-control-prev" href="#homepage-carousel" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#homepage-carousel" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
      </a>
  </div>
</template>

<script>
export default {
  name: 'Carousel',
  props: ['slides']
}
</script>
