import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QTextEdit, QPushButton, QHBoxLayout, QWidget, \
    QVBoxLayout, QToolTip, QLineEdit, QLabel, QCheckBox, QComboBox, QSpacerItem

class Principale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        #Création des boutons
        bouton1 = QPushButton("Valider")
        bouton2 = QPushButton("Ajouter Graphique")
        bouton3 = QPushButton("Supprimer Graphique")
        #Création des LineEdits
        edit1 = QLineEdit()
        edit2 = QLineEdit()
        #Création des Labels
        lab_edit1 = QLabel("Fréqunce Centrale :")
        lab_edit2 = QLabel("Bande Passante    :")
        lab_comboUSB = QLabel("Connexion USB   :")
        lab_comboVoix = QLabel("Connexion voix :")
        #Création des combos
        combo_USB = QComboBox()
        combo_voix = QComboBox()
        #Créations des layouts
        layouth1 = QHBoxLayout()
        layouth2 = QHBoxLayout()
        layouth3 = QHBoxLayout()
        layouth4 = QHBoxLayout()
        layouth5 = QHBoxLayout()
        layoutG = QVBoxLayout()
        layoutD = QVBoxLayout()
        #Ajouts des lineEdit et labels aux layouts
        layouth1.addWidget(lab_edit1)
        layouth1.addWidget(edit1)
        layouth2.addWidget(lab_edit2)
        layouth2.addWidget(edit2)
        #Ajout des combos box et labels aux layouts
        layouth3.addWidget(lab_comboUSB)
        layouth3.addWidget(combo_USB)
        layouth3.addWidget(lab_comboVoix)
        layouth3.addWidget(combo_voix)
        #Ajout Bouton Validé  aux layouts
        layouth4.addWidget(bouton1)
        #Ajout Bouton Ajouter Graph et Suppr
        layouth5.addWidget(bouton2)
        layouth5.addWidget(bouton3)
        #ajout des layouts au layout Vertical Gauche
        layoutG.addLayout(layouth1)
        layoutG.addLayout(layouth2)
        layoutG.addLayout(layouth3)
        layoutG.addLayout(layouth4)
        layoutG.addLayout(layouth5)
        #Déclaration d'un graph
        graph = fft_print().print()
        layoutD.addLayout(graph)
        #Layout Générale
        layoutGen = QHBoxLayout()
        layoutGen.addLayout(layoutD)
        layoutGen.addLayout(layoutD)
        w = QWidget()
        w.setLayout(layoutGen)
        self.setCentralWidget(w)
        self.show()
