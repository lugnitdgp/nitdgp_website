import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
//import Department from '@/components/Department'
//import Faculty from '@/components/Faculty'
import PageNotFound from '@/components/PageNotFound'

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
import Students from '@/components/activities/Students'

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

    // {
    //   path: '/department',
    //   name: 'Department',
    //   component: Department
    // },

    // {
    //   path: '/faculty',
    //   name: 'Faculty',
    //   component: Faculty
    // },

    // Academics
    {
      path: '/academics/admission',
      name: 'Admission',
      component: Admission
    },
    {
      path: '/academics/calendar',
      name: 'Calendar',
      component: Calendar
    },
    {
      path: '/academics/registrations',
      name: 'Registrations',
      component: Registrations
    },
    {
      path: '/academics/departments',
      name: 'Departments',
      component: Departments
    },
    {
      path: '/academics/documents',
      name: 'Documents',
      component: Documents
    },
    {
      path: '/academics/regulations',
      name: 'Regulations',
      component: Regulations
    },
    {
      path: '/academics/convocation',
      name: 'Convocation',
      component: Convocation
    },
    {
      path: '/academics/notices',
      name: 'Notices',
      component: Notices
    },
    {
      path: '/academics/examinations',
      name: 'Examinations',
      component: Examinations
    },

    // Administration
    {
      path: '/administration/visitor',
      name: 'Visitor',
      component: Visitor
    },
    {
      path: '/administration/mhrd',
      name: 'Mhrd',
      component: Mhrd
    },
    {
      path: '/administration/chairperson',
      name: 'Chairperson',
      component: Chairperson
    },
    {
      path: '/administration/bog',
      name: 'Bog',
      component: Bog
    },
    {
      path: '/administration/director',
      name: 'Director',
      component: Director
    },
    {
      path: '/administration/registrar',
      name: 'Registrar',
      component: Registrar
    },
    {
      path: '/administration/bwcifc',
      name: 'Bwcifc',
      component: Bwcifc
    },
    {
      path: '/administration/senate',
      name: 'Senate',
      component: Senate
    },
    {
      path: '/administration/deans',
      name: 'Deans',
      component: Deans
    },
    {
      path: '/administration/hods',
      name: 'Hods',
      component: Hods
    },

    // Activities
    {
      path: '/activities/placement',
      name: 'Placement',
      component: Placement
    },
    {
      path: '/activities/outreach',
      name: 'Outreach',
      component: Outreach
    },
    {
      path: '/activities/research',
      name: 'Research',
      component: Research
    },
    {
      path: '/activities/events',
      name: 'Events',
      component: Events
    },
    {
      path: '/activities/achievements',
      name: 'Achievements',
      component: Achievements
    },
    {
      path: '/activities/students',
      name: 'Students',
      component: Students
    },

    // Facilities
    {
      path: '/facilities/library',
      name: 'Library',
      component: Library
    },
    {
      path: '/facilities/hvl',
      name: 'Hvl',
      component: Hvl
    },
    {
      path: '/facilities/canteen',
      name: 'Canteen',
      component: Canteen
    },
    {
      path: '/facilities/hostels',
      name: 'Hostels',
      component: Hostels
    },
    {
      path: '/facilities/banks',
      name: 'Banks',
      component: Banks
    },
    {
      path: '/facilities/computercenter',
      name: 'Cc',
      component: Cc
    },
    {
      path: '/facilities/medicalunit',
      name: 'Mu',
      component: Mu
    },
    {
      path: '/facilities/ceam',
      name: 'Ceam',
      component: Ceam
    },
    {
      path: '/facilities/cif',
      name: 'Cif',
      component: Cif
    },
    {
      path: '/facilities/GuestHouse',
      name: 'Guest',
      component: Guest
    },
    {
      path: '/facilities/sac',
      name: 'Sac',
      component: Sac
    },
    {
      path: '/facilities/post-office',
      name: 'Po',
      component: Po
    },

    // Information
    {
      path: '/information/reports',
      name: 'Reports',
      component: Reports
    },
    {
      path: '/information/e-prashasan',
      name: 'Eprashasan',
      component: Eprashasan
    },
    {
      path: '/information/accounts',
      name: 'Accounts',
      component: Accounts
    },
    {
      path: '/information/teqip',
      name: 'Teqip',
      component: Teqip
    },
    {
      path: '/information/nba',
      name: 'Nba',
      component: Nba
    },
    {
      path: '/information/nirf',
      name: 'Nirf',
      component: Nirf
    },
    {
      path: '/information/rti',
      name: 'Rti',
      component: Rti
    },
    {
      path: '/information/publicgrievances',
      name: 'Grievances',
      component: Grievances
    },
    {
      path: '/information/history',
      name: 'History',
      component: History
    },
    {
      path: '/information/location',
      name: 'Location',
      component: Location
    },
    {
      path: '/information/more',
      name: 'Moreinfo',
      component: Moreinfo
    },
    {
      path: '/information/chanakya',
      name: 'Chanakya',
      component: Chanakya
    },
    {
      path: '/information/careers',
      name: 'Careers',
      component: Careers
    },
    {
      path: '/information/tenders',
      name: 'Tenders',
      component: Tenders
    },

    // This is meant to be at the last
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    }
  ]
})
