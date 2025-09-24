# exemplo de código HTML usando python no jupyter notebook

html_code = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Front-end com Python</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Esta é uma página web criada usando Python no Google Colab.</p>
</body>
</html>
"""

from IPython.display import HTML

HTML(html_code)
