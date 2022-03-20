from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField


class JobsForm(FlaskForm):
    job = StringField('Job Title')
    leader_id = IntegerField('Team Leader id')
    work_size = IntegerField('Work Size')
    collaborators = StringField('Collaborators')
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')
