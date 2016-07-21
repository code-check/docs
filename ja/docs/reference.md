

# Webエディタの使い方
## <a name="section1"> 1. Webエディタの使い方
### 1-1. ファイルの編集
#### ファイルの種類
![イメージ10](images/s10.png)
Webエディタ内の左側にはファイルツリーが表示されます。
アイコンの種類によって、編集可能なファイルとそうでないファイル（編集不能）を見分けることが出来ます。
問題文に従って、指定のファイルを編集するようにしてください。

### 1-2. Viewerの設定
![イメージ9](images/s9.png)
左上のセッティングアイコンをクリックすると、
* エディタのカラーテーマ
* TABキーの半角スペース変換
* HTMLビューワーのプレビュー方法（オートプレビュー）
* ファイルの保存時のダイアログの表示設定
等の設定をすることが出来ます。

### 1-3. テストの実行・プレビュー
#### テストの実行
Webエディタ右下の「RUN」ボタンでテストを実行することが可能です。
- テストコードについて
  - codecheckでは、テストはテストフレームワークを用いたUnitテストとして実行されます。
  - ここでいう「テスト」とは、各問題ごとに設定されているプログラムが正しいかどうかを判定するテストコードの事を指します。
  - テストコードは受験者に公開しているものはファイルを確認することが出来ます。

#### プレビュー
プレビューはHTML、CSS、Javascriptで構成されたアプリケーションのビューワーとして表示させるものです。
設定上でオートプレビューをオンにしていると、リロードすることなく、編集内容がプレビューに反映されます。

#### デバック
各言語ごと標準出力を記述してRUNボタンを実行してください。
テストの結果と同時に、出力結果が返されます。

### 1-4. 保存方法
編集内容の保存をするためには、画面右上の「SAVE」ボタンをクリックしてください。
![イメージ13](images/s13.png)
ボタンをクリックすると、編集したファイルが一覧で表示されます。
保存したいファイルを選択してOKボタンをクリックすると、ファイルが保存されます。

## <a name="section2"> 2. GitHubを利用した受験方法
GitHubを利用した受験には事前にGitHubのアカウント連携が必須となります。
設定方法は、[会員登録](how-to-use_ja.md#section2)から、「ソーシャルアカウントの追加」をご確認ください。

### 2-1. GitHubを使ってチャレンジを回答する
#### チャレンジのフォーク
Webエディタ内のフォークボタンをクリックすると、モーダルが立ち上がります。
![イメージ11](images/s11.png)
リポジトリ名を指定して、OKを選択すると、GitHubの生成されたリポジトリページに移動します。
もし、外部に公開しないプライベートリポジトリ（※GitHub上での有料プランが必要）を希望する場合は、Private Reopositoryボタンをチェックしてください。

#### ローカルへのクローン
![イメージ15](images/s15.png)
生成されたリポジトリをローカルにクローンします。
これは通常のGitHubのクローンと同様です。
```
$ git clone {GIT_URL}
```
で、ローカルにリポジトリを落としてきます。
これであとはお好きな環境、エディタで編集をしていただくことが出来ます。

### 2-2. 回答の保存
回答を編集したら、コミットをしてリモートのmasterにプッシュします。
無事にリモートのmasterにプッシュが完了すると、codecheck側にもmasterの編集内容が保存されます。
```
$ git push origin master
```
を実行した後に、試験の詳細画面でチャレンジが「保存」に切り替わったか確認をしてください。

## 3. 推奨ブラウザ
Webエディタでの回答にはHTML5/CSS3に対応したモダンブラウザを使用してください。
推奨ブラウザはGoogle Chromeです。


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


# How to create challenge

## はじめに
codecheckのチャレンジはGitHubのリポジトリから作成されます。
ただし、すべてのGitHubリポジトリをチャレンジとすることができるわけではありません。

リポジトリをチャレンジとしてcodecheckに取り込むためには以下の手順が必要です。

## チャレンジの基本的な作成手順
### 1. README.mdに問題文の記載
codecheckにリポジトリを取り込むには、
**リポジトリのルートに「README.md」というマークダウンファイルがある**
ことが必要です。README.mdにはチャレンンジの内容(問題文)を記述してください。

### 2. challenge.jsonの記載・設定
次に、**リポジトリのルートに「challenge.json」というjsonファイルを設定する** 必要があります。

challenge.jsonはリポジトリがcodecheckのチャレンジであることを識別するために使用されるファイルで、

- チャレンジで編集可能なファイル
- テストの実行方法

などが記述されます。

challenge.jsonでは以下のキーを定義することができます。

#### editable: Array[String]
編集可能なファイルを指定します。
値の指定にはワイルドカードが使用できます。(gitの.gitignoreで使用可能なワイルドカードと同じ書式が使用できます。)

#### ignores: Array[String]
チャレンジから完全に取り除くファイルを指定します。
値の指定にはワイルドカードが使用できます。(gitの.gitignoreで使用可能なワイルドカードと同じ書式が使用できます。)

#### includes: Array[String]/excludes: Array[String]
ユーザが参照可能なファイルを制限します。
値の指定にはワイルドカードが使用できます。(gitの.gitignoreで使用可能なワイルドカードと同じ書式が使用できます。)

excludesにマッチしたファイルはチャレンジのユーザからは見えなくなります。
ただし、ファイル名がexcludesとincludesの両方にマッチする場合はincludesの方が優先されユーザはそのファイルを見ることができます。

excludesが指定されていない場合はすべてのファイルはユーザ可視です。

例) testディレクトリに3つのテストファイルがある
- test/test1.js
- test/test2.js
- test/test3.js

