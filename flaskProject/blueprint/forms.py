import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db

# check if the register content vaild
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="invaild email!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="length error of verify code!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="length of username must between 3 and 20!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="length of password must between 6 and 20!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])


    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="this email has been registered!")


    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="wrong verify code!")
        #else:
            #db.session.delete(captcha_model)
            #db.session.commit()

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="invaild email!")])
    password = wtforms.StringField(
        validators=[Length(min=6, max=20, message="length of password must between 6 and 20!")])



class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="too long or too short")])
    content = wtforms.StringField(validators=[Length(min=3, message="content is too short")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="content is too short")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="question id must included!")])

