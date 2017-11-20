co2minimum=370
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
    hmotnost_co2=0
    zoznam_objektov=[]
    def __init__(self,meno,objem=0):
        self.meno=meno
        self.objem=self.objem+objem
        self.teplotaVzduchu = 0
        self.hmotnost_co2=co2minimum*1.8*self.objem
        print("nastavil hmotnost co2 na",self.hmotnost_co2,"objem",self.objem)
        self.zoznam_objektov=[]

    def stav(self):
        print("v",self.meno,"je",self.hmotnost_co2,"mg, to je",self.koncentracia_co2(),"ppm v",self.objem,"m3 vzduchu")
        for objekt in self.zoznam_objektov:
            print("v",self.meno,"je",objekt.meno)
            objekt.stav()
    def stavco2(self):
        print("v",self.meno,"je",self.hmotnost_co2,"mg, to je",self.koncentracia_co2(),"ppm v",self.objem,"m3 vzduchu")
        for objekt in self.zoznam_objektov:
            objekt.stavco2()

    def koncentracia_co2(self):
        if ( self.objem > 0 ):
            return (self.hmotnost_co2)/1.8/(self.objem)
        else:
            return 0
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
        self.stavco2()
        for objekt in self.zoznam_objektov:
            if isinstance(objekt,Clovek):
                self.hmotnost_co2 += objekt.krok_casu()
            else:
                objekt.krok_casu()

class Clovek:
    meno=""
    def __init__(self,meno):
        self.meno=meno
        print("Novy clovek!")
    def dychaj(self):
        # jeden 80kg clovek spravi 240kg co2/rok 27g/hodinu  0.46g/minutu
        # wiki 900g/den 37.5g/h 0.625g/m
        print(self.meno,"dycham!")
        return(625)
    def krok_casu(self):
        return(self.dychaj())
    def stav(self):
        print(self.meno,"zijem")
    def stavco2(self):
        1+1

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
clovek1=Clovek("clovek1")
clovek2=Clovek("clovek2")
spalna.pridaj(clovek1)
spalna.pridaj(clovek2)
dom.pridaj(obyvacka)
dom.pridaj(spalna)
#co2spalna=CO2meter(spalna)
#co2spalna.citaj()
#dom.stav()
print(svet.aktualny_cas)
svet.bez(480)
print(svet.aktualny_cas)
