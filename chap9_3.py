list1 = [['トップガン', 'リスキービジネス', 'マイノリティリポート'], ['タイタニック', 'The Revenant', 'インセプション'], ['トレイニングデイ', 'マンオンファイア', 'フライト']]

import csv

with open('chap9_4.csv', 'w', encoding = 'cp932') as f:
    w = csv.writer(f, delimiter =',')

    for row in list1:
        w.writerow(row)
