from django.conf.urls import url
from sirvasmsapp import views

from django.conf.urls import handler404, handler500

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^login/$',views.Login,name='login'),
	url(r'^logout/$', views.Logout,name='logout'),
  url(r'^home/$',views.home,name='home'),
  url(r'^received/$',views.received,name='received'),
  url(r'^sent/$',views.sent,name='sent'),
  url(r'^contacts/$',views.contacts,name='contacts'),
  url(r'^contacts/list/(?P<group>.*)$', views.contacts_list,name='contacts_list'),
  url(r'^contacts/delete/(?P<group>.*)$', views.contacts_delete,name='contacts_delete'),


  url(r'^queue/$',views.queue,name='queue'),
  url(r'^queue_blast/$',views.queue_blast,name='queue_blast'),
  url(r'^queue_blast/resend/(?P<tag>.*)$', views.queue_blast_resend,name='queue_blast_resend'),
  url(r'^sendsms/$',views.sendsms,name='sendsms'),
  url(r'^smsblast/upload/$',views.smsblast_upload,name='smsblast_upload'),
  url(r'^smsblast/group/$',views.smsblast_group,name='smsblast_group'),
  url(r'^smsblast_submit/$',views.smsblast_submit,name='smsblast_submit'),
  url(r'^smsblast_group_submit/$',views.smsblast_group_submit,name='smsblast_group_submit'),
  url(r'^contacts_submit/$',views.contacts_submit,name='contacts_submit'),
  url(r'^daterange/submit/$',views.daterange_submit,name='daterange_submit'),

  url(r'^ajax_queue_status/$',views.ajax_queue_status,name='ajax_queue_status'),

  url(r'^export/csv/$', views.export_received_csv, name='export_received_csv'),
]

handler404 = views.error_404
handler500 = views.error_500