# PrepScholar-AFK-Bot
This is a Python bot created to afk on https://www.prepscholar.com/. If you need a certain amount of hours, you can leave this on and it will make sure the website doesnt kick you out, and it will make sure you get credit for the AFK. You wont get any assignments complete so it is probably still a good idea to do some assignments so it doesnt look obvious, but if you need extra hours, this is how to do it.

> Please let me know any suggestions I can add or work on. I'll keep making this better over time.

## Usage

1. To use this bot, open it in your code editor and run the program. It will take over from there.
1. Next, make sure you are on the website linked above and you are on an assignment where you can read through it. Don't be in a quiz screen or anything else, you want to be in the lecture screen which usually has a video.
1. Now leave your mouse still and after about 10 seconds the bot will start.
1. To exit the program, simply close the terminal that you opened in the first place.

## Features

The following are features that I have added for ease of use.

- Every hour or so, the program will exit the lesson and restart it. This is so you continue to gain credit for the AFK time. I have found that after around an hour you no longer get credit while reading the lecture. This resets that timer so you keep getting credit.
- When you move your mouse at all, the bot wont work. You can leave it on in the background and as long as you dont leave the mouse still for over 10 seconds, the bot will stay disabled.

## Notes

In the current state of the program, the most you can AFK and get credit for is `5 hours`. You can add on to this if you would like by adding more of the following code snippet:

```py
elif switch_counter == 7200:
      pag.moveTo(a, b, speed)
      pag.leftClick()
      time.sleep(3)

      pag.moveTo(changing_x + a, b2, speed)
      pag.leftClick()
      time.sleep(3)

      changing_x += change_factor
      curr_cords = pag.position()
```

- > You do need to change the number `7200` to whatever increment follows (7200, 9000, 10800, ect.)
