from kps_pvp import KPSPelaajaVsPelaaja
from kps_pvadvai import KPSPelaajaVsTekoalyParannettu
from kps_pvai import KPSPelaajaVsTekoaly
from tuomari import Tuomari

class KPSPeli:
    def luo_peli(tyyppi):
        if tyyppi == 'a':
            return KPSPelaajaVsPelaaja(Tuomari())
        if tyyppi == 'b':
            return KPSPelaajaVsTekoaly(Tuomari())
        if tyyppi == 'c':
            return KPSPelaajaVsTekoalyParannettu(Tuomari())

        return None
