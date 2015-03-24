# -*- coding: utf-8 -*-
from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import Category

class NewIdeaForm(forms.Form):
    title = forms.CharField()

    description = forms.CharField(
        widget = forms.Textarea(),
    )

    categories = forms.MultipleChoiceField(
        choices = (
            (c.name, c.name) for c in Category.objects.all()
            )
        )

    tags = forms.CharField()

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_action = 'ideas:new_success'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        Field('title', css_class='input-xlarge'),
        Field('description', rows="3", css_class='input-xlarge'),
        'categories',
        Field('tags', rows="3", css_class='input-xlarge'),
        FormActions(
            Submit('share_your_idea',
                   'Share Your Idea!',
                   css_class="btn-primary"),
            css_class='text-center',
            )
    )

class IdeaLikeDislikeForm(forms.Form):

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_action = 'ideas:vote'
    helper.field_class = 'col-lg-12 column text-center'
    helper.layout = Layout(
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn btn-default")
            )
    )
