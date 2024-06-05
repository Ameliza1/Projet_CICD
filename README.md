# Projet_CICD
python -m venv venv créer un environnelent virtuel 2eme venv c'est le nom de dossier ce but est de mettre tous les dependences 
venv/Scripts/activate : pour activer l'environnement si ça marche pas execute power bash en tant que admin est exécuter la commande set-exucation...

pip install fastapi uvicorn uvicorn :versionning cela est installer dans le venv

pip freeze >requirement.txt créer un fichier requirement qui contient tous les dependances pour notre projet
requirement contient beaucoup arec qu'on a install fast api qui contient des sous dépendances

exemple si on fait clone d'un projet et qui contient un fichier requirement.txt juste on fait pip install requirement.txt

fastapi dev app/main.py : pour executer la commande


 pip install pipreqs
pipreqs ./ pour
 créer le fichier requirement ,a chaque fois quand ajoute un dependence on fait mise à jour de pireqs cad le requirement

pip install pytest-cov
 pytest --cov=. --cov-report html  pour générer le dossier htmlcov pour voir la coverage de site