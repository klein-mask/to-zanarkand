from scraping import HeadlessScraping
from doremi import Doremi
from audio import Audio
import time
from extension import Pycolor
import emoji

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
    print(Pycolor.RED + '最後かもしれないだろ、' + Pycolor.END)

    time.sleep(3)

    print(Pycolor.RED + 'だから全部話しておきたいんだ。' + Pycolor.END)

    print('\n')
    print(emoji.emojize(':bell:', use_aliases=True))
    print('\n')

    time.sleep(3)

    audio = Audio()

    audio.open()

    # 以下楽譜を参考に入力ベースのキーはA3とする
    BASE_KEY = doremi.A4

    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ソ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'シ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 2, 'ファ+'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 2, 'ソ'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY + 2, 'レ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'レ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ラ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 2, 'レ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 2, 'ファ+'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY + 1, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ラ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'レ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'ミ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'レ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'ソ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 2, 'ド'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ソ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'レ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'レ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ソ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ソ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ラ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY + 1, 'ソ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ラ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'シ'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'ソ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ファ+'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'レ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY + 1, 'ミ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY + 1, 'レ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L2)

    print('\n')
    print(emoji.emojize(':mega:', use_aliases=True))
    print('\n')

    audio.play(doremi.freq(BASE_KEY, 'ソ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY, 'ラ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'シ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'ラ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY + 1, 'レ'), audio.L4)
    audio.play(doremi.freq(BASE_KEY, 'ソ'), audio.L2)
    audio.play(doremi.freq(BASE_KEY, 'ソ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY, 'ファ+'), audio.L8)
    audio.play(doremi.freq(BASE_KEY, 'レ'), audio.L8)
    audio.play(doremi.freq(BASE_KEY, 'ミ'), audio.L4)


if __name__ == '__main__':
    main()
