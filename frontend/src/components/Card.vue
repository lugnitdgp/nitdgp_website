<template>
  <div class="card">
    <span class="card-header white-text">{{ title }}</span>
    <div class="card-body hidden">
      <div class="card-text">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    title: {
      type: String,
      required: true,
      default: "Title goes here"
    }
  }
}
</script>
