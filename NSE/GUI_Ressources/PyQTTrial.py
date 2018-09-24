#  -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2017 by the NSE analysis contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Alexander Schober <alexander.schober@mac.com>
#
# *****************************************************************************



from PyQt5 import QtCore, QtGui, QtWidgets

import pyqtgraph as pg
import sys
import numpy as np

 
def main():
 
    app 	= QtWidgets.QApplication(sys.argv)
    tabs	= QtWidgets.QTabWidget()
    w       = pg.GraphicsLayoutWidget()

    label = pg.LabelItem(justify='right')
    vb = w.addViewBox()

    x = np.arange(100)
    y = np.arange(100)
    z = np.random.rand(100,100)*100
    p = pg.ImageItem()
    vb.addItem(p)

    pos = np.array([0., 1., 0.5, 0.25, 0.75])
    color = np.array([[0,255,255,255], [255,255,0,255], [0,0,0,255], (0, 0, 255, 255), (255, 0, 0, 255)], dtype=np.ubyte)
    cmap = pg.ColorMap(pos, color)
    lut = cmap.getLookupTable(0.0, 1.0, 256)
    p.setLookupTable(lut)
    p.setLevels([0,100])
    p.setImage(z)

    vLine = pg.InfiniteLine(angle=90, movable=False)
    hLine = pg.InfiniteLine(angle=0, movable=False)
    vb.addItem(vLine)
    vb.addItem(hLine)
 
    def mouseMoved(evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        mousePoint = vb.mapSceneToView(pos)
        try:
            print("x=%0.1f z=%0.1f z=%0.1f" % (mousePoint.x(),mousePoint.y(),z[int(mousePoint.x()), int(mousePoint.y())]))
        except:
            pass
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())

    proxy = pg.SignalProxy(w.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

    # Create tabs
    tab1	= QtWidgets.QWidget()	
    tab2	= QtWidgets.QWidget()
    tab3	= QtWidgets.QWidget()
    tab4	= QtWidgets.QWidget()
 
    # Resize width and height
    tabs.resize(250, 150)
 
    # Set layout of first tab
    vBoxlayout	= QtWidgets.QVBoxLayout()
    pushButton1 = QtWidgets.QPushButton("Start")
    pushButton2 = QtWidgets.QPushButton("Settings")
    pushButton3 = QtWidgets.QPushButton("Stop")
    vBoxlayout.addWidget(pushButton1)
    vBoxlayout.addWidget(pushButton2)
    vBoxlayout.addWidget(pushButton3)
    tab1.setLayout(vBoxlayout)  

    vBoxlayout_2	= QtWidgets.QVBoxLayout()
    vBoxlayout_2.addWidget(w)
    tab2.setLayout(vBoxlayout_2)  
 
    # Add tabs
    tabs.addTab(tab1,"Tab 1")
    tabs.addTab(tab2,"Tab 2")
    tabs.addTab(tab3,"Tab 3")
    tabs.addTab(tab4,"Tab 4") 
 
    # Set title and show
    tabs.setWindowTitle('PyQt QTabWidget @ pythonspot.com')
    tabs.show()
 
    sys.exit(app.exec_())

 
if __name__ == '__main__':
    main()

