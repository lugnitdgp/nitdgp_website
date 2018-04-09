<template>
  <div>
    <ul class="pagination justify-content-center">
      <li class="page-item">
      	<a class="page-link" aria-label="Previous">
      	  <span aria-hidden="true">&laquo;</span>
      	  <span class="sr-only">Previous</span>
      	</a>
      </li>

      <li v-for="i in numOfPages" class="page-item" :class="{ active: i == 1 }">
        <a class="page-link" data-toggle="tab" :href="'#li' + i" role="tab">
          {{ i }}
        </a>
      </li>

      <li class="page-item">
      	<a class="page-link" aria-label="Next">
      	  <span aria-hidden="true">&raquo;</span>
      	  <span class="sr-only">Next</span>
      	</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PageList",
  props: {
    numOfPages: {
      type: Number,
      required: true,
      default: 1
    }
  }
}
</script>
