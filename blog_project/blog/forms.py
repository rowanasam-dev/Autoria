from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import UploadedFile
from .models import Post, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'brand', 'model_year', 'price', 'image', 'body']
        labels = {
            'title': 'Car name / post title',
            'category': 'Post type',
            'brand': 'Brand',
            'model_year': 'Model year',
            'price': 'Price in EGP (optional)',
            'image': 'Car photo (optional)',
            'body': 'Details',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 7, 'maxlength': 3000}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

    def clean_model_year(self):
        year = self.cleaned_data['model_year']
        if year < 1950 or year > date.today().year + 1:
            raise forms.ValidationError('Enter a realistic model year.')
        return year

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if isinstance(image, UploadedFile) and image.size > 3 * 1024 * 1024:
            raise forms.ValidationError('Image is too large (max 3 MB).')
        return image


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='Write your comment',
        max_length=500,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'maxlength': 500,
            'placeholder': 'Share your opinion...',
        }),
    )

    class Meta:
        model = Comment
        fields = ['content']