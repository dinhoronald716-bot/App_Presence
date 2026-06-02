const { Pool } = require('pg');

//Configuraton des identifiants de la base de donnees
const pool = new Pool({
    user: 'postgres', //Verifier nw ty bro
    host: 'localhost', //base de donnee tourne sur le meme machine
    database: 'emit_db', //Verifier sw fw ts i nom napaitraka nw agn
    password: 'votre_mot_de_passe', // mot de pass nw 
    port: 5432, //port par defaut de PostgreSQL
});

//Tester la connection au demarrage
pool.connect((err, client, release) => {
    if (err) {
        return console.error('Erreur de connection a PostgreSql:', err.stack);
    }
    console.log('Connection reussie a la base de donnees Postgresql !');
    release();
});

module.exports = {
    query: (text, params) => pool.query(text, params),
};