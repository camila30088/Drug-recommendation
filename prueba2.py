import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

msg =[""]
ClCr = 0
Em = False
Fr = False
Tu = False
Vi = False
Mu = False
Ob = False
Di = False
cant_am = 0
a = 0
x = []
MSG_NO = False
class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('interfaz1.ui', self)
        self.commandLinkButton.clicked.connect(lambda: self.abrirVentanados())
        self.Embarazo.clicked.connect(lambda: self.verificar())
        self.Fallorenal.clicked.connect(lambda: self.verificar())
        self.Tuberculosis.clicked.connect(lambda: self.verificar())
        self.VIH.clicked.connect(lambda: self.verificar())
        self.muta.clicked.connect(lambda: self.verificar())
        self.Obesidad.clicked.connect(lambda: self.verificar())
        self.Diabetes.clicked.connect(lambda: self.verificar())

    def abrirVentanados(self):
        self.fallorenal()
        self.edad()
        self.hide()
        o_v = Ventanados(self)
        o_v.show()
        
    def fallorenal(self):
        global ClCr
        if self.clcr1 != 0.0: 
            ClCr = float(self.clcr1.text())
            print(ClCr)
    def edad(self):
        global edad
        if self.lineEdit_2 != 00: 
            edad = float(self.lineEdit_2.text())
            print(edad)

    def verificar(self):
        global Em,Fr,Tu,Vi,Mu,Ob,Di
        btn1 = self.Embarazo
        btn2 = self.Fallorenal
        btn3 = self.Tuberculosis
        btn4 = self.VIH
        btn5 = self.muta
        btn6 = self.Obesidad
        btn7 = self.Diabetes
        if btn1.isChecked():
            Em = True
        if btn2.isChecked():
            Fr = True
            self.fallorenal()
        if btn3.isChecked():
            Tu = True
        if btn4.isChecked():
            Vi = True
        if btn5.isChecked():
            Mu = True
        if btn6.isChecked():
            Ob = True
        if btn7.isChecked():
            Di = True


