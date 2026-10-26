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

<img width="761" height="731" alt="image" src="https://github.com/user-attachments/assets/07d568c6-7826-4499-abd4-3416dd930497" />


### Font Size Adjustment
Demonstrate how moving the font size slider changes the preview text size.

<img width="762" height="732" alt="image" src="https://github.com/user-attachments/assets/86cf4b06-9691-4058-a461-2c3e1b1e7c93" />


### Text Color Adjustment
Demonstrate how the text color slider changes the preview text from black to white.

<img width="763" height="732" alt="image" src="https://github.com/user-attachments/assets/1e15135a-7476-4648-9949-b47ba1b2cbc1" />


### Background Color Adjustment
Demonstrate how the background color slider changes the preview background from black to white.

<img width="761" height="731" alt="image" src="https://github.com/user-attachments/assets/45a9c3c8-a80e-42ef-baca-1eeaacfe2a6d" />


### Reset Settings
Show the application after clicking Reset Settings, restoring the default font size and color values.

<img width="761" height="730" alt="image" src="https://github.com/user-attachments/assets/1a7be53a-8b97-4d4f-bbf6-c9a2da1b9f77" />


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
└── README.md
```

### Installation

**Step 1. Clone the repository**

```bash
git clone https://github.com/hndraa/app-FontStyleAdjuster.git
```

**Step 2. Navigate to the project directory**

```bash
cd app-FontStyleAdjuster
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
