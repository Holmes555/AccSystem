from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'accsyst'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='accsyst/index.html'), name='index'),
    url(r'^worker_list/$', views.WorkerListView.as_view(), name='worker_list'),
    url(r'^worker/(?P<worker_id>\d+)/$', views.WorkerView.as_view(), name='worker'),
    url(r'^card/(?P<worker_id>\d+)/$', views.CardView.as_view(), name='card'),
    url(r'^card_form/(?P<worker_id>\d+)/$', views.CardFormView.as_view(), name='card_form'),
    url(r'^report_list/$', views.ReportListView.as_view(), name='report_list'),
    url(r'^report/(?P<report_id>\d+)/$', views.ReportView.as_view(), name='report'),
    url(r'^report_form/$', views.ReportFormView.as_view(), name='report_form'),
    # url(r'^card/$', views.CardView.as_view(), name='card'),
]