class Ventanados(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanados, self).__init__(parent)
        loadUi('interfazp2.ui', self)
        self.commandLinkButton.clicked.connect(lambda: self.abrirVentanatres())
        self.Atras.clicked.connect(lambda: self.show_dialog())
        self.radioButton.clicked.connect(lambda: self.verificar())
        self.radioButton_2.clicked.connect(lambda: self.verificar())
        self.radioButton_3.clicked.connect(lambda: self.verificar())
        self.radioButton_4.clicked.connect(lambda: self.verificar())
        self.Amikacinapac.clicked.connect(lambda: self.verificar())
        self.Estreptomicinapac.clicked.connect(lambda: self.verificar())
        self.Gentamicinapac.clicked.connect(lambda: self.verificar())
        self.Tobramicinapac.clicked.connect(lambda: self.verificar())
        self.Netilmicinapac.clicked.connect(lambda: self.verificar())
        

    def abrirVentanatres(self):
        global a,x
        self.ver_edad(edad,cant_am)
        self.hide()
        a = 0
        x = []
        o_v = Ventanatres(self)
        o_v.show()
       
    
    def ver_edad(self,edad,cant_am):
        global msg,MSG_NO
        if (edad >= 18 and edad <= 30) and cant_am > 1 and Tu == False and Vi == False and Fr == False and Ob == False and Di == False and Em == False and Mu == False:
            if MSG_NO == False:
                msg[0] = msg[0] + "Se recomienda hacer las pruebas de evaluación para verificar que el paciente esté apto para seguir con el tratamiento con aminoglucósidos y preferiblemente usar solo uno. \n"
                print("Se recomienda hacer las pruebas de evaluación para verificar que el paciente esté apto para seguir con el tratamiento con aminoglucósidos y preferiblemente usar solo uno.")
        if (edad > 30 and edad <= 60) and cant_am > 1 and Tu == False and Vi == False and Fr == False and Ob == False and Di == False and Em == False and Mu == False:
            if MSG_NO ==False:
                msg[0] = msg[0] + "Se recomienda hacer las pruebas de evaluación para verificar que el paciente esté apto para seguir con el tratamiento con aminoglucósidos y usar solo uno. \n"
                print("Se recomienda hacer las pruebas de evaluación para verificar que el paciente esté apto para seguir con el tratamiento con aminoglucósidos y usar solo uno.")
        if (edad >= 18 and edad <= 60) and cant_am == 1 and Tu == False and Vi == False and Fr == False and Ob == False and Di == False and Em == False and Mu == False:
            if MSG_NO ==False:
                msg[0] = msg[0] + "Se recomienda hacer las pruebas de evaluación para verificar que el paciente pueda para seguir con el tratamiento con aminoglucósidos. \n"
                print("Se recomienda hacer las pruebas de evaluación para verificar que el paciente pueda para seguir con el tratamiento con aminoglucósidos.")
        if (edad > 60) and cant_am > 1 and Tu == False and Vi == False and Fr == False and Ob == False and Di == False and Em == False and Mu == False:
            MSG_NO=True
            print("Es recomendable no seguir el tratamiento con aminogluscósidos.")
       
    def verificar(self):
        global si1,no1,si2,no2,Am,Es,Ge,To,Ne,cant_am
        btn1 = self.radioButton
        btn2 = self.radioButton_2
        btn3 = self.radioButton_3
        btn4 = self.radioButton_4
        btn5 = self.Amikacinapac
        btn6 = self.Estreptomicinapac
        btn7 = self.Gentamicinapac
        btn8 = self.Tobramicinapac
        btn9 = self.Netilmicinapac
        si1 = False
        no1 = False
        si2 = False
        no2 = False
        Am = False
        Es = False
        Ge = False
        To = False
        Ne = False
        
        if btn1.isChecked():
            si1 = True
        if btn2.isChecked():
            no1 = True
        if btn3.isChecked():
            si2 = True
        if btn4.isChecked():
            no2 = True
        if btn5.isChecked():
            Am = True
            cant_am = cant_am + 1
        if btn6.isChecked():
            Es = True
            cant_am = cant_am + 1
        if btn7.isChecked():
            Ge = True
            cant_am = cant_am + 1
        if btn8.isChecked():
            To = True
            cant_am = cant_am + 1
        if btn9.isChecked():
            Ne = True
            cant_am = cant_am + 1
    def show_dialog(self):
        dialog = Advertencia2(self)  # self hace referencia al padre
        dialog.show()
    #def embarazada(self):
    #    #o_r = Ventanacuatro(self)
    #    #o_r.textEdit.setText('Miau')
    #    msg[0] = msg[0] + "\nNo se recomienda el tratamiento con aminoglucosidos"
    #    print("No se recomienda el tratamiento con aminoglucosidos, por favor busque otras alternativas")
    #def verificar(self):
    #    btn = self.radioButton
    #    if btn.isChecked():
    #        self.embarazada()


