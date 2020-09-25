# IroMikke-API

## データの通信概要
### リクエストボディの中身
```json=request
{
    'viewer_id': 0,
    'user_id': 0,
    'name': 'Kosen Taro'
}
```
データはAPI毎に中身が異なり、上記のものは*SignUp*の例である。

### レスポンスボディの中身
```json=response
{
    'data_headers': {
        'viewer_id': 0,
        'user_id': 0,
        'timestamp': 1601046969,
        'result_code': 1
    },
    'data': []
}

```
`data_headers`と`data`からなり、ともに Map（Dictionary） の形になる。

上記の例では`data`の中身が空なので、 Array の形をとる。

`data`はAPIによって中身が異なるため、各APIのレスポンスを参照のこと。

APIに必要なパラメータ以外は無視されることに注意。

### data_headers
- `int viewer_id` : ユーザの**viewer_id**、GETリクエストの場合、0に固定される。
- `int user_id` : ユーザの**user_id**、viewer_idと同様にGETリクエストの場合、0に固定される。
- `int timestamp` : サーバのUNIX時間。
- `int result_code` : リクエストに対するリザルトコード

詳しくは[リザルトコード一覧](#リザルトコード一覧)を参照されたい。

## エンドポイント一覧
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
空配列


## リザルトコード一覧
| result_code | APIType                 | 説明           |
| :---------: | :---------------------: | :----------: |
| 1           | All                     | サーバとの通信に成功   |
| 201         | [SignUp](#/tool/signup) | ユーザデータの登録に失敗 |
