import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Department from '@/components/Department'
import DepartmentProgrammes from '@/components/DepartmentProgrammes'
import DepartmentHOD from '@/components/DepartmentHOD'
import DepartmentPeople from '@/components/DepartmentPeople'
import DepartmentResearch from '@/components/DepartmentResearch'
import DepartmentProjects from '@/components/DepartmentProjects'
import DepartmentFacilities from '@/components/DepartmentFacilities'
import DepartmentActivities from '@/components/DepartmentActivities'
import DepartmentPhotoGallery from '@/components/DepartmentPhotoGallery'
import DepartmentContactUs from '@/components/DepartmentContactUs'
import ResearchAtAGlance from '@/components/ResearchAtAGlance'
import Faculty from '@/components/Faculty'
import Holidays from '@/components/Holidays'
import Archives from '@/components/Archives'
import Policies from '@/components/Policies'
import Webteam from '@/components/Webteam'
import Downloads from '@/components/Downloads'
import PageNotFound from '@/components/PageNotFound'
import Contacts from '@/components/Contacts'
import QuickLinks from '@/components/QuickLinks'
import Nad from '@/components/Nad'
import Liveconvocation from '@/components/Liveconvocation'
import SearchResults from '@/components/SearchResults'
import PowerSystem from '@/components/PowerSystem'
import Powerem from '@/components/Powerem'
import ResultDriver from '@/components/ResultDriver'
import ResultDriverRest from '@/components/ResultDriverRest'
import Cshortseminer from '@/components/Cshortseminer'

import Admission from '@/components/academics/Admission'
import Newadmission from '@/components/academics/Newadmission'
import Calendar from '@/components/academics/Calendar'
import Registrations from '@/components/academics/Registrations'
import Departments from '@/components/academics/Departments'
import Documents from '@/components/academics/Documents'
import Regulations from '@/components/academics/Regulations'
import Convocation from '@/components/academics/Convocation'
import Notices from '@/components/academics/Notices'
import Examinations from '@/components/academics/Examinations'
import Fees from '@/components/academics/Fees'
import Syllabus from '@/components/academics/Syllabus'
import Brochure from '@/components/academics/Brochure'

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
import Care from '@/components/activities/Care'
import Coeam from '@/components/activities/Coeam'
import Crew from '@/components/activities/Crew'
import Iotis from '@/components/activities/Iotis'
import Raa from '@/components/activities/Raa'
import Ncc from '@/components/activities/Ncc'
import Uba from '@/components/activities/Uba'
import Beat from '@/components/activities/Beat'
import Newsletters from '@/components/activities/Newsletters'
import Covidinfo from '@/components/activities/Covidinfo'
import Geothermal from '@/components/activities/Geothermal'
import FitIndiaMovement from '@/components/activities/FitIndiaMovement'

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
import Cc from '@/components/facilities/Cc'
import Brics from '@/components/facilities/Brics'
import Ipr from '@/components/facilities/Ipr'
import Ibsc from '@/components/facilities/Ibsc'
import Pcbd from '@/components/facilities/Pcbd'
import Logocompetition from '@/components/facilities/Logocompetition'
import Semievent from '@/components/facilities/Semievent'

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
import Mission from '@/components/information/Mission'
import Dpromotion from '@/components/information/Dpromotion'
import Rroster from '@/components/information/Rroster'
import Strategicalplan from '@/components/information/Strategicalplan'

