from scraping import HeadlessScraping
from doremi import Doremi
from audio import Audio


doremi = Doremi()


def main():
    soup = HeadlessScraping(
        url='https://composer-instruments.com/scale-and-frequency/').beatifulsoup()

    # 表を取得
    tr_list = soup.find_all('table')[0].tbody.find_all('tr')[1:]

    # 12個ずつに分ける(キーが上がるため)
    tmp = []
    for tr in tr_list:
        freq = float(tr.find_all('td')[3].text)
        tmp.append(freq)
        if len(tmp) >= 12:
            doremi.addFrequency(tmp)
            tmp = []

    play_zanarkand()


def play_zanarkand():
    audio = Audio()

    audio.open()

    # 以下楽譜を参考に入力ベースのキーはA3とする
    BASE_KEY = audio.A3

    audio.play(audio.freq(BASE_KEY + 1, 'ミ'), audio.L2)
    audio.play(audio.freq(BASE_KEY, 'ミ'), audio.L2)
    audio.play(audio.freq(BASE_KEY, 'ソ'), audio.L2)
    audio.play(audio.freq(BASE_KEY, 'シ'), audio.L2)
    audio.play(audio.freq(BASE_KEY + 1, 'ミ'), audio.L2)
    audio.play(audio.freq(BASE_KEY + 1, 'ファ+'), audio.L2)
    audio.play(audio.freq(BASE_KEY + 1, 'ソ'), audio.L2)


if __name__ == '__main__':
    main()
