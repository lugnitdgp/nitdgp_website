<template>
  <links-page>
    <card v-for="nirf in nirfs" :title="nirf.header" :key="nirf.id">
      <ul>
        <li v-for="content in nirf.linklist" :key="content.id">
          <a target="new" :href="content.link">
            {{ content.title }}
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
  name: "Nirf",
  data () {
    return {
      nirfs: []
    }
  },
  created () {
    this.nirfs = [
      {
        header: "National Institute Ranking Framework(Reports) 2018",
        linklist: [
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/NIT DURGAPUR Annual Report 2015-16_Final.pdf",
            title: "Annual_Report_2015-16"
          },
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/NIT%20Durgapur%20Annual%20nirf%202014-15.pdf",
            title: "Annual_Report_2014-15"
          },
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/NIT%20Durgapur%20Annual%20Report%202013-14.pdf",
            title: "Annual_Report_2013-14"
          },
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/Annual_Report_12-13.pdf",
            title: " Annual_Report_2012-13"
          },
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/Annual_Report_2011-12.pdf",
            title: "Annual_Report_2011-12"
          },
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/Annual_Report_2010-11.pdf",
            title: "Annual_Report_2010-11"
          },
          {
            link: "http://nitdgp.ac.in/information/Annual_Report/Annual_Report_2009-10.pdf",
            title: "Annual_Report_2009-10"
          }
        ]
      },
      {
        header: "National Institute Ranking Framework(Reports) 2017",
        linklist: [
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/NIT Durgapur_ Separate Audit Report_2015-16.pdf",
            title: "Audit Report 2015 - 2016"
          },
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/SAR_2014_15.pdf",
            title: "Audit Report 2014 - 2015"
          },
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/Audit%20Report%202013-2014.pdf",
            title: "Audit Report 2013 - 2014"
          },
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/Annual_Report_12-13.pdf",
            title: " Audit Report 2012 - 2013"
          },
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/Audit%20Report%202011%20-%202012.pdf",
            title: " Audit Report 2011 - 2012"
          },
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/Audit%20Report%202010%20-%202011.pdf",
            title: "Audit Report 2010 - 2011"
          },
          {
            link: "http://nitdgp.ac.in/information/Audit_Report/Audit%20Report%202009%20-%202010.pdf",
            title: " Audit Report 2009 - 2010"
          }
        ]
      }
    ]
    this.$emit('hideloader', true)
  },
  components: {
    Card,
    LinksPage
  }
}
</script>
