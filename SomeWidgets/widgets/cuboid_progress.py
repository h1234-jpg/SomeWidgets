# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 16:02
# @Author  : llc
# @File    : cuboid_progress.py
import math

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QColor, QPolygonF, QBrush, QPen
from PyQt5.QtWidgets import QWidget


class SHWidget(QWidget):
    def __init__(self, color1, color2, parent=None):
        super(SHWidget, self).__init__(parent)
        self.p1 = QPoint(0, 0)
        self.p2 = QPoint(0, 0)
        self.p3 = QPoint(0, 0)
        self.p4 = QPoint(0, 0)
        self.p5 = QPoint(0, 0)
        self.p6 = QPoint(0, 0)
        self.color1 = color1
        self.color2 = color2
        self.opacity = 0.5

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(self.opacity)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        painter.setPen(Qt.NoPen)
        painter.save()
        brush = QBrush(self.color1)
        painter.setBrush(brush)
        points = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]
        painter.drawPolygon(QPolygonF(points))
        painter.restore()
        if self.p6 == self.p7:
            return
        brush = QBrush(self.color2)
        painter.setBrush(brush)
        points = [self.p4, self.p5, self.p6, self.p7, self.p8, self.p9]
        painter.drawPolygon(QPolygonF(points))


class SVWidget(QWidget):
    def __init__(self, color1, color2, parent=None):
        super(SVWidget, self).__init__(parent)
        self.p1 = QPoint(0, 0)
        self.p2 = QPoint(0, 0)
        self.p3 = QPoint(0, 0)
        self.p4 = QPoint(0, 0)
        self.p5 = QPoint(0, 0)
        self.p6 = QPoint(0, 0)
        self.p7 = QPoint(0, 0)
        self.p8 = QPoint(0, 0)
        self.color1 = color1
        self.color2 = color2
        self.opacity = 0.5

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(self.opacity)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        painter.setPen(Qt.NoPen)
        painter.save()
        brush = QBrush(self.color1)
        painter.setBrush(brush)
        points = [self.p1, self.p2, self.p3, self.p4]
        painter.drawPolygon(QPolygonF(points))
        painter.restore()
        if self.p1 == self.p5:
            return
        brush = QBrush(self.color2)
        painter.setBrush(brush)
        points = [self.p5, self.p6, self.p7, self.p8]
        painter.drawPolygon(QPolygonF(points))


class SCuboidProgress(QWidget):
    def __init__(self, color1=QColor(0, 200, 0), color2=QColor(255, 255, 255), opacity=0.5, parent=None):
        super(SCuboidProgress, self).__init__(parent)

        self._sw1 = SHWidget(color1, color2, parent=self)
        self._sw2 = SVWidget(color1, color2, parent=self)

        self._opacity = opacity
        self._value = 0
        self.resize(self.size())

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if v < 0:
            v = 0
        elif v > 100:
            v = 100
        self._value = v
        self._sw1.value = v
        self.resizeEvent()

    @property
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, o):
        self._opacity = o
        self._sw1.opacity = o
        self._sw2.opacity = o
        self.update()

    def resizeEvent(self, event=None):
        """
           p1##################(p6,p1)##################(p7,p5)
           #                   # #                       # #
          #        sw1       #   #         sw1         #   #
         #                  #    #                    #    #
       p2############(p5,p2) sw2 ##############(p8,p6) sw2 #
        #                  #    (p4)                 #    (p8)
        #          sw1     #   #          sw1        #   #
        #                  # #                       # #
       p3#################(p4,p3)###################(p9,p7)
        """
        self.off = self.height() * 0.4 * math.tan(math.pi / 6)
        p = (self.width() - self.off) * self._value / 100
        self._sw1.resize(self.size())
        self._sw1.p1 = QPoint(self.off, 0)
        self._sw1.p2 = QPoint(0, self.height() * 0.4)
        self._sw1.p3 = QPoint(0, self.height())
        self._sw1.p4 = QPoint(p, self.height())
        self._sw1.p5 = QPoint(p, self.height() * 0.4)
        self._sw1.p6 = QPoint(self.off + p, 0)
        self._sw1.p7 = QPoint(self.width(), 0)
        self._sw1.p8 = QPoint(self.width() - self.off, self.height() * 0.4)
        self._sw1.p9 = QPoint(self.width() - self.off, self.height())

        self._sw2.resize(self.size())
        self._sw2.p1 = QPoint(self.off + p, 0)
        self._sw2.p2 = QPoint(p, self.height() * 0.4)
        self._sw2.p3 = QPoint(p, self.height())
        self._sw2.p4 = QPoint(self.off + p, self.height() * 0.6)
        self._sw2.p5 = QPoint(self.width(), 0)
        self._sw2.p6 = QPoint(self.width() - self.off, self.height() * 0.4)
        self._sw2.p7 = QPoint(self.width() - self.off, self.height())
        self._sw2.p8 = QPoint(self.width(), self.height() * 0.6)

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(self._opacity)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        painter.save()
        pen = QPen(Qt.DashLine)
        pen.setWidthF(0.5)
        pen.setColor(Qt.white)
        painter.setPen(pen)
        c = QPoint(self.off, self.height() * 0.6)
        painter.drawPolyline(self._sw1.p1, c)
        painter.drawPolyline(self._sw1.p3, c)
        painter.drawPolyline(c, self._sw2.p8)
        painter.restore()
        pen = QPen(Qt.SolidLine)
        pen.setWidthF(0.5)
        pen.setColor(Qt.white)
        painter.setPen(pen)
        painter.drawPolyline(self._sw1.p2, self._sw1.p8)
        painter.drawPolyline(self._sw1.p7, self._sw1.p8)
        painter.drawPolyline(self._sw1.p8, self._sw1.p9)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    window = SCuboidProgress()
    window.setStyleSheet("""background-color:#272822""")
    window.show()
    window.resize(600, 200)
    window.value = 50
    app.exec_()
