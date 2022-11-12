import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UCzI9taV9XGu8CPa90KJ-eCg")
img.save("AnshulGupta_Youtube.png")