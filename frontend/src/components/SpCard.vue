<template>
  <div class="card card-cascade narrower" :class="containerclass">
    <div class="view gradient-card-header tile-title">
      <slot name="header"></slot>
    </div>
    <div class="card-body" :class="bodyclass">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpCard",
  props: {
    containerclass: {
      required: false,
      default: undefined
    },
    bodyclass: {
      required: false,
      default: undefined
    }
  }
}
</script>
