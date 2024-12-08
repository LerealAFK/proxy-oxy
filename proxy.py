from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Page d'accueil avec formulaire pour entrer l'URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        target_url = request.form['url']
        return redirect(url_for('proxy', url=target_url))
    return render_template('form.html')  # Utilisation de render_template pour charger form.html depuis le dossier templates

# Proxy qui prend l'URL et fait la requête HTTP
@app.route('/proxy', methods=['GET'])
def proxy():
    target_url = request.args.get('url')
    
    if target_url is None:
        return "Veuillez fournir une URL en tant que paramètre 'url'. Exemple : /proxy?url=https://example.com"
    
    response = requests.get(target_url)
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
