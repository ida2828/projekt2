# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaPyQGISDialog
                                 A QGIS plugin
 Wtyczka na projekt 2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-08
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Ida Martyna
        email                : idarocho@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

import numpy as np
from scipy.spatial import Delaunay
from math import sqrt
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsMessageLog, Qgis

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Wtyczka_PyQGIS_dialog_base.ui'))


class WtyczkaPyQGISDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaPyQGISDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.policz_H.clicked.connect(self.policzH)
        self.policz_P.clicked.connect(self.policzP)
    
    def policzH(self):
        if self.warstwa.currentLayer() is None:
            QgsMessageLog.logMessage('Nie wybrano aktywnej warstwy.', 'Różnica wysokoci', Qgis.Warning)
            return False

        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        if len(zaznaczone_elementy) < 2:
            QgsMessageLog.logMessage('Wybierz co najmniej 2 punkty na warstwie.', 'Różnica wysokoci', Qgis.Warning)
            return False
        
        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        if len(zaznaczone_elementy) >  2:
            QgsMessageLog.logMessage('Wybierz co najwyżej 2 punkty na warstwie.', 'Różnica wysokoci', Qgis.Warning)
            return False
        
        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        h1 = zaznaczone_elementy[0]['h_plevrf2007nh'] 
        h2 = zaznaczone_elementy[1]['h_plevrf2007nh'] 
        roznica_H = float(h2)-float(h1)
        if roznica_H<0:
            roznica_H = roznica_H*(-1)
        elif roznica_H>0:
            roznica_H = roznica_H
        self.label_H.setText(str(roznica_H))
        
        QgsMessageLog.logMessage('Różnica wysokości między punktami wynosi: ' + str(roznica_H) + ' m' , ' Różnica wysokości', Qgis.Success)
        
        
    def policzP(self):
        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        if len(zaznaczone_elementy) < 3:
            QgsMessageLog.logMessage('Wybierz co najmniej 3 punkty na warstwie.', 'Pole powierzchni', Qgis.Warning)
            return False

        xy = np.array([(float(p['x2000']), float(p['y2000'])) for p in zaznaczone_elementy])

        tri = Delaunay(xy)

        pole_P = 0.0
        for simp in tri.simplices:
            a, b, c = simp
            x1, y1 = xy[a]
            x2, y2 = xy[b]
            x3, y3 = xy[c]
            pole_P += abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

        pole_P = round(pole_P, 3)

        QgsMessageLog.logMessage('Pole powierzchni między zaznaczonymi punktami: ' + str(pole_P) + ' m²', 'Pole powierzchni', Qgis.Success)


'''
#wersja tylko z trójkątem
    def policzP(self):
        if self.warstwa.currentLayer() is None:
            QgsMessageLog.logMessage('Nie wybrano aktywnej warstwy.', 'Pole powierzchni', Qgis.Warning)
            return False

        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        if len(zaznaczone_elementy) < 3:
            QgsMessageLog.logMessage('Wybierz co najmniej 3 punkty na warstwie.', 'Pole powierzchni', Qgis.Warning)
            return False
        
        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        if len(zaznaczone_elementy) > 3:
            QgsMessageLog.logMessage('Wybierz co najwyżej 3 punkty na warstwie.', 'Pole powierzchni', Qgis.Warning)
            return False
        
        zaznaczone_elementy = self.warstwa.currentLayer().selectedFeatures()
        x1 = zaznaczone_elementy[0]['x2000'] 
        y1 = zaznaczone_elementy[0]['y2000']
        x2 = zaznaczone_elementy[1]['x2000'] 
        y2 = zaznaczone_elementy[1]['y2000']
        x3 = zaznaczone_elementy[2]['x2000'] 
        y3 = zaznaczone_elementy[2]['y2000']
        def PL002GK(x_00,y_00):
            strefa = int(y_00/1000000)
            xgk = x_00/0.999923
            ygk = (y_00 - strefa * 1000000 - 500000)/0.999923
            return(xgk,ygk)
        xgk1, ygk1 = PL002GK(float(x1), float(y1))
        xgk2, ygk2 = PL002GK(float(x2), float(y2))
        xgk3, ygk3 = PL002GK(float(x3), float(y3))
        a = sqrt((xgk2 - xgk1)**2 + (ygk2 - ygk1)**2) #1-2
        b = sqrt((xgk2 - xgk3)**2 + (ygk2 - ygk3)**2) #2-3
        c = sqrt((xgk3 - xgk1)**2 + (ygk2 - ygk3)**2) #1-3
        s = (a + b + c) / 2
        pole_P = sqrt(s * (s - a) * (s - b) * (s - c))
        self.label_P.setText(str(pole_P))
        
        QgsMessageLog.logMessage('Pole powierzchni między zaznaczonymi punktami: ' + str(pole_P) , 'Pole powierzchni', Qgis.Success)
        '''
        
        
    
        
        