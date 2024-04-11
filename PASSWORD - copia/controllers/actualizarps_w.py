from PySide6.QtWidgets import QWidget
from views.actualizarps_ui import Ui_Form

class ActualizarpsWindow(QWidget, Ui_Form):
    
    def __init__(self):         
        super().__init__()
        self.setupUi(self) 

        #SIGNAL
        self.pushButton_actualizar.clicked.connect(self.actualizar_contrasena)
        self.pushButton_cancelar.clicked.connect (self.cerrar_ventana)  
    
    
    #def verificar_contrasena(contrasena_actual, nueva_contrasena):
	    #return contrasena_actual == nueva_contrasena
 
    
    def actualizar_contrasena(self):
        contrasena_actual = "contrasena123"  # Define la contraseña actual (puedes cambiarla)
        contrasena_actual_ingresada = self.campopssact_lineEdit.text()
        nueva_contrasena = self.campopssnew_lineEdit.text()
        confirmar_contrasena= self.campopssnewconf_lineEdit.text()
        
        if  contrasena_actual== contrasena_actual_ingresada:
                self.alerta1_label.setText("Ingresa Nueva Contraseña")
            
        else:
            self.alerta1_label.setText("Las contraseñas no coinciden. Inténtalo de nuevo.")
            #print("Las contraseñas no coinciden. Inténtalo de nuevo.")
        
        if nueva_contrasena == confirmar_contrasena:
                self.alerta2_label.setText("Contraseña actualizada correctamente.")
                #print("Contraseña actualizada correctamente.")
        else:
                self.alerta2_label.setText("Las contraseñas no coinciden. Inténtalo de nuevo.")
                #print("Las contraseñas no coinciden. Inténtalo de nuevo.")
    

# Ejecuta la función para cambiar la contraseña
    #actualizar_contrasena()


    def cerrar_ventana(self):
        self.close()