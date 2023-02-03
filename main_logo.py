import qrcode
from PIL import Image

url = input("Enter the URL: ")
logo_path = input("Enter the path to the logo image: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=70,
    border=1,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

logo = Image.open(logo_path)
logo_size = int(img.width / 3.58)
logo = logo.resize((logo_size, logo_size))

img_w, img_h = img.size
logo_w, logo_h = logo.size

offset = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
img.paste(logo, offset, logo)

img.save("qrcode_with_logo.png")

print("QR code with logo saved as 'qrcode_with_logo.png'")