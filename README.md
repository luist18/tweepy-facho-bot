# tweepy-facho-bot

Do you love anyone so much that you would spam them every day and every hour with 'lovely' messages? Well, this Twitter bot will help you do that automatically. You can now spam your favorite _fachos_ with lovely messages.

### _Facho_?

#### Portuguese

**fa·cho 2** (redução de fascista)

adjectivo de dois géneros e substantivo de dois géneros
[Portugal, Informal, Depreciativo] **Fascista**.

> _"Cala-te ó facho!" - Sr. Jerónimo de Sousa, Portuguese Communist Party (PCP) leader, in the portuguese parliament_

"facho", in [Dicionário Priberam da Língua Portuguesa](https://dicionario.priberam.org/facho)

#### English

**fa·cho**
(fascist derivative)

adjective and substantive [English, Informal, Depreciative] **Fascist**.

> _"Fachos culiao's mueranse!" would be "Fucking fascists die!"_

"facho", in [Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/english/fascism)

## Requirements

In order to run the bot you must install [tweepy](https://www.tweepy.org/), Python 3 and own a Twitter developer API key ([apply here](https://developer.twitter.com/en)).

## Running

To run the bot simply declare a bot class with your private keys as follows:

```python
bot = Bot(my_secrets, my_fachos, my_message, my_sleep_time)
```

If you own a second Twitter developer API key you can even add it to the bot and so if the _facho_ blocks your bot it will still be able to quote their tweets...

```python
bot = Bot(my_secrets, my_fachos, my_message, my_sleep_time, my_secrets_fetcher)
```

After this you have to login your bot into Twitter and then you can run it forever...

```python
bot.login()
bot.run()
```

### Data

To make the process easier declare your keys in a json file and load it to the runner .py script.

Here is an example of a valid json file:

```json
{
  "secrets": {
    "consumer": {
      "key": "your_bot_consumer_key",
      "secret_key": "your_bot_consumer_secret_key"
    },
    "access": {
      "token": "your_bot_token",
      "token_secret": "your_bot_token_secret"
    }
  },
  "secrets_fetcher": {
    "consumer": {
      "key": "your_fetcher_consumer_key",
      "secret_key": "your_fetcher_consumer_secret_key"
    },
    "access": {
      "token": "your_fetcher_token",
      "token_secret": "your_fetcher_token_secret"
    }
  },
  "fachos": ["your_facho1", "your_facho2"],
  "message": "your_lovely_message_to_the_fachos",
  "sleep_time": "your_time_recommended_300"
}

```

### License

[MIT](https://opensource.org/licenses/MIT)
