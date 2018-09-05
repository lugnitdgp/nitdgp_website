<template>
  <div class="card card-cascade narrower" :class="containerclass">
    <a @click="expansion" data-toggle="collapse"
      class="view gradient-card-header tile-title">
      <slot name="header"></slot>
    </a>
    <div class="card-body collapse" :class="bodyclass + (hide == false ? ' ' : ' show')" :id="bodyId">
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
      this.$root.$emit('test', this.row_index, this.hide)
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
    this.hide = this.show
    this.$root.$on('test', (index, state) => {
      if (index == this.row_index)
        this.hide = state
    })
  }
}
</script>

<style scoped>
</style>
