from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit,QApplication,QMessageBox, QMainWindow
import sys
import os
path = os.path.abspath('./')
sys.path.append(path)
from database.database_manager.products_database import ProductsData

class ConsultWindow(QMainWindow):
    def __init__(self,parent = None):
        super(ConsultWindow, self).__init__(parent = parent)
        self.setWindowTitle('Buscar')
        self.database_handle = ProductsData()
        self.setup_ui()
        self.data_out = None

    def setup_ui(self):
        self.id = QLineEdit()
        self.id.setPlaceholderText("Id") 
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("NOME")
        self.pesquisar = QPushButton("Pesquisar", clicked=self.search_product)
        self.name.returnPressed.connect(self.pesquisar.click)
        self.id.returnPressed.connect(self.pesquisar.click)
        widget = QWidget()
        layout = QHBoxLayout()
        
        layout.addWidget(self.id)
        layout.addWidget(self.name)
        layout.addWidget(self.pesquisar)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def search_product(self):
        self.data_out = self.verify_what_user_want_to_search()
    
    def verify_what_user_want_to_search(self):
        id_product = self.id.text()
        name_product = self.name.text()
        data = []
        if id_product and name_product:
            try:
                data = self.database_handle.get_product_by_id_and_name(id_product, name_product)
                self.parent().show_products(data)
                 
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao tentar buscar por id e por nome')
            if data:
                print(data)  
                return data
            else:
                self.show_dialog('Produto não encontrado')       
        
        elif id_product:
            try:
                print(id_product)
                data = self.database_handle.get_products_by_id(id_product)
                self.parent().show_products(data)
                
                
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao buscar pelo id')
            if data:
                print(data)  
                return data
            else:
                self.show_dialog('Produto não encontrado')
            
        elif name_product:
            try:
                data = self.database_handle.get_products_by_name(name_product)
                self.parent().show_products(data)
                
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao buscar pelo nome')
            if data:
                print(data) 
                 
                return data
            else:
                self.show_dialog('Produto não encontrado')
        
        else:
            self.show_dialog('Coloque alguma informação')
        
        
                 
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
     
if __name__ == "__main__":
    app = QApplication([])
    widget = ConsultWindow()
    widget.show()
    sys.exit(app.exec())