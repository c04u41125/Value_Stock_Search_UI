from PyQt5 import QtWidgets  #導入PyQt5函式庫使用UI介面
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main import Ui_Stock_Search            #導入main.py使用UI介面
import sys  
import webbrowser 
import time       
import threading                 
from stock_range import stock_dic,stock_code,stock_name          #導入stock_range.py使用stock_dic,stock_code,stock_name
from PY_B import now_price                #導入PY_B 的function
from PY_C import DB_GET                      #導入PY_C 的function
from PY_D import SAVE_info
from PY_E import LOAD_info


def pic_click(event):   #圖片點擊動作
    message=QMessageBox()
    message.setWindowTitle('error')
    message.setInformativeText('請在輸入框輸入股票代號或名稱')
    message.exec_()    

def action():           #按鈕動作
    global code
    global ans
    user_input=ui.input.text() #user_input=輸入框值
    if user_input in stock_name:
        code=stock_dic[user_input]
        DB=threading.Thread(target=DB_GET,args=(code,))
        PR=threading.Thread(target=now_price,args=(code,))
        DB.start()
        PR.start()
        DB.join
        PR.join
        i = DB_GET(code)
        p = now_price(code)
        ans = f"{i}\n\n{p}"
        ui.output.setText(ans)
    elif user_input in stock_code:
        code=user_input
        DB=threading.Thread(target=DB_GET,args=(code,))
        PR=threading.Thread(target=now_price,args=(code,))
        DB.start()
        PR.start()
        DB.join
        PR.join
        i = DB_GET(code)
        p = now_price(code)
        ans = f"{i}\n\n{p}"
        ui.output.setText(ans)


    else:
        ui.output.setText('輸入股票不在範圍內')

def jump_insert_save():      #彈跳輸入框
    message = QMessageBox()
    message.setWindowTitle(f"請輸入英文名字+生日四碼")
    dialog = QDialog()
    dialog.setWindowTitle('')
    layout = QVBoxLayout(dialog)
    lineedit = QLineEdit(dialog)
    layout.addWidget(lineedit)
    dialog.setLayout(layout)
    message.layout().addWidget(dialog)
    message.exec_()    
    userid=lineedit.text()
    try:
        last_five_chars = userid[-5:]  # 提取最後五個字元
        letter = last_five_chars[0]  # 第一個字元為英文
        numbers = last_five_chars[1:]  # 後四個字元為數字
        if letter.isalpha() and numbers.isdigit():
            LI=threading.Thread(target=SAVE_info,args=(userid,code,ans,))
            LI.start()
            LI.join
        else:
            QMessageBox.warning(None, "錯誤", "請輸入英文名字+生日四碼")
    except:
        QMessageBox.warning(None,"錯誤","請輸入英文名字+生日四碼")
def jump_insert_load():
    message = QMessageBox()
    message.setWindowTitle(f"請輸入英文名字+生日四碼")
    dialog = QDialog()
    dialog.setWindowTitle('')
    layout = QVBoxLayout(dialog)
    lineedit = QLineEdit(dialog)
    layout.addWidget(lineedit)
    dialog.setLayout(layout)
    message.layout().addWidget(dialog)
    message.exec_()    
    userid=lineedit.text()
    try:
        last_five_chars = userid[-5:]  # 提取最後五個字元
        letter = last_five_chars[0]  # 第一個字元為英文
        numbers = last_five_chars[1:]  # 後四個字元為數字
        if letter.isalpha() and numbers.isdigit():
            LI=threading.Thread(target=LOAD_info,args=(userid,))
            LI.start()
            LI.join
            a=LOAD_info(userid)
            return a
        else:
            QMessageBox.warning(None, "錯誤", "請輸入英文名字+生日四碼")
    except:
        QMessageBox.warning(None,"錯誤","請先建立存檔")
        # print(Exception)

def connet(event):
    webbrowser.open('https://lin.ee/UzYF7lj')
def save():
    jump_insert_save()
    ui.output.setText('已存檔')
def load():
    # jl=threading.Thread(target=jump_insert_load)
    # jl.start()
    # jl.join
    dk=jump_insert_load()
    print(dk)
    ans="<a href='"+dk+"' style='color:blue'>點擊此處下載</a>"
    # time.sleep(5)
    ui.output.setText(ans)
    ui.output.setOpenExternalLinks(True)
    print('end')
