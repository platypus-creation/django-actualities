from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from models import Actuality
from django.utils.translation import ugettext_lazy as _

currentSite = Site.objects.get_current()

class ActualitiesFeed(Feed):
    title = currentSite.name
    description = _(u"%s's actualities") % currentSite.name

    def link(self):
        return reverse('actualities.views.list')

    def items(self):
        return Actuality.objects.published()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_pubdate(self, item):
        return item.published_at
        
