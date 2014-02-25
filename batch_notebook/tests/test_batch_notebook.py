import unittest
import os

from batch_notebook import run_and_save

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

class TestRunAndSave(unittest.TestCase):
    def test_run_and_save(self):
        src_file = os.path.join(TEST_DIR, 'sample_notebook.ipynb')
        dst_file = os.path.join(TEST_DIR, 'sample_notebook_executed.ipynb')
        n_errors = run_and_save(src_file, dst_file)

        self.assertEqual(n_errors, 0)

        with open(dst_file) as f:
            contents = f.read()

        # This is a cheap way to make sure the output is correct.
        # It is dependent on sample_notebook.ipynb.
        self.assertIn('-0.022165', contents)  # Mean of X
        self.assertIn('The median is 0.000692', contents)  # Median of X

        os.remove(dst_file)

if __name__ == '__main__':
    unittest.main()
