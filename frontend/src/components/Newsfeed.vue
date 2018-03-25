<template>
  <div class="card card-cascade narrower card-news" >
    <div class="view gradient-card-header tile-title">
      <p class="tile-title-text">
        <a class="btn-floating btn-sm" href="#newscarowrap" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
        NEWSFEED
        <a class="btn-floating btn-sm" href="#newscarowrap" data-slide="next"><i class="fa fa-chevron-right"></i></a>
      </p>
    </div>
    <div class="card-body">
      <div id="newscarowrap" class="carousel slide carousel-multi-item" data-ride="carousel" data-interval="6000">
        <!--Slides-->
        <div class="carousel-inner" role="listbox">
          <div v-for="(news_slide,index) in newsfeed" class="carousel-item" :class="index == 0 ? 'active' : ''">
            <div v-for="news in news_slide" class="row card news-row anim2">
              <div class="col date-col">
                <div align="center" class="date-div">
                  <strong class="white-text">
                  <h3>{{ news.date }}</h3>
                  <h6>{{ news.month }}</h6>
                  </strong>
                </div>
                <div :href="news.link" class="black-text">{{ news.title }}</div>
              </div>
            </div>
          </div>
        </div>
        <!-- End of Slides-->
        <ol class="carousel-indicators newsc-indi">
          <li data-target="#newscarowrap" data-slide-to="0" class="active"></li>
          <li data-target="#newscarowrap" data-slide-to="1"></li>
          <li data-target="#newscarowrap" data-slide-to="2"></li>
          <li data-target="#newscarowrap" data-slide-to="3"></li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Newsfeed',
  data () {
    return {
      newsfeed: [],
      slides_count: 0
    }
  },
  created() {
    this.newsfeed = [
      {date: 1, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 2, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 3, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 4, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 5, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 11, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 12, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 13, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 14, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"},
      {date: 15, month: 'JAN', title: "Meeting due with director,to be held in senate room at 5:00 PM ,WebTeam is welcomed.Be there!Be there!Be there!", link: "http://nitdgp.ac.in"}]
      let newsfeed = []
      let news_slide = []
      this.newsfeed.map((news,index) => {
        news_slide.push(news)
        if ((index+1) % 4 == 0) {
          newsfeed.push(news_slide)
          news_slide = []
          this.slides_count++
        }
      })
      if (news_slide.length) {
        newsfeed.push(news_slide)
        this.slides_count++
      }
      this.newsfeed = newsfeed
  }
}
</script>
