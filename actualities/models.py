from django.db import models
import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
import datetime

class ActualityManager(models.Manager):
    def published(self):
        return self.filter(published=True, published_at__lte=datetime.datetime.now())

class Actuality(models.Model):
    """(Actuality description)"""

    published = models.BooleanField(_(u'Published'), default=False)
    published_at = models.DateTimeField(blank=True)

    objects = ActualityManager()
    
    class Meta:
        ordering = ('-published',)
        get_latest_by = ''
        verbose_name_plural = _(u'Actualities')

    def current(self):
        return self.versions.get(active=True)

    def __unicode__(self):
        return self.current().title
    
    def get_absolute_url(self):
        return self.current().get_absolute_url()

class Version(models.Model):
    """(Version description)"""
    
    actuality = models.ForeignKey(Actuality, related_name='versions')
    
    title = models.CharField(_(u'Title'), max_length=255)
    slug = AutoSlugField(_(u'Slug'), populate_from='title', max_length=255, editable=True)
    
    picture = models.ImageField(_(u'Picture'), upload_to=settings.ACTUALITIES_UPLOAD)
    text = models.TextField(_(u'Text'))
    short_text = models.CharField(_(u'Short text'), max_length=255)
    
    revision = models.IntegerField(blank=True)
    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, verbose_name=_(u'Author'))

    class Meta:
        ordering = ('-revision',)
        get_latest_by = ''
        verbose_name_plural = _(u'Versions')

    def __unicode__(self):
        return '%s %s' % (self.title, self.created_at)
    
    @models.permalink
    def get_absolute_url(self):
        return ('actualities.views.actuality', (), {
            'year': self.actuality.published_at.strftime('%Y'),
            'month': self.actuality.published_at.strftime('%m'),
            'day': self.actuality.published_at.strftime('%d'),
            'slug': self.slug,
        })
