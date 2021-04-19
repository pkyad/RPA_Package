from PIL import Image, ImageDraw, ImageFont

def draw_strike_text(draw, pos, text, font, **options):
    twidth, theight = draw.textsize(text, font=font)
    lx, ly = pos[0], pos[1] + theight
    draw.text(pos, text, font=font, **options)
    draw.line((lx, ly-7, lx + twidth, ly-7), **options)


def text_on_img(productName, rating,mrp,price,txtbgColor):
    im = Image.open('test.png', 'r')
    img_w, img_h = im.size
    #Create text with background
    image = Image.new(mode = "RGB", size = (img_w,110), color = txtbgColor)
    draw = ImageDraw.Draw(image)
    #font style file.ttf , font Size
    fnt = ImageFont.truetype('arial.ttf', 20)

    draw.text((20,15), productName, font=fnt, fill=(255,255,255))
    # draw.text((20,45), mrp, font=fnt, fill=(255,255,255))
    draw.text((20,45), "Price :", font=fnt, fill=(255,255,255))
    draw.text((80,45), price, font=fnt, fill=(255,255,255))
    draw_strike_text(draw, (150, 45), mrp, font=fnt, fill=128)
    draw.text((20,75), rating, font=fnt, fill=(255,255,255))

    #read input image
    img = Image.open('test.png', 'r')
    background = Image.new('RGBA', (img_w,img_h+110), (255, 255, 255, 255))
    bg_w, bg_h = background.size

    offset = (0, 110)
    #paste input image
    background.paste(img, offset)
    #paste Text
    background.paste(image,(0,0))
    # Save output Image
    background.save('deepak.png')

def strikethrough(text):
    return '\u0336'.join(text) + '\u0336'

if __name__ == '__main__':

    text_on_img("Name : Sumsung M31 ","Rating : 8.5/10","19999","16499","black")
