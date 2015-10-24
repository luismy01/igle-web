from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context
	
		

class LoginRequiredMixin(object):
	
	"""
		This view is based on LoginRequiredMixin class of the django-guardian app
		For more detail, visit: https://github.com/django-guardian/django-guardian/blob/devel/guardian/mixins.py
	"""
	
	redirect_field_name = "next"
	login_url = reverse_lazy("login")

	def dispatch(self, request, *args, **kwargs):
		return login_required(redirect_field_name=self.redirect_field_name,
			login_url=self.login_url)(
			super(LoginRequiredMixin, self).dispatch
		)(request, *args, **kwargs)