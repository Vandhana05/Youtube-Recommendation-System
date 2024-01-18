from .models import VideoForm 
from django import forms 

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoForm
        fields = ["CategoryId", "Category", "ChannelName", "Title", "video"]

        widgets = {
            'CategoryId': forms.TextInput(attrs={'class': 'form-control'}),
            'Category': forms.TextInput(attrs={'class': 'form-control'}),
            'ChannelName': forms.TextInput(attrs={'class': 'form-control'}),
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={
                'class': 'form-group btn-rounded form-control',
                'label': 'video'
            }),
        }
