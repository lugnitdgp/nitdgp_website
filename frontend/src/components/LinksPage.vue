<template>
  <div class="l1 page-type-links">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "LinksPage"
}
</script>

<style>
  .l1 {
    min-height: 650px;
    padding-top: 4em;
    padding-bottom: 2em;
    padding-right: 5%;
    padding-left: 5%;
  }
</style>
