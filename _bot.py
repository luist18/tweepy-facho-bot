import datetime
import time
import tweepy

__all__ = ['Bot']


class Bot:

    def __init__(self, secrets, fachos, message, sleep_time, secrets_fetcher=None):
        self.secrets = secrets
        self.fachos = fachos
        self.message = message
        self.sleep_time = sleep_time
        self.secrets_fetcher = secrets_fetcher
        self.last_lookup = datetime.datetime.utcnow()

    def login(self):
        try:
            auth = tweepy.OAuthHandler(
                self.secrets['consumer']['key'], self.secrets['consumer']['secret_key'])
            auth.set_access_token(
                self.secrets['access']['token'], self.secrets['access']['token_secret'])

            self.bot = tweepy.API(auth)

            if self.secrets_fetcher is None:
                self.fetcher = Bot
            else:
                auth = tweepy.OAuthHandler(
                    self.secrets_fetcher['consumer']['key'], self.secrets_fetcher['consumer']['secret_key'])
                auth.set_access_token(
                    self.secrets_fetcher['access']['token'], self.secrets_fetcher['access']['token_secret'])
                self.fetcher = tweepy.API(auth)

        except Exception as e:
            print('Could not authenticate...')
            pass

    def run(self):
        while True:
            # Safe backup for the last lookup
            backup_lookup = self.last_lookup

            for user in self.fachos:
                # Try/Except in case the user blocked the bot and no fetcher is provided
                try:
                    statuses = self.fetcher.user_timeline(screen_name=user)
                except Exception:
                    continue

                tweets_replied = 0

                for status in statuses:
                    # Verifies if the tweet is new and not a retweet
                    if status.created_at > backup_lookup and not hasattr(status, 'retweeted_status'):
                        try:
                            # Try/Except in case the user blocked the bot
                            self.bot.update_status(
                                status=f"@{status.user.screen_name} {self.message}", in_reply_to_status_id=status.id)

                            # Safe sleep time in order to Twitter do not detect the bot
                            time.sleep(5)
                        except Exception:
                            pass

                        # URL necessary to quote retweet
                        url = f'https://twitter.com/{status.user.screen_name}/status/{status.id}'
                        self.bot.update_status(
                            status=self.message,  attachment_url=url)

                        time.sleep(5)

                        tweets_replied += 1

                # Updates the last look up date
                if len(statuses) > 0 and statuses[0].created_at > self.last_lookup:
                    self.last_lookup = statuses[0].created_at

                # Information message
                print(f'@{user} did not tweet recently...') if tweets_replied == 0 else print(
                    f'@{user} killed {tweets_replied} times!')

            # Information message
            date_string = self.last_lookup.strftime('%m-%d-%Y, %H:%M:%S')
            print(f'Last lookup updated to {date_string}')

            time.sleep(int(self.sleep_time))
