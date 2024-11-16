import unittest
from emulator import ls_command, cd_command, head_command

class TestShellCommands(unittest.TestCase):

    # Тесты для команды ls
    def test_ls_root(self):
        files = ls_command('/', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertIn('home', files)  

    def test_ls_subdirectory(self):
        files = ls_command('/home', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertIn('user', files) 

    # Тесты для команды cd
    def test_cd_to_home(self):
        new_dir = cd_command('/', 'home', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertEqual(new_dir, '/home')  

    def test_cd_to_parent_directory(self):
        new_dir = cd_command('/home/user', '..', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertEqual(new_dir, '/home') 

    # Тесты для команды head
    def test_head_valid_file(self):
        content = head_command('./home/user/file1.txt', '/Users/min7t/emulator/virtual_fs.tar')
        self.assertTrue(len(content) > 0) 

    def test_head_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError): 
            head_command('./home/user/nonexistent.txt', '/Users/min7t/emulator/virtual_fs.tar')

if __name__ == '__main__':
    unittest.main()
