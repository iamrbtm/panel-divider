import panelDivider as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# TODO: Add a way to bring panels in from a db
# TODO: bring boards and panels in from a csv 
boards = []
boards.append(pd.Board(width=20, length=40, thickness=.5, name='Rside'))
boards.append(pd.Board(width=20, length=40, thickness=.5, name='Lside'))
boards.append(pd.Board(width=20, length=30, thickness=.5, name='Front'))
boards.append(pd.Board(width=30, length=30, thickness=.5, name='Back'))
boards.append(pd.Board(width=2, length=5, thickness=.5, name='smTest'))
boards.append(pd.Board(width=5, length=7, thickness=.5, name='test'))


panels = []
panels.append(pd.Board(width=48,length=96,thickness=.5,name="half inch plywood"))
# panels.append(pd.Board(width=48, length=96, thickness=.5, name="three quearter plywood"))

div = pd.Divider(boards, panels, 0)

output = div.divide()

panelsUsed = []

for item in output: 
    if item[3] not in panelsUsed:
        panelsUsed.append(item[3])
        
for panel in panelsUsed:
    fig, ax = plt.subplots()
    plt.axis([0,48,0,96])
    
    for o in output:
        if o[3] == panel:
            print("Board \"" + o[1] + "\" #" + str(o[2]) + " on panel \"" + o[3] + "\" #" + str(o[4]) + " at (" + str(o[0].x) + ", " + str(o[0].y) + ", " + str(o[0].w) +", " + str(o[0].h) +")")

            ax.add_patch(Rectangle((o[0].x, o[0].y), o[0].w, o[0].h,EdgeColor='red'))

    plt.savefig('test')