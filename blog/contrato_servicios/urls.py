from django.conf.urls import url
from blog.contrato_servicios.views import Jyn_view, JyJ_view, NyJ_view, NyN_view

urlpatterns = [
    url(r'^jyn', Jyn_view , name='jyn_juridico'),
    url(r'^jyj', JyJ_view , name='jyj_juridico'),
    url(r'^nyj', NyJ_view , name='nyj_juridico'),
    url(r'^nyn', NyN_view , name='nyn_juridico'),
   # url(r'^natural$', contrato_natural_view, name='natural'),
]
