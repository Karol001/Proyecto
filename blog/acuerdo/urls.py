from django.conf.urls import url     
from blog.acuerdo.views import representante_view, rnatural_view

urlpatterns = [
    url(r"^juridico", representante_view,  name="representante_crear"),
    url(r"^natural", rnatural_view,  name="natural_crear"),
]