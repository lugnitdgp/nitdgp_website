<template>
  <div class="card">
    <div class="card-header" role="tab" :id="headId">
      <a data-toggle="collapse" data-parent="#accordionEx" :href="'#' + bodyId" aria-expanded="true" :aria-controls="bodyId">
        <h5 class="mb-0">
          {{ title }} <i class="fa fa-angle-down rotate-icon"></i>
        </h5>
      </a>
    </div>
    <div :id="bodyId" class="collapse" :class="{ show: show }" role="tabpanel" aria-labelledby="headId">
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
      default: "Title goes here"
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
      bodyId: ""
    }
  },
  created () {
    this.headId = getUniqueId("col-card-", 4)
    this.bodyId = getUniqueId(this.headId + "-", 4)
  },
  methods: {
    getUniqueId
  }
}
</script>
