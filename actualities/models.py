from django.db import models
import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager
import datetime

class ActualityManager(models.Manager):
    def published(self):
        return self.filter(published=True, published_at__lte=datetime.datetime.now())

class Actuality(models.Model):
    """(Actuality description)"""

    title = models.CharField(_(u'Title'), max_length=255)
    slug = AutoSlugField(_(u'Slug'), populate_from='title', max_length=255, editable=True)
    
    picture = models.ImageField(_(u'Picture'), upload_to=settings.ACTUALITIES_UPLOAD)
    text = models.TextField(_(u'Text'), blank=True)
    short_text = models.CharField(_(u'Short text'), max_length=255)

    published = models.BooleanField(_(u'Published'), default=False)
    published_at = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User, verbose_name=_(u'Author'))

    enable_comments = models.BooleanField(_(u'Enable comments'), default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    tags = TaggableManager()
    
    objects = ActualityManager()
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('actualities.views.actuality', (), {
            'year': self.published_at.strftime('%Y'),
            'month': self.published_at.strftime('%m'),
            'day': self.published_at.strftime('%d'),
            'slug': self.slug,
        })

    class Meta:
        ordering = ('-published',)
        get_latest_by = ''
        verbose_name = _(u'News')
        verbose_name_plural = _(u'News')

