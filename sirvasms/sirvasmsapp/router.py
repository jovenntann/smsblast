from django.conf import settings

class DBRouter(object):

  def db_for_read(self, model, **hints):
    if model._meta.app_label == 'goip':
        return 'goip'
    else:
        return 'default'


  def db_for_write(self, model, **hints):
    if model._meta.app_label == 'goip':
        return 'goip'
    else:
        return 'default'
