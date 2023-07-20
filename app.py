# Import qrcode package
import qrcode

qr = qrcode.QRCode(version=10,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=3)

qr.add_data("https://www.linkedin.com/in/appan-merari/")
qr.make(fit=True)

img = qr.make_image(fill_color="darkblue", back_color="white")
img.save("profile1.png")