<template>
  <div id="app">
    <div class="loader" v-show="loader">
      <span class="loader-dot-one"></span>
      <span class="loader-dot-two"></span>
    </div>
    <Header/>
    <router-view @hideloader="hideLoader" />
    <Footer/>
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'

export default {
  name: 'App',
  data () {
    return {
      loader: true
    }
  },
  methods: {
    hideLoader (val) {
      if (typeof val == 'boolean')
        this.loader = !val
      else
        this.loader = false
    }
  },
  components: {
    Header,
    Footer
  }
}
</script>

<style scoped>
  .loader {
    opacity:0.98;
    background-color:#fff;
    position:fixed;
    width: 100%;
    height:100%;
    top:0px;
    left:0px;
    z-index:1050;
  }

  .loader-dot-one {
    position: absolute;
    background-image: url("/static/img/nitdgp_logo.png");
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    top: calc(50% - 125px);
    height: 150px;
    width: 100%;
    animation-name: grow-n-shrink;
    animation-duration: 1.5s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-out;
    animation-delay: 0.1s;
  }

  .loader-dot-two {
    position: absolute;
    top: calc(50% + 75px);
    width: 50%;
    left: 25%;
    border-bottom: 6px solid #215863;
    animation-name: move;
    animation-duration: 1.5s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-out;
    animation-delay: 0.1s;
  }

  @keyframes grow-n-shrink {
    0% {
      transform: scale(1);
    }
    10% {
      transform: scale(1.05);
    }
    20% {
      transform: scale(1.1);
    }
    30% {
      transform: scale(1.18);
    }
    40% {
      transform: scale(1.25);
    }
    50% {
      transform: scale(1.20);
    }
    60% {
      transform: scale(1.15);
    }
    70% {
      transform: scale(1.20);
    }
    80% {
      transform: scale(1.28);
    }
    90% {
      transform: scale(1.15);
    }
    100% {
      transform: scale(1);
    }
  }

  @keyframes move {
    0% {
      transform: scaleX(0);
    }
    50% {
      transform: scaleX(1);
    }
    100% {
      transform: scaleX(0);
    }
  }
</style>
