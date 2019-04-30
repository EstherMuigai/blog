from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = TextAreaField(validators = [Required()])
    submit = SubmitField('Comment')

class DeleteButton(FlaskForm):
    delete = SubmitField('Delete')

class EditButton(FlaskForm):
    edit = SubmitField('Edit')