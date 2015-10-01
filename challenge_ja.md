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

#### includes: Array[Stringg]/excludes: Array[String]
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
