from PIL import Image
import qrcode

def create_new_shirt(url):
	img = Image.open("ponzi_base.png")
	new_qr = qrcode.make(url)
	new_qr.save('qr_code.png')

	img2 = Image.open("qr_code.png")
	img.paste(img2, (300,500))
	img.show()