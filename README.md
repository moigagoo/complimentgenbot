# Комплимент-бот

На свидании наступила неловкая пауза, и тебе срочно нужен комплимент? Заходи к [Комплимент-боту](https://t.me/complimentgenbot)!

Команда /compliment выдаст случайный романтичный комплимент. Ты точно уйдёшь домой не один! 😜


## Deploy

1. Clone the repo.
1. `cd complimentgenbot`
1. Put your Telegram token in .env: `TELEGRAM_BOT_TOKEN="supersecret"`
1. `docker build -t complimentgenbot . && docker run -d -v $(pwd):/usr/src/app --rm complimentgenbot`
