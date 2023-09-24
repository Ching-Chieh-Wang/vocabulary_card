def btnInfoOutLineStyle():
    return """
        QPushButton {
            background-color: transparent;
            color: #17a2b8; /* Info color */
            border: 2px solid #17a2b8; /* Info color for the border */
            border-radius: 5px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #17a2b8; /* Info color on hover */
            color: #ffffff; /* White text color on hover */
        }
        QPushButton:pressed {
            background-color: #138496; /* Darker info color on pressed */
            border: 2px solid #138496; /* Darker info color for the border on pressed */
        }
        QPushButton:disabled {
            background-color: transparent; /* Transparent background when disabled */
            color: #9BA4B5; /* Lighter text color when disabled */
            border: 2px solid #b0b0b0; /* Lighter border color when disabled */
        }
    """
def btnSuccessOutlineStyle():
    return """
        QPushButton {
            background-color: transparent;
            color: #28a745; /* Success color */
            border: 2px solid #28a745; /* Success color for the border */
            border-radius: 5px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #28a745; /* Success color on hover */
            color: #ffffff; /* White text color on hover */
        }
        QPushButton:pressed {
            background-color: #1c7430; /* Darker success color on pressed */
            border: 2px solid #1c7430; /* Darker success color for the border on pressed */
        }
        QPushButton:disabled {
            background-color: transparent; /* Transparent background when disabled */
            color: #b0b0b0; /* Lighter text color when disabled */
            border: 2px solid #b0b0b0; /* Lighter border color when disabled */
        }
    """
def tBStyle():
    return    """
        QLineEdit {
            border: 2px solid #cccccc;
            border-radius: 15px; /* Adjust the border-radius to make the QLineEdit more rounded */
        }
    """
def btnSuccessStyle():
    return """
        QPushButton {
            background-color: #28a745; /* Success color */
            color: #ffffff; /* White text color */
            border: 2px solid #28a745; /* Success color for the border */
            border-radius: 5px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #218838; /* Darker success color on hover */
        }
        QPushButton:pressed {
            background-color: #1c7430; /* Even darker success color on pressed */
            border: 2px solid #1c7430; /* Even darker success color for the border on pressed */
        }
    """
def btnDangerStyle():
    return """
        QPushButton {
            background-color: #dc3545; /* Danger color */
            color: #ffffff; /* White text color */
            border: 2px solid #dc3545; /* Danger color for the border */
            border-radius: 5px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #c82333; /* Darker danger color on hover */
        }
        QPushButton:pressed {
            background-color: #bd2130; /* Even darker danger color on pressed */
            border: 2px solid #bd2130; /* Even darker danger color for the border on pressed */
        }
    """
    