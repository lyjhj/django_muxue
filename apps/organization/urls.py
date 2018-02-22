from apps.organization.views import OrgView
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
]
