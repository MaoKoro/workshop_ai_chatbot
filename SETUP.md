# Configuration de l'environnement pour le projet de détection de spam dans les e-mails

## Initialisation de l'environnement virtuel Python

1. Assurez-vous d'avoir Python installé sur votre système.

2. Ouvrez un terminal et naviguez jusqu'au répertoire de votre projet.

3. Utilisez la commande suivante pour créer un environnement virtuel nommé "workshop_AI" :

    ```bash
    python -m venv workshop_AI
    ```
    ou
    ```bash
    python3 -m venv workshop_AI
    ```

4. Activez l'environnement virtuel en exécutant la commande appropriée selon votre système d'exploitation :

    - Sur Windows :

    ```bash
    workshop_AI\Scripts\activate
    ```

    - Sur macOS/Linux :

    ```bash
    source workshop_AI/bin/activate
    ```

## Installation des bibliothèques nécessaires

1. Une fois l'environnement virtuel activé, utilisez pip pour installer les bibliothèques suivantes :

    ```bash
    pip install ipykernel scikit-learn numpy pandas matplotlib tensor-sensor
    ```

## Accès à Jupyter Notebook

1. Assurez-vous que votre environnement virtuel est toujours activé.

2. Installez Jupyter Notebook en exécutant la commande suivante :

    ```bash
    pip install jupyter
    ```

3. Lancez Jupyter Notebook en exécutant la commande suivante :

    ```bash
    jupyter notebook
    ```

> Assurez vous que votre code Jupyter s'éxecute bien dans votre venv.

4. Votre navigateur par défaut devrait s'ouvrir, affichant l'interface de Jupyter Notebook. Vous pouvez maintenant créer de nouveaux notebooks et commencer à travailler sur votre projet de détection de spam dans les e-mails. Vous pouvez aussi y accéder depuis VSCode avec l'extension Jupyter
