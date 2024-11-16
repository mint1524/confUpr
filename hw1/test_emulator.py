import unittest
from emulator import ls_command, cd_command, head_command

class TestShellCommands(unittest.TestCase):

    def test_ls(self):
        files = ls_command('/', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertIn('home', files)

    def test_cd(self):
        new_dir = cd_command('/', 'home', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertEqual(new_dir, '/home')

    def test_head(self):
        content = head_command('./home/user/file1.txt', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertTrue(len(content) > 0)

if __name__ == '__main__':
    unittest.main()
