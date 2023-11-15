from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipement, Character
from .forms import MoveForm
from django.contrib import messages

def post_list(request):
    soldat = Character.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'blog/post_list.html', {'stormtroopers':soldat,'equipements': equipements})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    lieu = character.lieu
    form=MoveForm()
    if request.method == "POST":
        ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            form.save(commit=False)
            nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
            if nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_equip=="armurerie" and character.etat=='reposé':
                character.etat="pret"
                character.save()
                nouveau_lieu.disponibilite="occupe"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Le Stormtrooper est équipé !')
            elif nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_equip=="champ de tir" and character.etat=='pret':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                character.etat="a faim"
                nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                if character.precision <100:
                    character.precision+=1
                character.save()
                messages.add_message(request, messages.SUCCESS, 'Le Stormtrooper a amélioré sa précision au champ de tir  !')  
            elif nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_equip=="cantina" and character.etat=='a faim':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                character.etat="rassasié"
                character.save()
                nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Le Stormtrooper a mangé à la Cantina !')
            elif nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_equip=="base" and character.etat=='rassasié':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                character.etat="fatigué"
                character.save()
                nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Le Stormtrooper a patrouillé la base !')
            elif nouveau_lieu.id_equip=="dortoirs" and character.etat=='fatigué':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                character.etat="reposé"
                character.save()
                nouveau_lieu.disponibilite = "libre"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, "Le Stormtrooper s'est reposé aux dortoirs !")
            elif nouveau_lieu==ancien_lieu:
                messages.add_message(request, messages.WARNING, 'Le Stormtrooper est déjà à cet endroit.')
            else :
                print('message')
                messages.add_message(request, messages.ERROR, 'Désolé, vous ne pouvez pas déplacer ce Stormtrooper à cet endroit.')
        return redirect('character_detail', id_character=id_character)
    else:
        form = MoveForm()
        return render(request,
                  'blog/character_detail.html',
                  {'character': character, 'lieu': lieu, 'form': form})