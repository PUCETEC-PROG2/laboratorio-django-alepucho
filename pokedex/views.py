from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm
from pokedex.forms import TrainerForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons=Pokemon.objects.all()
    trainers=Trainer.objects.all()
    template=loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons':pokemons,
        'trainers':trainers
        }, request))

def pokemon(request, id: int):
    pokemon=Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context={
        'pokemon':pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, id: int):
    trainer=Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context={
        'trainer':trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method =="POST":
        form= PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form= PokemonForm()
    return render(request, "pokemon_form.html", {'form': form})

@login_required
def edit_pokemon(request, id: int):
    pokemon=Pokemon.objects.get(id=id)
    if request.method =="POST":
        form= PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form= PokemonForm(instance=pokemon)
    return render(request, "pokemon_form.html", {'form': form})

@login_required
def delete_pokemon(request, id: int):
    pokemon=Pokemon.objects.get(id=id)
    pokemon.delete()
    return redirect("pokedex:index")

@login_required
def trainers(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainers.html')
    context = {
        'trainers': trainers
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_trainer(request):
    if request.method =="POST":
        form= TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form= TrainerForm()
    return render(request, "trainer_form.html", {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login_form.html'