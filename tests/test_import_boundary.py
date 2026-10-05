"""Keep archival imports free of execution output and nested Git state."""
import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ImportBoundary(unittest.TestCase):
    def test_imported_notebooks_have_no_execution_outputs(self):
        for raw in subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).split(b'\0'):
            if not raw:
                continue
            path = ROOT / raw.decode()
            if path.suffix != '.ipynb':
                continue
            for cell in json.loads(path.read_text())['cells']:
                if cell['cell_type'] == 'code':
                    self.assertEqual(cell.get('outputs', []), [], str(path.relative_to(ROOT)))
                    self.assertIsNone(cell.get('execution_count'), str(path.relative_to(ROOT)))

    def test_no_nested_gitlinks_are_added(self):
        rows = subprocess.check_output(['git', 'ls-files', '--stage'], cwd=ROOT, text=True)
        self.assertFalse(any(line.startswith('160000 ') for line in rows.splitlines()))
