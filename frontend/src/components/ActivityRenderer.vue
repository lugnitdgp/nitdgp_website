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
          <!-- <td v-html="data" v-for="data in row">
          </td> -->
          <td>{{ row.speakers }}</td>
          <td v-html="row.programme"></td>
          <td>{{ row.start_date }}</td>
          <td v-if="row.end_date=='1959-01-01'">-</td>
          <td v-else>{{ row.end_date}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ActivityRenderer",
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

