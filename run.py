#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 17:13
# @Author  : Lqq/linqingqing
# @Site    :
# @File    : run.py
# @Software: PyCharm

import sys
import os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import traceback
import requests
import time
import json

from bs4 import BeautifulSoup as bs
from PyQt5 import QtCore, QtWidgets
from view.movie import Ui_Form
from util.database import Db
from util.web import WebUrl


class Worker(QtCore.QThread):
    sig = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            count = self.num*20
            url = WebUrl().get_url(count, "电影")
            response = requests.get(url, headers=WebUrl().headers)
            response.encoding = 'utf-8'
            data = response.text
            jdata = json.loads(data)
            if response.status_code == 200:
                self.num = self.num + 1
                list = jdata['data']
                self.sig.emit(list)
                time.sleep(1)


class Combosel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Combosel, self).__init__(parent)

        self.ui_sel = Ui_Form()
        self.ui_sel.setupUi(self)

        # 清理结果集
        self.ui_sel.textEdit.clear()

        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        self.thread = Worker()
        self.thread.sig.connect(self.get_data)

        # 连接自己的槽函数
        self.ui_sel.pushButton.clicked.connect(self.onActivatedpushButton)

    # 获取网页数据
    def get_data(self, dicts):
        try:
            host = self.ui_sel.host.text()
            port = self.ui_sel.port.text()
            user = self.ui_sel.user.text()
            passwd = self.ui_sel.passwd.text()
            db = self.ui_sel.db.text()
            charset = self.ui_sel.charset.text()
            for i in dicts:
                response = requests.get(i['url'], headers=WebUrl().headers)
                response.encoding = 'utf-8'
                data = response.content
                if response.status_code == 200:
                    soup = bs(data, 'html.parser')
                    span = soup.find("span", attrs={"property": "v:initialReleaseDate"})
                    release_date = ''
                    if span:
                        release_date = span.get_text()
                    else:
                        release_date =  ''
                    if Db(host, port, user, passwd, db, charset).get_website(i['title']) == 0:
                        Db(host, port, user, passwd, db, charset).insert_movie(i['rate'], release_date,i['title'])
                        self.ui_sel.textEdit.insertPlainText("标题：" + i['title'] + "数据添加成功\n")

        except:
            traceback.print_exc()

    # 点击
    def onActivatedpushButton(self):
        try:

            self.thread.start()
        except:
            traceback.print_exc()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        Appcombosel = Combosel()
        Appcombosel.show()
        sys.exit(app.exec_())
    except:
        traceback.print_exc()
