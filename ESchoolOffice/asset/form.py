from django.forms import ModelForm

from ESchoolOffice.asset.models import Stock, AssetManagementOut, AssetManagementDetails, AssetManagementIn, Asset, \
    Merchant


class MerchantForm(ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetManagementInForm(ModelForm):
    class Meta:
        model = AssetManagementIn
        fields = '__all__'


class AssetManagementDetailsForm(ModelForm):
    class Meta:
        model = AssetManagementDetails
        fields = '__all__'


class AssetManagementOutForm(ModelForm):
    class Meta:
        model = AssetManagementOut
        fields = '__all__'


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
