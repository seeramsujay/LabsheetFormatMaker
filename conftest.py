import sys
from unittest.mock import MagicMock
if "docx2pdf" not in sys.modules:
    sys.modules["docx2pdf"] = MagicMock()
