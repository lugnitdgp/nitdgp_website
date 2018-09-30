<template>
  <div class="l1 page-type-links">
    <!-- CONTENT -->
    <div class="card">
      <a class="card-header white-text">Health Care</a>
      <div class="card-body">
        <div style="text-align: center;">
          <img style="max-height:200px;width: 500px;max-width: 100%" src="/static/img/mu.jpg" width="100%"><br>
        </div>
        There is a Medical Unit-cum-Hospital with arrangement for both indoor and outdoor treatment of the patients. The medical unit is served by two resident doctors and other medical staff round the clock. The students and the staff with their family members are
        benefited by the services of the Medical Unit. For any specialised treatment the patients are referred to the State Government
        Hospital situated at the other end of the city, or some Advanced Medical Centre.<br><br>
        <strong>Mediacl Officer</strong>
        <p>
          <strong>Dr. B. K. Sarkar ( MBBS )</strong><br>
          Phone: +91-343-2757118<br>
          Mobile: +91-9434788075<br>
          Email: b.sarkar@admin.nitdgp.ac.in<br>
          <strong>Dr. ( Mrs. )S. Patra ( MBBS )</strong><br>
          Phone: +91-343-2757116<br>
          Mobile: +91-9434788076<br>
          Email: s.patra@admin.nitdgp.ac.in<br>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Mu',
  created () {
    this.$emit('hideloader', true)
  }
}
</script>
