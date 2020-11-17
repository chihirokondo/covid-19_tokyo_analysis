# covid-19_tokyo_analysis
東京都における新型コロナウィルスの感染状況を都の公開している[サイト](https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv)から取得し、解析するコード。

## 実行環境
jupyter (python3) 環境が必要です。

### サードパーティライブラリ
以下のサードパーティライブラリを使用しています。
- requests
- matplotlib
- pandas

## 使い方

### データの取得
http_request.pyを実行することで、HTTPリクエストを送信して、都の最新データ (csvファイル) が取得できます。

```Bash
python3 http_request.py
```

covid-19_tokyo.csvというファイルが生成されます。

短時間に多数回送信するとサーバやネットワークに負荷がかかり、DoS攻撃と認識されてしまう可能性があるので、必要な時だけ使ってください。
基本的に多くても一日一回で十分です。

### 解析

jupyter環境でcovid-19_tokyo.ipynbを実行してください。