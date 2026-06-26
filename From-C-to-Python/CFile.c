#include <stdio.h>
#include <string.h>

#define MAX_ETUDIANTS 50
#define MAX_NOM 50

typedef struct {
    char nom[MAX_NOM];
    float notes[3];
    char mention[20];
} Etudiant;

float calculer_moyenne(float notes[], int nb) {
    float somme = 0;
    for (int i = 0; i < nb; i++) somme += notes[i];
    return somme / nb;
}

void attribuer_mention(Etudiant *e) {
    float moy = calculer_moyenne(e->notes, 3);
    if (moy >= 16.0)       strcpy(e->mention, "Très bien");
    else if (moy >= 14.0)  strcpy(e->mention, "Bien");
    else if (moy >= 12.0)  strcpy(e->mention, "Assez bien");
    else if (moy >= 10.0)  strcpy(e->mention, "Passable");
    else                   strcpy(e->mention, "Ajourné");
}

void afficher_etudiant(Etudiant e) {
    float moy = calculer_moyenne(e.notes, 3);
    printf("%s — Moyenne : %.2f — %s\n", e.nom, moy, e.mention);
}

int main() {
    Etudiant etudiants[MAX_ETUDIANTS];
    int nb = 0;

    // Ajout manuel
    strcpy(etudiants[0].nom, "Alice");
    etudiants[0].notes[0] = 17.5;
    etudiants[0].notes[1] = 15.0;
    etudiants[0].notes[2] = 18.0;
    attribuer_mention(&etudiants[0]);
    nb++;

    strcpy(etudiants[1].nom, "Bob");
    etudiants[1].notes[0] = 9.0;
    etudiants[1].notes[1] = 11.5;
    etudiants[1].notes[2] = 8.0;
    attribuer_mention(&etudiants[1]);
    nb++;

    strcpy(etudiants[2].nom, "Charlie");
    etudiants[2].notes[0] = 13.0;
    etudiants[2].notes[1] = 12.5;
    etudiants[2].notes[2] = 14.0;
    attribuer_mention(&etudiants[2]);
    nb++;

    // Affichage
    printf("=== Résultats ===\n");
    for (int i = 0; i < nb; i++) {
        afficher_etudiant(etudiants[i]);
    }

    // Meilleur étudiant
    int best = 0;
    for (int i = 1; i < nb; i++) {
        if (calculer_moyenne(etudiants[i].notes, 3) >
            calculer_moyenne(etudiants[best].notes, 3)) {
            best = i;
        }
    }
    printf("\nMeilleur étudiant : %s\n", etudiants[best].nom);

    return 0;
}