# Q: プロフィールの変更が反映されない

解答するチャレンジに氏名・生年月日の入力が必要だが、マイプロフィールより変更後保存を押しても変更内容が消えてしまいます。  
どうすればよいでしょうか？

## Answer:

当サービスは使用上、プロフィール編集画面より変更後保存を押しても氏名と生年月日はプロフィールページ( https://app.code-check.io/users/{ユーザー名} )に表示されません。
プロフィール編集画面( https://app.code-check.io/settings/profile )をアクセスしていただければ入力された氏名と生年月日が確認できます。

なお、正常に登録されてあれば、解答されたいチャレンジを受けることが可能の筈です。
再度チャレンジのページをアクセスしてご確認下さい。

# Q: GitHub の解答が反映されていない

GitHub で解答したけど codecheck 側で確認すると、更新した箇所が反映されていません。  
何か自分から対応できる事はないでしょうか？

## Answer:

codecheck は、解答の更新を GitHub の Webhook を活用して行っているため、まずは GitHub の Webhook が正常に動作しているかの確認をお願いします。

以下、GitHub Webhook の確認手順です。

1. 自身のリポジトリの `Settings` タブにアクセスする
1. `Settings` タブ内にある、`Webhooks` メニューにアクセスする  
[画像で確認する](./images/github_repo_settings.png)
1. `Webhooks` の一覧に `https://app.code-check.io/github/hook` という欄がある事を確認する
1. 右側にある `Edit` ボタンをクリックする  
[画像で確認する](./images/github_repo_settings_webhooks.png)
1. 下の方に `Recent Delivers` というセクションがあるので、一番上にある記録の右側にある `...` という部分をクリック  
[画像で確認する](./images/github_repo_settings_webhooks_manage.png)
1. `Redeliver` というボタンが現れるので、そのボタンをクリック
1. `Response` のタブの横に緑の枠で `200` という数値が表示されている事を確認する  
[画像で確認する](./images/github_repo_settings_webhooks_redeliver.png)
