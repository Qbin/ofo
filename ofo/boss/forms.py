# -*- coding:utf-8 -*-



from django import forms

from boss.models import Vehicle


class VehicleAddForm(forms.Form):
    
    vehicle_id = forms.CharField(max_length=6, error_messages={'invalid': u'id应为整数'})
    password = forms.CharField(max_length=4, error_messages={'invalid': u'password应为整数'})

    def clean_vehicle_id(self):
        vehicle_id = self.cleaned_data['vehicle_id']
        try:
            int(vehicle_id)
        except Exception as e:
            raise forms.ValidationError(u"车架号应为6位整数") 
        if len(vehicle_id) == 6:
            return vehicle_id
        
        raise forms.ValidationError(u"车架号应为6位整数") 


    def clean_password(self):
        password = self.cleaned_data['password']
        try:
            int(vehicle_id)
        except Exception as e:
            raise forms.ValidationError(u"密码应为4位整数") 
        if len(vehicle_id) == 4:
            return password

        raise forms.ValidationError(u"密码应为4位整数") 


class VehicleFindForm(forms.Form):
    
    vehicle_id = forms.CharField(max_length=6, error_messages={'invalid': u'id应为整数'})

    def clean_vehicle_id(self):
        vehicle_id = self.cleaned_data['vehicle_id']
        try:
            int(vehicle_id)
        except Exception as e:
            raise forms.ValidationError(u"车架号应为6位整数") 
        if len(vehicle_id) == 6:
            return vehicle_id
        
        raise forms.ValidationError(u"车架号应为6位整数") 
