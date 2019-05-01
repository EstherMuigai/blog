from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email

class CommentForm(FlaskForm):
    name = StringField(validators = [Required()])
    email = StringField(validators = [Required(),Email()])
    comment = TextAreaField(validators = [Required()])
    submit = SubmitField('Comment')

class DeleteButton(FlaskForm):
    delete = SubmitField('Delete')

class EditButton(FlaskForm):
    edit = SubmitField('Edit')