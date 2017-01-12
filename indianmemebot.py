from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
im= Image.open("mainpic.jpg")
width,height=im.size
size=(width,height)
file=Image.new("RGB",(width+20,height+100),"white")
file.paste(im,(10,100))
font= ImageFont.truetype("arial.ttf",26)
draw=ImageDraw.Draw(file)
draw.text((5,0),"This is already working!",(0,0,0),font=font)

file.save("finalmeme.jpg")