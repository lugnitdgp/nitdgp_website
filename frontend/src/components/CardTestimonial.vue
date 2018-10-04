<template>
  <div class="card testimonial-card">
    <div class="card-up">
    </div>
    <a v-if="id" align="center" :href="'/faculty/' + id">
      <img :src="imageModified" class="avatar mx-auto rounded-circle img-fluid">
    </a>
    <div v-if="!id" align="center">
      <img :src="imageModified" class="avatar mx-auto rounded-circle img-fluid">
    </div>
    <div class="card-body-in">
      <p v-if="id" class="card-title">
        <strong>
          <a class="blue-text notranslate" :href="'/faculty/' + id">
            {{ name }}
          </a>
        </strong>
      </p>
      <p v-if="!id" class="card-title notranslate">
          {{ name }}
      </p>
      <h6 class="black-text">{{ desig }}</h6>
      <hr>
      <p class="min-profile">
        <slot></slot>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardTestimonial",
  data() {
    return {
      imageModified: this.image === null ? 'https://newsdesk.si.edu/sites/default/files/imagecache/photo_pagewidth/photos/anonymous_silhouette.jpg' : this.image
    }
  },
  props: ['image', 'name', 'desig', 'id'],
}
</script>
