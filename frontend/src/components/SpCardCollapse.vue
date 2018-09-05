<template>
  <div class="card card-cascade narrower" :class="containerclass">
    <a @click="expansion" data-toggle="collapse"
      class="view gradient-card-header tile-title">
      <slot name="header"></slot>
    </a>
    <div class="card-body collapse" :class="bodyclass + (hide == true ? ' hide_me' : ' show_me')" :id="bodyId">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { getUniqueId } from '@/common.js'

export default {
  name: "SpCardCollapse",
  methods: {
    expansion() {
      console.log(this.row_index)
      this.hide = !this.hide
      if (this.hide == false)
        this.$root.$emit('show-all', this.row_index)
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
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      bodyId: "",
      hide: false
    }
  },
  created () {
    this.bodyId = getUniqueId("spc-card-", 4)
    this.hide = !this.show
    this.$root.$on('show-all', index => {
      if (index == this.row_index)
        this.hide = false
    })
  }
}
</script>

<style scoped>
  div {
    transition: all .4s ease !important;
  }
  .hide_me {
    display: none;
    max-height: 0;
  }
  .show_me {
    display: block;
    animation-duration: .6s;
    animation-name: fadeIn;
    animation-delay: 0s;
    animation-timing-function: initial;
    animation-iteration-count: initial;
    animation-direction: initial;
    animation-fill-mode: initial;
    animation-play-state: initial;
  }
</style>
