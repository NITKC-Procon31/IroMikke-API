# IroMikke-API

## エンドポイント一覧

レスポンスには個別のものに加え、リザルトコードを示す`int result`が付与される。

詳しくは[リザルトコード一覧](#リザルトコード一覧)を参照されたい。

## /information
### 仕様

メソッド : GET

APIType : Information

備考 : バージョンなどの情報を取得

### レスポンス
- `int version` : APIサーバのバージョン

## /tool/signup
### 仕様

メソッド : POST

APIType : SignUp

備考 : ユーザデータの登録

### リクエスト
- `int viewer_id` : 適当な整数で初期化
- `int user_id` : 適当な整数で初期化
- `string name` : 任意のユーザ名

### レスポンス
- `int viewer_id` : 登録された**viewer_id**
- `int user_id` : 登録された**user_id**

## /tool/delete
### 仕様

メソッド : POST

APIType : Delete

備考 : ユーザデータの削除

### リクエスト
- `int viewer_id` : クライアントに保存された**viewer_id**
- `int user_id` : クライアントに保存された**user_id**

### レスポンス
なし


## リザルトコード一覧
| result_code | APIType                 | 説明           |
| :---------: | :---------------------: | :----------: |
| 1           | All                     | サーバとの通信に成功   |
| 201         | [SignUp](#/tool/signup) | ユーザデータの登録に失敗 |
| 202         | [Delete](#/tool/delete) | ユーザデータの削除に失敗 |