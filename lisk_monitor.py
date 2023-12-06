# Lisk Telegram Monitor v0.2 by HelpingHand - updated for Liskv4

import requests
import json

# Add your validator address to monitor below (can be multiple)
validators_to_monitor = ['lskq3mtp4vkzc32nqbod9nfyzhbwwzfnswasrtor6']

# Add the list of your Lisk Service server(s) to fetch validator data here
servers = ['service.lisk.com', 'mainnet-service.lemii.dev']

# Add your Telegram bot token and chat id(s)
bot_token = ''
chat_ids = ['']

def check_missed_blocks(validators_to_monitor, servers):
    for validator_address in validators_to_monitor:
        data_fetched = False
        for server in servers:
            try:
                response = requests.get(f'https://{server}/api/v3/pos/validators?address={validator_address}')
                response.raise_for_status()  # Raise an exception in case of error
                data = response.json()
                account_data = data['data'][0]
                if account_data:
                    username = account_data.get('name')
                    consecutiveMissedBlocks = account_data.get('consecutiveMissedBlocks')
                    if consecutiveMissedBlocks > 0:
                        send_telegram_message(f"Validator {username} is MISSING BLOCKS! \n\n The validator currently missed {consecutiveMissedBlocks} blocks. \n\n FIX IT QUICK!", chat_ids, bot_token)
                data_fetched = True
                break  # If data is fetched successfully, stop checking other servers
            except requests.exceptions.RequestException:
                continue  # If data fetching failed, try the next server
        if not data_fetched:
            # Handle the scenario when none of the servers are available
            send_telegram_message("Failed to fetch validator data. Please check servers.", chat_ids, bot_token)

def send_telegram_message(message, chat_ids, bot_token):

    for chat_id in chat_ids:
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&text=' + message
        response = requests.get(send_text)
    return

check_missed_blocks(validators_to_monitor, servers)
