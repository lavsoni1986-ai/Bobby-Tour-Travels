from django import forms
from .models import BookingEnquiry


class BookingEnquiryForm(forms.ModelForm):
    """ModelForm for the Booking Enquiry section on the Contact page."""

    class Meta:
        model  = BookingEnquiry
        fields = ['full_name', 'phone_number', 'pickup_location', 'destination', 'car_requirement', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Common Tailwind classes for all text inputs / textareas
        input_classes = (
            "w-full px-4 py-3.5 rounded-2xl border border-slate-200 "
            "focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-red-500 "
            "text-sm text-slate-800 bg-slate-50 transition"
        )
        select_classes = (
            "w-full px-4 py-3.5 rounded-2xl border border-slate-200 "
            "focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-red-500 "
            "text-sm text-slate-800 bg-slate-50 transition appearance-none"
        )

        self.fields['full_name'].widget.attrs.update({
            'class': input_classes,
            'placeholder': 'e.g. Ramesh Patel',
        })
        self.fields['phone_number'].widget = forms.TextInput(attrs={
            'class': input_classes,
            'placeholder': 'e.g. 9424489377',
            'type': 'tel',
        })
        self.fields['pickup_location'].widget.attrs.update({
            'class': input_classes,
            'placeholder': 'e.g. Shahdol Railway Station',
        })
        self.fields['destination'].widget.attrs.update({
            'class': input_classes,
            'placeholder': 'e.g. Bandhavgarh / Bhopal / Amarkantak',
        })
        self.fields['car_requirement'].widget.attrs.update({
            'class': select_classes,
        })
        self.fields['message'].widget = forms.Textarea(attrs={
            'class': input_classes,
            'placeholder': 'Mention vehicle choice (Innova Crysta, Dzire, Ertiga), travel date, or passenger count...',
            'rows': 4,
        })
