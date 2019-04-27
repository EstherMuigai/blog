from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required

class NewPostForm(FlaskForm):
    title = StringField('Title',validators = [Required()])
    content = TextAreaField()
    submit = SubmitField('Post')

class DeleteButton(FlaskForm):
    delete = SubmitField('Delete')

class EditButton(FlaskForm):
    edit = SubmitField('Edit')
