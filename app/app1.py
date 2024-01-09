from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.camera = Camera(index=0, resolution=(640, 480), play=True)

        # self.camera = Camera(resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        button = Button(text="Take Picture")
        button.bind(on_press=self.take_picture)
        layout.add_widget(button)

        return layout

    def take_picture(self, instance):
        # Capture and save the picture here
        self.camera.export_to_png("captured_image.png")
        print("Picture taken and saved as captured_image.png")


if __name__ == '__main__':
    CameraApp().run()