class Ventanatres(QMainWindow):

    def __init__(self, parent=None):
        super(Ventanatres, self).__init__(parent)
        loadUi('intefazp3.ui', self)
        self.commandLinkButton.clicked.connect(lambda: self.abrirVentanacuatro())
        self.Atras2.clicked.connect(lambda: self.show_dialog())
        self.radioButton.clicked.connect(lambda: self.verificar())
        self.radioButton_2.clicked.connect(lambda: self.verificar())
        self.radioButton_3.clicked.connect(lambda: self.verificar())
        self.radioButton_4.clicked.connect(lambda: self.verificar())
        self.radioButton_5.clicked.connect(lambda: self.verificar())
        self.radioButton_6.clicked.connect(lambda: self.verificar())
        self.listWidget.itemClicked.connect(lambda: self.items())
        self.lineEdit

    def abrirVentanacuatro(self):
        if sim == True:
            self.verificacion()
        if sia == True:
            self.comp_audio(audio)
        if sic == True:
            self.creatin()
        self.hide()
        o_v = Ventanacuatro(self)
        o_v.show()
        

    def items(self): #REVISAR CUANDO SE ESCOGE SOLO UNO VARIAS VECES / *BOTON PARA ELIMINAR ULTIMO SELECCIONADO
        global a,x
        x.append(str(self.listWidget.selectedItems()[a].text()))
        a = a + 1
        print(x)

    def audio(self):
        global audio
        if self.lineEdit != 0.0: 
            audio = float(self.lineEdit.text())
            print(audio)

    def comp_audio(self,audio):
        global msg
        global MSG_NO
        if audio > 40:
            MSG_NO = True
            print("No se recomienda el tratamiento con aminoglucosidos, alta probabilidad de ototoxicidad")
        if audio <= 40:
            if MSG_NO == False:
                msg[0] = msg[0] + "El nivel de audición se encuentra en los rangos normales. \n"
                print("El nivel de audición se encuentra en los rangos normales")

    def creatin(self):
        global ClCr
        if self.lineEdit_2 != 0.0: 
            ClCr = float(self.lineEdit_2.text())
            print(ClCr)

    def verificacion(self):
        global vecm,x,MSG_NO
        vecm = ['Heparina','Nitrito de sodio','Penicilina']
        if (len(x)==1 and (x[0]!= 'Ninguno de los anteriores' and x[0] != vecm[0] and x[0] != vecm[1] and x[0] != vecm[2])) or (len(x)>1 and ((x.count(vecm[0]) == 0) or (x.count(vecm[1]) == 0) or (x.count(vecm[2]) == 0))) or  (len(x)>3 and ((x.count(vecm[0]) == 1) and (x.count(vecm[1]) == 1) and (x.count(vecm[2]) == 1) and (x.count('Ninguno de los anteriores') == 0))) :
            MSG_NO = True
            print("No es recomendable continuar el tratamiento con aminoglucosidos por alto riesgo de ototoxicidad por los medicamentos seleccionados anteriormente")
        else:
            MSG_NO = True
            print("Se recomienda no continuar el tratamiento con aminoglucosidos y buscar otra alternativa más eficaz para el tratamiento de la infección.")

    def verificar(self):
        global sim,nom,sia,noa,sic,noc
        btn1 = self.radioButton_5
        btn2 = self.radioButton_6
        btn3 = self.radioButton
        btn4 = self.radioButton_2
        btn5 = self.radioButton_4
        btn6 = self.radioButton_3
        sim = False
        nom = False 
        sia = False
        noa = False
        sic = False
        noc = False
        if btn1.isChecked():
            sim = True 
        if btn2.isChecked():
            nom = True
        if btn3.isChecked():
            sia = True
            self.audio()
        if btn4.isChecked():
            noa = True
        if btn5.isChecked():
            sic = True
            self.creatin()
        if btn6.isChecked():
            noc = True
    def show_dialog(self):
        dialog = Advertencia3(self)  # self hace referencia al padre
        dialog.show()



