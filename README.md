# Font Style Adjuster

**SOFTWARE** | **DESKTOP APPLICATION** | **PYTHON ‧ PYQT5**

A desktop application that allows users to customize text appearance through interactive sliders. Users can adjust font size, grayscale text color, and grayscale background color with a real-time preview.

## 01. Project Overview

### Description
Font Style Adjuster is a desktop-based GUI application developed using Python and PyQt5. It provides a simple interface for modifying text appearance through interactive controls.

### Objectives
- Provide an intuitive interface for text customization.
- Enable real-time preview of font and color changes.
- Demonstrate GUI development and event handling using PyQt5.

### Problem Statement
Manually adjusting text appearance through separate settings can be inconvenient for users who need a simple and interactive customization tool.

### Solution
This application integrates font size, text color, and background color controls into a single interface, allowing users to preview changes immediately without restarting the application.

### Key Features
- **Font Size Adjustment:** Change font size from 20 pt to 60 pt.
- **Text Color Adjustment:** Adjust grayscale text intensity from black to white.
- **Background Color Adjustment:** Change the preview background from black to white.
- **Live Preview:** Display appearance changes immediately.
- **Color Indicators:** Show the current grayscale intensity and color swatches.
- **Reset Settings:** Restore the default appearance settings.
- **Close Application:** Exit the application using the Close button.

## 02. Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| GUI Framework | PyQt5 |
| UI Design | Qt Designer UI file (`.ui`) |
| UI Loading | PyQt5 `uic.loadUi()` |
| Development Environment | Python 3.12 |
| Code Editor | Visual Studio Code |

## 03. Screenshots / Results

### Application Interface
Display the main application window, including the live preview area, customization controls, and action buttons.

**Screenshot:** `screenshots/main-interface.png`

### Font Size Adjustment
Demonstrate how moving the font size slider changes the preview text size.

**Screenshot:** `screenshots/font-size-adjustment.png`

### Text Color Adjustment
Demonstrate how the text color slider changes the preview text from black to white.

**Screenshot:** `screenshots/text-color-adjustment.png`

### Background Color Adjustment
Demonstrate how the background color slider changes the preview background from black to white.

**Screenshot:** `screenshots/background-color-adjustment.png`

### Reset Settings
Show the application after clicking Reset Settings, restoring the default font size and color values.

**Screenshot:** `screenshots/reset-settings.png`

*Note: Replace these screenshot placeholders with actual screenshots captured from the running application.*

## 04. Installation & Usage

### Prerequisites
- Python 3.12 or compatible Python 3 version.
- pip package manager.
- PyQt5 library.

### Project Structure

```text
app-font-style-adjuster/
├── main.py
├── font_style_adjuster.ui
├── screenshots/
│   ├── main-interface.png
│   ├── font-size-adjustment.png
│   ├── text-color-adjustment.png
│   ├── background-color-adjustment.png
│   └── reset-settings.png
└── README.md
```

### Installation

**Step 1. Clone the repository**

```bash
git clone https://github.com/Hndraa-Apss/app-font-style-adjuster.git
```

**Step 2. Navigate to the project directory**

```bash
cd app-font-style-adjuster
```

**Step 3. Install the dependency**

```bash
python -m pip install PyQt5
```

### Configuration

Ensure that `main.py` and `font_style_adjuster.ui` are located in the same directory. The application loads its interface from the `.ui` file at runtime.

No additional configuration is required.

### Run the Application

Execute the following command from the project directory:

```bash
python main.py
```

### Usage Instructions

1. Launch the application.
2. Adjust the **Font Size** slider to change the preview text size.
3. Adjust the **Text Color** slider to change the text grayscale intensity.
4. Adjust the **Background Color** slider to change the preview background intensity.
5. Observe the changes in the live preview.
6. Click **Reset Settings** to restore the default values.
7. Click **Close** to exit the application.

## Author

**Hndraa Apss**

GitHub: [Hndraa-Apss](https://github.com/Hndraa-Apss)
