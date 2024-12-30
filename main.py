import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>500</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Квадрат-объектив — 2</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>K = </string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>10</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>N = </string>
    </property>
   </widget>
   <widget class="QPushButton" name="draw">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>0</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Рисовать</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="k">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>10</y>
      <width>113</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="n">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>10</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Square2(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.color = QColor(0, 0, 0)
        self.draw.clicked.connect(self.act)
        self.flag = False

    def act(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_squares(qp)
            qp.end()
        self.flag = False

    def draw_squares(self, qp):
        coeff = float(self.k.text())
        points = [[150, 150], [350, 150], [350, 350], [150, 350]]
        qp.setPen(self.color)
        for i in range(int(self.n.text())):
            polygon = QPolygonF()
            polygon.append(QPointF(*points[0]))
            polygon.append(QPointF(*points[1]))
            polygon.append(QPointF(*points[2]))
            polygon.append(QPointF(*points[3]))
            qp.drawPolygon(polygon)
            points = [[points[0][0] + (points[1][0] - points[0][0]) * (1 - coeff), points[0][1] + (points[1][1] -
                                                                                                   points[0][1]) *
                       (1 - coeff)],
                      [points[1][0] + (points[2][0] - points[1][0]) * (1 - coeff), points[1][1] + (points[2][1] -
                                                                                                   points[1][1]) *
                       (1 - coeff)],
                      [points[2][0] + (points[3][0] - points[2][0]) * (1 - coeff), points[2][1] + (points[3][1] -
                                                                                                   points[2][1]) *
                       (1 - coeff)],
                      [points[3][0] + (points[0][0] - points[3][0]) * (1 - coeff), points[3][1] + (points[0][1] -
                                                                                                   points[3][1]) *
                       (1 - coeff)]]


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exception = except_hook
    sys.exit(app.exec())
