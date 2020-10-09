from django.conf.urls import url

from activities.views import *

app_name = 'activities'

urlpatterns = [

    url(r'^activities/student-clubs/$', StudentViewSet.as_view(), name='view-student-clubs'),
    url(r'^activities/festivals/$', FestivalViewSet.as_view(), name='view-festivals'),
    url(r'^activities/grievance-cell/$', GrievanceCellViewSet.as_view(), name='view-grievance-cell'),
    url(r'^activities/seminars-and-events/$', SeminarEventViewSet.as_view(), name='view-seminars-events'),
    url(r'^activities/achievements/$', AchievementsViewSet.as_view(), name='view-achievements'),
    url(r'^activities/research/$', ResearchViewSet.as_view(), name='view-research'),
    url(r'^activities/placement/$', PlacementViewSet.as_view(), name='view-placement'),
    url(r'^activities/visitors/$', VisitorViewSet.as_view(), name='view-visitors'),
    url(r'^activities/placement-links/$', PlacementLinksViewSet.as_view(), name='view-placement-links'),
    url(r'^activities/outreach/$', OutreachViewSet.as_view(), name='view-outreach'),
    url(r'^activities/collaboration/$', CollaborationViewSet.as_view(), name='view-collaboration'),
    url(r'^activities/brics/$', BricsViewSet.as_view(), name='view-brics'),
    url(r'^activities/coe/$', CoeViewSet.as_view(), name='view-coe'),
    url(r'^activities/coecarousel/$', CoecarouselViewSet.as_view(), name='view-coecarousel'),
    url(r'^activities/alljournal/$', AlljournalViewSet.as_view(), name='view-all-journal'),
    url(r'^activities/allpatent/$', AllpatentViewSet.as_view(), name='view-all-patent'),
    url(r'^activities/allproject/$', AllprojectViewSet.as_view(), name='view-all-project'),
    url(r'^activities/newsletters/$', NewslettersViewSet.as_view(), name='view-newsletter'),


]
