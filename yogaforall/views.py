from django.views.generic.base import TemplateView
from review.models import Review
from product.models import Product
from core.models import Meta, About, SectionName


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = Meta.objects.last()
        context['about'] = About.objects.last()
        context['section_name'] = SectionName.objects.last()
        context['products'] = Product.objects.filter(published=True)
        context['reviews'] = Review.objects.filter(published=True)
        if not self.request.COOKIES.get('uslgid'):
            context['show_cookie'] = True
        return context
    
    def render_to_response(self, context, **response_kwargs):
        response = super(IndexView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('uslgid', 'has_shown')
        return response