test1のみユーザに公開する
```
{
  "excludes": ["test/*"],
  "includes": ["test1.js"]
}
```

※ README.mdはここでの指定に関わらずチャレンジのファイルセットには含まれません。(ユーザはChallengeViewerでREADME.mdを参照することができます。)

#### allowNewFile: Boolean
デフォルト値：false
ChallengeViewerでファイルの追加を許可するかどうかを指定します。

#### allowRunTest: Boolean
デフォルト値：true
ChallengeViewerでテストの実行を許可するかどうかを指定します。

#### test: String
テストに使用するコマンドを指定します。
テストには任意のテストフレームワークが使用できます。([codecheck CLI](#codecheck-cli)参照)

例)
```
{
  "test": "mocha"
}
```

```
{
  "test": "sbt test"
}
```

#### markdownTest: Array[String]
マークダウンテストとするファイルへのパスを指定します。([Markdown Test](#markdown-test)参照)

例)
```
{
  "markdownTest": ["question1.md"]
}
```

### 3. ユーザーに非表示にするコードの設定
任意のテキストファイル内で「BEGIN_CHALLENGE」という文字列を含む行から「END_CHALLENGE」という文字列を記載することで、チャレンジからユーザーに非表示にするコードを設定することが出来ます。

例) Before
``` javascript
function fizzbuzz(n) {
  //Write your answer here
  //BEGIN_CHALLENGE
  if (n % 15 === 0) {
    return "FizzBuzz";
  } else if (n % 5 === 0) {
    return "Buzz";
  } else if (n % 3 === 0) {
    return "Fizz";
  } else {
    return n;
  }
  //END_CHALLENGE
}
```

例) After
``` javascript
function fizzbuzz(n) {
  //Write your answer here
}
```

各種テストフレームワークを使用したテストを作成する際には、テストが成功する実装がなければそのテストコード自体が正しいかどうかを判断できません。

この機能を利用することで、テストが完全に動作するチャレンジを作成しつつ、その実装のみをユーザから隠蔽することができます。

## 自動テストの実行環境
各種言語／テストフレームワークがあらかじめインストールされたDocker環境(ubuntu14.04)で実行されます。
言語やテストフレームワークは常にバージョンアップするものなので、この環境は必要に応じて随時更新されます。

## codecheck CLI
codecheck CLIは自動テストで使用されるコマンドラインのテストランナーです。

オープンソースで公開されておりnpmコマンドでインストールすることができます。

https://www.npmjs.com/package/codecheck

``` bash
npm install codecheck -g
```