class Ventanacuatro(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanacuatro, self).__init__(parent)
        loadUi('intefazp4.ui', self)
        self.Fin.clicked.connect(lambda: self.cerrar())
        #self.Atras3.clicked.connect(lambda: self.abrirVentanatres())
        self.Atras3.clicked.connect(lambda: self.show_dialog())
        self.recomienda.clicked.connect(lambda: self.procedimiento())
        

    

    def embarazada(self):
        global msg
        global MSG_NO
        MSG_NO = True
        print("No se recomienda el tratamiento con aminoglucosidos, por favor busque otras alternativas")
    def dosisnormal(self, amino,op,doc):
        if ((amino == 'Gentamicina') or (amino =='Tobramicina') or (amino == 'Netilmicina')) and (doc>0):
            if (doc>7) and op=='1 (24h)' :
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis única esté entre 5-7 mg/kg/dia. \n"
                    print("Se recomienda que la dosis única esté entre 5-7 mg/kg/dia")
            if (doc<7 or doc==7) and op=='1 (24h)' :
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print("La dosis es apropiada")
            if (doc>3.5) and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 3.5mg/kg cada 12 horas. \n"
                    print("Se recomienda que se suministre máximo 3.5mg/kg cada 12 horas")
            if (doc<3.5 or doc==3.5) and op== '2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")        
            if (doc>2.3) and op== '3 (8h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 2.3mg/kg cada 8 horas. \n"
                    print ("Se recomienda que se suministre máximo 2.3mg/kg cada 8 horas")
            if (doc<2.3 or doc==2.3) and op== '3 (8h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")

        if (amino == 'Amikacina') and doc>0 :
            if (doc>20) and op=='1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis única esté entre 15-20 mg/kg/dias. \n"
                    print("Se recomienda que la dosis única esté entre 15-20 mg/kg/dia")
            if (doc<=20) and op=='1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis es apropiada. \n"
                    print("La dosis es apropiada")
            if (doc>10) and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 10 mg/kg cada 12 horas. \n"
                    print("Se recomienda que se suministre máximo 10 mg/kg cada 12 horas")
            if (doc<=10) and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")
            if (doc>6.7) and op=='3 (8h)': 
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 6.7 mg/kg cada 8 horas. \n"
                    print("Se recomienda que se suministre máximo 6.7 mg/kg cada 8 horas")
            if (doc<=6.7) and op=='3 (8h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")

        if (amino == 'Estreptomicina') and doc>0:
            if (doc>25) and op=='1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis única esté entre 15-25 mg/kg/dia. \n"
                    print("Se recomienda que la dosis única esté entre 15-25 mg/kg/dia")
            if (doc<=25) and op=='1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis es apropiada. \n"
                    print("La dosis es apropiada")
            if (doc>12.5) and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 12.5 mg/kg cada 12 horas. \n"
                    print("Se recomienda que se suministre máximo 12.5 mg/kg cada 12 horas")
            if (doc<=12.5) and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")
            if (doc>8.3) and op== '3 (8h)': 
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 8.3 mg/kg cada 8 horas. \n"
                    print("Se recomienda que se suministre máximo 8.3 mg/kg cada 8 horas")
            if (doc<=8.3) and op== '3 (8h)': 
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")
    
    def fallosrenales(self,renal,amino,op,doc,clcr):
        global msg
        if ((amino == 'Gentamicina') or (amino =='Tobramicina') or (amino == 'Netilmicina')) and (doc>0) and clcr>0:
            if (clcr<=60 and clcr>40):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea 5mg/kg/36h. \n"
                    print("Se recomienda que la dosis sea 5mg/kg/36 h")
            if (clcr<=40 and clcr>20):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea 5mg/kg/48h. \n"
                    print("Se recomienda que la dosis sea 5mg/kg/48 h")
            if clcr<=20:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea 2 mg/kg/48h. \n"
                    print("Se recomienda que la dosis sea 2 mg/kg/48 h ")
            if clcr>60 and Vi == False and Tu == False:
                self.dosisnormal(amino,op,doc)  
            if clcr>60 and Vi == True and Tu == False:
                self.pacientesvih(Vi,amino,op,doc)
            if clcr>60 and Tu == False:
                self.tuberculosis(Tu,amino,op,doc) 

        if (amino == 'Amikacina') and doc>0 and clcr>0:
            if (clcr<=60 and clcr>30) and (doc < 9 or doc > 12) and ((op == '1 (24h)') or (op=='2 (12h)') or (op=='3 (8h)')):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea de 9-12 mg/kg/día. \n"
                    print("Se recomienda que la dosis sea de 9-12 mg/kg/día ")
            if (clcr<=60 and clcr>30) and (doc >= 9 and doc <= 12) and ((op=='2 (12h)') or (op=='3 (8h)')):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea de 9-12 mg/kg/día. \n"
                    print("Se recomienda que la dosis sea de 9-12 mg/kg/día ")
            if (clcr<=60 and clcr>30) and (doc >= 9 and doc <= 12) and op == '1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print("La dosis es apropiada")
            if (clcr<=30 and clcr>10) and (doc < 4 or doc > 9) and ((op == '1 (24h)') or (op=='2 (12h)') or (op=='3 (8h)')):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea de 4-9 mg/kg/día. \n"
                    print("Se recomienda que la dosis sea de 4-9 mg/kg/día ")
            if (clcr<=30 and clcr>10) and (doc >= 4 and doc <= 9) and ((op=='2 (12h)') or (op=='3 (8h)')):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea de 4-9 mg/kg/día. \n"
                    print("Se recomienda que la dosis sea de 4-9 mg/kg/día ")
            if (clcr<=30 and clcr>10) and (doc >= 4 and doc <= 9) and ((op == '1 (24h)')):
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print("La dosis es apropiada")
            if clcr<=10:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis sea 5 mg/kg/48h. \n"
                    print("Se recomienda que la dosis sea 5 mg/kg/48 h ")
            if clcr>60 and Vi == False and Tu == False:
                self.dosisnormal(amino,op,doc)  
            if clcr>60 and Vi == True and Tu == False:
                self.pacientesvih(Vi,amino,op,doc)
            if clcr>60 and Tu == True:
                self.tuberculosis(Tu,amino,op,doc) 

        if (amino == 'Estreptomicina') and doc>0 :
            if (clcr<=80 and clcr>50) and (op=='1 (24h)') and  doc > 7.5:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis máxima sea de 7.5 mg/kg/día. \n"
                    print("Se recomienda que la dosis máxima sea de 7.5 mg/kg/día ")
            if (clcr<=80 and clcr>50) and (op=='1 (24h)') and  doc <= 7.5:
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print("La dosis es apropiada ")
            if (clcr<=50 and clcr>10) and ((op=='1 (24h)') or (op=='2 (12h)') or (op=='3 (8h)')) : 
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis máxima sea de 7.5 mg/kg de 24 a 72h. \n"
                    print("Se recomienda que la dosis máxima sea de 7.5 mg/kg de 24 a 72h ")
            if (clcr<=10) and ((op=='1 (24h)') or (op=='2 (12h)') or (op=='3 (8h)')):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis  máxima sea de 7.5 mg/kg de 72 a 96h. \n"
                    print("Se recomienda que la dosis  máxima sea de 7.5 mg/kg de 72 a 96 h ") 
            if clcr>80 and Vi == False and Tu == False:
                self.dosisnormal(amino,op,doc) 
            if clcr>80 and Vi == True and Tu == False:
                self.pacientesvih(Vi,amino,op,doc)  
            if clcr>80 and Tu == True:
                self.tuberculosis(Tu,amino,op,doc) 
            if ((op=='2 (12h)') or (op=='3 (8h)')) and ((clcr<=80 and clcr>50) or (clcr<=80 and clcr>50)):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis se de en un intervalo mínimo de 24 horas y sea máximo de 7.5 mg/kg. \n"
                    print("Se recomienda que la dosis se de en un intervalo mínimo de 24 horas y sea máximo de 7.5 mg/kg ")
            
    def tuberculosis (self,tuber,amino,op,doc):
        global msg
        if (amino == 'Estreptomicina'):
            if doc>15 and op=='1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis inicial máxima sea de 15 mg/kg/dia. \n"
                    print("Se recomienda que la dosis inicial máxima sea de 15 mg/kg/dia")
            if doc<=15 and op=='1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print("La dosis es apropiada") 
            if doc>7.5 and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que las dosis sean de máximo 7.5 mg/kg cada 12 horas. \n"
                    print("Se recomienda que las dosis sean de máximo 7.5 mg/kg cada 12 horas")
            if doc<=7.5 and op=='2 (12h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis son apropiadas. \n"
                    print("Las dosis son apropiadas")
            if  op=='3 (8h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que la dosis de máximo de 7.5 mg/kg cada 12 horas o de 15 mg/kg/dia. \n"
                    print("Se recomienda que la dosis de máximo de 7.5 mg/kg cada 12 horas o de 15 mg/kg/dia")

        if ((amino == 'Gentamicina') or (amino =='Tobramicina') or (amino == 'Netilmicina')) and (doc>0) and (Vi == False):
            if (op == '1 (24h)') or (op =='2 (12h)'):
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 1.67 mg/kg cada 8 horas. \n"
                    print("Se recomienda que se suministre máximo 1.67 mg/kg cada 8 horas")
            if op=='3 (8h)' and doc>1.67:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda que se suministre máximo 1.67 mg/kg cada 8 horas. \n"
                    print("Se recomienda que se suministre máximo 1.67 mg/kg cada 8 horas")
            if op=='3 (8h)' and doc<=1.67:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Las dosis son apropiadas. \n"
                    print("Las dosis son apropiadas ")
        
        if (amino == 'Amikacina') and doc>0:
            if doc>15 or (op =='2 (12h)' or op=='3 (8h)') or doc<15:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda una dosis única de 15 mg/kg/dia. \n"
                    print("Se recomienda una dosis única de 15 mg/kg/dia")
            if doc==15 and op == '1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print ("La dosis es apropiada")

    def pacientesvih(self,VIH,amino,op,doc):
        global msg
        if (amino == 'Amikacina') and doc>0 and (Tu == False):
            if doc>15 or (op =='2 (12h)' or op=='3 (8h)') or doc<15:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda una dosis única de 15 mg/kg/dia. \n"
                    print("Se recomienda una dosis única de 15 mg/kg/dia")
            if doc==15 and op == '1 (24h)':
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis es apropiada. \n"
                    print ("La dosis es apropiada")
        if (amino == 'Estreptomicina') and doc>0 and (Tu == False):
            if doc>40 or doc<20:
                if MSG_NO == False:
                    msg[0] = msg[0] + "Se recomienda una dosis única entre 20-40 mg/kg/dia y que este tratamiento sea por 2 meses. \n"
                    print("Se recomienda una dosis única entre 20-40 mg/kg/dia y que este tratamiento sea por 2 meses ")
            if doc<=40 and doc>=20 :
                if MSG_NO == False:
                    msg[0] = msg[0] + "La dosis única es apropiada, se recomienda que continue el tratamiento por 2 meses. \n"
                    print("La dosis única es apropiada, se recomienda que continue el tratamiento por 2 meses")
        if ((amino == 'Gentamicina') or (amino =='Tobramicina') or (amino == 'Netilmicina')) and (doc>0):
            if MSG_NO == False:
                msg[0] = msg[0] + "Se recomienda que el tratamiento se realice con Amikacina con una dosis de 15 mg/kg/dia o Estreptomicina con una dosis entre 20-40 mg/kg/dia. \n"
                print("Se recomienda que el tratamiento se realice con Amikacina con una dosis de 15 mg/kg/dia o Estreptomicina con una dosis entre 20-40 mg/kg/dia")
    def diabeticoyobeso(self,amino,op,doc):
        global msg
        if MSG_NO == False:
            msg[0] = msg[0] + "Paciente con riesgo de ototoxicidad ,se recomienda realizar pruebas de evaluación con frecuencia. \n"
            print("Paciente con riesgo de ototoxicidad ,se recomienda realizar pruebas de evaluación con frecuencia ")
        self.dosisnormal(amino,op,doc) 
    
    def msg_no(self):
        self.textEdit.setText("No se recomienda el tratamiento con aminoglucosidos, por favor busque otras alternativas.")
        print('entré')
    def msg_si(self):
        self.textEdit.setText(msg[0])
        print('entré2')

    
    def procedimiento(self):
        amino = self.comboBox.currentText()
        op = self.comboBox_2.currentText()
        doc = float(self.dosistotalingresada.text())
        #self.dosisnormal(amino,op,doc)
        if Em == True or Mu == True:
            self.embarazada()
            self.escribir()
            return
        if Fr == True:
            self.fallosrenales(Fr,amino,op,doc,ClCr)
            self.escribir()
            return
        if Tu == True:
            self.tuberculosis(Tu,amino,op,doc)
        if Vi == True:
            self.pacientesvih(Vi,amino,op,doc) #REVISAR s
        if ((Ob == True) or (Di == True)) and Vi == False and Tu == False:
            self.diabeticoyobeso(amino,op,doc)
        if Ob == False and Di == False and Mu == False and Em == False and Mu == False and Fr == False and Tu == False and Vi == False and sic == False:
            self.dosisnormal(amino,op,doc)
        if sic == True:
            self.fallosrenales(sic,amino,op,doc,ClCr)
        self.escribir()

    def escribir(self):
        if MSG_NO == True:
            self.msg_no()
        if MSG_NO == False:
            self.msg_si()

    def show_dialog(self):
        dialog = Advertencia4(self)  # self hace referencia al padre
        dialog.show()

    def cerrar(self):
        dialog = Final(self)  # self hace referencia al padre
        dialog.show()

