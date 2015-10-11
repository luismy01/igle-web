from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home_view(request):
	return HttpResponseRedirect(reverse("personas:list_view"))
