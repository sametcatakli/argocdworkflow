from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template_string('''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HEH Projet</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f0f2f5;
            text-align: center;
        }
        .content {
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 { 
            color: #2c3e50; 
            margin-bottom: 20px; 
            font-size: 2.5em;
        }
        p {
            color: #555;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>HEH Projet</h1>
        <p>Tricarico</p>
    </div>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(debug=True)