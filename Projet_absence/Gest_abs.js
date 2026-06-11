document.getElementById("scan-btn").addEventListener("click", function() {
    const readerDiv = document.getElementById("reader");
    readerDiv.style.display = "block";
    try {
        const html5QrCode = new Html5Qrcode("reader");
        html5QrCode.start(
            { facingMode: "environment" },
            { fps: 10, qrbox: 250 },
            qrCodeMessage => {
                alert("QR détecté : " + qrCodeMessage);
                html5QrCode.stop();
                readerDiv.style.display = "none";
            }
        );
    } 
    catch(err) {
        alert("Erreur: " + err);
        console.error(err);
    }
});
