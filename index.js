const express = require('express');
const cors = require('cors');

//pour que la connection se lance de le depart
const db = require('./config/db');

const app = express();
const PORT = 3000;

//Pour autoriser le front react a fouller API
app.use(cors());

//Permet a Express de lire et comprendre le format JSON
app.use(express.json());

//Une route de test pour verifier que tout fonctionne
app.get('/api/test', (req, res) => {
    res.json({
        statut: "Ok",
        message: "Mon tache fonctionne parfaitement"
    });
});

//Lancer l'ecoute du serveur
app.listen(PORT, () => {
    console.log(`Le serveur tourne sur : http://localhost:${PORT}`);
});