import os
from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Page d'accueil avec formulaire pour entrer l'URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        target_url = request.form['url']
        return redirect(url_for('proxy', url=target_url))
    return render_template('form.html')

# Proxy qui prend l'URL et fait la requête HTTP
@app.route('/proxy', methods=['GET'])
def proxy():
    target_url = request.args.get('url')
    
    if target_url is None:
        return "Veuillez fournir une URL en tant que paramètre 'url'. Exemple : /proxy?url=https://example.com"
    
    try:
        # Envoie une requête GET avec suivi des redirections et gestion des erreurs SSL
        response = requests.get(target_url, allow_redirects=True, verify=True)
        return response.text
    except requests.exceptions.SSLError:
        return "Erreur SSL: Impossible de vérifier la connexion sécurisée."
    except requests.exceptions.RequestException as e:
        return f"Une erreur est survenue : {str(e)}"

if __name__ == '__main__':
    # Utilisation de la variable d'environnement PORT, ou 5000 par défaut si non définie
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
