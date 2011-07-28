from django.db import models
from django.utils.translation import ugettext_lazy as _

class Actuality(models.Model):
    """(Actuality description)"""

    published = models.BooleanField(_(u'Published'), default=False)
    published_at = models.DateTimeField(blank=True)
    
    class Meta:
        ordering = ('',)
        get_latest_by = ''
        verbose_name_plural = ('Actualities',)

    def __unicode__(self):
        return u"Actuality"
    
    @models.permalink
    def get_absolute_url(self):
        return ('actualities.views.actuality', attrs=(self.id))

class Version(models.Model):
    """(Version description)"""
    
    title = models.CharField(_(u'Title'), blank=True, max_length=255)
    picture = models.ImageField(_(u'Picture'), upload_to=settings.ACTUALITY_UPLOAD)
    text = models.TextField(_(u'Text'), blank=True)
    short_text = models.CharField(_(u'Short text'), blank=True, max_length=255)
    
    revision = models.IntegerField(blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-revision',)
        get_latest_by = ''
        verbose_name_plural = ('Versions',)

    def __unicode__(self):
        return u"Version"
    