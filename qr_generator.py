import qrcode

properties = qrcode.QRCode(version=1, box_size=50, border=5)
properties.add_data("https://www.linkedin.com/in/adedamola-adekeye/")
properties.make(fit=True)
generate_img = properties.make_image(fill_color="black", back_color="white")
generate_img.save('link.png')
