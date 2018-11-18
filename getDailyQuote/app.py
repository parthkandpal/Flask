from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    return "This is an app build using Flask.  input /hello/yourname in URL to get Daily Quote"

#@app.route("/hello/<string:name>")


@app.route("/hello/<string:name>/")
def hello(name):
    #    return name
    quotes = ['Learning to listen is the essence of intelligent living. -Sadhguru',
              'Confidence and stupidity are a very dangerous combination, but they generally go together. -Sadhguru',
              'Death is a fiction created by people who live their lives in total unawareness. There is only life, life and life alone, moving from one dimension to another, another dimension to another. -Sadhguru',
              'When you have that, you dream of this and when you have this, you dream of that. Maybe you call it romantic, but it’s just plain stupidity. It destroys life. -Sadhguru',
              'It is our compulsive reaction to the situations in which we are placed that causes stress. -Sadhguru',
              'The only thing that stands between you and your well-being is a simple fact: you have allowed your thoughts and emotions to take instruction from the outside rather than the inside.-Sadhguru',
              'To rise above the modifications of your mind, when you cease your mind, when you cease to be a part of your mind, that is yoga. -Sadhguru',
              'Your life is just about craving, and making something else tremendously more important than you. -Sadhguru',
              'To program the calories you must consume and the number of hours you must sleep is a foolish way to handle life. -Sadhguru',
              'Confusion is a good state to be in. It means you are looking, constantly looking.  -Sadhguru',
              'The man who does only as much as is needed will only get that much. -Sadhguru',
              'Generally, the smartest people on the planet – those people who think they are really smart – tend to have the most horrible relationships. -Sadhguru',
              'Yogis are not against pleasure. It is just that they are unwilling to settle for little pleasures. They are greedy. -Sadhguru',
              'Money is definitely needed, but how much money do we really need? If we would change our idea of a successful life to a joyful life, we would find our need for money would dramatically decrease. -Sadhguru',
              'The way you eat not only decides your physical health, but the very way you think, feel, and experience life. Trying to eat intelligently means understanding what kind of fuel this body is designed for and accordingly supplying it, so that it functions at its best. -Sadhguru',
              'To be enlightened is not a condition of certainty. It is to move from limited knowing to boundless unknowing, from gravitas to grace. -Sadhguru',
              'The most incredible thing is that you can know everything you wish to know with your eyes closed. -Sadhguru',
              'Most carnivorous animals do not eat every day—definitely not three times a day! They know the food they eat moves very slowly through their tracts. -Sadhguru',
              'Mysticism is like pure science; it has no use. Mysticism is just the human longing to know… Occult is not science. Occult is just technology. -Sadhguru',
              'You cannot choose a Guru. Deepen your longing and the Guru will choose you. -Sadhguru',
              'Only if you know to what extent your logic should go and where it should not go, your life will be beautiful. -Sadhguru',
              'One should use information and logic as a drunkard would use a lamp post, only for support, not for illumination. -Sadhguru',
              'Your body is on loan from the planet. All the countless numbers of people who have lived on this planet before you and me have all become topsoil, and so will you. This planet will collect back atom by atom what it has loaned to you. -Sadhguru',
              'Responsibility simply means your ability to respond. -Sadhguru',
              ]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]

    images = [
                "https://i.pinimg.com/564x/83/4a/ae/834aae96670c642483246f7afccc56eb.jpg",
                "https://i.pinimg.com/564x/c0/95/02/c0950274ef1bdaa908c18168037e9392.jpg",
                "https://i.pinimg.com/564x/1c/5e/2d/1c5e2d75dec4b99900b88ef011fa036c.jpg",
                "https://i.pinimg.com/564x/43/22/c1/4322c14d80a507d4bbeb067add0d05fe.jpg",
                "https://i.pinimg.com/564x/44/f2/e5/44f2e58fc3731a5d7a83fbc9f3bc0c38.jpg",
                "https://i.pinimg.com/564x/97/65/8c/97658c803c01c0a45eced2f04f2b5407.jpg",
                "https://i.pinimg.com/564x/50/29/07/502907537dc2f5c8f6afc7f65d484e8d.jpg",
                "https://i.pinimg.com/564x/1c/5e/2d/1c5e2d75dec4b99900b88ef011fa036c.jpg",
                "https://i.pinimg.com/564x/60/4e/5e/604e5e975a0983a39be5c62a59c937ff.jpg",
                "https://i.pinimg.com/564x/ae/8f/68/ae8f682bd99e14b6ed5dd8ab491373b4.jpg",
                "https://i.pinimg.com/236x/50/87/8b/50878b503f859e59c33e165368485a18.jpg",
                "https://i.pinimg.com/564x/bb/b7/4b/bbb74bb48663bac9bd5534e29e4135e6.jpg",
                "https://i.pinimg.com/236x/79/92/3b/79923b552324589d31bfcfbb729e7429.jpg",
                "https://i.pinimg.com/564x/41/b4/c7/41b4c7edf630765efb3a0d1cc82ee555.jpg",
                "https://i.pinimg.com/564x/7f/88/20/7f88205deeba30cf30b97892f61b2e94.jpg",
                "https://i.pinimg.com/originals/1c/bb/e5/1cbbe505da25b31ff2fc1227859d066d.jpg",
                "https://i.pinimg.com/564x/ea/9c/ef/ea9cefc6d1f01a6bdda15c28737f4f7b.jpg",
                "https://i.pinimg.com/originals/98/f9/52/98f952860276b67287ae20a7b0899d14.jpg",
                "https://i.pinimg.com/originals/90/c2/34/90c2340c026a52241f88adaed588d776.jpg",
                "https://i.pinimg.com/originals/28/65/38/286538bc96d5bcd86f112c8faa00c562.jpg",
                "https://i.pinimg.com/564x/37/85/eb/3785eb7d7fdd361c6444dedb79704413.jpg",
                "https://i.pinimg.com/564x/06/c0/eb/06c0ebc5c7cdd2ab4b573273a3e53dac.jpg",
                "https://i.pinimg.com/564x/8c/be/5b/8cbe5b91f118f4748645b3241ae501a0.jpg",
                "https://i.pinimg.com/564x/37/85/eb/3785eb7d7fdd361c6444dedb79704413.jpg",
                "https://i.pinimg.com/originals/3d/41/3a/3d413a3e3490509b4ca3d1e4e6fe6529.jpg",
                "https://i.pinimg.com/564x/2d/a6/cf/2da6cfe1e60d3f782ba2049d8dd37296.jpg",
                "https://i.pinimg.com/564x/fa/bd/66/fabd66043be600670f6a120aa78bb027.jpg",
                "https://i.pinimg.com/564x/a4/96/cd/a496cd64cc95b55a6bb83739b4314bcd.jpg",
                "https://i.pinimg.com/564x/7a/36/22/7a36229796527e63fc12e72a273b7d26.jpg",
                "https://i.pinimg.com/564x/a5/e8/57/a5e8575f68cb45dafbd623ca0a7d0029.jpg",
                "https://i.pinimg.com/564x/71/55/fd/7155fd8f9255456b979791b059f5e2a5.jpg",
                "https://i.pinimg.com/564x/87/77/c7/8777c7ef5fbb745d6d10754aae598e90.jpg",
                "https://i.pinimg.com/564x/3f/c8/d7/3fc8d710eaa2a8bd1838c6887a3065d3.jpg",
                "https://i.pinimg.com/564x/57/a1/1c/57a11c50a5762096f4d6ed9ae8252028.jpg",
                "https://i.pinimg.com/564x/19/93/3c/19933c4dfb09046f06b8e7c2eeaf4226.jpg",
                "https://i.pinimg.com/564x/c1/74/67/c17467659ea37570f6ecd6a14cd48837.jpg",
                "https://i.pinimg.com/564x/bc/5b/14/bc5b149af52f92acf79a782eb1acb16b.jpg",
                "https://i.pinimg.com/564x/2c/2b/1a/2c2b1a1d37a4b4cda965d64b907fb24c.jpg",
                "https://i.pinimg.com/564x/79/73/37/7973377b002f57af9fae799a6877be98.jpg",
                "https://i.pinimg.com/564x/66/91/dc/6691dc8b77e9ab9879f706ff26912347.jpg",
                "https://i.pinimg.com/564x/30/05/e7/3005e79f5714d11978790ef81c350e03.jpg",
                "https://i.pinimg.com/564x/5a/b4/29/5ab4294dc64134fff78033c0f67f06d9.jpg",
                "https://i.pinimg.com/564x/53/43/27/534327e0a8a79346dc26498409e74dc9.jpg",
                "https://i.pinimg.com/564x/61/f1/c1/61f1c16286c02c9728b5e7bc0330bbce.jpg",
                "https://i.pinimg.com/originals/31/b5/97/31b597d1efd68ee71ea8928631a420bd.jpg",
                "https://i.pinimg.com/564x/12/a8/54/12a8546d767fd5cc74dbb9ef98170c2f.jpg",
                "https://i.pinimg.com/564x/e7/a9/b7/e7a9b7a4fda71572ef53ae1c67d21ff8.jpg",
                "https://i.pinimg.com/564x/9c/88/7c/9c887cf0778de3a8d8c2dd57e389e63e.jpg",
                "https://i.pinimg.com/564x/7e/3d/77/7e3d779ebf6080bab701e26ff3297c3b.jpg",
                "https://i.pinimg.com/564x/21/43/c5/2143c5fa0dfcb017ca7f2b5ad1513c07.jpg",
                "https://i.pinimg.com/564x/06/67/00/066700da0e2d345f61ceaf71a2a9921b.jpg",
                "https://i.pinimg.com/originals/ae/61/13/ae61136bad7caaabcf02164fb1624d06.jpg",
                "https://i.pinimg.com/564x/a3/8e/18/a38e18f937bc08e671aa661c419bf458.jpg",
                "https://i.pinimg.com/564x/f8/8b/7f/f88b7fb60bd8a49438dd0228dee9e09a.jpg",
            ]
    randomNumber = randint(0, len(images) - 1)
    image= images[randomNumber]



    return render_template(
        'hello.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
