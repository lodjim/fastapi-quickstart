# fastapi-quickstart


## Description

Ce code est un exemple d'implémentation d'un serveur FastAPI en utilisant la bibliothèque FastAPI et uvicorn. Il crée un serveur API avec une route `/heartbit` qui renvoie un objet `HearbitResponse` avec le statut `alive`.

### Fonctionnalités principales

1. Utilise FastAPI pour créer un serveur API.
2. Ajoute une route `/heartbit` qui répond à une requête GET et renvoie un objet `HearbitResponse`.
3. Utilise uvicorn pour lancer le serveur avec la configuration donnée.
4. Gère les arguments en ligne de commande pour définir l'hôte et le port du serveur.

### Comment l'utiliser

- Installez les dépendances nécessaires, comme FastAPI et uvicorn.
- Exécutez le script avec les arguments optionnels `--host` et `--port` pour définir l'hôte et le port du serveur (par défaut, ils sont respectivement "0.0.0.0" et 8080).

### Exemple d'utilisation

Pour lancer le serveur avec les paramètres par défaut, exécutez simplement le script :

```bash
    python api.py --host 127.0.0.1 --port 5000
```