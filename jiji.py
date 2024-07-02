import json
from telethon.sync import TelegramClient

api_id = '25597308'
api_hash = '308c30b86e8f78d648753b371bcfe4aa'

def main():
    phone_number = input("Por favor, insira o número do Telegram (inclua o código do país): ")
    
    # Inicialize o cliente Telegram
    with TelegramClient(phone_number, api_id, api_hash) as client:
        # Conecte-se à conta do Telegram usando o número de telefone
        client.connect()
        
        if not client.is_user_authorized():
            # Se o usuário não estiver autorizado, envie o código de verificação para o número fornecido
            client.send_code_request(phone_number)
            code = input("Por favor, insira o código de verificação recebido: ")
            
            # Faça o login na conta do Telegram
            client.sign_in(phone_number, code)
        
        # Se estiver autenticado, imprima uma mensagem
        print("Conectado com sucesso!")
        
        # Coletar dados da conta
        me = client.get_me()
        account_data = {
            "session_file": phone_number,
            "phone": phone_number,
            "user_id": me.id,
            "app_id": api_id,
            "app_hash": api_hash,
            "first_name": me.first_name,
            "last_name": me.last_name,
            "username": me.username,
        }
        
        # Escrever os dados da conta em um arquivo JSON com o nome do número do telefone
        filename = f"{phone_number}.json"
        with open(filename, 'w') as json_file:
            json.dump(account_data, json_file, indent=4)
            
        print(f"Dados da conta salvos no arquivo '{filename}'")

if __name__ == '__main__':
    main()
