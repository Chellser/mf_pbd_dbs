
import unittest

from process_changes import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('Jimmy', commits[420]['author'])
        self.assertEqual('r1551558', commits[3]['revision'])
        self.assertEqual('r1491254', commits[419]['revision'])
        self.assertEqual('2015-07-13', commits[421]['date'])
        self.assertEqual('2015-11-27', commits[6]['date'])
        self.assertEqual('06:10:10', commits[5]['time'])
        self.assertEqual('09:21:48', commits[421]['time'])
        self.assertEqual('Mon,', commits[417]['weekday'])
        self.assertEqual('Fri,', commits[1]['weekday'])
        self.assertEqual('07', commits[4]['hour_of_day'])
        self.assertEqual('15', commits[7]['hour_of_day'])
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                commits[24]['comment'])
        self.assertEqual(['directed the auth callback to point at the AtpAuthActivity class'], commits[415]['comment'])
                

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])

if __name__ == '__main__':
    unittest.main()
