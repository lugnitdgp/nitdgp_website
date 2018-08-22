import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Department from '@/components/Department'
import Faculty from '@/components/Faculty'
import Holidays from '@/components/Holidays'
import Archives from '@/components/Archives'
import Policies from '@/components/Policies'
import Webteam from '@/components/Webteam'
import PageNotFound from '@/components/PageNotFound'
import Contacts from '@/components/Contacts'

import Admission from '@/components/academics/Admission'
import Calendar from '@/components/academics/Calendar'
import Registrations from '@/components/academics/Registrations'
import Departments from '@/components/academics/Departments'
import Documents from '@/components/academics/Documents'
import Regulations from '@/components/academics/Regulations'
import Convocation from '@/components/academics/Convocation'
import Notices from '@/components/academics/Notices'
import Examinations from '@/components/academics/Examinations'

import Visitor from '@/components/administration/Visitor'
import Mhrd from '@/components/administration/Mhrd'
import Chairperson from '@/components/administration/Chairperson'
import Bog from '@/components/administration/Bog'
import Director from '@/components/administration/Director'
import Registrar from '@/components/administration/Registrar'
import Bwcifc from '@/components/administration/Bwcifc'
import Senate from '@/components/administration/Senate'
import Deans from '@/components/administration/Deans'
import Hods from '@/components/administration/Hods'

import Placement from '@/components/activities/Placement'
import Outreach from '@/components/activities/Outreach'
import Research from '@/components/activities/Research'
import Events from '@/components/activities/Events'
import Achievements from '@/components/activities/Achievements'
import Clubs from '@/components/activities/Clubs'
import EventVisitors from '@/components/activities/EventVisitors'

import Library from '@/components/facilities/Library'
import Mu from '@/components/facilities/Mu'
import Ceam from '@/components/facilities/Ceam'
import Cif from '@/components/facilities/Cif'
import Hostels from '@/components/facilities/Hostels'
import Po from '@/components/facilities/Po'
import Banks from '@/components/facilities/Banks'
import Guest from '@/components/facilities/Guest'
import Sac from '@/components/facilities/Sac'
import Hvl from '@/components/facilities/Hvl'
import Canteen from '@/components/facilities/Canteen'
import Cc from '@/components/facilities/Cc'

