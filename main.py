import pandas
import pyautogui
import pyperclip
from time import sleep


pyautogui.PAUSE = 1


# Passo 1: Entrar no sistema (no caso entrar no link).
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.alert('Iniciando. Aperte OK e aguarde!')
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')  # Site vai carregar...
sleep(5)

# Passo 2: Navegar no sistema e encontrar a base de dados (Entrar na pasta Exportar).
pyautogui.click(x=402, y=362)


# Passo 3: Download da base de dados.
pyautogui.rightClick()
pyautogui.press('up')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=324, y=58)
pyperclip.copy("C:\\Users\\procl\\Desktop\\Intensivão de python\\Aula 1\\Exportar")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.click(x=468, y=458)

# Passo 4: Calcular os indicadores(faturamento, quantidade de produtos).
tabela = pandas.read_excel('C:\\Users\\procl\\Desktop\\Intensivão de python\\Aula 1\\Exportar\\Vendas - Dez.xlsx')
quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor Final'].sum()

# Passo 5: Entrar no email.
pyautogui.click(x=280, y=68)
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)

# Passo 6: Mandar um email para a diretorica com os indicadores.
texto = f'''
Bom dia,
O faturamento de ontem foi de R${faturamento}
A quantidade de produtos foi de {quantidade}

Abs
Raphael IM
'''
pyautogui.click(x=115, y=185)
sleep(1)
pyautogui.write('procliperII@hotmail.com')
pyautogui.press('enter')
pyautogui.press('tab')
pyperclip.copy('Teste de automação')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=387, y=928)
pyautogui.alert('Email Enviado')
