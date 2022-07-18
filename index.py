import pyqrcode
import png

link = ("digitisetechno.in")
qr_code = pyqrcode.create(link)
qr_code.png("Qr.png", scale=5)
 