import Reports from '@/components/information/Reports'
import Eprashasan from '@/components/information/Eprashasan'
import Accounts from '@/components/information/Accounts'
import Teqip from '@/components/information/Teqip'
import Nba from '@/components/information/Nba'
import Nirf from '@/components/information/Nirf'
import Rti from '@/components/information/Rti'
import Grievances from '@/components/information/Grievances'
import History from '@/components/information/History'
import Location from '@/components/information/Location'
import Moreinfo from '@/components/information/Moreinfo'
import Careers from '@/components/information/Careers'
import Tenders from '@/components/information/Tenders'
import Chanakya from '@/components/information/Chanakya'


Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Home
    },

    {
      path: '/department/:short_code',
      name: 'Department',
      component: Department
    },

    {
      path: '/faculty/:id',
      name: 'Faculty',
      component: Faculty
    },

    // Academics
    {
      path: '/admission',
      name: 'Admission',
      component: Admission
    },
    {
      path: '/calendar',
      name: 'Calendar',
      component: Calendar
    },
    {
      path: '/registrations',
      name: 'Registrations',
      component: Registrations
    },
    {
      path: '/departments',
      name: 'Departments',
      component: Departments
    },
    {
      path: '/documents',
      name: 'Documents',
      component: Documents
    },
    {
      path: '/regulations',
      name: 'Regulations',
      component: Regulations
    },
    {
      path: '/convocation',
      name: 'Convocation',
      component: Convocation
    },
    {
      path: '/notices/:tab',
      name: 'Notices',
      component: Notices
    },
    {
      path: '/examinations',
      name: 'Examinations',
      component: Examinations
    },

    // Administration
    {
      path: '/visitor',
      name: 'Visitor',
      component: Visitor
    },
    {
      path: '/mhrd',
      name: 'Mhrd',
      component: Mhrd
    },
    {
      path: '/chairperson',
      name: 'Chairperson',
      component: Chairperson
    },
    {
      path: '/bog',
      name: 'Bog',
      component: Bog
    },
    {
      path: '/director',
      name: 'Director',
      component: Director
    },
    {
      path: '/registrar',
      name: 'Registrar',
      component: Registrar
    },
    {
      path: '/bwcifc',
      name: 'Bwcifc',
      component: Bwcifc
    },
    {
      path: '/senate',
      name: 'Senate',
      component: Senate
    },
    {
      path: '/deans',
      name: 'Deans',
      component: Deans
    },
    {
      path: '/hods',
      name: 'Hods',
      component: Hods
    },

    // Activities
    {
      path: '/placement',
      name: 'Placement',
      component: Placement
    },
    {
      path: '/outreach',
      name: 'Outreach',
      component: Outreach
    },
    {
      path: '/research',
      name: 'Research',
      component: Research
    },
    {
      path: '/events',
      name: 'Events',
      component: Events
    },
    {
      path: '/eventvisitors',
      name: 'Event Visitors',
      component: EventVisitors
    },
    {
      path: '/achievements',
      name: 'Achievements',
      component: Achievements
    },
    {
      path: '/clubs',
      name: 'Clubs',
      component: Clubs
    },

    // Facilities
    {
      path: '/library',
      name: 'Library',
      component: Library
    },
    {
      path: '/hvl',
      name: 'Hvl',
      component: Hvl
    },
    {
      path: '/canteen',
      name: 'Canteen',
      component: Canteen
    },
    {
      path: '/hostels',
      name: 'Hostels',
      component: Hostels
    },
    {
      path: '/banks',
      name: 'Banks',
      component: Banks
    },
    {
      path: '/computercenter',
      name: 'Cc',
      component: Cc
    },
    {
      path: '/medicalunit',
      name: 'Mu',
      component: Mu
    },
    {
      path: '/ceam',
      name: 'Ceam',
      component: Ceam
    },
    {
      path: '/cif',
      name: 'Cif',
      component: Cif
    },
    {
      path: '/GuestHouse',
      name: 'Guest',
      component: Guest
    },
    {
      path: '/sac',
      name: 'Sac',
      component: Sac
    },
    {
      path: '/post-office',
      name: 'Po',
      component: Po
    },

    // Information
    {
      path: '/reports',
      name: 'Reports',
      component: Reports
    },
    {
      path: '/e-prashasan',
      name: 'Eprashasan',
      component: Eprashasan
    },
    {
      path: '/accounts',
      name: 'Accounts',
      component: Accounts
    },
    {
      path: '/teqip',
      name: 'Teqip',
      component: Teqip
    },
    {
      path: '/nba',
      name: 'Nba',
      component: Nba
    },
    {
      path: '/nirf',
      name: 'Nirf',
      component: Nirf
    },
    {
      path: '/rti',
      name: 'Rti',
      component: Rti
    },
    {
      path: '/publicgrievances',
      name: 'Grievances',
      component: Grievances
    },
    {
      path: '/history',
      name: 'History',
      component: History
    },
    {
      path: '/location',
      name: 'Location',
      component: Location
    },
    {
      path: '/more',
      name: 'Moreinfo',
      component: Moreinfo
    },
    {
      path: '/chanakya',
      name: 'Chanakya',
      component: Chanakya
    },
    {
      path: '/careers',
      name: 'Careers',
      component: Careers
    },
    {
      path: '/tenders',
      name: 'Tenders',
      component: Tenders
    },
    {
      path: '/holidays',
      name: 'Holidays',
      component: Holidays
    },
    {
      path: '/archives',
      name: 'Archives',
      component: Archives
    },
    {
      path: '/policies',
      name: 'Policies',
      component: Policies
    },
    {
      path: '/webteam',
      name: 'Webteam',
      component: Webteam
    },
    {
      path: '/contacts',
      name: 'Contacts',
      component: Contacts
    },

    // This is meant to be at the last
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    }
  ]
})
