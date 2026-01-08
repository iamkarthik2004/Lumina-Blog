from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'category', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Enter Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Enter Subtitle'}),
            'category': forms.TextInput(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'e.g. Tech, Art'}),
            'content': forms.Textarea(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary h-40', 'placeholder': 'Write your story...'}),
        }
