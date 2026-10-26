
import sys
from pathlib import Path

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor, QPalette


class FontAdjusterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        ui_file = Path(__file__).resolve().parent / "font_style_adjuster.ui"
        uic.loadUi(str(ui_file), self)

        self.setWindowTitle("Font Studio | Hndraa Apss")

        # Connect sliders to live preview updates
        self.fontSizeSlider.valueChanged.connect(self.update_font_size)
        self.fontColorSlider.valueChanged.connect(self.update_font_color)
        self.backgroundColorSlider.valueChanged.connect(
            self.update_background_color
        )

        # Update displayed slider values
        self.fontSizeSlider.valueChanged.connect(
            lambda value: self.fontSizeValue.setText(f"{value} pt")
        )
        self.fontColorSlider.valueChanged.connect(
            lambda value: self.fontColorValue.setText(str(value))
        )
        self.backgroundColorSlider.valueChanged.connect(
            lambda value: self.backgroundColorValue.setText(str(value))
        )

        # Connect action buttons
        self.resetButton.clicked.connect(self.reset_settings)
        self.closeButton.clicked.connect(self.close)

        # Apply initial settings
        self.update_font_size()
        self.update_font_color()
        self.update_background_color()

    def update_font_size(self, value=None):
        """Apply the selected font size to the preview."""
        font = self.previewLabel.font()
        font.setPointSize(self.fontSizeSlider.value())
        self.previewLabel.setFont(font)

        self.fontSizeValue.setText(
            f"{self.fontSizeSlider.value()} pt"
        )

    def update_font_color(self, value=None):
        """Apply the selected grayscale text color."""
        intensity = self.fontColorSlider.value()

        self.previewLabel.setStyleSheet(
            f"""
            QLabel#previewLabel {{
                color: rgb({intensity}, {intensity}, {intensity});
                background-color: rgb(
                    {self.backgroundColorSlider.value()},
                    {self.backgroundColorSlider.value()},
                    {self.backgroundColorSlider.value()}
                );
                border-radius: 12px;
            }}
            """
        )

        self.fontColorValue.setText(str(intensity))
        self.fontColorSwatch.setStyleSheet(
            f"""
            background-color: rgb({intensity}, {intensity}, {intensity});
            border: 1px solid #64748b;
            border-radius: 6px;
            """
        )


    def update_background_color(self, value=None):
        """Apply the selected grayscale background color."""
        intensity = self.backgroundColorSlider.value()
        font_intensity = self.fontColorSlider.value()

        self.previewLabel.setStyleSheet(
            f"""
            QLabel#previewLabel {{
                color: rgb({font_intensity}, {font_intensity}, {font_intensity});
                background-color: rgb({intensity}, {intensity}, {intensity});
                border-radius: 12px;
            }}
            """
        )

        self.backgroundColorValue.setText(str(intensity))
        self.backgroundColorSwatch.setStyleSheet(
            f"""
            background-color: rgb({intensity}, {intensity}, {intensity});
            border: 1px solid #64748b;
            border-radius: 6px;
            """
        )

    def reset_settings(self):
        """Restore the default appearance settings."""
        self.fontSizeSlider.setValue(30)
        self.fontColorSlider.setValue(255)
        self.backgroundColorSlider.setValue(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    window = FontAdjusterApp()
    window.show()

    sys.exit(app.exec_())
