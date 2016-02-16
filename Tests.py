"""
QT_CSV Tests
"""
from unittest import TestCase
from Controller import Controller


class Tests(TestCase):
    """
    Klasse fuer die Testcases
    """

    def test_csv_read(self):
        """
        Testet ob ein CSV File erfolgreich ingelesen werden kann
        """
        c = Controller()
        self.assertEqual(None, c.reader)

    def test_delimiter(self):
        """
        testet ob der richtige delimiter benutzt wird
        """
        c = Controller()
        c.delimiter = ';'
        self.assertEqual(c.delimiter, ';')

    def test_non_delimiter(self):
        """
        testet ob ein delimiter vorhanden ist
        """
        c = Controller()
        self.assertIsNone(c.delimiter)

    def test_wrong_delimiter(self):
        """
        testet ob ein falscher delimiter verwendet wird
        """
        c = Controller()
        c.delimiter = ' '
        self.assertEqual(c.delimiter, ' ')

    def test_wrong_delimiter2(self):
        """
        testet ob ein falscher delimiter verwendet wird
        """
        c = Controller()
        c.delimiter = ','
        self.assertEqual(c.delimiter, ',')