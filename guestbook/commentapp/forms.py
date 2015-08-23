from django import forms
from .models import GuestPost

class GuestPostForm(forms.ModelForm):
    
    spamdb = [
    '$$$',
    '100% free',
    'act now',
    'ad',
    'affordable',
    'amazing stuff',
    'apply now',
    'auto email removal',
    'cash bonus',
    'collect child support',
    'compare rates',
    'compete for your business',
    'credit',
    'credit bureaus',
    'dig up dirt on friends',
    'double your income',
    'earn $',
    'earn extra cash',
    'eliminate debt',
    'email marketing',
    'explode your business',
    'extra income',
    'f r e e',
    'fast cash',
    'financial freedom',
    'financially independent',
    'free gift',
    'free grant money',
    'free info',
    'free installation',
    'free investment',
    'free leads',
    'free membership',
    'free offer',
    'free preview',    
    '‘hidden’ assets',
    'home based',
    'homebased business',
    'income from home',
    'increase sales',
    'increase traffic',
    'increase your sales',
    'incredible deal',
    'info you requested',
    'information you requested',
    'internet market',
    'limited time offer',
    'make $',
    'mortgage rates',
    'multi level marketing',
    'no investment',
    'obligation',
    'online marketing',
    'opportunity',
    'order now',
    'prices',
    'promise you',
    'refinance',
    'reverses aging',
    'save $',
    'search engine listings',
    'serious cash',
    'stock disclaimer statement',
    'stop snoring',
    'unsubscribe',
    'web traffic',
    'weight loss'
    ]

    class Meta:
        model = GuestPost
        fields = ('name', 'email', 'comment')

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        for keyword in self.spamdb:
            if keyword in comment.lower():
                raise forms.ValidationError("Your post smells spammy.")
        return comment

