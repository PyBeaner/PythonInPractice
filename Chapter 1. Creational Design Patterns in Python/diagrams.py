__author__ = 'PyBeaner'

class DiagramFactory:

    def make_diagram(self,width,height):
        return Diagram(width,height)

    def make_rectangle(self,x,y,width,height,fill="white",stroke="black"):
        return Rectangle(x,y,width,height,fill,stroke)

    def make_text(self,x,y,text,fontsize=12):
        return Text(x,y,text,fontsize)


class SvgDiagramFactory(DiagramFactory):
    def make_diagram(self,width,height):
        return SvgDiagram(width,height)

class Text:
    def __init__(self,x,y,text,fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]

SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

SVG_SCALE = 20

class SvgText:
    def __init__(self,x,y,text,fontsize):
        x*=SVG_SCALE
        y*=SVG_SCALE
        fontsize*=SVG_SCALE
        self.svg = SVG_TEXT.format(**locals())

class Diagram:
    def add(self,component):
        for y,row in enumerate(component.rows):
            for x,char in enumerate(row):
                self.diagram[y+component.y][x+component.x] = char

class SvgDiagram:
    def add(self,component):
        self.diagram.append(component.svg)


def main():
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory())
    svgDiagram.save(svgFilename)

def create_diagram(factory):
    diagram = factory.make_diagram(30,7)
    rectangle = factory.make_rectangle(4,1,22,5,"yellow")
    text = factory.make_text(7,3,"Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram
