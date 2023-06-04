from telethon.sync import TelegramClient

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = '+1234567890'  # Your phone number linked to the Telegram account

# List of group usernames or invite links where you want to share the promo message
group_list = [
    'group_username1',
    'group_username2',
    'group_invite_link3',
    # Add more groups here
]

promo_message = 'Your promotional message goes here'

with TelegramClient(phone_number, api_id, api_hash) as client:
    for group in group_list:
        try:
            client.send_message(group, promo_message)
            print(f"Promo message sent to {group}")
        except Exception as e:
            print(f"Failed to send message to {group}: {str(e)}")
