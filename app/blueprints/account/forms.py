from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput



class PokeDataForm(FlaskForm):
    poke_name = HiddenField(validators=[DataRequired()])
    submit = SubmitField()