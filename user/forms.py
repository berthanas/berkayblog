from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Kullanıcı Adı")
    password = forms.CharField(max_length=50, label = "Şifre", widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(max_length=50, label = "Şifre Tekrar", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        passwordConfirm = self.cleaned_data.get("passwordConfirm")

        if password and passwordConfirm and password != passwordConfirm:
            raise forms.ValidationError("Şifreler aynı değil")
        
        values = {
            "username" : username,
            "password" : password
        }
        
        return values

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Kullanıcı Adı")
    password = forms.CharField(max_length=50, label = "Şifre", widget = forms.PasswordInput)
    