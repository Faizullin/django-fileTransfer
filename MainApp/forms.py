from django import forms
from .models import FileModel#FileModel to connect with database

class UploadFileForm(forms.ModelForm):
    # title = forms.CharField(max_length=50,label="Заголовок",required=False,widget=forms.TextInput(attrs={
    #     'class':'form-input','placeholder':'None'}))
    # sender = forms.CharField(max_length=50,label="Отправитель",required=False,widget=forms.TextInput( attrs={
    #     'class':'form-input','placeholder':'user'}))
    # file = forms.FileField(label="Файл") #upload_to='files'
    #this variable are also in models(database) => Meta
    class Meta:
        model=FileModel;
        fields= ['title','sender','file'] #'__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input','placeholder':'None'}),
            'sender':forms.TextInput(attrs={'class':'form-input','placeholder':'None'}),
        }
