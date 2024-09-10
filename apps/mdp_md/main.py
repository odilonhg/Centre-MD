from PySide2 import QtCore, QtGui, QtWidgets
from random import choice
from sys import argv

app = QtWidgets.QApplication (argv)

def genererMDP (tailleMDP = 12, minuscules = True, majuscules = True, chiffres = True, symboles = True):
    caracteres = ""
    MDP = ""
    
    if minuscules:
        caracteres += "abcdefghijklmnopqrstuvwxyz"
    if majuscules:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if chiffres:
        caracteres += "0123456789"
    if symboles:
        caracteres += "&~#{([-|_\^@)=+$]}*%!/:.;?,"
    
    for i in range (tailleMDP):
        MDP += choice (caracteres)
    
    return(MDP)

class main_Fenetre (QtWidgets.QDialog):
    def __init__ (self, parent = None):
        
        QtWidgets.QDialog.__init__ (self, parent)
        
        self.__caseMinuscules = QtWidgets.QCheckBox ("Minuscules")
        self.__caseMajuscules = QtWidgets.QCheckBox ("Majuscules")
        self.__caseChiffres = QtWidgets.QCheckBox ("Chiffres")
        self.__caseSymboles = QtWidgets.QCheckBox ("Symboles")
        
        self.__boutonQuitter = QtWidgets.QPushButton ("Quitter")
        self.__boutonCopier = QtWidgets.QPushButton ("Copier le MDP")
        self.__boutonGenerer = QtWidgets.QPushButton ("Générer !")
        
        self.__champTexte = QtWidgets.QLineEdit("Par Dylan M.")
        
        self.__glissiereTaille = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        
        self.__labelTaille = QtWidgets.QLabel("Taille du mot de passe : " + str(self.__glissiereTaille.value()))
        
        layout = QtWidgets.QGridLayout ()
        
        layout.addWidget (self.__caseMinuscules, 0, 0)
        layout.addWidget (self.__labelTaille, 0, 1)
        layout.addWidget (self.__caseChiffres, 0, 2)
        layout.addWidget (self.__caseMajuscules, 1, 0)
        layout.addWidget (self.__glissiereTaille, 1, 1)
        layout.addWidget (self.__caseSymboles, 1, 2)
        layout.addWidget (self.__champTexte, 2, 1)
        layout.addWidget (self.__boutonQuitter, 3, 0)
        layout.addWidget (self.__boutonCopier, 3, 1)
        layout.addWidget (self.__boutonGenerer, 3, 2)
        
        self.setLayout (layout)
        self.setWindowTitle ("Générateur MDP - Team MD")
        
        self.__caseMinuscules.setChecked (True)
        self.__caseMajuscules.setChecked (True)
        
        self.__glissiereTaille.setMinimum(12)
        self.__glissiereTaille.setMaximum(30)
        
        icone = QtGui.QIcon ()
        icone.addPixmap(QtGui.QPixmap ("security.png"))
        self.setWindowIcon (icone)
        
        self.__boutonQuitter.clicked.connect (self.quitter)
        self.__boutonCopier.clicked.connect (self.copier)
        self.__boutonGenerer.clicked.connect (self.generer)
        self.__glissiereTaille.valueChanged.connect (self.changerTailleMDP)
    
    def quitter (self):
        self.accept ()
    
    def copier (self):
        pressePapier = QtWidgets.QApplication.clipboard ()
        pressePapier.setText (self.__champTexte.text ())
    
    def generer (self):
        tailleMDP = self.__glissiereTaille.value ()
        minuscules = self.__caseMinuscules.isChecked ()
        majuscules = self.__caseMajuscules.isChecked ()
        chiffres = self.__caseChiffres.isChecked ()
        symboles = self.__caseSymboles.isChecked ()
        self.__champTexte.setText (genererMDP (tailleMDP, minuscules, majuscules, chiffres, symboles))
    
    def changerTailleMDP (self):
        self.__labelTaille.setText ("Taille du mot de passe : " + str(self.__glissiereTaille.value ()))

def mdp_md ():    
    dialog = main_Fenetre()
    dialog.exec_()