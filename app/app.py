from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Cette page est maintenant la porte d'entrée avec le bouton vers ArgoCD
    return render_template_string('''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project ArgoCD 1</title>
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
        .card {
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 { color: #2c3e50; margin-bottom: 20px; }
        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: #e8590c;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            transition: background 0.3s;
        }
        .btn:hover { background: #fc8621; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Project ArgoCD 1</h1>
        <p>Hello, World! updated 3</p>
        <br>
        <a href="/argocd" class="btn">Voir le guide ArgoCD</a>
    </div>
</body>
</html>
''')
@app.route("/argocd")
def argocd():
    return render_template_string('''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArgoCD - Guide Complet</title>
    <style>
        * {
            margin: 0; 
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

                                  
                                  
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }

        header {
            background: linear-gradient(135deg, #e8590c 0%, #fc8621 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }

        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .content {
            padding: 40px;
        }

        .section {
            margin-bottom: 35px;
        }

        .section h2 {
            color: #e8590c;
            font-size: 1.8em;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 3px solid #fc8621;
        }

        .section h3 {
            color: #667eea;
            font-size: 1.4em;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .section p {
            margin-bottom: 15px;
            text-align: justify;
        }

        .highlight {
            background-color: #fff3e0;
            padding: 20px;
            border-left: 4px solid #e8590c;
            margin: 20px 0;
            border-radius: 5px;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .feature-card h4 {
            color: #667eea;
            margin-bottom: 10px;
        }

        footer {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
        }

        .back-link {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s ease;
        }

        .back-link:hover {
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 ArgoCD</h1>
            <p>GitOps Continuous Delivery pour Kubernetes</p>
        </header>

        <div class="content">
            <div class="section">
                <h2>Qu'est-ce qu'ArgoCD ?</h2>
                <p>
                    ArgoCD est un outil de livraison continue (CD) déclaratif et basé sur GitOps pour Kubernetes. 
                    Il permet d'automatiser le déploiement d'applications sur des clusters Kubernetes en utilisant 
                    Git comme source de vérité unique pour les configurations d'infrastructure et d'application.
                </p>
                <div class="highlight">
                    <strong>Philosophie GitOps :</strong> Toute la configuration de votre infrastructure est stockée 
                    dans Git, et ArgoCD synchronise automatiquement l'état du cluster avec celui défini dans les dépôts Git.
                </div>
            </div>

            <div class="section">
                <h2>Fonctionnalités principales</h2>
                <div class="features">
                    <div class="feature-card">
                        <h4>🔄 Synchronisation automatique</h4>
                        <p>Détecte et applique automatiquement les changements depuis Git vers Kubernetes.</p>
                    </div>
                    <div class="feature-card">
                        <h4>🎯 Déclaratif</h4>
                        <p>Gestion déclarative des applications avec support de Helm, Kustomize, et manifestes YAML.</p>
                    </div>
                    <div class="feature-card">
                        <h4>👁️ Visualisation</h4>
                        <p>Interface utilisateur web intuitive pour visualiser l'état des applications et des ressources.</p>
                    </div>
                    <div class="feature-card">
                        <h4>🔐 Sécurité</h4>
                        <p>Contrôle d'accès basé sur les rôles (RBAC) et intégration SSO.</p>
                    </div>
                    <div class="feature-card">
                        <h4>📊 Multi-cluster</h4>
                        <p>Gestion de plusieurs clusters Kubernetes depuis une seule instance ArgoCD.</p>
                    </div>
                    <div class="feature-card">
                        <h4>↩️ Rollback</h4>
                        <p>Retour en arrière facile vers des versions précédentes en quelques clics.</p>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>Comment ça fonctionne ?</h2>
                <h3>1. Définition de l'application</h3>
                <p>
                    Vous créez une ressource "Application" dans ArgoCD qui pointe vers un dépôt Git contenant 
                    vos manifestes Kubernetes. Cette ressource définit la source (le dépôt Git) et la destination 
                    (le cluster et le namespace Kubernetes).
                </p>

                <h3>2. Surveillance continue</h3>
                <p>
                    ArgoCD surveille en permanence le dépôt Git spécifié. Lorsqu'un changement est détecté 
                    (nouveau commit), ArgoCD compare l'état souhaité (Git) avec l'état actuel du cluster.
                </p>

                <h3>3. Synchronisation</h3>
                <p>
                    Si des différences sont détectées, ArgoCD peut automatiquement (ou manuellement selon la configuration) 
                    synchroniser le cluster pour qu'il corresponde à l'état défini dans Git. Cela garantit que votre 
                    cluster est toujours à jour avec votre code.
                </p>
            </div>

            <div class="section">
                <h2>Avantages d'ArgoCD</h2>
                <p><strong>Traçabilité :</strong> Chaque changement est versionné dans Git avec un historique complet.</p>
                <p><strong>Récupération rapide :</strong> En cas de problème, revenir à une version précédente est simple et rapide.</p>
                <p><strong>Standardisation :</strong> Même processus de déploiement pour toutes les équipes et environnements.</p>
                <p><strong>Audit :</strong> Visibilité complète sur qui a déployé quoi et quand.</p>
                <p><strong>Collaboration :</strong> Les équipes utilisent les workflows Git familiers (pull requests, code review).</p>
            </div>

            <div class="section">
                <h2>Cas d'usage</h2>
                <p>
                    ArgoCD est idéal pour les équipes qui gèrent des applications sur Kubernetes et souhaitent 
                    automatiser leurs déploiements tout en maintenant un contrôle strict sur les changements. 
                    Il est particulièrement utile dans les environnements multi-clusters et pour les architectures 
                    microservices où de nombreuses applications doivent être déployées et mises à jour régulièrement.
                </p>
            </div>

            <a href="/" class="back-link">← Retour à l'accueil</a>
        </div>

        <footer>
            <p>ArgoCD - GitOps made easy | © 2024</p>
        </footer>
    </div>
</body>
</html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)