# docker-composeテスト

Node.js Python MySQL phpmyadmin のコンテナをcomposeでまとめて起動する

## DBコンテナのテスト

localhost:8080 にアクセス

## Node.js コンテナのテスト

localhost:8000 にアクセス  
"Welcom to Expres" と表示されたらOK

## Node.jsコンテナとDBコンテナの接続テスト

localhost:8000/f1 にアクセス  
タイトルが「F1 2020 Constructors Ranking」

## Python コンテナのテスト

localhost:8001 にアクセス

## PythonコンテナとDBコンテナの接続テスト

localhost:8001/f1 にアクセス