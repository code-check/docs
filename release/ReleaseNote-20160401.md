# Release Note v2016-04-01

## Main Release
### Applicant Summary
  - 受験者ベースの情報を表示するページの追加
  - 受験者一覧のユーザー名をクリックする事で遷移可能

### Environment Variable
  - Challenge の中で環境変数を使えるように機能を追加
  - 受験者が Heroku 等のようにサービス上で環境変数を設定する事が可能になりました
    - API token のような credential な情報を使った Challenge が作成可能です

### Update challenge without cancelling the challenge
  - Challenge を受けている途中に内容の更新ができる機能を追加
  - Challenge の内容が更新された場合、ユーザーは受けている Challenge をキャンセルする事無く更新する事が可能になりました
  - GitHub 受験の場合は更新用 Pull Request を生成します
  - Challenge の更新はオプトイン方式をとっています（受験者が明示的に更新する必要があります）

### Cancel exam
  - 配信した Exam が未読の場合のみ、配信の取り消しができる機能を追加
  - 間違ったメールアドレスへ送ってしまった場合を想定した取り消し機能です

### Webhook の確認機能
  - GitHub の webhook 設定が失敗してしまう問題に対応する機能の追加
  - リポジトリや Webhook の設定情報を確認して、必要であれば修正します。
  - 設定の修正はオプトイン方式をとっています

## Hot-fixes in this release
### Webhook
GitHub のリポジトリや webhook に関する設定が上手く動作しない問題の修正

### Expire Batch
Challeng の cancel に Batch 機能が対応していなかった問題の修正

### Applicant list tab
Submitted タブに Expired 状態の Exam が表示される問題の修正
