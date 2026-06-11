from bottle import Bottle, run, request, static_file
import sqlite3

app = Bottle()

# 📦 Création base de données
conn = sqlite3.connect("presence.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS presence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    qr TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# 🏠 Page principale
@app.route("/")
def index():
    return static_file("Gest_abs.html", root="./")

# 📷 Page scan
@app.route("/scan.html")
def scan_page():
    return static_file("scan.html", root="./")

# 📁 Fichiers (css/js)
@app.route("/<filename>")
def server_static(filename):
    return static_file(filename, root="./")

@app.post("/scan")
def scan_qr():
    data = request.json
    qr_code = data.get("qr")

    print("QR reçu :", qr_code)

    # 🔍 Vérifier étudiant
    cursor.execute("SELECT id, nom FROM etudiants WHERE qr = ?", (qr_code,))
    etudiant = cursor.fetchone()

    if etudiant:
        etudiant_id, nom = etudiant

        # 💾 Enregistrer présence
        cursor.execute("INSERT INTO presence (etudiant_id) VALUES (?)", (etudiant_id,))
        conn.commit()

        return {"message": f"{nom} marqué présent ✅"}
    else:
        return {"message": "QR inconnu ❌"}

@app.route("/list")
def list_presence():
    cursor.execute("SELECT * FROM presence")
    data = cursor.fetchall()
    return {"data": data}

@app.route("/presence")
def voir_presence():
    cursor.execute("""
    SELECT etudiants.nom, etudiants.classe, presence.date
    FROM presence
    JOIN etudiants ON presence.etudiant_id = etudiants.id
    """)
    data = cursor.fetchall()

    return {"presence": data}
# ▶️ Lancer serveur
run(app, host="0.0.0.0", port=5000, debug=True)
