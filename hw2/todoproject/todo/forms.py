from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=128,
        widget=forms.TextInput(
            attrs={"class" : "form-control", "placeholder" : "Enter todo", "aria-label" : "Todo", "aria-describedby" : "add-btn"}
        )
    )
