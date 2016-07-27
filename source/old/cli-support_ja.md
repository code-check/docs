# チャレンジでのCLIアプリケーションサポートについて
## CLIアプリケーションとは
CLI(Command Line Interface)アプリケーションとはコマンドライン上でのコマンド入力によって実行可能なアプリケーションのことです。

典型的なCLIアプリケーションは引数として入力を受け取り、なんらかの処理の結果を標準出力(または標準エラー出力)に出力します。

## CLIアプリケーションをサポートすることの背景
codecheckではさまざまな言語・テストフレームワークをサポートしていますが、このことが逆に言語を問わないアルゴリズムを問う問題を作成する場合は各言語ごとにチャレンジを作成しなければならないという問題がありました。

このようなアルゴリズム問題をCLIアプリケーションの作成問題として出題することでひとつのチャレンジで複数の言語に対応させることができます。

## CLIチャレンジの受験方法
CLIチャレンジでは出題側から使用可能な言語が指定されています。

受験者は最初に自分の好きな言語を選択してチャレンジを開始します。

開始したチャレンジにはあらかじめ選択した言語でのCLIアプリケーションのテンンプレートが含まれています。
デフォルトでは単純に引数を標準出力に出力するだけのエコーアプリケーションとして実装されているので、これを改変していく形でチャレンジを進めてください。

各言語固有の補足説明は「<言語名>.md」というファイルに記載されています。

### 使用言語の変更
チャレンジの途中で使用言語を変更することも可能です。
ただし、その場合はそれまでに編集したファイルの内容が失われるので注意してください。(GitHub受験の場合はPullRequestが作成されます。)

## CLIチャレンジの作成方法
サンプルとしてFizzBuzzのチャレンジが以下のリポジトリで公開されています。

https://github.com/code-check/fizzbuzz/tree/cli

CLIチャレンジの作成も基本的には[通常のチャレンジの作成方法](challenge_ja.md)と同じです。

その上で以下の定義を行ってください。

- challenge.jsonに`cli`というキーで使用可能な言語を配列として指定する
- challenge.jsonで`allowNewFile: true`とする
- codecheck.ymlを作成し`test`にテストコマンドを記述する
- challenge.jsonで以下のファイルをeditableにする
  - codecheck.yml
  - .gitignore(チャレンジに含まれる場合)
  - package.json(使用可能な言語にnode.jsが含まれる場合)
- challenge.jsonで以下のファイルをexcludeする
  - challenge.json

## ユニットテストの作り方
ユーザが作成したCLIアプリケーションの起動コマンドはAPP_COMMANDという環境変数に設定されています。

テスト作成の要件としては以下のようになります。

- 環境変数`APP_COMMAND`を読んでそのコマンドをプロセスとして実行する
- コマンド実行時に引数を渡せるようにする
- コマンドの実行結果を標準出力から読み取り、結果を検証する

この要件が満たされていれば、どのような言語・フレームワークを用いてテストを作成しても構いませんが、[codecheck CLI](https://www.npmjs.com/package/codecheck)にCLIテスト作成用のユーティリティが含まれているので、それを利用してテストを作成することができます。

FizzBuzzサンプルにはmocha + codecheckで作成されたテストが含まれています。

https://github.com/code-check/fizzbuzz/blob/cli/test/fizzbuzz.test.js

以下にcodecheckのユーティリティの簡易説明は以下です。

- codecheck#consoleAppメソッドにCLIアプリケーションの実行コマンドを引数に渡すことでCLIアプリケーションのラッパー(app)を取得する
- app#runでCLIアプリケーションを実行できる
  - 引数は可変で複数渡すことができる
  - 返り値はPromise
- runの結果のPromiseから実行結果を取得し結果を検証する
  - このPromiseは複数の値を持つので結果はspreadで取得する
  - 第一引数はコマンドの返り値
  - 第二引数はコマンドの標準出力の改行区切りでの配列

特に理由がない限りこのサンプルと同じ形式でテストを作成することを推奨します。


## サポートしている言語について
対応予定の言語は以下です。
challenge.jsonのcliには以下の値を指定してください。
(リンクになっていない言語は現在未実装です。)

- [nodejs](https://github.com/code-check/cli-template-node)
- [ruby](https://github.com/code-check/cli-template-ruby)
- [go](https://github.com/code-check/cli-template-go)
- [python](https://github.com/code-check/cli-template-python)
- [java](https://github.com/code-check/cli-template-java)
- php
- c/c++
- perl
- haskell
- groovy
- scala
