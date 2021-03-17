import panelDivider as pd
from PIL import Image, ImageDraw, ImageFont

# TODO: Add a way to bring panels in from a db
# TODO: bring boards and panels in from a csv 
boards = []
boards.append(pd.Board(width=20, length=40, thickness=.5, name='Rside'))
boards.append(pd.Board(width=20, length=40, thickness=.5, name='Lside'))
boards.append(pd.Board(width=20, length=30, thickness=.75, name='Front'))
boards.append(pd.Board(width=20, length=30, thickness=.75, name='Back'))


panels = []
panels.append(pd.Board(width=48,length=96,thickness=.5,name="half inch plywood"))
panels.append(pd.Board(width=48, length=96, thickness=.75, name="three quearter plywood"))

div = pd.Divider(boards, panels, 0)

output = div.divide()

panelsUsed = []

for item in output: 
    if item[3] not in panelsUsed:
        panelsUsed.append(item[3])
        
for panel in panelsUsed:
    im = Image.new('RGB', ((panels[0].length*2), (panels[0].width)*2), (128, 128, 128))
    draw = ImageDraw.Draw(im)
    
    for o in output:
        if o[3] == panel:
            print("Board \"" + o[1] + "\" #" + str(o[2]) + " on panel \"" + o[3] + "\" #" + str(o[4]) + " at (" + str(o[0].x) + ", " + str(o[0].y) + ", " + str(o[0].w) +", " + str(o[0].h) +")")

            draw.rectangle((o[0].x*2, o[0].y*2, o[0].h*2, o[0].w*2), fill=(0, 192, 192), outline=(255, 255, 255))
            font = ImageFont.load_default()
            draw.text((o[0].x*2+2, o[0].y*2+2), str(o[0].h) + "," + str(o[0].w), font=font)

    im.save(panel+'_imagedraw.jpg', quality=95)