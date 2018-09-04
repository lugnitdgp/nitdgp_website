<template>
  <div class="card card-cascade narrower" :class="containerclass">
    <a v-on:click="expansion(row_index,bodyId)" class="view gradient-card-header tile-title">
      <slot name="header"></slot>
    </a>
    <div class="card-body hide_me" :class="bodyclass + (show != true ? ' ' : ' show')" :id="bodyId">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { getUniqueId } from '@/common.js'

export default {
  name: "SpCardCollapse",
  methods: {
    expansion(index, bodyId) {
      // if open
      console.log(index)
      var element = document.getElementById(bodyId)
      if( element.classList.contains("show_me") ) {
          element.classList.remove("show_me")
          element.classList.add("hide_me")
      }
      // else closed       
      else {
        var i=0
        var elements = document.getElementsByClassName("click-bait-"+index)
        for (i = 0; i < elements.length; i++) {
          elements[i].classList.remove("hide_me")
          elements[i].classList.add("show_me")
          // elements[i].classList.add("collapsing")
        }
      }
    }
  },
  props: {
    containerclass: {
      required: false,
      default: undefined
    },
    bodyclass: {
      required: false,
      default: undefined
    },
    row_index: {
      required: false,
      default: undefined
    },
    show: {
      required: false,
      default: true
    }
  },
  data () {
    return {
      bodyId: ""
    }
  },
  created () {
    this.bodyId = getUniqueId("spc-card-", 4)
  }
}
</script>

<style scoped>
.hide_me{
  display: none;
  max-height: 0;
}
.show_me{
  animation-duration: .5s;
  animation-name: fadeIn;
  animation-delay: 0s;
  animation-timing-function: initial;
  animation-iteration-count: initial;
  animation-direction: initial;
  animation-fill-mode: initial;
  animation-play-state: initial;
}
</style>
