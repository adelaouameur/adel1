from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Le mot de passe correct
SECRET_WORD = "amour"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Récupérer le mot de l'utilisateur
        user_word = request.form.get("word")

        # Vérifier si le mot est correct
        if user_word == SECRET_WORD:
            # Rediriger vers la page du cœur si le mot est correct
            return redirect(url_for("heart"))
        else:
            # Afficher un message d'erreur
            return render_template("index.html", error="Mot incorrect. Veuillez réessayer.")

    return render_template("index.html")


@app.route("/heart")
def heart():
    # Afficher la page du cœur si le mot est correct
    return render_template("heart.html")


if __name__ == "__main__":
    app.run(debug=True)