def read_me():
    info=('@查詢器只限查閱台灣上市櫃公司@'+'\n'+'\n'+'@詳細清單可以參閱左側選單中的股票清單@'+'\n'+'\n'+
        '1.在說明鈕左側框輸入要查詢的股票代號或名稱'+'\n'+'\n'+'2.按下牛牛圖進行查詢'+'\n'+'\n'+'3.查詢完的資訊可以點擊存檔按鈕進行個人化雲端儲存'+
        '\n'+'\n'+'4.如果已經有個人化雲端儲存紀錄，可以點擊讀檔按鈕進行讀取'+'\n'+'\n'+'@本查詢器提供資訊僅供參考，不負任何投資盈虧責任@')
    message=QMessageBox()
    message.setWindowTitle('Readme')
    message.setInformativeText(info)
    message.exec_()    
def timetime():
    while True:
        current_time = time.localtime()
        T = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
        ui.TIME_TIME.setText(T)
        time.sleep(1)  # 暫停 1 秒




def combo():
    if ui.combox.currentIndex()==1:
        message=QMessageBox()
        message.setWindowTitle('水泥工業')
        pixmap = QPixmap('range_1.png')
        message.setIconPixmap(pixmap)
        message.exec_()
    elif ui.combox.currentIndex()==2:
        message=QMessageBox()
        message.setWindowTitle('食品工業')
        pixmap = QPixmap('range_2.png')
        message.setIconPixmap(pixmap)
        message.exec_()    
    elif ui.combox.currentIndex()==3:
        message=QMessageBox()
        message.setWindowTitle('塑膠工業')
        pixmap = QPixmap('range_3.png')
        message.setIconPixmap(pixmap)
        message.exec_()   
    elif ui.combox.currentIndex()==4:
        message=QMessageBox()
        message.setWindowTitle('紡織纖維')
        pixmap = QPixmap('range_4.png')
        message.setIconPixmap(pixmap)
        message.exec_()   
    elif ui.combox.currentIndex()==5:
        message=QMessageBox()
        message_2=QMessageBox()
        message.setWindowTitle('電機機械')
        message_2.setWindowTitle('電機機械')
        pixmap = QPixmap('range_5_1.png')
        pixmap_2=QPixmap('range_5_2.png')
        message.setIconPixmap(pixmap)
        message_2.setIconPixmap(pixmap_2)
        message.exec_() 
        message_2.exec_()
    elif ui.combox.currentIndex()==6:
        message=QMessageBox()
        message.setWindowTitle('電器電纜')
        pixmap = QPixmap('range_6.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==7:
        message=QMessageBox()
        message.setWindowTitle('化學工業')
        pixmap = QPixmap('range_7.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==8:
        message=QMessageBox()
        message_2=QMessageBox()
        message.setWindowTitle('生技醫療')
        message_2.setWindowTitle('生技醫療')
        pixmap = QPixmap('range_8_1.png')
        pixmap_2=QPixmap('range_8_2.png')
        message.setIconPixmap(pixmap)
        message_2.setIconPixmap(pixmap_2)
        message.exec_() 
        message_2.exec_()
    elif ui.combox.currentIndex()==9:
        message=QMessageBox()
        message.setWindowTitle('玻璃陶瓷')
        pixmap = QPixmap('range_9.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==10:
        message=QMessageBox()
        message.setWindowTitle('造紙工業')
        pixmap = QPixmap('range_10.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==11:
        message=QMessageBox()
        message.setWindowTitle('鋼鐵工業')
        pixmap = QPixmap('range_11.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==12:
        message=QMessageBox()
        message.setWindowTitle('橡膠工業')
        pixmap = QPixmap('range_12.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==13:
        message=QMessageBox()
        message.setWindowTitle('汽車工業')
        pixmap = QPixmap('range_13.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==14:
        message=QMessageBox()
        message_2=QMessageBox()
        message.setWindowTitle('半導體業')
        message_2.setWindowTitle('半導體業')
        pixmap = QPixmap('range_14_1.png')
        pixmap_2=QPixmap('range_14_2.png')
        message.setIconPixmap(pixmap)
        message_2.setIconPixmap(pixmap_2)
        message.exec_() 
        message_2.exec_()
    elif ui.combox.currentIndex()==15:
        message=QMessageBox()
        message.setWindowTitle('電腦周邊')
        pixmap = QPixmap('range_15.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==16:
        message=QMessageBox()
        message.setWindowTitle('光電業')
        pixmap = QPixmap('range_16.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==17:
        message=QMessageBox()
        message_2=QMessageBox()
        message.setWindowTitle('通信網路')
        message_2.setWindowTitle('通信網路')
        pixmap = QPixmap('range_17_1.png')
        pixmap_2=QPixmap('range_17_2.png')
        message.setIconPixmap(pixmap)
        message_2.setIconPixmap(pixmap_2)
        message.exec_() 
        message_2.exec_()
    elif ui.combox.currentIndex()==18:
        message=QMessageBox()
        message_2=QMessageBox()
        message.setWindowTitle('電子組件')
        message_2.setWindowTitle('電子組件')
        pixmap = QPixmap('range_18_1.png')
        pixmap_2=QPixmap('range_18_2.png')
        message.setIconPixmap(pixmap)
        message_2.setIconPixmap(pixmap_2)
        message.exec_() 
        message_2.exec_()
    elif ui.combox.currentIndex()==19:
        message=QMessageBox()
        message.setWindowTitle('電子通路')
        pixmap = QPixmap('range_19.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==20:
        message=QMessageBox()
        message.setWindowTitle('資訊服務')
        pixmap = QPixmap('range_20.png')
        message.setIconPixmap(pixmap)
        message.exec_()
    elif ui.combox.currentIndex()==21:
        message=QMessageBox()
        message.setWindowTitle('其他電子')
        pixmap = QPixmap('range_21.png')
        message.setIconPixmap(pixmap)
        message.exec_()  
    elif ui.combox.currentIndex()==22:
        message=QMessageBox()
        message.setWindowTitle('建材營造')
        pixmap = QPixmap('range_22.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==23:
        message=QMessageBox()
        message.setWindowTitle('航運業')
        pixmap = QPixmap('range_23.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==24:
        message=QMessageBox()
        message.setWindowTitle('觀光事業')
        pixmap = QPixmap('range_24.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==25:
        message=QMessageBox()
        message.setWindowTitle('保險業')
        pixmap = QPixmap('range_25.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==26:
        message=QMessageBox()
        message.setWindowTitle('貿易百貨')
        pixmap = QPixmap('range_26.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==27:
        message=QMessageBox()
        message.setWindowTitle('油電燃氣')
        pixmap = QPixmap('range_27.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==28:
        message=QMessageBox()
        message.setWindowTitle('其他類')
        pixmap = QPixmap('range_28_1.png')
        message.setIconPixmap(pixmap)
        message.exec_()
        message_2=QMessageBox()
        message_2.setWindowTitle('其他類')
        pixmap_2=QPixmap('range_28_2.png')
        message_2.setIconPixmap(pixmap_2) 
        message_2.exec_()
    elif ui.combox.currentIndex()==29:
        message=QMessageBox()
        message.setWindowTitle('文化創意')
        pixmap = QPixmap('range_29.png')
        message.setIconPixmap(pixmap)
        message.exec_()     
    elif ui.combox.currentIndex()==30:
        message=QMessageBox()
        message.setWindowTitle('農業科技')
        pixmap = QPixmap('range_30.png')
        message.setIconPixmap(pixmap)
        message.exec_()    
    elif ui.combox.currentIndex()==31:
        message=QMessageBox()
        message.setWindowTitle('電子商務')
        pixmap = QPixmap('range_31.png')
        message.setIconPixmap(pixmap)
        message.exec_()  
    elif ui.combox.currentIndex()==32:
        message=QMessageBox()
        message.setWindowTitle('金控業')
        pixmap = QPixmap('range_32.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==33:
        message=QMessageBox()
        message.setWindowTitle('銀行業')
        pixmap = QPixmap('range_33.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    elif ui.combox.currentIndex()==34:
        message=QMessageBox()
        message.setWindowTitle('證券業')
        pixmap = QPixmap('range_34.png')
        message.setIconPixmap(pixmap)
        message.exec_() 
    else:
        pass  
def button_connet():
    ui.pushButton.clicked.connect(action) #牛牛背後按鍵
    ui.save.clicked.connect(save) #存檔
    ui.load.clicked.connect(load) #讀檔
    ui.readme.clicked.connect(read_me)
    ui.background.mouseReleaseEvent=pic_click #點背景圖
    ui.combox.addItems(['水泥工業','食品工業','塑膠工業','紡織纖維','電機機械','電器電纜','化學工業','生技醫療','玻璃陶瓷','造紙工業',
                        '鋼鐵工業','橡膠工業','汽車工業','半導體業','電腦周邊','光電業','通信網路','電子組件','電子通路','資訊服務',
                        '其他電子','建材營造','航運業','觀光事業','保險業','貿易百貨','油電燃氣','其他類','文化創意','農業科技','電子商務'
                        ,'金控業','銀行業','證券業'])
    ui.combox.activated.connect(combo)
    ui.logo.mouseReleaseEvent=connet #點logo圖
    # timetime()
app = QtWidgets.QApplication(sys.argv)
Stock_Search = QtWidgets.QMainWindow()
ui = Ui_Stock_Search()
ui.setupUi(Stock_Search)
t1=threading.Thread(target=timetime)
t1.start()
button_connet()
Stock_Search.show()
sys.exit(app.exec_())





