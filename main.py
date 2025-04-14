from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import qrcode
from io import BytesIO
from PIL import Image
from kivy.core.image import Image as CoreImage

class QRLayout(BoxLayout):
    def generate_qr(self):
        data = self.ids.input_field.text
        if data:
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = BytesIO()
            img.save(buffer, format='PNG')
            buffer.seek(0)
            kivy_image = CoreImage(buffer, ext='png')
            self.ids.qr_image.texture = kivy_image.texture

class QRApp(App):
    def build(self):
        print("App is building the UI...")
        return QRLayout()

if __name__ == '__main__':
    QRApp().run()
