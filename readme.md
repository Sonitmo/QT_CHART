1. Tạo file multilanguages.pro
```commandline
SOURCES = ./modules/interface.py
TRANSLATIONS += ./locate/eng-vi.ts
TRANSLATIONS += ./locate/eng-th.ts
```

2. Chạy file (lưu ý: nên cài pyqt5 mới chạy được)

```commandline
pip install pyqt5
pylupdate5 -verbose multilanguages.pro
```

3. Vào QT Linguist để mở file eng-vi.ts rồi chuyển đổi ngôn ngữ  ->> release as --> lưu file .qm
Lưu ý: file chạy QT Linguist nằm ở folder:
C:\Users\sonit\AppData\Local\Programs\Python\Python311\Lib\site-packages\qt6_applications\Qt\bin\linguist.exe

