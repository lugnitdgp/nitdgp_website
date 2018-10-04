<template>
  <div class="col tile-small">
    <a :href="link">
      <div class="tile-content" align="center">
        <i class="fa fa-2x notranslate" :class="icon">{{ title }}</i>
        <br>
        <p class="tile-small-text">{{ desc }}</p>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: "SmallTile",
  props: {
    link: {
      required: false,
      default: undefined
    },
    title: {
      required: false,
      default: ""
    },
    icon: {
      required: false,
      default: undefined
    },
    desc: {
      required: true
    }
  }
}
</script>
