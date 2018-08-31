<template>
  <div class="card">
    <div class="card-header" role="tab" :id="headId">
      <a class="" data-toggle="collapse" data-parent="#accordionEx" :href="'#' + bodyId" aria-expanded="false" :aria-controls="bodyId" v-on:click="show_status = !show_status">
        <h5 class="mb-0">
          {{ title }} <i class="fa fa-angle-down" :class="show_status ? 'rotate-icon' : ''"></i>
        </h5>
      </a>
    </div>
    <div :id="bodyId" class="collapse" :class="{show : show}" role="tabpanel" aria-labelledby="headId">
      <div class="card-body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
import { getUniqueId } from '@/common.js'

export default {
  name: 'CardCollapse',
  props: {
    title: {
      type: String,
      required: true,
    },
    show: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  data () {
    return {
      headId: "",
      bodyId: "",
      show_status: true
    }
  },
  created () {
    this.headId = getUniqueId("col-card-", 4)
    this.bodyId = getUniqueId(this.headId + "-", 4)
    this.show_status = this.show
  },
  methods: {
    getUniqueId
  }
}
</script>

<style>
  @media screen and (max-width: 600px){
    .card-body{
      padding: 15px 5px;
    }
  }
</style>
