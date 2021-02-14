import tkinter
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class LieuGeo:
    """Radius of a single point"""
    POINT_RADIUS = 4

    def __init__(self):
        #Gui
        self.main_window = tkinter.Tk()
        self.main_window.title("Lieu géométrique MA/MB=k")

        self.canvas = tkinter.Canvas(self.main_window, width=320, height=240, bg="white")
        self.canvas.grid(row = 0, column = 0, columnspan = 10, rowspan=12)

        textA = tkinter.Label(self.main_window, text="A")
        textA.grid(row=0,column=11)

        textB = tkinter.Label(self.main_window, text="B")
        textB.grid(row=0,column=12)

        textX = tkinter.Label(self.main_window, text="X")
        textX.grid(row=1,column=10)

        textY = tkinter.Label(self.main_window, text="Y")
        textY.grid(row=2,column=10)

        self.entryXA = tkinter.Entry(self.main_window)
        self.entryXA.grid(row = 1, column=11)

        self.entryYA = tkinter.Entry(self.main_window)
        self.entryYA.grid(row = 2, column=11)

        self.entryXB = tkinter.Entry(self.main_window)
        self.entryXB.grid(row = 1, column=12)

        self.entryYB = tkinter.Entry(self.main_window)
        self.entryYB.grid(row = 2, column=12)

        self.textK = tkinter.Label(self.main_window, text="K")
        self.textK.grid(row = 3, column=10)

        self.entryK = tkinter.Entry(self.main_window)
        self.entryK.grid(row = 3, column=11)

        btnDraw = tkinter.Button(self.main_window, text="Dessiner", command=self.draw_all)
        btnDraw.grid(row=4,column=11)
        
        #datas
        self.pointA = Point(0,0)
        self.pointB = Point(0,0)

    def med_case(self):
        a = self.pointA
        b = self.pointB
        middle = Point()
        middle.x = (a.x+b.x)/2
        middle.y = (a.y+b.y)/2
        self.draw_point(middle)

        ap = Point(middle.y-a.y + middle.x, a.x-middle.x+middle.y)
        bp = Point(middle.y-b.y + middle.x, b.x-middle.x+middle.y)
        #self.draw_point(ap)
        #self.draw_point(bp)
        self.canvas.create_line(ap.x, ap.y, bp.x, bp.y, fill="red")

        
    def circle_case(self):
        #On cheche d'abord le barycentre
        bary = Point()
        a = self.pointA
        b = self.pointB
        k = self.k
        alpha = k**2
        beta = 1 - alpha
        bary.x, bary.y = (a.x-alpha*b.x)/beta, (a.y-alpha*b.y)/beta
        ga2 = self.distance_carre(a, bary)
        gb2 = self.distance_carre(b, bary)

        rayon_lg = k*math.sqrt(gb2)
        self.canvas.create_oval(bary.x-rayon_lg, bary.y-rayon_lg, bary.x+rayon_lg, bary.y+rayon_lg, outline="red")

    """Calcule la disance au carre entre 2 points"""
    def distance_carre(self, p1, p2):
        mx, my = p1.x-p2.x, p1.y-p2.y
        return mx**2+my**2

    def update_data(self):
        self.pointA.x = eval(self.entryXA.get())
        self.pointA.y = eval(self.entryYA.get())
        self.pointB.x = eval(self.entryXB.get())
        self.pointB.y = eval(self.entryYB.get())
        self.k = eval(self.entryK.get())

    def draw_point(self, point):
        x = point.x
        y = point.y
        self.canvas.create_oval(x-self.POINT_RADIUS, y-self.POINT_RADIUS, x+self.POINT_RADIUS,y+self.POINT_RADIUS, fill="black")

    def draw_all(self):
        self.update_data()
        self.canvas.delete("all")
        self.draw_point(self.pointA)
        self.draw_point(self.pointB)
        self.canvas.create_line(self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y)
        if self.k == 1:
            self.med_case()
        else:
            self.circle_case()
        
if __name__ == "__main__":
    program = LieuGeo()
    program.main_window.mainloop()
    program.main_window.destroy()