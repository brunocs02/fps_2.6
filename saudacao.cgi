#!/bin/bash

echo "Content-Type: text/html"
echo ""

# Ler o input do formulário
read -r input

# cortando os extras do campo nome
nome=$(echo "$input" | sed 's/^nome=//')

echo "<!DOCTYPE html>"
echo "<html lang=\"pt-br\">"
echo "<head>"
echo "    <meta charset=\"UTF-8\">"
echo "    <title>Duvido ler aqui</title>"
echo "</head>"
echo "<body BACKGROUND="/penguin.jpg">"
echo "    <h1>Boas vindas, $nome!</h1>"
echo "    <p><h2>É um prazer te receber!</h2></p>"
echo "<style>"
echo "body{\nbackground-size: cover;\n}"
echo "<\style>"
echo "</body>"
echo "</html>"