codecheckコマンドは以下のことを行います。

- 子プロセスとして任意のテストコマンドを実行
- 標準出力／エラー出力からテストの実行件数／成功件数を取得

原理的にはあらゆるテストコマンドが実行できますが、非対応のテストフレームワークからは正しく実行件数／成功件数が取得できません。

現在対応している言語／テストフレームワークは以下です。

- Ruby
  - RSpec
  - TestUnit
- Java
  - Maven(JUnit)
- Groovy
  - Gradle(JUnit/Spock)
- JavaScript(Node.js)
  - Mocha
- Python
  - Nosetests
- Scala
  - SBT(ScalaTest/Specs2)
- Perl
  - Prove
- PHP
  - PHPUnit
- Haskell
  - Cabal
- Go
  - Go Test
- C++

テストフレームワークへの対応は随時更新されます。

また、後述の言語不問のチャレンジやWebアプリケーションチャレンジをサポートするユーティリティが含まれています。

## チャレンジのサンプル
JavaScriptでFizzBuzz問題を出題するサンプルです。

https://github.com/code-check/challenge-fizzbuzz-js

このチャレンジは以下のような内容になっています。

- 編集可能なファイルはapp.jsのみ(ファイルの追加は不可)
  - app.jsのfunction fizzbuzzを編集して正しく実装する
  - app.jsにあらかじめ記述されている正答例は削除される
- test.public.jsはユーザが見ることができ、実行することが可能
- test.private.jsはユーザは見ることができず、採点時のみ実行される
- テストフレームワークはmocha

## あらゆる形式のチャレンジ作成方法
### Markdown式チャレンジの作成
Markdownチャレンジとはマークダウン形式で記述された選択式の文章問題テストのことです。

#### 作成方法
チェックボックス付きのリスト(`- [ ]`/`- [x]`)を利用して選択問題を作成することが出来ます。

例)
```
Q1. xxx
- [ ] aaa
- [x] bbb
- [ ] ccc
- [ ] ddd

Q2. xxx
- [ ] aaa
- [ ] bbb
- [ ] ccc
- [x] ddd

Q3. xxx
- [x] aaa
- [ ] bbb
- [ ] ccc
- [x] ddd
```

問題作成時に正解の選択肢にはあらかじめチェックをいれておきます。
複数選択の正解を設定することも可能です。

正解はユーザからは見ることができず、提出時には自動採点されます。

※1
問題の選択肢は必ず連続するチェックボックスリストの１行として定義してください。
チェックボックスリスト以外の行が含まれた場合は別の問題と判定されます。

※2
README.mdをMarkdownチャレンジにすることはできません。
(README.mdはチャレンジを開始する前の段階でユーザに公開されます。)

#### 自動採点の仕組み
チャレンジ生成時にmochaのテストコードが自動的に生成されます。
このため生成されたチャレンジのファイルセットにはpackage.jsonが含まれ、challenge.jsonは改変されます。

マークダウンテストではこれらのファイルはユーザに見える必要はないので、あらかじめchallenge.jsonでexcludesしておくことが推奨されます。

```
{
  "markdownTest": [
    "question1.md",
    "question2.md"
  ],
  "excludes": [
    "package.json",
    "challenge.json"
  ]
}
```

マークダウンテストをそれ以外のテストと組み合わせることは可能ですが非推奨です。

### 言語不問式チャレンジの作成
言語不問のチャレンジを作成する場合はユーザには以下の要件を課すことになります。

- 任意の言語でコンソールアプリケーションを作成してもらう
- そのアプリは標準入力またはコマンドライン引数でパラメータを受け取る
- そのアプリは標準出力に結果を出力した後に終了する

逆から言うとチャレンジ作成者は以下のようなテストを作成する必要があります。

- 任意のコマンドラインアプリケーションを実行し、
- そこに標準入力またはコマンドライン引数でパラメータを渡し、
- 標準出力の結果を評価する

この要件が満たされてさえいれば任意のテストフレームワークを使用してテストを作成することができますが、codecheck CLIにはこの形式のテストを支援するためのユーティリティが含まれているのでそれを利用して作成するのが簡単です。

