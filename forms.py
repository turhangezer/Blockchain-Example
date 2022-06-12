from wtforms import Form, StringField, DecimalField, IntegerField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Tam Adınız', [validators.Length(min=1,max=50)])
    username = StringField('Kullanıcı adınız', [validators.Length(min=4,max=25)])
    email = StringField('Email', [validators.Length(min=6,max=50)])
    password = PasswordField('Şifre', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Tekrar Şifre')


class SendMoneyForm(Form):
    username = StringField('Alıcı Kullanıcı adı', [validators.Length(min=4,max=25)])
    amount = StringField('Miktar', [validators.Length(min=1,max=50)])


class BuyForm(Form):
    amount = StringField('Miktar', [validators.Length(min=1,max=50)])