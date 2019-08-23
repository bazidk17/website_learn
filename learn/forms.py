from django import forms
from .models import topic,subtopics,course,subtopics_info

class topic_add(forms.ModelForm):
    class Meta:
        model=topic
        fields=['topic_name']

class topic_remove_from_course(forms.Form):
    select_topic= forms.ModelChoiceField(queryset=topic.objects.all())
    def __init__(self, *args, **kwargs):
        cc = kwargs.pop('cname', None)
        super(topic_remove_from_course, self).__init__(*args, **kwargs)

        if cc:
            self.fields['select_topic'].queryset = topic.objects.filter(course_id=cc)

class subtopic_remove_from_topic(forms.Form):
    select_subtopic= forms.ModelChoiceField(queryset=subtopics.objects.all())
    def __init__(self, *args, **kwargs):
        cc = kwargs.pop('cname', None)
        super(subtopic_remove_from_topic, self).__init__(*args, **kwargs)

        if cc:
            self.fields['select_subtopic'].queryset = subtopics.objects.filter(topic_id=cc)

class subtopic_add(forms.ModelForm):
    class Meta:
        model=subtopics
        fields=['subtopics_name']

class subtopics_info_edit(forms.ModelForm):
    class Meta:
        model=subtopics_info
        fields=['theory','diagram','code_py','code_cpp']