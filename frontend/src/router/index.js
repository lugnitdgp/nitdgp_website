import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Department from '@/components/Department'
import Faculty from '@/components/Faculty'
import Holidays from '@/components/Holidays'
import Archives from '@/components/Archives'
import Policies from '@/components/Policies'
import Webteam from '@/components/Webteam'
import Downloads from '@/components/Downloads'
import PageNotFound from '@/components/PageNotFound'
import Contacts from '@/components/Contacts'
import QuickLinks from '@/components/QuickLinks'
import Liveconvocation from '@/components/Liveconvocation'

import Admission from '@/components/academics/Admission'
import Calendar from '@/components/academics/Calendar'
import Registrations from '@/components/academics/Registrations'
import Departments from '@/components/academics/Departments'
import Documents from '@/components/academics/Documents'
import Regulations from '@/components/academics/Regulations'
import Convocation from '@/components/academics/Convocation'
import Notices from '@/components/academics/Notices'
import Examinations from '@/components/academics/Examinations'
import Fees from '@/components/academics/Fees'

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
import Wardens from '@/components/administration/Wardens'
import Officers from '@/components/administration/Officers'

import Festivals from '@/components/activities/Festivals'
import Alumni from '@/components/activities/Alumni'
import Placement from '@/components/activities/Placement'
import Outreach from '@/components/activities/Outreach'
import Research from '@/components/activities/Research'
import Events from '@/components/activities/Events'
import Achievements from '@/components/activities/Achievements'
import Clubs from '@/components/activities/Clubs'
import EventVisitors from '@/components/activities/EventVisitors'
import GrievanceCell from '@/components/activities/GrievanceCell'

import Library from '@/components/facilities/Library'
import Question from '@/components/facilities/Question'
import Mu from '@/components/facilities/Mu'
import Coe from '@/components/facilities/Coe'
import Cif from '@/components/facilities/Cif'
import Hostels from '@/components/facilities/Hostels'
import Po from '@/components/facilities/Po'
import Banks from '@/components/facilities/Banks'
import Guest from '@/components/facilities/Guest'
import Sac from '@/components/facilities/Sac'
import Hvl from '@/components/facilities/Hvl'
import Canteen from '@/components/facilities/Canteen'
import Centers from '@/components/facilities/Centers'
import Cec from '@/components/facilities/Cec'

import Reports from '@/components/information/Reports'
import Eprashasan from '@/components/information/Eprashasan'
import Accounts from '@/components/information/Accounts'
import Teqip from '@/components/information/Teqip'
import Nba from '@/components/information/Nba'
import Nirf from '@/components/information/Nirf'
import Rti from '@/components/information/Rti'
import History from '@/components/information/History'
import Location from '@/components/information/Location'
import Moreinfo from '@/components/information/Moreinfo'
import Careers from '@/components/information/Careers'
import Tenders from '@/components/information/Tenders'
import Chanakya from '@/components/information/Chanakya'
import Icc from '@/components/information/Icc'
import Pgcell from '@/components/information/Pgcell'
import Pension from '@/components/information/Pension'

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
      path: '/home',
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
      path: '/convocation-pictures',
      name: 'Liveconvocation',
      component: Liveconvocation
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
    {
      path: '/fees',
      name: 'Fees',
      component: Fees
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
      path: '/heads',
      name: 'Hods',
      component: Hods
    },
    {
      path: '/wardens',
      name: 'Wardens',
      component: Wardens
    },
    {
      path: '/officers',
      name: 'Officers',
      component: Officers
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
      path: '/grievancecell',
      name: 'GrievanceCell',
      component: GrievanceCell
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
      path: '/question',
      name: 'Question',
      component: Question
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
     path: '/centers',
      name: 'Centers',
      component: Centers
    },
    {
      path: '/medicalunit',
      name: 'Mu',
      component: Mu
    },
    {
      path: '/coe',
      name: 'Coe',
      component: Coe
    },
    {
      path: '/cif',
      name: 'Cif',
      component: Cif
    },
    {
      path: '/cec',
      name: 'Cec',
      component: Cec
    },
    {
      path: '/GuestHouse',
      name: 'Guest',
      component: Guest
    },
    {
      path: '/sa&sports',
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
      path: '/eprashasan',
      name: 'Eprashasan',
      component: Eprashasan
    },
    {
      path: '/Pension',
      name: 'Pension',
      component: Pension
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
      path: '/pgcell',
      name: 'Pgcell',
      component: Pgcell
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
      path: '/icc',
      name: 'Icc',
      component: Icc
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
      path: '/downloads',
      name: 'Downloads',
      component: Downloads
    },
    {
      path: '/contacts',
      name: 'Contacts',
      component: Contacts
    },

    // new added
    {
      path: '/alumni',
      name: 'Alumni',
      component: Alumni
    },
    {
      path: '/festivals',
      name: 'Festivals',
      component: Festivals
    },
    {
      path: '/quicklinks',
      name: 'QuickLinks',
      component: QuickLinks
    },

    // This is meant to be at the last
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    }
  ]
})
