from apps.organization.views import OrgView, AddUserAskView
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]
