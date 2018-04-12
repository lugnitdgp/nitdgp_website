<template>
  <div class="card card-cascade narrower card-news" >
    <div class="view gradient-card-header tile-title">
      <span class="tile-title-text">
        <a class="btn-floating btn-sm" href="#newscarowrap" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
        NEWSFEED
        <a class="btn-floating btn-sm" href="#newscarowrap" data-slide="next"><i class="fa fa-chevron-right"></i></a>
      </span>
    </div>
    <div class="card-body">
      <div id="newscarowrap" class="carousel slide carousel-multi-item" data-ride="carousel" data-interval="6000">
        <!--Slides-->
        <div class="carousel-inner" role="listbox">
          <div v-for="(news_slide,index) in notices" class="carousel-item" :class="index == 0 ? 'active' : ''">
            <a :href="news.file" target="new" v-for="news in news_slide" class="row card news-row anim2">
              <div class="col date-col">
                <div align="center" class="date-div">
                  <strong class="white-text">
                  <h3>{{ news.date }}</h3>
                  <h6>{{ news.month }}</h6>
                  </strong>
                </div>
                <div class="black-text">{{ news.title }}</div>
              </div>
            </a>
          </div>
        </div>
        <!-- End of Slides-->
        <div class="indiwrap">
          <ol class="carousel-indicators newsc-indi">
            <li v-for="(slides,index) in notices" data-target="#newscarowrap" :data-slide-to="index" :class="index == 0 ? 'active' : ''"></li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Newsfeed',
  props: ['notices']
}
</script>
