<template>
  <div id="app">
    <div class="loader" v-show="loader">
      <span class="loader-dot"></span>
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

  .loader-dot {
    position: absolute;
    display: inline-block;
    top: 48%;
    height: 10px;
    left: 50%;
    width: 0px;
    background-color: #f00;
  }

  @keyframes move {
    0% {
      width: 0px;
      left: 50%;
    }
    50% {
      width: 100%;
      left: 0%;
    }
    100% {
      width: 0px;
      left: 50%;
    }
  }
  .loader-dot {
    animation-name: move;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-out;
    animation-delay: 0.1s;
  }
</style>
