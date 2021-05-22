from django.forms import ModelForm, TextInput, forms
from django.forms.widgets import NumberInput
from .models import NameRequest, CoordRequest, BuildingRequest, Building

class NameRequestForm(ModelForm):
    class Meta:
        model = NameRequest
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}

class CoordRequestForm(ModelForm):
    class Meta:
        model = CoordRequest
        fields = ['longitude', 'latitude']
        widgets = { 'longitude' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Place longitude'}),
                    'latitude' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Place latitude'})
                    }

class BuildingRequestForm(ModelForm):
    class Meta:
        model = BuildingRequest
        fields = ['building_id']
        # widgets = {'building_id' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}

class BuildingForm(ModelForm) :
    class Meta :
        model = Building
        fields = ['building_name', 'building_id', 'owner_name', 'longitude', 'latitude', 'yesterday_min', 'yesterday_max', 'db_yesterday_min', 'db_yesterday_max']
        widgets = { 'building_name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Building Name'}),
                    'building_id' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Building ID'}),
                    'owner_name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Owner Name'}),
                    'longitude' : TextInput(attrs={'class' : 'input', 'placeholder' : 'longitude'}),
                    'latitude' : TextInput(attrs={'class' : 'input', 'placeholder' : 'latitude'}),
                    'yesterday_min' : NumberInput(attrs={'class' : 'input', 'placeholder' : 'yesterday_min'}),
                    'yesterday_max' : NumberInput(attrs={'class' : 'input', 'placeholder' : 'yesterday_max'}),
                    'db_yesterday_min' : NumberInput(attrs={'class' : 'input', 'placeholder' : 'db_yesterday_min'}),
                    'db_yesterday_max' : NumberInput(attrs={'class' : 'input', 'placeholder' : 'db_yesterday_max'}),
                    }

class BuildingUpdateForm(ModelForm) :
    class Meta :
        model = Building
        fields = ['building_name', 'building_id', 'owner_name']