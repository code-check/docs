# リファレンス

## チャレンジでのCLIアプリケーションサポートについて
##### CLIアプリケーションとは
CLI(Command Line Interface)アプリケーションとはコマンドライン上でのコマンド入力によって実行可能なアプリケーションのことです。

典型的なCLIアプリケーションは引数として入力を受け取り、なんらかの処理の結果を標準出力(または標準エラー出力)に出力します。

##### CLIアプリケーションをサポートすることの背景
codecheckではさまざまな言語・テストフレームワークをサポートしていますが、このことが逆に言語を問わないアルゴリズムを問う問題を作成する場合は各言語ごとにチャレンジを作成しなければならないという問題がありました。

このようなアルゴリズム問題をCLIアプリケーションの作成問題として出題することでひとつのチャレンジで複数の言語に対応させることができます。

##### CLIチャレンジの受験方法
CLIチャレンジでは出題側から使用可能な言語が指定されています。

受験者は最初に自分の好きな言語を選択してチャレンジを開始します。

開始したチャレンジにはあらかじめ選択した言語でのCLIアプリケーションのテンンプレートが含まれています。
デフォルトでは単純に引数を標準出力に出力するだけのエコーアプリケーションとして実装されているので、これを改変していく形でチャレンジを進めてください。

各言語固有の補足説明は「<言語名>.md」というファイルに記載されています。

##### 使用言語の変更
チャレンジの途中で使用言語を変更することも可能です。
ただし、その場合はそれまでに編集したファイルの内容が失われるので注意してください。(GitHub受験の場合はPullRequestが作成されます。)

##### CLIチャレンジの作成方法
サンプルとしてFizzBuzzのチャレンジが以下のリポジトリで公開されています。

https://github.com/code-check/fizzbuzz/tree/cli

CLIチャレンジの作成も基本的には[通常のチャレンジの作成方法](guide_organizing_challenges.md)と同じです。

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

##### ユニットテストの作り方
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


##### サポートしている言語について
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


## サンプルテスト問題集

##### アルゴリズムチャレンジ
アルゴリズムチャレンジとは、受験者がある特定のプログラムファイルを編集し、与えられた入力値に対して、適切な出力を出来るのかを問う問題の事です。

- 対応言語: C,C++,C#,Java,Javascript,Scala,PHP,Perl,Python,Ruby,Go,Haskell,Groovy
- 具体的な問題:FizzBuzz,Primaryなど

##### フレームワークチャレンジ
フレームワークチャレンジとは、それぞれの言語や環境ごとのWebフレームワーク、ライブラリ等の開発力を試す事ができるチャレンジです。

|Language|Frameworks|
|---|---|
|Ruby|RubyOnRails,Sinatra|
|PHP|CakePHP,Larval,Wordpress|
|Python|django|
|Java|PlayFramework,Spring|
|Scala|PlayFramework|
|Javascript|Express,SailsJS,JQuery,Bootstrap,AnglarJS,ReactJS|
|SQL|SQLite|

##### APIチャレンジ
APIチャレンジとは、言語やフレームワークは不問。正しいAPIサーバを実装することが出来るのかを試すことが出来るチャレンジです。
受験者は、自分自身が得意とするフレームワークや言語で問題を回答することが可能です。

##### HTMLチャレンジ
HTMLチャレンジは、HTML5、CSS3などのWebデザインや、Javascriptを活用した描画を出来るかを試すチャレンジです。
エディタ上のViwerを活用し、正しく描画できているかどうかを判断します。（自動採点はなし）

##### 選択式・記述式チャレンジ
選択式チャレンジとは、4択問題や記述の問題を出題することが出来るチャレンジです。
問題は、マークダウンファイルを編集することで作成することが出来ます。また、選択式の問題については、自動採点も設定することが可能です。

##### サンプル問題集
codecheckではオフィシャル問題として、それぞれのカテゴリにおいて、サンプルの問題を作成し、無償で提供しております。

|難易度|アルゴリズム|フレームワーク|API|HTML|選択・記述式|
|:-:|---|---|---|---|---|---|---|
|とても難しい|[数独(上級)][sudoku]<br />[ラジンダール][rijndael]|[EntityFramework][entity-framework]|[イベントアプリを作ろう][eventapp]<br />[ログインAPIを実装しよう][login-api]|||||
|難しい||||||||
|普通|[数独(中級)][sudoku-medium]<br />[ラジンダール(中級)][rijndael-medium]|||||||
|簡単|[数独(初級)][sudoku-easy]<br>[配列][arrays]<br />[暗号化(ROT13)][rot13]||[SQL][sql]|||||
|とても簡単|[Fizzbuzz][fizzbuzz]<br />[バイナリ変換][binary-tostring]||||||||

[fizzbuzz]: https://github.com/code-check/fizzbuzz
[sql]: https://github.com/code-check/challenge-sql
[arrays]: https://github.com/code-check/challenge-arrays
[eventapp]: https://github.com/code-check/challenge-eventapp
[login-api]: https://github.com/code-check/challenge-login-api
[entity-framework]: https://github.com/code-check/challenge-entity-framework
[sudoku-easy]: https://github.com/code-check/challenge-sudoku-easy
[sudoku-medium]: https://github.com/code-check/challenge-sudoku-medium
[sudoku]: https://github.com/code-check/challenge-sudoku
[rijndael-medium]: https://github.com/code-check/challenge-rijndael-medium
[rijndael]: https://github.com/code-check/challenge-rijndael
[binary-tostring]: https://github.com/code-check/challenge-binary-tostring
[rot13]: https://github.com/code-check/challenge-rot13

## アクセス権限

||Owner|Admin|Regular|Supporter|
|---|:-:|:-:|:-:|:-:|
|受験者、解答の閲覧|◯|◯|◯|◯|
|解答の採点|◯|◯|◯|◯|
|Challengeの作成|◯|◯|◯|◯|
|企業Challengeの編集|◯|◯|◯|-|
|試験の作成|◯|◯|◯|-|
|メンバーの招待・削除|◯|◯|-|-|
|メンバーの権限の変更|◯|◯|-|-|
|企業情報の編集|◯|◯|-|-|
