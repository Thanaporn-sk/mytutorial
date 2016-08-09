from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^d3$', views.d3Chain, name='d3Chain'),
    url(r'^d3circlepack$', views.d3circlepack, name='d3circlepack'),
    url(r'^d3lineChart$', views.d3lineChart, name='d3lineChart'),    
        url(r'^d3barChart$', views.d3barChart, name='d3barChart'),   
    url(r'^d3multiLineChart$', views.d3multiLineChart, name='d3multiLineChart'),
    url(r'^d3sunburst$', views.d3sunburst, name='d3sunburst'),  

      
]