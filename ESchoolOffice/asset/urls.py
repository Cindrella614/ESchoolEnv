from django.conf.urls import url
from .views import asset, edit_asset, delete_asset, merchant

app_name = 'asset'
urlpatterns = [
    url(r'^$', asset, name='AssetForms'),
    url(r'edit_asset/(?P<pk>\d+)/$', edit_asset, name='edit_asset'),
    url(r'delete_asset/(?P<pk>\d+)/$', delete_asset, name='delete_asset'),
    url(r'^$', merchant, name='MerchantForms'),
]
