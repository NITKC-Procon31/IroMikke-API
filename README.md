# IroMikke-API

## データの通信概要
### リクエストヘッダ
#### USER-ID
*viewer_id*と*user_id*の間に + を加え、文字列を結合し、さらに暗号化を施したもの。

暗号化については、[Cryptographer](#Cryptographer) を参照されたい。

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

## Cryptographer
[USER-ID](#USER-ID)で利用されている暗号化アルゴリズム。

実装自体は非常に単純なものとなっている。

### エンコード
文字列を1文字ずつ読んでいき、ASCIIコードに変換し10を足す。さらにASCIIコードを文字に戻し、文字の前後に 1～9 のランダムな数字を結合し、新しい文字列を生成する。

以下、Pythonでの実装例。

```python
def encode(s: str) -> str:
    new_s = ''
    for i in range(0, len(s)):
        new_s += str(random.randrange(10)) \
              + chr(ord(s[i]) + 10) \
              + str(random.randrange(10))

    return new_s
```

### デコード
文字列を2文字目から3文字飛ばしながら（2文字分無視しながら）読んでいき、ASCIIコードに変換し10を引く。さらにASCIIコードを文字に戻し、新しい文字列の最後尾に結合する。

以下、PHPでの実装例。
```php
function encode(string $s): string
{
    $new_s = "";
    for ($i = 1; $i < strlen($s); $i += 3) {
        $new_s .= chr(ord($s[$i]) - 10);
    }

    return $new_s;
}
```

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
