from django.views.generic.base import TemplateView

# Create your views here.
class Heroes(TemplateView):
	template_name = "heroes.html"


class Cloud(TemplateView):
	template_name = "detail_cloud.html"


class Sunflowey(TemplateView):
	template_name = "detail_sunflowey.html"


class Jester(TemplateView):
	template_name = "detail_jester.html"