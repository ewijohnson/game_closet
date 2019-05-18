from django import forms

from gamelist.models import Person, Game


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

    def clean_person_name(self):
        return self.cleaned_data['person_name'].strip()


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def clean_game_name(self):
        return self.cleaned_data['game_name'].strip()
