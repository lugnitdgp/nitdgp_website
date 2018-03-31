<template>
  <links-page>
    <card title="TEQIP">
      <ul>
        <li v-for="teqip in teqips">
          <a target="new" :href="teqip.link">
            {{ teqip.title }}
          </a>
        </li>
      </ul>
    </card>
  </links-page>
</template>

<script>
import Card from "@/components/Card"
import LinksPage from "@/components/LinksPage"

export default {
  name: "Teqips",
  data () {
    return {
      teqips: [
        {
          link: "http://nitdgp.ac.in/information/Annual_Report/NIT DURGAPUR Annual Report 2015-16_Final.pdf",
          title: "Annual_Report_2015-16"
        },
        {
          link: "http://nitdgp.ac.in/information/Annual_Report/NIT%20Durgapur%20Annual%20teqip%202014-15.pdf",
          title: "Annual_Report_2014-15"
        },
        {
          link: "http://nitdgp.ac.in/information/Annual_Report/NIT%20Durgapur%20Annual%20Report%202013-14.pdf",
          title: "Annual_Report_2013-14"
        },
        {
          link: "http://nitdgp.ac.in/information/Annual_Report/Annual_Report_12-13.pdf",
          title: " Annual_Report_2012-13"
        }
      ]
    }
  },
  created () {
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
