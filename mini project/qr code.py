import qrcode

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=20,
                 border=2)

qr.add_data("https://www.charusat.ac.in/")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("my fifth try.png")
