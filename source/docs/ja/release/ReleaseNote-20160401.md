# Release Note v2016-04-01

## Main Release
### Applicant Summary（受験者サマリーページ）
  - 受験者ベースの情報を表示するページの追加
  - 受験者一覧のユーザー名をクリックする事で遷移可能

### Environment Variable（環境変数の指定）
  - Challenge の中で環境変数を使えるように機能を追加
  - 受験者が Heroku 等のようにサービス上で環境変数を設定する事が可能になりました
    - API token のような credential な情報を使った Challenge が作成可能です

### Update challenge without cancelling the challenge（問題の更新に対する対応）
  - Challenge を受けている途中に内容の更新ができる機能を追加
  - Challenge の内容が更新された場合、ユーザーは受けている Challenge をキャンセルする事無く更新する事が可能になりました
  - GitHub 受験の場合は更新用 Pull Request を生成します
  - Challenge の更新はオプトイン方式をとっています（受験者が明示的に更新する必要があります）

### Cancel exam（試験配信の取り消し）
  - 配信した Exam が未読の場合のみ、配信の取り消しができる機能を追加
  - 間違ったメールアドレスへ送ってしまった場合を想定した取り消し機能です

### Webhook の確認機能
  - GitHub の webhook 設定が失敗してしまう問題に対応する機能の追加
  - リポジトリや Webhook の設定情報を確認して、必要であれば修正します。
  - 設定の修正はオプトイン方式をとっています

### Expired tab（時間切れ受験者の表示）
  - Submitted タブに Expired（時間切れ） 状態の Answer（解答） が表示される問題の修正
  - Expired状態の解答は、Expired（時間切れ）というタブ内でのみ表示されるようになりました