codecheckのユーティリティを使用するためにはまずcodecheck CLIをローカルにインストールします。

``` bash
npm install codecheck --save
```

その後、mocha等のテストフレームワークを使用したテストを作成します。

``` javascript
var assert = require("chai").assert;
var codecheck = require("codecheck");

//コンソールアプリケーションの実行コマンドを環境変数から取得
var appCommand = process.env.APP_COMMAND;

describe("test", function() {

  before(function() {
    //環境変数が正しく設定されていることのチェック
    assert(appCommand);
  });

  it("test1", function(done) {
    //コンソールアプリケーションの作成
    var app = codecheck.consoleApp(appCommand);

    //inputで標準入力に渡す内容を指定。(可変長引数。または配列も可)
    app.input("3");

    //expectedで標準出力の期待値を指定。(可変長引数。または配列も可)
    app.expected("fizz");

    //実行して期待値通りの出力がされることを確認
    app.runAndVerify(function(result) {
      assert(result.succeed, result.getMessage() || "none");
      done();
    })
  });
});
```

テスト実行時の環境変数はcodecheck.ymlで指定できるので、ユーザには自分の作成したアプリの実行コマンドをcodecheck.ymlのenvironmentセクションに設定してもらいます。

また、作成したアプリの実行にbuildが必要な場合はそのコマンドをbuildセクションに設定してもらいます。

codecheck.yml
``` yaml
build:
  - npm install
environment:
  APP_COMMAND: node app.js
```

### Webアプリケーション式チャレンジの作成
codecheck CLIにはテスト実行前に任意のWebアプリケーションを起動する機能があります。

codecheck.yml
```
web:
  command: sbt run
  port: 9000
  console: true
  testUrl: /
  dir: app
```

上記の設定内容は以下の通りです。

- command: sbt run - Webアプリケーションの実行コマンドは「sbt run」
- port: 9000 - Webアプリケーションのポートは9000
- console: true - Webアプリケーションの標準出力をcodecheckコマンドの標準出力にも出力する
- testUrl: / - 起動コマンド実行後このURLに対してGETリクエストを発行し、200が帰ってくるまでウェイトする
- dir: app - コマンドの実行ディレクトリはapp

この機能を利用することでRuby on RailsやPlayframeworkなどの任意のWebフレームワークの穴埋め問題を作成することが可能です。
先の言語不問問題の作成方法と組み合わせると言語不問でWebアプリケーションをユーザに作成させることさえできます。

ただし、DBを使用したい場合はどうするか？等の課題もあるので、この機能はまだ実験的な段階と言えます。
(H2やSQLLite等の軽量データベースの使用はおそらく可能ですが未検証です。)


# サンプルテスト問題集

## カテゴリ
### 1. アルゴリズムチャレンジ
アルゴリズムチャレンジとは、受験者がある特定のプログラムファイルを編集し、与えられた入力値に対して、適切な出力を出来るのかを問う問題の事です。

* 対応言語: C,C++,C#,Java,Javascript,Scala,PHP,Perl,Python,Ruby,Go,Haskell,Groovy
* 具体的な問題:FizzBuzz,Primaryなど

### 2. フレームワークチャレンジ
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

### 3. APIチャレンジ
APIチャレンジとは、言語やフレームワークは不問。正しいAPIサーバを実装することが出来るのかを試すことが出来るチャレンジです。
受験者は、自分自身が得意とするフレームワークや言語で問題を回答することが可能です。

### 4. HTMLチャレンジ
HTMLチャレンジは、HTML5、CSS3などのWebデザインや、Javascriptを活用した描画を出来るかを試すチャレンジです。
エディタ上のViwerを活用し、正しく描画できているかどうかを判断します。（自動採点はなし）

### 5. 選択式・記述式チャレンジ
選択式チャレンジとは、4択問題や記述の問題を出題することが出来るチャレンジです。
問題は、マークダウンファイルを編集することで作成することが出来ます。また、選択式の問題については、自動採点も設定することが可能です。

## サンプル問題集
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


# アクセス権限

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
