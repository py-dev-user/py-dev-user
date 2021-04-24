from django import forms
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
#
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

from ckeditor.widgets import CKEditorWidget

from .tasks import send_circular_message

# from .models import Profile


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
#
# class ProfileForm(forms.ModelForm):
#
#     def clean_date_of_birth(self):
#         data = self.cleaned_data['date_of_birth']
#         now = datetime.now().date()
#         years = relativedelta(now, data).years
#
#         if years < 18:
#             raise ValidationError(_("Your age less than 18 years"))
#
#         return data
#
#     class Meta:
#         model = Profile
#         fields = ('date_of_birth', 'avatar',)


class SendMessage(forms.Form):
    subject = forms.CharField(max_length=255, label='Subject')
    body = forms.CharField(widget=CKEditorWidget, label='Message')
    is_seller = forms.BooleanField(label='Seller only', required=False)

    def send_messages(self):
        if len(self.cleaned_data['subject']) and len(self.cleaned_data['body']):
            subj = self.cleaned_data['subject']
            body = self.cleaned_data['body']
            is_seller = bool(self.cleaned_data['is_seller'])
            send_circular_message.delay(subj, body, is_seller)