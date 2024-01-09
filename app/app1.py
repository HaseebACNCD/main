import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtCore import Qt

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder()
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

        # Create a label
        self.label = QLabel("Hello, World!", self)
        self.label.setAlignment(Qt.AlignCenter)

        # Create a button to open the camera
        self.camera_button = QPushButton("Open Camera", self)
        self.camera_button.clicked.connect(self.on_camera_button_clicked) 

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.camera_button)
        layout.addWidget(self.viewfinder)
        self.setLayout(layout)

    # Function to handle the camera button click event
    def on_camera_button_clicked(self):
        cameras = QCameraInfo.availableCameras()
        if cameras:
            self.camera.setCamera(cameras[0])
            self.camera.start()
        else:
            QMessageBox.warning(self, "No Camera", "No camera available on this device!")

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = CameraApp()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
