from kps_pelaa import KiviPaperiSaksetPeli
from tekoaly import Tekoaly

class KPSPelaajaVsTekoaly(KiviPaperiSaksetPeli):
    def __init__(self, tuomari) -> None:
        super().__init__(tuomari)
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self._tekoaly.anna_siirto()