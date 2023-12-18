from kps_pelaa import KiviPaperiSaksetPeli
from tekoaly_parannettu import TekoalyParannettu

class KPSPelaajaVsTekoalyParannettu(KiviPaperiSaksetPeli):
    def __init__(self, tuomari) -> None:
        super().__init__(tuomari)
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self._tekoaly.anna_siirto()