# Lisk Telegram Monitor v0.1 by HelpingHand

import requests
import json

# Add your delegate (hex) address to monitor here (can be multiple)
delegate_to_monitor = ['aa0b32245400d183d4ccd34fe883a6bdc1e3eef9']

# Add the list of your server(s) to fetch delegate data here
servers = ['mainnet.lisk.io', 'mainnet-api.lemii.dev']

# Add your Telegram bot token and chat id(s)
bot_token = ''
chat_ids = ['']

def check_missed_blocks(delegate_to_monitor, servers):
    for delegate_address in delegate_to_monitor:
        data_fetched = False
        for server in servers:
            try:
                response = requests.get(f'https://{server}/api/accounts/{delegate_address}')
                response.raise_for_status()  # Raise an exception in case of error
                data = response.json()
                account_data = data.get('data', {})
                delegate_info = account_data.get('dpos', {}).get('delegate', None)

                if delegate_info:
                    username = delegate_info.get('username')
                    consecutiveMissedBlocks = delegate_info.get('consecutiveMissedBlocks')
                    if consecutiveMissedBlocks > 0:
                        send_telegram_message(f"Delegate {username} is MISSING BLOCKS! \n\n The delegate currently missed {consecutiveMissedBlocks} blocks.", chat_ids, bot_token)
                data_fetched = True
                break  # If data is fetched successfully, stop checking other servers
            except requests.exceptions.RequestException:
                continue  # If data fetching failed, try the next server
        if not data_fetched:
            # Handle the scenario when none of the servers are available
            send_telegram_message("Failed to fetch delegate data. Please check servers.", chat_ids, bot_token)

def send_telegram_message(message, chat_id_list, bot_token):
    for chat_id in chat_ids:
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&text=' + message
        response = requests.get(send_text)
    return

check_missed_blocks(delegate_to_monitor, servers)
