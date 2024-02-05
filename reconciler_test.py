import unittest
from unittest.mock import patch
import csv
from reconciler import Reconciler

class TestReconciler(unittest.TestCase):
    def setUp(self):
        self.source_data = [
            {'ID': '1', 'Name': 'John', 'Age': '20'},
            {'ID': '2', 'Name': 'Jane', 'Age': '21'},
            {'ID': '3', 'Name': 'Jill', 'Age': '22'},
            {'ID': '4', 'Name': 'Jack', 'Age': '23'},
        ]
        self.target_data = [
            {'ID': '1', 'Name': 'John', 'Age': '20'},
            {'ID': '2', 'Name': 'Jane', 'Age': '21'},
            {'ID': '3', 'Name': 'Jill', 'Age': '22'},
            {'ID': '4', 'Name': 'Jack', 'Age': '23'},
            {'ID': '5', 'Name': 'Jake', 'Age': '24'},
        ]

    @patch('reconcile.Reconcile._read_csv')
    def test_check_missing_records(self, mock_read_csv):
        mock_read_csv.side_effect = [self.source_data, self.target_data]
        reconcile = Reconciler('source.csv', 'target.csv')
        missing_in_target, missing_in_source = reconcile.reconcile_data()
        self.assertEqual(missing_in_target, {'5'})
        self.assertEqual(missing_in_source, {'5'})

    @patch('reconciler.Reconciler._read_csv')
    def test_report_generation(self, mock_read_csv):
        mock_read_csv.return_value = []
        reconciler = Reconciler('source.csv', 'target.csv')
        report = reconciler.reconcile_data()

        with patch('reconciler.ReconciliationReport.generate_report') as mock_generate_report:
            reconciler.reconcile_data().generate_report('output.csv')
            mock_generate_report.assert_called_once_with('output.csv')
