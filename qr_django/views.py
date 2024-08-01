# from django.http import HttpResponse
from django.shortcuts import render
import qrcode


def home(req):
    qr_text = ""
    try:
        if req.method == "POST":
            qr_text = req.POST.get("qr_text")
            # img = qrcode.make(qr_text)
            # img.save("static/QR.png")

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                border=1,
            )
            qr.add_data(qr_text)
            qr.make(fit=True)
            img = qr.make_image()
            img.save("static/QR.png")
            print(f"QR Generated for {qr_text}")
    except Exception:
        pass
    return render(req, "index.html", {"qr_text": qr_text})
