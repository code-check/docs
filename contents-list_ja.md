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


### 6. モバイルチャレンジ
モバイルチャレンジとは、スマートフォンアプリケーションの実装を試すことが出来るチャレンジです。
現在以下の2つのテストの作成をサポートすることを予定しております。
* Cordova
* Android

### 7. ゲームチャレンジ
ゲームチャレンジとは、ゲームエンジンを活用したアプリケーションの実装をすることが出来るチャレンジです。
現在は以下のゲームエンジンへの対応を予定しております。
* Unity
* cocos2dx

## サンプル問題集
codecheckではオフィシャル問題として、それぞれのカテゴリにおいて、サンプルの問題を作成し、無償で提供しております。

|難易度|アルゴリズム|フレームワーク|API|HTML|選択・記述式|モバイル|ゲーム|
|:-:|---|---|---|---|---|---|---|
|とても難しい|[Sudoku][sudoku]<br />[Rijndael][rijndael]|[EntityFramework][entity-framework]|[Recruting Application][sample-test]<br />[Login API][login-api]|||||
|難しい||||||||
|普通|[Sudoku][sudoku-medium]<br />[Rijndael][rijndael-medium]|||||||
|簡単|[Sudoku][sudoku-easy]<br>[array(C#)][arrays]<br />[ROT13][rot13]||[SQL][sql]|||||
|とても簡単|[Fizzbuzz][fizzbuzz]<br />[Binary ToString][binary-tostring]||||||||

[fizzbuzz]: https://github.com/code-check/fizzbuzz
[sql]: https://github.com/code-check/challenge-sql
[arrays]: https://github.com/code-check/challenge-arrays
[sample-test]: https://github.com/code-check/sample-test
[login-api]: https://github.com/code-check/challenge-login-api
[entity-framework]: https://github.com/code-check/challenge-entity-framework
[sudoku-easy]: https://github.com/code-check/challenge-sudoku-easy
[sudoku-medium]: https://github.com/code-check/challenge-sudoku-medium
[sudoku]: https://github.com/code-check/challenge-sudoku
[rijndael-medium]: https://github.com/code-check/challenge-rijndael-medium
[rijndael]: https://github.com/code-check/challenge-rijndael
[binary-tostring]: https://github.com/code-check/challenge-binary-tostring
[rot13]: https://github.com/code-check/challenge-rot13
