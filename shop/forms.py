from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import Category, Product, Subproduct, ExtendUser


class ProductForm(forms.Form):
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=200)
    slug = forms.SlugField(max_length=200)
    # image = forms.FileField()
    stock = forms.IntegerField()
    description = forms.CharField()
    price = forms.DecimalField()

    def save(self):
        product = Product.objects.create(
            category_id=self.cleaned_data['category_id'],
            name=self.cleaned_data['name'], slug=self.cleaned_data['slug'],
            description=self.cleaned_data['description'], stock=self.cleaned_data['stock'],
            # image=self.cleaned_data['image'],
            price=self.cleaned_data['price']
        )
        return product


class SubproductForm(forms.ModelForm):
    class Meta:
        model = Subproduct
        fields = ['name', 'image', 'description', 'price']


class RegForm(forms.Form):
    CHOICES = (
        ('Выбор 1', 'Выбор 1'),
        ('Выбор 2', 'Выбор 2'),
        ('Выбор 3', 'Выбор 3'),
    )
    login = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, label='Подтвердите пароль', widget=forms.PasswordInput)
    surname = forms.CharField(max_length=50, label='Фамилия')
    phone = forms.CharField(max_length=50, label='Телефон')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    reg_date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={"type": "date"}))
    check = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple, label='Чек-боксы')
    radio = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Радио-кнопки')
    file = forms.FileField(required=False, label='Файл')
    image = forms.ImageField(required=False, label='Картинка')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            msg = "Повторенный пароль не соответствует исходному."
            self.add_error('password2', msg)


class UserForm(forms.Form):
    login = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class UserFormRegister(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль',
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повтор пароля',
                                help_text='Введите пароль повторно для проверки')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()

        return user

    class Meta:
        model = ExtendUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'message')


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Старый пароль')
    new_password1 = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Новый пароль')
    new_password2 = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = ExtendUser
        fields = ['old_password', 'new_password1','new_password2']
