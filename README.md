# wxPython sample

wxpython のサンプル

## develop

wxPython は GUI アプリケーションのため、Framework build python を使う必要がある。

そのため、pyenv + virtualenv + mac な環境で実行する場合は、以下のようなコマンドを実行する

```
# if you use virtualenv 
source env

PYTHONPATH=env/lib/python2.7/site-packages ~/.anyenv/envs/pyenv/versions/2.7.14/Python.frame
work/Versions/2.7/bin/python main.py
```
