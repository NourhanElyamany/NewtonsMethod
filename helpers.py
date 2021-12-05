authers ="""Nourhan Elyamany
Mohamed Osama
Karim Kohel
Aly Khaled
Amr Mekki
Omar Tamer
Youssef Saed"""

def cleanInput(expr):
    expr = expr.replace("^", "**")
    expr = expr.replace("X", 'x')
    return expr

class Holder():
    def __init__(self) -> None:
        pass

    def setTable(self, table, tableName):
        self.table = table
        self.tableName = tableName
    def setPlot(self, plot, plotName):
        self.plot = plot
        self.plotName = plotName
    

    def saveTable(self):
        self.table.savefig(self.tableName, format='png')

    def savePlot(self):
        self.plot.savefig(self.plotName, format='png')