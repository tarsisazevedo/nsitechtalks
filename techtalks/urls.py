from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','techtalks.views.index'),
    (r'^palestrante/(?P<palestrante_id>\d+)/$','techtalks.views.palestrante'),
    (r'^anteriores$','techtalks.views.anteriores'),
    (r'^detalhes_edicao/(?P<edicao_id>\d+)/$','techtalks.views.detalhes_edicao'),
    
)

