import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
# import sys
# sys.path.append('../src')

from my_packages.lesogplottCsv import TidsseriePlotter
from my_packages.sammenligning import sammenlign_plot

class TestSammenlignPlot(unittest.TestCase):

    @patch('my_packages.sammenligning.plt')  # Mock plt
    @patch('my_packages.lesogplottCsv.pd.read_csv')  # Mock lesing av CSV
    def test_sammenlign_plot_fungerer(self, mock_read_csv, mock_plt):
        # Simulert CSV-data
        mock_data = {
            'Dato': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'Verdi': [1.0, 2.0, 3.0]
        }
        mock_df = pd.DataFrame(mock_data)
        mock_read_csv.return_value = mock_df

        # Lag to TidsseriePlotter-objekter med forskjellig visning
        ts1 = TidsseriePlotter(
            '../data/temperatur.csv',
            enhet='°C',
            periode='dag',
            visningsnavn='Temperatur',
            konvertering=None,
            slutt='2024-01-01',
            start=None,
            graf_type='line'
        )

        ts2 = TidsseriePlotter(
            '../data/temperatur.csv',
            enhet='°C',
            periode='uke',
            visningsnavn='Temperatur',
            konvertering=None,
            slutt='2024-01-01',
            start=None,
            graf_type='scatter'
        )

        # Kall funksjonen som skal testes
        sammenlign_plot(ts1, ts2, tittel='Sammenligningstest')

        # Sjekk at plt ble brukt
        self.assertTrue(mock_plt.plot.called or mock_plt.scatter.called)
        mock_plt.title.assert_called_with('Sammenligningstest')
        self.assertTrue(mock_plt.show.called)

if __name__ == '__main__':
    unittest.main()
