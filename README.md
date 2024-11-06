# LibreOfficeCalc Register設定用プログラム

LibreOfficeCalcを使ってレジスタを設定するためのデータを
生成するプログラム。

AlmaLinux 8、9、ubuntu 2024.04 LTSで動作を確認しています。

## Libreofficeマクロのドキュメント

- https://wiki.documentfoundation.org/Macros/Python_Guide/ja
- https://wiki.documentfoundation.org/Macros/Python_Guide/My_first_macro/ja

## LibreOffice Calcインストール

### AlmaLinux 8, 9

```
# dnf install libreoffice-calc
```

### Ubuntu 2024.04 LTS

```
apt install libreoffice-calc libreoffice-script-provider-python
```

## LibreOffice Calcの起動

デスクトップ環境のメニューバーからLibreOffice Calcを起動することも可能だが、
pythonマクロ内からprint()関数でデバッグ風文字列を出力 しているので
ターミナルエミュレータからCalcを起動する。

```
% libreoffice --calc [filename]
```

``[filename]``は省略可能です。

起動後に
Tools -> Options -> LibreOffice -> Security -> [Macro Security ...] ボタン
でSecurity LevelをMediumにセットしてください。
次回からマクロを含んだファイルを開くとマクロを有効にするかどうかの
ダイアログがでるので有効にするを選んでください。

## Scriptの置き場所

Calcファイルに上で走らせるpythonプログラムの保存場所は

```
$HOME/.config/libreoffice/4/user/Scripts/python
```

です。Calcを起動すると``$HOME/.config/libreoffice/4/user/``ディレクトリは
自動で作成されますが、``Scripts/python``ディレクトリは自動では作成
されないようなので手動で作成しておきます。

```
cd $HOME/.config/libreoffice/4/user
mkdir -p Scripts/python
```

## Hello, world

Programming Language C (K & R)出版以来、最初に書くプログラムはHello worldです。
``$HOME/.config/libreoffice/4/user/Scripts/python/``ディレクトリに
[my_first_macro_calc.py](my_first_macro_calc.py)
にあるプログラムをコピーします。
(
https://wiki.documentfoundation.org/Macros/Python_Guide/My_first_macro/ja
からもってきて、下記ボタンからも起動できるように
``def my_first_macro_calc()``に引数``*args``を追加したものです。このプログラムでは
``*args``は使わないですがないとボタンを押したときにエラーになります
)。

Calcを起動して

Tools →Macros → Run Macro → MyMacrosの▼をクリックして my_first_macro_calc
を選択→ Macro Nameでmy_first_macro_calcが自動選択されているのを確認
→ Runボタン

でA1セルに「PythonからCalcでHello world」と入ります。

## シート上にボタンを設置して、pythonプログラムをバインドする



