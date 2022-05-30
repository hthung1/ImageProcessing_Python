
import sys, cv2, os
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget, QGraphicsPixmapItem, QGraphicsScene, QFileDialog, qApp
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QEvent, Qt
from cv2 import blur
from gui import Ui_MainWindow
from fun import fun
from PIL import Image

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.mwg = Ui_MainWindow()
        self.fun = fun()
        self.directory = os.path.expanduser("~")
        self.mwg.setupUi(self.main_win)

        self.mwg.actionOpen.triggered.connect(self.open_file)
        self.mwg.actionSave.triggered.connect(self.save_image)
        self.mwg.actionSave_as.triggered.connect(self.save_as_image)
        self.mwg.actionClose.triggered.connect(qApp.quit)

        self.mwg.actionHistogram.triggered.connect(self.histogram)
        self.mwg.action_dao_anh.triggered.connect(self.dao_anh)
        self.mwg.action_muc_xam.triggered.connect(self.anh_xam)
        self.mwg.action_gamma.triggered.connect(self.gamma)
        self.mwg.action_logaric.triggered.connect(self.logaric)
        self.mwg.actionRotateLeft.triggered.connect(self.rotate_left)
        self.mwg.actionRotateRight.triggered.connect(self.rotate_right)
        self.mwg.actionFlipVertical.triggered.connect(self.flip_vertical)
        self.mwg.actionFlipHorizontal.triggered.connect(self.flip_horizontal)
        self.mwg.actionReset.triggered.connect(self.reset)

        # xử lí slider
        self.mwg.slider_min.valueChanged.connect(self.edge_detection)
        self.mwg.slider_max.valueChanged.connect(self.edge_detection)
        self.mwg.slider_blur.valueChanged.connect(self.fn_blur)
        self.mwg.slider_brightness.valueChanged.connect(self.brightness)
        self.mwg.slider_contrast.valueChanged.connect(self.contrast)
        self.mwg.red.valueChanged.connect(self.color)
        self.mwg.green.valueChanged.connect(self.color)
        self.mwg.blue.valueChanged.connect(self.color)

        self.mwg.check_canny.toggled.connect(self.update)

        self.mwg.graphicsView.viewport().installEventFilter(self)
        self.mwg.graphicsView_2.viewport().installEventFilter(self)

        self.files = None
        self.img = None
        self.value_blur = 0
        self.value_contrast = 0
        self.value_brightness = 100
        self.min_edge = 0
        self.max_edge = 0
        self.mwg.slider_brightness.setValue(self.value_brightness)
        self.red = 0
        self.green = 0
        self.blue = 0



    def open_file(self):
        files = QFileDialog.getOpenFileNames(self, "Open Image", self.directory, filter="Image (*.*)")[0]
        if files:
            self.files = files
            self.img = cv2.imread(self.files[0])
            print(self.files[0],self.files)
            self.image = self.img
            self.load_img(self.img)
            self.load_img_2(self.img)

    def load_img(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)

        item = QGraphicsPixmapItem(pixmap)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.mwg.graphicsView.setScene(scene)

    def load_img_2(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)

        item = QGraphicsPixmapItem(pixmap)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.mwg.graphicsView_2.setScene(scene)

    def eventFilter(self, source, event):
        if (
            event.type() == QEvent.Wheel and
            event.modifiers() == Qt.ControlModifier):
                if event.angleDelta().y() > 0:
                    scale = 1.25
                else:
                    scale = 0.8
                self.mwg.graphicsView.scale(scale, scale)
                self.mwg.graphicsView_2.scale(scale, scale)

                return True
        return super().eventFilter(source, event)

    def histogram(self):
        if (self.files):
            fun.histogram(self.img)

    def dao_anh(self):
        if (self.files):
            self.img = fun.dao_anh(self.img)
            self.load_img_2(self.img)

    def anh_xam(self):
        if (self.files):
            self.img = fun.anh_Xam(self.img)
            self.load_img_2(self.img)
    def gamma(self):
        if (self.files):
            self.img = fun.Chuyen_Doi_Gamma(self.img)
            self.load_img_2(self.img)
    def logaric(self):
        if (self.files):
            self.img = fun.Chuyen_doi_logarit(self.img)
            self.load_img_2(self.img)

    def rotate_left(self):
        # (h, w) = self.img.shape[:2]
        # center = (w / 2, h / 2)
        # angle = 30
        # scale = 1
        # M = cv2.getRotationMatrix2D(center, angle, scale)
        # self.img = cv2.warpAffine(self.img, M, (w, h))
        if (self.files):
            self.img = cv2.rotate(self.img,cv2.ROTATE_90_COUNTERCLOCKWISE)
            self.load_img_2(self.img)

    def rotate_right(self):
        if (self.files):
            self.img = cv2.rotate(self.img,cv2.ROTATE_90_CLOCKWISE)
            self.load_img_2(self.img)
    def flip_vertical(self):
        if (self.files):
            self.img = cv2.flip(self.img, 0)
            self.load_img_2(self.img)
    def flip_horizontal(self):
        if (self.files):
            self.img = cv2.flip(self.img, 1)
            self.load_img_2(self.img)

    def edge_detection(self):
        if (self.files):
            self.max_edge = self.mwg.slider_max.value()
            self.min_edge = self.mwg.slider_min.value()
            self.update()

    def fn_blur(self):
        if(self.files):
            self.value_blur = self.mwg.slider_blur.value()
            self.update()            
            
    
    def brightness(self):
        if(self.files):
            self.value_brightness = self.mwg.slider_brightness.value()
            self.update()            
    def color(self):
        if(self.files):
            self.red = self.mwg.red.value()
            self.green = self.mwg.green.value()
            self.blue = self.mwg.blue.value()
            self.update()
    def contrast(self):
        if(self.files):
            self.value_contrast = self.mwg.slider_contrast.value()
            self.update()            

    def update(self):
        self.img = fun.brightness(self.image,self.value_brightness)
        self.img = fun.contrast(self.img,self.value_contrast)
        self.img = fun.blur(self.img,self.value_blur)
        self.img = fun.color(self.img, self.red, self.green, self.blue)
        if self.mwg.check_canny.isChecked():
            self.img = fun.canny_edge_detection(self.img,self.min_edge,self.max_edge)

        self.load_img_2(self.img)

    def save_is_success(self):
        QMessageBox.about(self, "Message", "Save is Success !")

    def reset(self):
        self.mwg.slider_blur.setValue(0)
        self.mwg.slider_min.setValue(0)
        self.mwg.slider_max.setValue(0)
        self.mwg.red.setValue(0)
        self.mwg.blue.setValue(0)
        self.mwg.green.setValue(0)
        self.mwg.slider_brightness.setValue(100)
        self.img = self.image
        self.load_img_2(self.img)

    def save_as_image(self):
        filename = QFileDialog.getSaveFileName(self, "Save Image", self.directory, filter=".jpg;;.png;;.tiff;;.bmp")
        if (filename[0]):
            if (self.files):
                self.files = ''.join(filename)
                cv2.imwrite(self.files,self.img)

    def save_image(self):
        if(self.files):
            cv2.imwrite(self.files[0],self.img)
            self.save_is_success()
            
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication([])
    form = Main()
    form.show()

    sys.exit(app.exec_())