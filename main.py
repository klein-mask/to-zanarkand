from scraping import HeadlessScraping
from doremi import Doremi


def main():
    hs = HeadlessScraping(
        url='https://composer-instruments.com/scale-and-frequency/')

    # 解析結果を受け取る
    soup = hs.beatifulsoup()

    # 表を取得
    tr_list = soup.find_all('table')[0].tbody.find_all('tr')[1:]

    # ドレミのインスタンス
    doremi = Doremi()
    # 12個ずつに分ける(キーが上がるため)
    tmp = []
    for tr in tr_list:
        freq = float(tr.find_all('td')[3].text)
        tmp.append(freq)

        if len(tmp) == 12:
            doremi.addFrequency(tmp)
            tmp = []


if __name__ == "__main__":
    main()
