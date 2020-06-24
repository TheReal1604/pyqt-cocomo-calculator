class CocomoMath:
    ptype_values = {
        "embedded": {
            "alpha": 3.6,
            "beta": 1.2,
            "gamma": 0.32
        },
        "organic": {
            "alpha": 2.4,
            "beta": 1.05,
            "gamma": 0.38
        },
        "semi-detached": {
            "alpha": 3.0,
            "beta": 1.12,
            "gamma": 0.35
        }
    }

    lang = {
        "Assembler": 213,
        "C": 91,
        "Fortran 95": 71,
        "Pascal": 91,
        "Tcl": 62,
        "C++": 53,
        "Java": 53,
        "Haskell": 38,
        "Visual Basic 5": 29,
        "Smalltalk": 21,
        "SQL": 13
    }

    modvalues = {
        "RELY": {
            "very low": 0.75,
            "low": 0.88,
            "normal": 1.00,
            "high": 1.15,
            "very high": 1.4,
        },
        "DATA": {
            "low": 0.94,
            "normal": 1.00,
            "high": 1.08,
            "very high": 1.16
        },
        "CPLX": {
            "very low": 0.70,
            "low": 0.85,
            "normal": 1.00,
            "high": 1.15,
            "very high": 1.30,
            "ultra high": 1.65
        },
        "TIME": {
            "normal": 1.00,
            "high": 1.11,
            "very high": 1.30,
            "ultra high": 1.66
        },
        "STOR": {
            "normal": 1.00,
            "high": 1.06,
            "very high": 1.21,
            "ultra high": 1.56
        },
        "VIRT": {
            "low": 0.87,
            "normal": 1.00,
            "high": 1.15,
            "very high": 1.30
        },
        "TURN": {
            "low": 0.87,
            "normal": 1.00,
            "high": 1.07,
            "very high": 1.15,
        },
        "ACAP": {
            "very low": 1.46,
            "low": 1.19,
            "normal": 1.00,
            "high": 0.86,
            "very high": 0.71,
        },
        "AEXP": {
            "very low": 1.29,
            "low": 1.13,
            "normal": 1.00,
            "high": 0.91,
            "very high": 0.82,
        },
        "PCAP": {
            "very low": 1.42,
            "low": 1.17,
            "normal": 1.00,
            "high": 0.86,
            "very high": 0.70,
        },
        "VEXP": {
            "very low": 1.21,
            "low": 1.10,
            "normal": 1.00,
            "high": 0.90,
        },
        "LTEX": {
            "very low": 1.14,
            "low": 1.07,
            "normal": 1.00,
            "high": 0.95
        },
        "MODP": {
            "very low": 1.24,
            "low": 1.10,
            "normal": 1.00,
            "high": 0.91,
            "very high": 0.82
        },
        "TOOL": {
            "very low": 1.24,
            "low": 1.10,
            "normal": 1.00,
            "high": 0.91,
            "very high": 0.83
        },
        "SCED": {
            "very low": 1.23,
            "low": 1.08,
            "normal": 1.00,
            "high": 1.04,
            "very high": 1.10
        }
    }

    def __init__(self, ptype, ufp, sellang, selmodi, precision, **kwargs):
        self.ufp = ufp
        self.selmodi = selmodi
        self.ptype = ptype
        self.langvalue = self.lang[sellang]
        self.precision = precision

        if ptype == "embedded":
            self.pvalues = self.ptype_values["embedded"]
        elif ptype == "organic":
            self.pvalues = self.ptype_values["organic"]
        else:
            self.pvalues = self.ptype_values["semi-detached"]

        if kwargs.get("kloc"):
            self.kdloc = kwargs.get("kloc")
        else:
            self.kdloc = self.calcKDLOC(ufp)

        self.modificator = self.calcMod()
        self.pm = self.calcPM()
        self.tdev = self.calctdev()
        self.tg = self.calctg()

    def calcKDLOC(self, ufp):
        return (ufp * self.langvalue) / 1000

    def calcMod(self):
        mod = 1
        for key, value in self.selmodi.items():
            mod = mod * self.modvalues[key][value]

        return mod

    def calcPM(self):
        return round(self.pvalues["alpha"] * pow(self.kdloc, self.pvalues["beta"]) * self.modificator, self.precision)

    def calctdev(self):
        return round(2.5 * pow(self.getpm(), self.pvalues["gamma"]), self.precision)

    def calctg(self):
        return round(self.getpm() / self.gettdev(), self.precision)

    def getkdlocformula(self):
        return "({} * {}) / 1000".format(self.ufp, self.langvalue)

    def getmodformula(self):
        count = 1
        modstr = ""
        for key, value in self.selmodi.items():
            if count < len(self.selmodi.items()):
                modstr += str(self.modvalues[key][value]) + "*"
            else:
                modstr += str(self.modvalues[key][value])

            count += 1

        return modstr

    def getpmformula(self):
        return "{} * {}^{} * {}".format(self.pvalues["alpha"], self.getkdloc(), self.pvalues["beta"], self.modificator)

    def gettdevformula(self):
        return "2.5 * {}^{}".format(self.getpm(), self.pvalues["gamma"])

    def gettgformula(self):
        return "{} / {}".format(self.getpm(), self.gettdev())

    def getkdloc(self):
        return self.kdloc

    def getmod(self):
        return self.modificator

    def getpm(self):
        return self.pm

    def gettdev(self):
        return self.tdev

    def gettg(self):
        return self.tg

    def getalpha(self):
        return self.ptype_values[self.ptype]["alpha"]

    def getbeta(self):
        return self.ptype_values[self.ptype]["beta"]

    def getgamma(self):
        return self.ptype_values[self.ptype]["gamma"]