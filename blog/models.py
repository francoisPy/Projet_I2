from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip
 
 
class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    ETAT_CHOIX=[("reposé","reposé"),("pret","pret"),("a faim","a faim"),("rassasié","rassasié"),("fatigué","fatigué")]
    etat = models.CharField(max_length=200,choices=ETAT_CHOIX)
    CLASSE_CHOIX=[("Stormtrooper","Stormtrooper"),("Death trooper","Death trooper"),("Magma trooper","Magma trooper"),("Night trooper","Night trooper"),("Purge trooper","Purge trooper"),("Sand trooper","Sand trooper"),("Scout trooper","Scout trooper"),("Shoretrooper","Shoretrooper"),("Snowtrooper","Snowtrooper"),("Shock trooper","Shock trooper")]
    classe = models.CharField(max_length=200,choices=CLASSE_CHOIX)
    GRADE_CHOIX=[("Stormtrooper","Stormtrooper"),("Caporal","Caporal"),("Sergent","Sergent"),("Squad leader","Squad leader"),("ARC Trooper","ARC trooper"),("Officier","Officier"),("Général","Général")]
    grade = models.CharField(max_length=200,choices=GRADE_CHOIX)
    precision = models.IntegerField(default=1,validators=[MinValueValidator(0), MaxValueValidator(100)])
    PHOTO_CHOIX=[('https://static.wikia.nocookie.net/frstarwars/images/6/61/Un_Stormtrooper.png/revision/latest?cb=20221112210508','https://static.wikia.nocookie.net/frstarwars/images/6/61/Un_Stormtrooper.png/revision/latest?cb=20221112210508'),('https://static.wikia.nocookie.net/frstarwars/images/c/c3/Death_trooper.png/revision/latest?cb=20161110201800','https://static.wikia.nocookie.net/frstarwars/images/c/c3/Death_trooper.png/revision/latest?cb=20161110201800'),('https://static.wikia.nocookie.net/frstarwars/images/b/b8/Magma_trooper.png/revision/latest?cb=20230729160506','https://static.wikia.nocookie.net/frstarwars/images/b/b8/Magma_trooper.png/revision/latest?cb=20230729160506'),('https://static.wikia.nocookie.net/frstarwars/images/0/04/Soldat_de_la_Nuit.png/revision/latest?cb=20230928080045','https://static.wikia.nocookie.net/frstarwars/images/0/04/Soldat_de_la_Nuit.png/revision/latest?cb=20230928080045'),('https://static.wikia.nocookie.net/frstarwars/images/d/d9/Purge_Trooper_JFO.png/revision/latest?cb=20190414095300','https://static.wikia.nocookie.net/frstarwars/images/d/d9/Purge_Trooper_JFO.png/revision/latest?cb=20190414095300'),('https://static.wikia.nocookie.net/frstarwars/images/7/78/Sandtrooper_DICE.png/revision/latest?cb=20230729160403','https://static.wikia.nocookie.net/frstarwars/images/7/78/Sandtrooper_DICE.png/revision/latest?cb=20230729160403'),('https://static.wikia.nocookie.net/frstarwars/images/7/72/Scout_trooper.png/revision/latest?cb=20230729160529','https://static.wikia.nocookie.net/frstarwars/images/7/72/Scout_trooper.png/revision/latest?cb=20230729160529'),('https://static.wikia.nocookie.net/frstarwars/images/b/bd/Shoretrooper.png/revision/latest?cb=20160930154701','https://static.wikia.nocookie.net/frstarwars/images/b/bd/Shoretrooper.png/revision/latest?cb=20160930154701'),('https://static.wikia.nocookie.net/frstarwars/images/f/f4/Snowtrooper.png/revision/latest?cb=20230729160411','https://static.wikia.nocookie.net/frstarwars/images/f/f4/Snowtrooper.png/revision/latest?cb=20230729160411'),('https://static.wikia.nocookie.net/frstarwars/images/0/09/Shock_trooper_Imp%C3%A9rial.png/revision/latest?cb=20230729160551','https://static.wikia.nocookie.net/frstarwars/images/0/09/Shock_trooper_Imp%C3%A9rial.png/revision/latest?cb=20230729160551')]
    photo = models.CharField(max_length=200,choices=PHOTO_CHOIX)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_character