from datetime import date
from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, ValidationError


class DateForm(FlaskForm):
  date = DateField(format='%m/%d/%Y', render_kw={"placeholder": "MM/DD/YYYY"})
  submit = SubmitField('Submit')

  def validate_date(self, field):
    if field.data < date(1851, 9, 18):
      raise ValidationError('NYT Archive only goes back to Sept 18, 1851.')