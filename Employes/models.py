from django.db import models

class Department(models.Model):
       nom = models.CharField(max_length=100, verbose_name="Nom du département")
       description = models.TextField(blank=True, verbose_name="Description")

       def __str__(self):
           return self.nom

       class Meta:
           verbose_name = "Département"
           verbose_name_plural = "Départements"

class Poste(models.Model):
       nom = models.CharField(max_length=100, verbose_name="Nom du poste")
       description = models.TextField(blank=True, verbose_name="Description")

       def __str__(self):
           return self.nom

       class Meta:
           verbose_name = "Poste"
           verbose_name_plural = "Postes"

class Employee(models.Model):
       SEXE_CHOICES = [
           ('H', 'Homme'),
           ('F', 'Femme'),
           ('A', 'Autre'),
       ]
       prenom = models.CharField(max_length=50, verbose_name="Prénom")
       nom = models.CharField(max_length=50, verbose_name="Nom")
       email = models.EmailField(unique=True, verbose_name="Email")
       date_embauche = models.DateField(verbose_name="Date d'embauche")
       salaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salaire")
       departement = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employes', verbose_name="Département")
       poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name='employes', verbose_name="Poste")
       sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, verbose_name="Sexe")
       est_actif = models.BooleanField(default=True, verbose_name="Actif")

       def __str__(self):
           return f"{self.prenom} {self.nom}"

# === NOUVEAU : Gestion des Congés ===
class Conge(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employé")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    motif = models.CharField(max_length=200, verbose_name="Motif")
    statut = models.CharField(
        max_length=20,
        choices=[
            ('EN_ATTENTE', 'En attente'),
            ('APPROUVE', 'Approuvé'),
            ('REFUSE', 'Refusé')
        ],
        default='EN_ATTENTE',
        verbose_name="Statut"
    )
    date_demande = models.DateTimeField(auto_now_add=True, verbose_name="Date de demande")

    class Meta:
        verbose_name = "Congé"
        verbose_name_plural = "Congés"

    def __str__(self):
        return f"{self.employe} - {self.motif} ({self.statut})"


# === NOUVEAU : Gestion des Primes ===
class Prime(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employé")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant (FCFA)")
    motif = models.CharField(max_length=200, verbose_name="Motif de la prime")
    date_attribution = models.DateField(auto_now_add=True, verbose_name="Date d'attribution")

    class Meta:
        verbose_name = "Prime"
        verbose_name_plural = "Primes"

    def __str__(self):
        return f"Prime de {self.montant} FCFA - {self.employe}"
    class Meta:
           verbose_name = "Employé"
           verbose_name_plural = "Employés"