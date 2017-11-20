co2minimum=350
class Svet:
    zoznam_objektov=[]
    aktualny_cas=0
    def __init__(self,meno):
        self.meno=meno
        self.teplotaVzduchu=20
        self.co2=co2minimum
        self.aktualny_cas=0
        print("Novy svet",self.meno,"teplota:",self.teplotaVzduchu,"C a co2 je",self.co2,"ppm")
    def pridaj(self,objekt):
        print("pridal",objekt.meno,"do sveta")
        self.zoznam_objektov.append(objekt)
    def krok_casu(self):
        print("krok casu svet (cas",self.aktualny_cas,")")
        for priestor in self.zoznam_objektov:
            priestor.krok_casu()
    def bez(self,cas):
        zaciatocny_cas=self.aktualny_cas
        while (self.aktualny_cas < (zaciatocny_cas+cas)):
            self.krok_casu()
            self.aktualny_cas += 1

class Priestor(object):
    meno=""
    objem=0
    teplotaVzduchu=0
    co2=0
    zoznam_objektov=[]
    def __init__(self,meno,objem=0):
        self.meno=meno
        self.objem=self.objem+objem
        self.teplotaVzduchu = 0
        self.co2 = 0
        self.zoznam_objektov=[]

    def stav(self):
        #self.objem=self.sucetObjemov()
        #print("Priestor",self.meno,"o objeme",self.objem,"m3 je",self.teplotaVzduchu, "C a", self.co2,"ppm a obsahuje tieto priestory:")
        for objekt in self.zoznam_objektov:
            print("v",self.meno,"je",objekt.meno)
            objekt.stav()

    def pridaj(self,objekt):
        print("pridal", objekt.meno, "do", self.meno)
        self.zoznam_objektov.append(objekt)

    def sucetObjemov(self):
        self.objem=0
        for izba in self.zoznam_objektov:
            self.objem=self.objem+izba.objem
        print("spolu",self.objem)

    def krok_casu(self):
        print("krok_casu",self.meno)
        for objekt in self.zoznam_objektov:
            objekt.krok_casu()

class Clovek:
    meno=""
    def __init__(self,meno):
        self.meno=meno
        print("Novy clovek!")
    def dychaj(self):
        # jeden 80kg clovek spravi 240kg co2/rok 27g/hodinu  0.46g/minutu
        print("este neviem ako dychat")
    def krok_casu(self):
        self.dychaj()
    def stav(self):
        print(self.meno,"zijem")

class CO2meter:
    umiestnenie="nezname"
    stav=0
    def __init__(self,priestor):
        self.umiestnenie=priestor
        self.stav=co2minimum
        print("Novy CO2 meter v priestore",self.umiestnenie.meno,"nastaveny na", self.stav)
    def citaj(self):
        print("CO2meter",self.umiestnenie.meno,"precital",self.stav,'ppm')
    def krok_casu(self):
        self.citaj()

svet=Svet("svet")
dom=Priestor("dom",0)
svet.pridaj(dom)
obyvacka=Priestor("obyvacka",96)
spalna=Priestor("spalna",48)
ja=Clovek("ja")
spalna.pridaj(ja)
dom.pridaj(obyvacka)
dom.pridaj(spalna)
#dom.stav()
#dom.sucetObjemov()
co2spalna=CO2meter(spalna)
co2spalna.citaj()
dom.stav()
print(svet.aktualny_cas)
svet.bez(10)
print(svet.aktualny_cas)
