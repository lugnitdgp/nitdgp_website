<template>
  <div class="card card-cascade narrower" :class="containerclass">
    <a class="view gradient-card-header tile-title"
      data-toggle="collapse" :href="'#' + bodyId">
      <slot name="header"></slot>
    </a>
    <div class="card-body collapse" :class="bodyclass + (show != true ? ' ' : ' show')" :id="bodyId">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { getUniqueId } from '@/common.js'

export default {
  name: "SpCardCollapse",
  props: {
    containerclass: {
      required: false,
      default: undefined
    },
    bodyclass: {
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
