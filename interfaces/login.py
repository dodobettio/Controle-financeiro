"""""
 _____             _            _             _  _    _         __ _____      
/  __ \           | |          | |           (_)| |  | |       / /|____ |     
| /  \/  ___    __| |  ___   __| | __      __ _ | |_ | |__    / /     / /     
| |     / _ \  / _` | / _ \ / _` | \ \ /\ / /| || __|| '_ \  < <      \ \     
| \__/\| (_) || (_| ||  __/| (_| |  \ V  V / | || |_ | | | |  \ \ .___/ /     
 \____/ \___/  \__,_| \___| \__,_|   \_/\_/  |_| \__||_| |_|   \_\\____/      
                                                                              
                                                                              
          _____         _     _____                _____  _____  _____  _____ 
   ____  |  _  |       | |   |_   _|              / __  \|  _  |/ __  \|____ |
  / __ \ | | | |  __ _ | | __  | |   _ __    ___  `' / /'| |/' |`' / /'    / /
 / / _` || | | | / _` || |/ /  | |  | '_ \  / __|   / /  |  /| |  / /      \ \
| | (_| |\ \_/ /| (_| ||   <  _| |_ | | | || (__  ./ /___\ |_/ /./ /___.___/ /
 \ \__,_| \___/  \__,_||_|\_\ \___/ |_| |_| \___| \_____/ \___/ \_____/\____/ 
  \____/    
  
                            github.com/vbsx    
                            https://www.oakbox.com.br
                            https://www.linkedin.com/in/oak-borges                                                             
 """""  
import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.main_page import MainPage
from database.database_manager.products_database import ProductsData
from passlib.hash import sha256_crypt

class LoginPage(QtWidgets.QWidget):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.database_get = ProductsData()
        self.initUI()

    def initUI(self):
        # Configurações da janela
        key_icon_path = r'images/key-security.png'
        self.setWindowIcon(QtGui.QIcon(key_icon_path))
        self.setWindowTitle('Logar')
        self.resize(400, 200)

        # Criação dos objetos de entrada de texto e mensagens
        self.username_input = QtWidgets.QLineEdit()
        self.username_message = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.username_message.setText("Coloque o usuário")
        self.password_input = QtWidgets.QLineEdit()
        self.password_message = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.password_message.setText("Coloque a senha")
        self.logar = QtWidgets.QPushButton("Logar", clicked=self.login_process)
        self.password_input.returnPressed.connect(self.logar.click)
        # Define que a entrada de senha não mostrará o que está sendo digitado
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        # Define as folhas de estilo para o modo claro e modo escuro
        self.light_stylesheet = "padding: 15px;"
        self.dark_stylesheet = "padding: 15px; background-color: #333; color: #EEE;"
        # Criação do botão de modo escuro
        self.dark_mode_checkbox = QtWidgets.QCheckBox("Dark Mode")
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)

        # Adição dos elementos à página usando um QVBoxLayout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.username_message)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_message)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.logar)
        self.layout.addWidget(self.dark_mode_checkbox)

        # Set dark mode stylesheet to the layout and widgets
        self.toggle_dark_mode()

    def set_stylesheet(self, stylesheet):
        """Atualiza a folha de estilo da janela e seus elementos"""
        self.setStyleSheet(stylesheet)
        self.username_input.setStyleSheet(stylesheet)
        self.logar.setStyleSheet(stylesheet)
        self.username_message.setStyleSheet(stylesheet)
        self.password_message.setStyleSheet(stylesheet)
        self.password_input.setStyleSheet(stylesheet)

    def toggle_dark_mode(self):
        """Ativa ou desativa o modo escuro, atualizando a folha de estilo"""
        if self.dark_mode_checkbox.isChecked():
            self.set_stylesheet(self.light_stylesheet)
        else:
            self.set_stylesheet(self.dark_stylesheet)

    def open_main_page(self):
        self.main_page = MainPage()
        self.main_page.show()

    def login_process(self):
        if self.verify_if_field_arent_null() == True:
            if self.verify_credentials() == True:
                self.close()
                self.open_main_page()
            else:
                self.show_dialog('Usuário e senha não está correto')
        else:
            self.show_dialog('Coloque o usuário e a senha antes de continuar!')
                  
    def verify_if_field_arent_null(self):
        user = self.username_input.text()
        password = self.password_input.text()
        if user and password:
            return True
        else:
            return False
    #TODO senha_criptografada = sha256_crypt.hash(senha_original)
    
    def verify_if_password_is_corect(self, user, password_informed):
        correct_password_encrypted = self.database_get.get_password_by_user(user)
        returned_some_password = len(correct_password_encrypted) > 0
        
        if returned_some_password:
            if sha256_crypt.verify(password_informed, correct_password_encrypted[0][0]):
                print("Senha válida!")
                return True
     
    def verify_credentials(self):
        user = self.username_input.text()
        password = self.password_input.text()
        if self.verify_if_password_is_corect(user, password):
            return True        

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = LoginPage()
    widget.show()
    sys.exit(app.exec())