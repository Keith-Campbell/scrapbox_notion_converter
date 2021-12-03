# scrapbox_notion_converter

（制作中）scrapbox の文法を markdown の文法に変換します。

※ 基本的な文法しか実装しておらず、途中でめんどくさくなって投げ出してしまいました。

## 使い方

1. scrapbox のプロジェクト設定から json ファイルをダウンロードしてください。
2. 本プロジェクト内に json ファイルを配置してください。
3. `prefix` にはプロジェクト名（json 拡張子を除いたファイル名）を記入してください。
4. Python で `parser.py` を実行すると、`generated`フォルダ内にプロジェクト名の mk ファイルがページごとに生成されます。
