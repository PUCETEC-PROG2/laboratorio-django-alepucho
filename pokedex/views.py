from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render, get_object_or_404
from pokedex.forms import PokemonForm, TrainerForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
    }, request))

def pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, id=id)
    template = loader.get_template('display_pokemon.html')
    return HttpResponse(template.render({'pokemon': pokemon}, request))

def trainer(request, id: int):
    trainer = get_object_or_404(Trainer, id=id)
    template = loader.get_template('display_trainer.html')
    return HttpResponse(template.render({'trainer': trainer}, request))

# ------------------- POKEMON CRUD -------------------

@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = PokemonForm()
    return render(request, "pokemon_form.html", {'form': form})

@login_required
def edit_pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, "pokemon_form.html", {'form': form})

@login_required
def delete_pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, id=id)
    pokemon.delete()
    return redirect("pokedex:index")

# ------------------- TRAINER CRUD -------------------

@login_required
def trainers(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainers.html')
    return HttpResponse(template.render({'trainers': trainers}, request))

@login_required
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = TrainerForm()
    return render(request, "trainer_form.html", {'form': form})

@login_required
def edit_trainer(request, id: int):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = TrainerForm(instance=trainer)
    return render(request, "trainer_form.html", {'form': form})

@login_required
def delete_trainer(request, id: int):
    trainer = get_object_or_404(Trainer, id=id)
    trainer.delete()
    return redirect("pokedex:index")

# ------------------- LOGIN -------------------

class CustomLoginView(LoginView):
    template_name = 'login_form.html'