import Collaboration from '@/components/activities/Collaboration'
import Srcc from '@/components/Srcc'

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
      path: '/department/:short_code/programmes',
      name: 'DepartmentProgrammes',
      component: DepartmentProgrammes
    },
    {
      path: '/department/:short_code/HOD',
      name: 'DepartmentHOD',
      component: DepartmentHOD
    },
    {
      path: '/department/:short_code/people',
      name: 'DepartmentPeople',
      component: DepartmentPeople
    },
    {
      path: '/department/:short_code/research',
      name: 'DepartmentResearch',
      component: DepartmentResearch
    },
    {
      path: '/department/:short_code/projects',
      name: 'DepartmentProjects',
      component: DepartmentProjects
    },
    {
      path: '/department/:short_code/facilities',
      name: 'DepartmentFacilities',
      component: DepartmentFacilities
    },
    {
      path: '/department/:short_code/activities',
      name: 'DepartmentActivities',
      component: DepartmentActivities
    },
    {
      path: '/department/:short_code/photo-gallery',
      name: 'DepartmentPhotoGallery',
      component: DepartmentPhotoGallery
    },
    {
      path: '/department/:short_code/contact-us',
      name: 'DepartmentContactUs',
      component: DepartmentContactUs
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
      path: '/newadmission',
      name: 'Newadmission',
      component: Newadmission
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
      path: '/curriculum',
      name: 'Syllabus',
      component: Syllabus
    },
    {
      path: '/live-convocation',
      name: 'Liveconvocation',
      component: Liveconvocation
    },
    {
      path: '/academicdocument',
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
    {
      path: '/Academicbrochure',
      name: 'Brochure',
      component: Brochure
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
      path: '/care',
      name: 'Care',
      component: Care
    },
    {
      path: '/coeam',
      name: 'Coeam',
      component: Coeam
    },
    {
      path: '/crew',
      name: 'Crew',
      component: Crew
    },
    {
      path: '/iotis',
      name: 'Iotis',
      component: Iotis
    },
    {
      path: '/beat',
      name: 'Beat',
      component: Beat
    },
    {
      path: '/newsletters',
      name: 'Newsletters',
      component: Newsletters
    },
    {
      path: '/covid19informations',
      name: 'Covidinfo',
      component: Covidinfo
    },
    {
      path: '/rashtriyaavishkarabhiyan',
      name: 'Raa',
      component: Raa
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
      path: '/scientificevents',
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
    {
      path: '/ncc',
      name: 'Ncc',
      component: Ncc
    },
    {
      path: '/uba',
      name: 'Uba',
      component: Uba
    },
    {
      path: '/heliumgeothemal',
      name: 'Geothermal',
      component: Geothermal
    },
    {
      path: '/researchataglance',
      name: 'ResearchAtAGlance',
      component: ResearchAtAGlance
    },
    {
      path: '/fitindiamovement',
      name: 'FitIndiaMovement',
      component: FitIndiaMovement
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
      path: '/coes',
      name: 'Coe',
      component: Coe
    },
    {
      path: '/cif',
      name: 'Cif',
      component: Cif
    },
    {
      path: '/cc',
      name: 'Cc',
      component: Cc
    },
    {
      path: '/cec',
      name: 'Cec',
      component: Cec
    },
    {
      path: '/srcc',
      name: 'Srcc',
      component: Srcc
    },
    {
      path: '/GuestHouse',
      name: 'Guest',
      component: Guest
    },
    {
      path: '/activities&sports',
      name: 'Sac',
      component: Sac
    },
    {
      path: '/post-office',
      name: 'Po',
      component: Po
    },
    {
      path: '/brics',
      name: 'Brics',
      component: Brics
    },
    {
      path: '/ipr',
      name: 'Ipr',
      component: Ipr
    },
    {
      path: '/ibsc',
      name: 'Ibsc',
      component: Ibsc
    },
    {
      path: '/pcbd',
      name: 'Pcbd',
      component: Pcbd
    },
    {
      path: '/logocompetition',
      name: 'Logocompetition',
      component: Logocompetition
    },
    {
      path: '/childreneducation',
      name: 'Semievent',
      component: Semievent
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
      path: '/accreditation',
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
      path: '/aboutus',
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
      path: '/mission&vision',
      name: 'Mission',
      component: Mission
    },
    {
      path: '/departmentalpromotion',
      name: 'Dpromotion',
      component: Dpromotion
    },
    {
      path: '/reservationrosters',
      name: 'Rroster',
      component: Rroster
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
    {
      path: '/strategicalplan',
      name: 'Strategicalplan',
      component: Strategicalplan
    },
    //Reasearch and Collaboration
    {
      path: '/collaboration',
      name: 'Collaboration',
      component: Collaboration
    },

    // new added
    {
      path: '/alumnipage',
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
    {
      path: '/nad',
      name: 'Nad',
      component: Nad
    },
    {
      path: '/search',
      name: 'SearchResults',
      component: SearchResults
    },
    {
      path: '/powersystem',
      name: 'PowerSystem',
      component: PowerSystem
    },
    {
      path: '/powerelectronics',
      name: 'Powerem',
      component: Powerem
    },
    {
      path: '/resultdriver',
      name: 'ResultDriver',
      component: ResultDriver
    },
    {
      path: '/resultdriverrest',
      name: 'ResultDriverRest',
      component: ResultDriverRest
    },
    {
      path: '/candidateseminer',
      name: 'Cshortseminer',
      component: Cshortseminer
    },
    {
      path: '/icis2020/:icis2020',
      // name: 'icis2020'
    },
    
    // This is meant to be at the last
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    }
  ]
})
