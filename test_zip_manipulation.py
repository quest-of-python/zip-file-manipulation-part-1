import pathlib
import unittest

from zip_manipulation import retrieve_text_file_names


class TestZipManipulation(unittest.TestCase):
    def test_retrieve_text_file_names(self):
        zip_path = pathlib.Path("random_files.zip")

        self.assertEqual(
            retrieve_text_file_names(zip_path=zip_path),
            [
                "every.txt",
                "force.txt",
                "hard.txt",
                "image.txt",
                "land.txt",
                "mr.txt",
                "newspaper.txt",
                "pick.txt",
                "probably.txt",
                "she.txt",
                "take.txt",
            ]
        )


if __name__ == '__main__':
    unittest.main()
