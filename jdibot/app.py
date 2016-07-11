
import threading
from bot import Bot
import config

i_bot = Bot(config.token)

def listener():
	i_bot.updates()

def pusher():
	i_bot.activity()


def exit():
	return False

def executer():
	t1 = threading.Thread(target=listener)
	t2 = threading.Thread(target=pusher)

	t1.start()
	t2.start()

	t1.join()
	t2.join()


if __name__ == '__main__':

	while not exit():
		executer()
