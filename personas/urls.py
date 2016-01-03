from django.conf.urls import patterns, url
from .views import PersonaCreateView, PersonaDeleteView, PersonaDetailView, PersonaEditView, PersonaListView, PersonaSearchView

urlpatterns = [
	url(r'^$', PersonaListView.as_view(), name="list_view"),
	url(r'^listar$', PersonaListView.as_view(), name="list2_view"),
	url(r'^agregar$', PersonaCreateView.as_view(), name="create_view"),
	url(r'^buscar$', PersonaSearchView.as_view(), name="search_view"),
	
	url(r'^(?P<slug>(\w|\s|\W)+)/ver$', PersonaDetailView.as_view(), name="detail_view"),
	url(r'^(?P<slug>\w+)/editar$', PersonaEditView.as_view(), name="edit_view"),
	url(r'^(?P<slug>\w+)/eliminar$', PersonaDeleteView.as_view(), name="delete_view")
]
