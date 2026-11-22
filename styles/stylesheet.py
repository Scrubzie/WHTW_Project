
from pathlib import Path

from PySide6.QtWidgets import QApplication

# Stylesheet directory
STYLES_DIR = Path(__file__).resolve().parent

def load_stylesheet(filename: str) -> str:

    stylesheet_path = STYLES_DIR / filename

    try:
        return stylesheet_path.read_text(encoding="utf-8")

    except OSError as exc:
        raise RuntimeError(
            f"Unable to load stylesheet: {stylesheet_path}"
        ) from exc


def apply_global_stylesheet(app: QApplication) -> None:
    stylesheet = load_stylesheet("main.qss")
    app.setStyleSheet(stylesheet)
