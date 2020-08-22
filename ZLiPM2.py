from GUI_ZLiPM import *

def signalsZL(self):
    self.ZL_sprawdz.clicked.connect(self.calcZL)

def signalsPM(self):
    self.PM_sprawdz.clicked.connect(self.calcPM)


def calcZL(self):
    a2=self.ZL_wysokosc_budynku.text()
    wysokosc=float(a2.replace(",","."))
    b2=self.ZL_ilosc_kondygnacji.text()
    kondygnacje=int(b2.replace(",","."))
    c2 = self.ZL_poziom_stropu.text()
    pierwszaKondygnacja = float(c2.replace(",", "."))
    zl2=self.zagrozenia_ludzmi.currentText()
    if zl2=="ZL I":
        zl=1
    elif zl2=="ZL II":
        zl=2
    elif zl2=="ZL III":
        zl=3
    elif zl2=="ZL IV":
        zl=4
    elif zl2=="ZL V":
        zl=5

    if wysokosc < 12.0 and kondygnacje < 5:
        grupa_wysokosciowa="Niski (N)"
        bu = 0
    elif wysokosc < 25.0 and kondygnacje < 10:
        grupa_wysokosciowa="Średniowysokie (SW)"
        bu = 1
    elif wysokosc < 55.0 and kondygnacje < 19:
        grupa_wysokosciowa="Wysokie (W)"
        bu = 2
    else:
        grupa_wysokosciowa="Wysokościowe (WW)"
        bu = 3

    a = [["B", "B", "C", "D", "C"], ["B", "B", "B", "C", "B"], ["B", "B", "B", "B", "B"], ["A", "A", "A", "B", "A"]]

    # sprawdzenie czy mozna obnizyc kategorie
    if (kondygnacje <= 2 and wysokosc < 12.0 and (zl == 1 or zl == 2 or zl == 3)):
        if (kondygnacje == 1 and pierwszaKondygnacja <= 9.0):
            if zl == 1:
                ostatnia = "D"
            elif zl == 2:
                ostatnia = "D"
            elif zl == 3:
                ostatnia = "D"
            else:
                print("Nie moża obniżyć klasy.")
        elif (kondygnacje == 2 and pierwszaKondygnacja <= 9.0):
            if zl == 1:
                ostatnia = "C"
            elif zl == 2:
                ostatnia = "C"
            elif zl == 3:
                ostatnia = "D"
            else:
                print("Nie moża obniżyć klasy.")
        else:
            print("Coś poszło nie tak.")
    else:
        ostatnia="-"

    spr=a[bu][zl-1]

    self.Wynik.setHtml('<p style="text-align:center;font-size:30px;color:green;">Kategoria obiektu: '+spr+'<p style="text-align:center;font-size:18px;color:green;">Można obniżyć do klasy: '+ostatnia+'<p style="text-align:center;font-size:15px;color:black;">Grupa wysokościowa: '+grupa_wysokosciowa)

    if spr=="A":
        zmiana_tablicy=1
    elif spr=="B":
        zmiana_tablicy=2
    elif spr=="C":
        zmiana_tablicy=3
    elif spr=="D":
        zmiana_tablicy=4
    elif spr=="E":
        zmiana_tablicy=5
    else:
        zmiana_tablicy=0

    self.Tablica.setCurrentIndex(zmiana_tablicy)

