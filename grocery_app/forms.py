from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=80)])
    # - address - StringField
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=80)])
    # - submit button
    submit = SubmitField('Submit')
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=80)])
    # - price - FloatField
    price = FloatField('Price', validators=[DataRequired()])
    # - category - SelectField (specify the 'choices' param)
    category = SelectField('Category', choices=['PRODUCE', 'DELI', 'BAKERY', 'PANTRY', 'FROZEN', 'OTHER'], validators=[DataRequired()])
    # - photo_url - StringField (use a URL validator)
    photo_url = StringField('Photo URL', validators=[DataRequired()])
    # - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False, get_label='Title')
    # - submit 
    submit = SubmitField('Submit')
    
