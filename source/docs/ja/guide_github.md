# GitHubを利用した受験方法
なんとcodecheckは他のサービスには真似できない、  
ローカル環境でチャレンジに挑戦することが出来るんだぞ。  

## 必須条件
- <a href="https://github.com/join" target="_blank">Githubアカウント</a>
- <a href="https://git-scm.com/" target="_blank">Git</a> (Gitの使い方・ドキュは[ここ](https://git-scm.com/book/ja/v2)。)  
- <a href="https://nodejs.org/en/download/" target="_blank">Node.js/npm</a>
- <a href="https://app.code-check.io/settings/social" target="_blank">GitHubアカウントをcodecheck.ioに接続</a>  
- 最後に `npm install codecheck -g` ってCLIで唱えてcodecheck CLI を召喚しておいてね。
- あとチャレンジのREADME.mdと[指定言語].mdに他の条件が記載してあったらそれもお願いね。

## セットアップ

![Githubでローカルにチャレンジをセットアップする方法](images/start_challenge_github.gif)

- **必須条件は確実に満たしておいてね**。
- 開始したチャレンジのページから![GitHubで解くボタン](images/open_github.png)を選択。
- リポジトリ名を指定して、OKを選択。
- リンクをクリックしてGitHubの生成されたリポジトリページへ移動。
- 「Clone or Download」からリンクをコピー。
- CLIから`git clone {レポジトリのリンク}`で、ローカルにリポジトリを落としてきます。  
- あとは好きな環境、エディタで編集して、チャレンジをぶっつぶしてね！

## テストの実行
- テストする心の準備ができたら、  
CLIで`codecheck`コマンドを走らせるぞ。
- そしたらテスト結果が以下のように標準出力されるよ:  
```
$ codecheck
codecheck version 0.5.3
chai@2.3.0 node_modules/chai
├── assertion-error@1.0.0
└── deep-eql@0.1.3 (type-detect@0.1.1)
Finish build: npm install (1966ms)
////////////////
テストファイルの実行結果
////////////////
codecheck: Finish with code 9
codecheck: tests  : 9
codecheck: success: 0
codecheck: failure: 9
```

## チャレンジの保存
- 回答を編集したら、masterにコミットしておいてね。（やり方は[gitのドキュ](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E5%A4%89%E6%9B%B4%E5%86%85%E5%AE%B9%E3%81%AE%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%B8%E3%81%AE%E8%A8%98%E9%8C%B2)で）
- 次に`git push origin master`でリモートのmasterにプッシュ。　
- 無事プッシュが完了すると、codecheck側にもmasterの編集内容が同時保存される。  
- プッシュ後に、試験の詳細画面でチャレンジが「保存」に切り替わったか確認をしてね。

## チャレンジの提出
- 準備ができたら上記の手順で回答を保存しとく。
- 開始したチャレンジのページにある![提出](images/submit.png)ボタンをポチッと押す。
- 終わり！イェーイ！
