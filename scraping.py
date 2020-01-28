# 必要モジュールをインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import chromedriver_binary


class HeadlessScraping:

    # コンストラクタの引数にはスクレイピングしたいURLを指定
    def __init__(self, *, url):
        # ヘッドレスブラウザにする
        options = Options()
        options.add_argument('--headless')
        self.__driver = webdriver.Chrome(options=options)
        self.__url = url
        self.__soup = None
        self.__data = {}

    # BeautifulSoupのインスタンスを返すメソッド
    def beatifulsoup(self):
        # 指定したURLのページを開く
        self.__driver.get(self.__url)

        # BeautifulSoupに読み込ませる、パーサーはlxmlで基本的にはトライして、ダメならhtml5libを指定
        try:
            self.__soup = BeautifulSoup(self.__driver.page_source, "lxml")
        except:
            self.__soup = BeautifulSoup(self.__driver.page_source, "html5lib")

        # ブラウザ終了
        self.__driver.close()

        return self.__soup
