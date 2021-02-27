from django.forms import ModelForm

from .models import Stock, AssetManagementOut, AssetManagementDetails, AssetManagementIn, Asset, Merchant


class MerchantForms(ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'


class AssetForms(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetManagementInForms(ModelForm):
    class Meta:
        model = AssetManagementIn
        fields = '__all__'


class AssetManagementDetailsForms(ModelForm):
    class Meta:
        model = AssetManagementDetails
        fields = '__all__'


class AssetManagementOutForms(ModelForm):
    class Meta:
        model = AssetManagementOut
        fields = '__all__'


class StockForms(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
