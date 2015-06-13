__author__ = 'PyBeaner'

# avoid name conflicts
class DiagramFactory:
    @classmethod
    def make_diagram(cls,width,height):
        return cls.Diagram(width,height)

    @classmethod
    def make_rectangle(cls,x,y,width,height,fill="white",stroke="black"):
        return cls.Rectangle(x,y,width,height,fill,stroke)

    @classmethod
    def make_text(cls,x,y,text,fontsize=12):
        return cls.Text(x,y,text,fontsize)

    class Diagram:
        def add(self,component):
            for y,row in enumerate(component.rows):
                for x,char in enumerate(row):
                    self.diagram[y+component.y][x+component.x] = char

    class Text:
        def __init__(self,x,y,text,fontsize):
            self.x = x
            self.y = y
            self.rows = [list(text)]


class SvgDiagramFactory(DiagramFactory):

    SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
    font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

    SVG_SCALE = 20

    class Diagram:
        def add(self,component):
            self.diagram.append(component.svg)

    class Text:
        def __init__(self,x,y,text,fontsize):
            x*=SvgDiagramFactory.SVG_SCALE
            y*=SvgDiagramFactory.SVG_SCALE
            fontsize*=SvgDiagramFactory.SVG_SCALE
            self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())


def main():
    # no need to create the factory instances
    txtDiagram = create_diagram(DiagramFactory)
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)

def create_diagram(factory):
    diagram = factory.make_diagram(30,7)
    rectangle = factory.make_rectangle(4,1,22,5,"yellow")
    text = factory.make_text(7,3,"Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram
