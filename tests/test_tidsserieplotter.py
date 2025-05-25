import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from my_packages.lesogplottCsv import TidsseriePlotter

class TestTidsseriePlotter(unittest.TestCase):

    @patch('my_packages.lesogplottCsv.plt')  # Mock matplotlib
    @patch('my_packages.lesogplottCsv.pd.read_csv')  # Mock pandas lesing av CSV
    def test_plotter_initialisering_og_vis_graf(self, mock_read_csv, mock_plt):
        # Simulert data
        mock_data = {
            'Dato': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'Verdi': [1.0, 2.0, 3.0]
        }
        import pandas as pd
        mock_read_csv.return_value = pd.DataFrame(mock_data)

        # Initialiser objektet
        plotter = TidsseriePlotter(
            filsti='../data/Vannføring.csv',
            enhet='L/s',
            periode='år',
            visningsnavn='Vannføring',
            konvertering=1000,
            slutt=None,
            start=None,
            graf_type='line'
        )

        # Test at data ble riktig konvertert
        expected_values = np.array([1000.0, 2000.0, 3000.0])
        np.testing.assert_array_equal(plotter.data['Verdi'].values, expected_values)

        # Test grafvisning
        plotter.vis_graf(median=True, mean=True, maximum=True, minimum=True)

        # Sjekk at plt.show() ble kalt (indikerer at graf ble forsøkt vist)
        self.assertTrue(mock_plt.show.called)

    def test_plotter_med_feil_fil(self):
        with self.assertRaises(FileNotFoundError):
            _ = TidsseriePlotter(
                filsti='../data/fil_som_ikke_finnes.csv',
                enhet='L/s',
                periode='år',
                visningsnavn='Test',
                konvertering=1
            )

if __name__ == '__main__':
    unittest.main()
