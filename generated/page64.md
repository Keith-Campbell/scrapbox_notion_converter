# Distributionally Robust Neural Networks
Distributionally Robust Neural Networks

#機械学習 #数理最適化 #ニューラルネットワーク #ロバスト最適化



**参考記事　https://www.acceluniverse.com/blog/developers/2020/01/distributionally-robust-neural-networks.html

**原著　https://openreview.net/attachment?id=ryxGuJrFvS&name=original_pdf



　DROの考え方を機械学習に応用した非常に面白いモデル。



### 動機

　平均的な汎化誤差の最小化は正則化項を加える手法が一般的だが、時に極端なインプットに対して誤認する可能性が高まる場合がある。

　例えば画像認識の問題で『水辺の鳥(waterbird)が写っている写真（背景：水辺vs野原=9:1）』と『野原の鳥(landbird)が写っている写真（背景：水辺vs野原=1:9）』を訓練データとして、テストデータで『野原の背景に水辺の鳥が写っている写真』や『水辺の背景に野原の鳥が写っている写真』に対する認識精度が上がらないという問題が起こる。

[https://scrapbox.io/files/606691ef11c3c40022ad6c0d.png

　このような事例は特徴ベクトルの次元がサンプルよりも多いときに過適合として起こる。



### 手法





### 気になる点

　DROに定式化し、ambiguity set を線形結合と仮定したため下記のようなmin-max問題：

[https://scrapbox.io/files/606693a0521a660022bf8ef1.png

として帰着できたが、残差関数は$gに関してどんな数学的性質を持っているのだろうか...

 もし、nonconcaveだとかであれば、これに対する変分不等式の手法を考えるのもありかもしれない。

 ambiguity set が「考えうる分布の線形結合」というのがどれほど一般的なのかがわからない。



