def calculatrice():
    historique = []

    while True:
        try:
            num1 = float(input('Entrez le premier nombre : '))
            operateur = input("Entrez l'opérateur (+, -, *, /, %) : ")
            num2 = float(input('Entrez le deuxième nombre : '))

            if operateur == '+':
                resultat = num1 + num2
            elif operateur == '*':
                resultat = num1 * num2
            elif operateur == '%':
                resultat = num1 % num2
            elif operateur == '/':
                if num2 == 0:
                    print('Division par zéro invalide')
                    continue
                else:
                    resultat = num1 / num2
            elif operateur == '-':
                resultat = num1 - num2
            else:
                print('Opérateur invalide')
                continue

            print(resultat)

            # Ajouter à l'historique
            operation = f"{num1} {operateur} {num2} = {resultat}"
            historique.append(operation)

            continuer = input("Voulez-vous effectuer une autre opération ? (o/n) : ").lower()
            if continuer != 'o':
                print("Historique des opérations :")
                for operation in historique:
                    print(operation)
                break

        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
        except ZeroDivisionError:
            print("Erreur : Division par zéro.")
        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    calculatrice()
