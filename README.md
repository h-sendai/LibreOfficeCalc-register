# LibreOfficeCalc Register設定用プログラム

LibreOfficeCalcを使ってレジスタを設定するためのデータを
生成するプログラム。

AlmaLinux 8、9、ubuntu 2024.04 LTSで動作を確認しています。

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



