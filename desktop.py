import webview
import os

# frontend papkasidagi index.html faylining yo'lini ko'rsatamiz
html_path = os.path.abspath('frontend/index.html')

if __name__ == '__main__':
    # Dastur oynasini yaratish va ochish
    webview.create_window(
        title='EcoHelp - Desktop Application',
        url=f'file:///{html_path}',
        width=1100,
        height=750,
        resizable=True
    )
    webview.start()