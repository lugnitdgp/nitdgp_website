<template>
  <div class="table-wrapper-2 table-bordered">
    <table class="table table-responsive-md">
      <thead class="mdb-color lighten-4">
        <tr>
          <th class="th-lg" v-for="thead in theader">
            {{ thead }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in table">
          <td v-html="data" v-for="data in row">
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "TableRenderer",
  props: {
    table: {
      required: true
    },
    theader: {
      required: true
    }
  }
}
</script>
<style scoped>
td {
  font-weight: normal !important;
}
</style>

