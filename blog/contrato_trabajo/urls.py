from django.conf.urls import url
from blog.contrato_trabajo.views import contrato_juridico_view, contrato_natural_view

urlpatterns = [
    url(r'^juridico$', contrato_juridico_view, name='juridico'),
    url(r'^natural$', contrato_natural_view, name='natural'),
]
