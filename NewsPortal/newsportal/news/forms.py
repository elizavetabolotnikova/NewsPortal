from .models import Articles
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields=['title','first_words','text_feild','date']

        widgets={"title":TextInput(attrs={
            'class':'form-control',
            'placeholder':'Название новости'
        }),"first_words":TextInput(attrs={
            'class':'form-control',
            'placeholder':'Анонс новости'
        }),"date":DateTimeInput(attrs={
            'class':'form-control',
            'placeholder':'Дата публикации'
        }),"text_feild":Textarea(attrs={
            'class':'form-control',
            'placeholder':'Текст новости'
        })

        }