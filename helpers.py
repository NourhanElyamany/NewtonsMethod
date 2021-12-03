authers ="""Nourhan Elyamany
Mohamed Osama
Karim Kohel
Amr Mekki
Omar Tamer
Youssef Saed
Aly Khaled"""

def cleanInput(expr, xi, iterations, errorGiven):
    expr = expr.replace("^", "**")
    expr = expr.replace("X", 'x')
    xi = float(xi)
    iterations = int(iterations)

    if not errorGiven:
        errorGiven=0
    errorGiven = float(errorGiven)
    return expr, xi, iterations, errorGiven

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