class Advertencia4(QDialog):
    def __init__(self,parent=None):
        super(Advertencia4, self).__init__(parent)
        loadUi('adverdia1.ui', self)
        self.buttonBox.accepted.connect(lambda: self.si())
        self.buttonBox.rejected.connect(lambda: self.reject)

    def si(self):
        self.abrirVentanatres()

    def abrirVentanatres(self):
        self.parent().parent().show()
        self.parent().close()

class Advertencia3(QDialog):
    def __init__(self,parent=None):
        super(Advertencia3, self).__init__(parent)
        loadUi('adverdia2.ui', self)
        self.buttonBox.accepted.connect(lambda: self.si())
        self.buttonBox.rejected.connect(lambda: self.reject)

    def si(self):
        self.abrirVentanados()

    def abrirVentanados(self):
        self.parent().parent().show()
        self.parent().close()

class Advertencia2(QDialog):
    def __init__(self,parent=None):
        super(Advertencia2, self).__init__(parent)
        loadUi('adverdia3.ui', self)
        self.buttonBox.accepted.connect(lambda: self.si())
        self.buttonBox.rejected.connect(lambda: self.reject)

    def si(self):
        self.abrirVentanaPrincipal()

    def abrirVentanaPrincipal(self):
        self.parent().parent().show()
        self.parent().close()

class Final(QDialog):
    def __init__(self,parent=None):
        super(Final, self).__init__(parent)
        loadUi('adfin.ui', self)
        self.buttonBox.accepted.connect(lambda: self.si())
        self.buttonBox.rejected.connect(lambda: self.reject)

    def si(self):
        self.Finalizar()

    def Finalizar(self):
        self.parent().close()
        self.close()





app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())