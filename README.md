# A.I-Yogi
Its an online A.I yoga instructor to teach Yogasanas right at your place. In pandemic mental &amp; physical health is endanger so its best solution as it will teach Yogasanas for physical &amp; mental health


Go to the directory where this project is and run python file.
![Screenshot 2021-06-27 195456](https://user-images.githubusercontent.com/78293363/123548418-58c5a400-d782-11eb-8c7b-76cc3a497b0e.png)

The url would be generated go to that url and flask web would be running on your browser.
Ensure having all require libraries given in requirement.txt file.

## Inspiration
I am from India & from long time back Yoga is very important part of India and it has spread all over the world. I am always very enthusiast about spirituality & mysticism. Also we see in this covid pandemic situation many people's both physical and mental health is endanger. Surveys are saying that even after covid case may happen that we have face mental pandemic which we have started observing. In such case Yoga is best solution. As it creates not just physical but mental well-being too. So I have designed this A.I Yogi platform where people can learn and practice Yogasanas by themselves right at their own place/home which is very much helpful in terms of regulation of pandemic rules and safety.

## What it does
It is A.I based platform. It uses the web camera of your device and maps your body postures and limbs' positions.  It draws a skeleton around user's body in web camera and accordingly from that it knows if user is doing Asanas(Yogasanas) in proper way or not and accordingly update status for user so that user will know.

## How I built it
I used flask frame framework to develop website using python & html. From html page web camera streaming is given which is done from python. Every frame of stream is consider for body position detection. This is done using Mediapipe library. So every frame them is streamed through html page and result is generated and shown on screen as of user is doing asana properly or not.

## Challenges I ran into
Firstly I was trying to do this using JavaScript and html instead of python but it was giving errors in computation so then I shifted flask app with python and now its running properly.

## Accomplishments that I'm proud of
I am proud of the accomplishment that I have created a product which is very useful to all society for not just pandemic situation but all the time that now user can perform and practice asanas at their home with no need of physical instructor.

## What I learned
I learned as to how to use image processing techniques and deep learning libraries or model to detect body positions and how to connect web camera from python to html and create useful things for current situation

## What's next for A.I Yogi
Next part would be to include all 84 asanas in A.I Yogi and also will use augmented reality to create a nice user experience of being in presence of virtual trainer.
