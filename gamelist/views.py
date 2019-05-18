from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from gamelist.forms import GameForm, PersonForm

from .models import (
    Game,
    Person,
)


class GameList(ListView):
    model = Game


class GameDetail(View):

    def get(self, request, pk):
        game = get_object_or_404(
            Game,
            pk=pk
        )
        game_name = game.game_name
        person_list = game.person.all()
        return render(
            request,
            'gamelist/game_detail.html',
            {'game': game,
             'game_name': game_name,
             'person_list': person_list}
        )


class GameCreate(CreateView):
    form_class = GameForm
    model = Game


class GameUpdate(UpdateView):
    form_class = GameForm
    model = Game
    template_name = 'gamelist/game_form_update.html'


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('gamelist_game_list_urlpattern')


class PersonList(ListView):
    model = Person


class PersonDetail(View):

    def get(self, request, pk):
        person = get_object_or_404(
            Person,
            pk=pk
        )
        person_name = person.person_name
        game_list = person.games.all()
        return render(
            request,
            'gamelist/person_detail.html',
            {'person': person,
             'person_name': person_name,
             'game_list': game_list}
        )


class PersonCreate(CreateView):
    form_class = PersonForm
    model = Person


class PersonUpdate(UpdateView):
    form_class = PersonForm
    model = Person
    template_name = 'gamelist/person_form_update.html'


class PersonDelete(View):

    def get(self, request, pk):
        person = self.get_object(pk)
        games = person.games.all()
        if games.count() > 0:
            return render(
                request,
                'gamelist/person_refuse_delete.html',
                {'person': person,
                 'games': games}
            )
        else:
            return render(
                request,
                'gamelist/person_confirm_delete.html',
                {'person': person}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Person,
            pk=pk
        )

    def post(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return redirect('gamelist_person_list_urlpattern')
