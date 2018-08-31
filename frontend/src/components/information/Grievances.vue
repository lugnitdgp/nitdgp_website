<template>
  <links-page>
    <card title="Public Grievances">
      <span>
        <h4>Staff Grievance Officer</h4>
        Prof. Vijay Kumar Dwivedi<br>
        Department of Civil Engineering,<br>
        National Institute of Technology,<br>
        Durgapur, West Bengal-713209.<br>
        Mobile: +91-9434788097<br>
        Email: sgo@admin.nitdgp.ac.in<br>
      </span>
      <br>
      <ul>
        <li><a href="http://nitdgp.ac.in/information/Public Grievances/SGO_Form.doc"> Staff Grievance Form</a></li>
        <li><a href="http://nitdgp.ac.in/information/Public Grievances/public20001.pdf" target="_blank">Public Grievances Related Order</a></li>
      </ul>
      </div>
    </card>
  </links-page>
</template>

<script>

import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: 'Grievances',
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    LinksPage,
    Card
  }
}
</script>
