"""""
 _____             _            _             _  _    _         __ _____      
/  __ \           | |          | |           (_)| |  | |       / / |____ |     
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

from PySide6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QDockWidget,
    QTextEdit,
    QVBoxLayout,
    QApplication,
    QLabel
)
from PySide6.QtGui import QAction, QIcon, Qt, QDesktopServices, QPalette, QColor,QPixmap,QImage
from PySide6.QtCore import QUrl
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.login import *
from interfaces.products.products_window import ProductsPage
from interfaces.stock.window_stock import StockPage
from interfaces.checkout.cashier_window import CheckoutPage
from interfaces.mesurament_unity.mesurament_unit_window import WindowUnit
from interfaces.category.category_window import CategoryWindow
class MainPage(QMainWindow):
    def __init__(self, parent=None):
        super(MainPage,self).__init__(parent)
        self.image_shopping_cart = r'images/shopping-cart.png'
        self.image_warehouse = r'images/warehouse.png'
        self.image_cash_register = r'images/cash-register.png'
        self.image_box = r'images/box.png'
        self.image_rule = r'images/ruler.png'
        self.category_image = r'images/category.png'
        self.smartedge_logo = r'images/smartedge.png'
        #config of the window
        self.setWindowIcon(QtGui.QIcon(self.smartedge_logo))
        self.setWindowTitle('SmartEdge ERP')
        self.setMinimumSize(1400,720)
        self.config_the_menubar()
        # Set up the main window and sidebar
        self.create_main_layout()
        self.set_dark_mode('enable')
        
    def create_main_layout(self):
        # Create a QWidget for the main content
        self.layout_vertical = QVBoxLayout()
        
        img = QImage(self.smartedge_logo)
        pixmap = QPixmap(img.scaledToWidth(225))
        label = QLabel()
        label.setPixmap(pixmap) 
        label.setAlignment(Qt.AlignCenter)
        self.layout_vertical.addWidget(label)
        layout_botao = QHBoxLayout()
        
        self.button_products = QPushButton("Produtos", clicked=self.open_products_window)
        self.button_estoque = QPushButton("Estoque", clicked=self.abrir_janela_estoque)
        self.button_caixa = QPushButton("Caixa", clicked=self.abrir_caixa)
        self.button_mesurement = QPushButton("Unidades de medida", clicked=self.open_mesurement_unit_window)
        self.button_category = QPushButton("Categorias", clicked=self.open_category_window)
        
        self.set_icons_and_resize_and_alter_font(self.button_caixa, self.image_cash_register)
        self.set_icons_and_resize_and_alter_font(self.button_estoque, self.image_warehouse)
        self.set_icons_and_resize_and_alter_font(self.button_products, self.image_box)
        self.set_icons_and_resize_and_alter_font(self.button_mesurement, self.image_rule)
        self.set_icons_and_resize_and_alter_font(self.button_category, self.category_image)
        
        layout_botao.addWidget(self.button_estoque)
        layout_botao.addWidget(self.button_products)
        layout_botao.addWidget(self.button_caixa)
        layout_botao.addWidget(self.button_mesurement)
        layout_botao.addWidget(self.button_category)
        
        self.layout_vertical.addLayout(layout_botao)

        # Set the main window widget
        main_widget = QWidget()
        main_widget.setLayout(self.layout_vertical)
        self.setCentralWidget(main_widget)
        self.create_sidebar()  

    def create_sidebar(self):
        # Create a QDockWidget for the sidebar
        self.sidebar = QDockWidget("Sidebar", self)
        self.sidebar.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.sidebar.move(0, 0)
        # Create a QTextEdit widget to hold the contents of the sidebar
        self.sidebar_contents = QTextEdit()
        self.sidebar_contents.setReadOnly(True)
        self.sidebar.setWidget(self.sidebar_contents)
        self.sidebar.setFixedWidth(200)
        # Add a button widget to the sidebar to open the GitHub link
        self.github_button = QPushButton("GitHub")
        self.github_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/vbsx")))
        self.reset_sidebar_button = QPushButton("Voltar Ao Menu")
        self.reset_sidebar_button.clicked.connect(self.reset_layout)
        
        #Label Version
        self.label = QLabel("Beta v.0.0.0.1")
        
        # Add the buttons to the sidebar layout
        self.sidebar_contents_layout = QVBoxLayout()
        self.sidebar_contents_layout.addWidget(self.github_button)
        self.sidebar_contents_layout.addWidget(self.reset_sidebar_button)
        self.sidebar_contents_layout.addWidget(self.label)
        self.sidebar_contents_layout.addStretch()
        
        # Create a container widget to hold the sidebar layout
        self.sidebar_contents_container = QWidget()
        self.sidebar_contents_container.setLayout(self.sidebar_contents_layout)
        self.sidebar.setWidget(self.sidebar_contents_container)
        
        # Add the sidebar to the left dock widget area
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)
        # Add the sidebar to the left dock widget area and set it as fixed
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)
        self.sidebar.setFixedHeight(self.height())
        self.sidebar.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.NoDockWidgetFeatures)

    def reset_layout(self):
        # Remove all widgets from the sidebar layout
        while self.sidebar_contents_layout.count() > 0:
            item = self.sidebar_contents_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
        # Remove the sidebar from the dock widget area
        self.removeDockWidget(self.sidebar)
        self.sidebar.setParent(None)
        
        # Remove the central widget
        self.centralWidget().setParent(None)
        # Recreate the layout
        self.create_main_layout()
        
    def set_icons_and_resize_and_alter_font(self, item, icon):
        item.setStyleSheet("padding :30px;font-size:18px;margin-top:30px;")
        item.setIcon(QIcon(icon))
        item.setIconSize(QtCore.QSize(64,64))
    
    def logoff(self):
        self.close()
        self.login = LoginPage()
        self.login.show()

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)

    def config_the_menubar(self):   
        button_action_logoff = QAction("logoff", self)
        button_action_logoff.triggered.connect(self.logoff)
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('self.teste')
        log = bar.addMenu('Usuário')
        log.addAction(button_action_logoff)
       
    def open_products_window(self):
        self.w_product = ProductsPage()
        self.setCentralWidget(self.w_product)
        
        
    def abrir_janela_estoque(self):
        self.janela_estoque = StockPage()
        self.setCentralWidget(self.janela_estoque)
        
    def abrir_caixa(self):
        self.janela_caixa = CheckoutPage()
        self.setCentralWidget(self.janela_caixa)
        
    def open_mesurement_unit_window(self):
        self.mesurement_window = WindowUnit(self)
        self.setCentralWidget(self.mesurement_window)
    
    def open_category_window(self):
        self.category = CategoryWindow(self)
        self.setCentralWidget(self.category)    
        
    def set_dark_mode(self, enabled):
        if enabled:
            qApp.setStyle("Fusion")
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)
            dark_palette.setColor(QPalette.PlaceholderText, Qt.white)
            qApp.setPalette(dark_palette)
            
        else:
            qApp.setStyle("Fusion")
            qApp.setPalette(QApplication.style().standardPalette())


if __name__ == "__main__":
    app = QApplication([])
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())