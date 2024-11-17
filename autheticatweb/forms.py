# from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
#     description = forms.CharField(required=True)
#     image = forms.ImageField(required=True)
#     class Meta:
#         model = Post
#         fields = ['description', 'image']
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter description...'})
    )
    image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = Post
        fields = ['description', 'image']