def calcPM(self):
    e2 = self.PM_gestosc_obciazenia_ogniowego.text()
    pm_gestosc_obciazenia_ogniowego=float(e2.replace(",","."))
    f2 = self.PM_ilosc_kondygnacji.text()
    pm_ilosc_kondygnacji=float(f2.replace(",","."))
    g2 = self.PM_wysokosc_budynku.text()
    pm_wysokosc_budynku=float(g2.replace(",","."))

    if pm_ilosc_kondygnacji<2:
        grupa_wysokosciowa_pm="Budynek o jednej kondygnacji(bez ograniczeń wysokośći)"
        bu = 0
    elif pm_wysokosc_budynku<12.0 and pm_ilosc_kondygnacji<5:
        grupa_wysokosciowa_pm="Niski (N)"
        bu = 1
    elif pm_wysokosc_budynku<25.0 and pm_ilosc_kondygnacji<10:
        grupa_wysokosciowa_pm="Średniowysokie (SW)"
        bu = 2
    elif pm_wysokosc_budynku<55.0 and pm_ilosc_kondygnacji<19:
        grupa_wysokosciowa_pm="Wysokie (W)"
        bu = 3
    else:
        grupa_wysokosciowa_pm="Wysokościowe (WW)"
        bu = 4

    a= [["E", "D", "C", "B", "B"],["D", "D", "C", "B", "B"],["C", "C", "C", "B", "B"],["B", "B", "B", "*", "*"],["A", "A", "A", "*", "*"]]
    to=[["R 240", "R 30", "REI 120", "EI 120 (O<->I)", "EI 60", "RE 30"],["R 120", "R 30", "REI 60", "EI 60 (O<->I)", "EI 30 (4.)", "RE 30"],["R 60", "R 15", "REI 60", "EI 30 (O<->I)", "EI 15 (4.)", "RE 15"],["R 30", "(-)", "REI 30", "EI 30 (O<->I)", "(-)", "(-)"],["(-)", "(-)", "(-)", "(-)", "(-)", "(-)", ]]

    if pm_gestosc_obciazenia_ogniowego<=500.0:
        wgo=0
    elif pm_gestosc_obciazenia_ogniowego<=1000.0:
        wgo=1
    elif pm_gestosc_obciazenia_ogniowego<=2000.0:
        wgo=2
    elif pm_gestosc_obciazenia_ogniowego<=4000.0:
        wgo=3
    else:
        wgo=4
    spr_pm=a[wgo][bu]

    self.Wynik.setHtml(
    '<p style="text-align:center;font-size:30px;color:green;">Kategoria obiektu: ' + spr_pm + '<p style="text-align:center;font-size:15px;color:black;">Grupa wysokościowa: ' + grupa_wysokosciowa_pm)
    if spr_pm == "A":
        zmiana_tablicy_pm = 1
    elif spr_pm == "B":
        zmiana_tablicy_pm = 2
    elif spr_pm == "C":
        zmiana_tablicy_pm = 3
    elif spr_pm == "D":
        zmiana_tablicy_pm = 4
    elif spr_pm == "E":
        zmiana_tablicy_pm = 5
    else:
        zmiana_tablic_pm = 0

    self.Tablica.setCurrentIndex(zmiana_tablicy_pm)


Ui_Dialog.signalsZL=signalsZL
Ui_Dialog.calcZL=calcZL
Ui_Dialog.signalsPM=signalsPM
Ui_Dialog.calcPM=calcPM

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QDialog()
    ui=Ui_Dialog()
    ui.setupUi(Dialog)
    ui.signalsPM()
    ui.signalsZL()
    Dialog.show()
    sys.exit(app.exec_())

# kategoria A
#
# <TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 240</TD><TR><TD>-Konstrukcja dachu:</TD><TD>R 30</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 120</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 120 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>EI 60 (4.)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>RE 30</TD></TR></TABLE>
#
# kategoria B
#
# <TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 120</TD><TR><TD>-Konstrukcja dachu:</TD><TD>R 30</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 60</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 60 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>EI 30 (4.)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>RE 30</TD></TR></TABLE>
#
# kategoria C
#
# <TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 60</TD><TR><TD>-Konstrukcja dachu:</TD><TD>R15</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 60</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 30 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>EI 15 (4.)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>RE 15</TD></TR></TABLE>
#
# kategoria D
#
# <TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 30</TD><TR><TD>-Konstrukcja dachu:</TD><TD>(-)</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 30</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 30 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>(-)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>(-)</TD></TR></TABLE>
#
# kategoria E
#
# <TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>(-)</TD><TR><TD>-Konstrukcja dachu:</TD><TD>(-)</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>(-)</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>(-)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>(-)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>(-)</TD></TR></TABLE>