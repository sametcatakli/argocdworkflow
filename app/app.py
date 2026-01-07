from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template_string("""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HEH Projet</title>
</head>
<body>
    <div class="content">
        <h1>HEH Projet</h1>
        <p>Tricarico</p>
        <p>Samet</p>
    </div>
</body>
</html>
""")


if __name__ == "__main__":
    app.run(debug=True)
