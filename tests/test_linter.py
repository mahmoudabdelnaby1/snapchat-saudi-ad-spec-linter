import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from snap_spec_linter import lint_snap_ad

class TestSnapLinter(unittest.TestCase):
    def test_lint(self):
        m = Path(__file__).resolve().parent.parent / "examples" / "sample_manifest.json"
        res = lint_snap_ad(str(m))
        self.assertEqual(res["status"], "PASS")

if __name__ == "__main__":
    unittest.main()
