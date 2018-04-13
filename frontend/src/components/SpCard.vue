<template>
  <div class="card card-cascade narrower" :class="containerclass">
    <div class="view gradient-card-header tile-title">
      <p class="tile-title-text">{{ title }}</p>
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
    title: {
      required: true,
      default: "Heading Default"
    },
    bodyclass: {
      required: false,
      default: undefined
    }
  }
}
</script>
