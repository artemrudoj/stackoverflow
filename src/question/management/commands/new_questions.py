# -*- coding: utf-8 -*-
from random import randint
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from question.models import Question, Answer, Rates
from random import randrange
from datetime import timedelta, datetime

__author__ = 'artem'




titles = [
    u'What are your strengths?',
    u'What are your weaknesses?',
    u'What are three things your former manager would like you to improve on?',
    u'Are you willing to relocate?',
    u'Are you willing to travel?',
    u'What is your dream job?',
    u'What are your weaknesses?',
    u'Why should we hire you?',
    u'What can you do for us that other candidates cant?',
    u'Why are you looking for a new job?',
    u'Would you work holidays/weekends?',
    u'What are three positive things your last boss would say about you?',
    u'What salary are you seeking?',
    u'If you were an animal, which one would you want to be?',
    u'What do you like the most and least about working in this industry?',
    u'Are you a leader or a follower?',
    u'What are your hobbies?',
    u'What would your direct reports say about you?',
    u'What are your career goals?',
    u'What is the name of our CEO?',
]

answers = [
    u"Another seemingly innocuous question, this is actually a perfect opportunity to stand out and show your passion for and connection to the company. For example, if you found out about the gig through a friend or professional contact, name drop that person, then share why you were so excited about it. If you discovered the company through an event or article, share that. Even if you found the listing through a random job board, share what, specifically, caught your eye about the role.",
    u"It’s a free class from The Muse with short, practical and—dare we say—fun lessons sent directly to you.",
    u"Any candidate can read and regurgitate the company’s “About” page. So, when interviewers ask this, they aren't necessarily trying to gauge whether you understand the mission—they want to know whether you care about it. Start with one line that shows you understand the company's goals, using a couple key words and phrases from the website, but then go on to make it personal. Say, “I’m personally drawn to this mission because…” or “I really believe in this approach because…” and share a personal example or two.",
    u'''Again, companies want to hire people who are passionate about the job, so you should have a great answer about why you want the position. (And if you don't? You probably should apply elsewhere.) First, identify a couple of key factors that make the role a great fit for you (e.g., “I love customer support because I love the constant human interaction and the satisfaction that comes from helping someone solve a problem"), then share why you love the company (e.g., “I’ve always been passionate about education, and I think you guys are doing great things, so I want to be a part of it”).''',
    u"This question seems forward (not to mention intimidating!), but if you're asked it, you're in luck: There's no better setup for you to sell yourself and your skills to the hiring manager. Your job here is to craft an answer that covers three things: that you can not only do the work, you can deliver great results; that you'll really fit in with the team and culture; and that you'd be a better hire than any of the other candidates.",
    u"If you are currently employed, you should be honest about the start date and show professionalism. You should tell them you would have to discuss a transition with your current company and see if they require a two-week notice. If you currently have a critical role, your potential new employer would expect a transition period.",
    u"If you can start right away (and they know you are not currently employed), you certainly can say you’re able to start tomorrow. Sense of urgency and excitement about starting work at the new company is always a good thing.",
    u"Here’s another opportunity to differentiate yourself. Everyone claims to be: a hard worker, good communicator, and team player. But how many are a: problem-solver, game-changer, leader in the industry? Be creative, and have stories to back it up. The interviewer will want to know why someone thinks you are one of these things.",
    u"A question that can sink you unless you’re careful. Obviously, “I work too hard” is not the answer.",
    u"Before a face-to-face, you typically have a phone screen you need to get through. Here are some tips for getting through to the next round.",
    u"Now granted some of these questions may seem tired and cliche, but I guarantee you they are still being asked in interview rooms consistently, around the world. So you need to prepare for them!",
    u"Leverage your company research and the job description to find exactly why the company is hiring someone for this position. What problem/pain points does the new hire have to solve? You need to show that you are the perfect candidate that can solve those problems/pain points.",
    u"Don’t get discouraged if the hiring manager mentions that “they have lots of very well qualified candidates…” before they lead into this question. (It’s a common “lead in”)",
    u"Grab hold of the opportunity this question gives you. This question really lets you guide the interview where you want it to go. This your chance to relate your most impressive success story, so take advantage!",
    u"This classic question freaks people out but it shouldn’t. As long as you pick a weakness that isn’t a key competency for the job and you show that you have taken steps to “work on it”, you will be fine.",
]



tags = [
    u'C++',
    u'python',
    u'java',
    u'swift',
    u'android',
    u'development',
    u'C',
    u'filesystem',
    u'opengl',
    u'c#',
    u'x86',
    u'arm',
    u'localhost'
]


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        count = options['n']
        # for answer in Answer.objects.all():
        #     answer.delete()
        # for question in Question.objects.all():
        #     question.delete()
        for q in Question.objects.all():
            q.delete()
        for r in Rates.objects.all():
            r.delete()
        for i in range(0, count):
            number = randint(0,len(titles)-1)
            question = Question()
            question.title = titles[ number ]
            number = randint(0,len(titles)-1)
            question.text = titles[ number ]
            User = get_user_model()
            number = randint(0,User.objects.count()-1)
            question.author = User.objects.all()[number]
            d1 = datetime.strptime('1/1/2014 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('1/1/2015 4:50 AM', '%m/%d/%Y %I:%M %p')
            question.data = random_date(d1, d2)
            rate = Rates()

            number = randint(0,User.objects.count())
            rate.count = number
            rate.save()
            for i in range(number):
                rate.users.add(User.objects.all()[i])
            question.rate = rate
            number = randint(0,len(tags)-1)
            question.save()

            for i in range(number):
                question.addTag(tags[i])
            for j in range(0,randint(0,10)):
                answer = Answer()
                number = randint(0,len(answers)-1)
                answer.text = answers[number]
                d1 = datetime.strptime('1/1/2014 1:30 PM', '%m/%d/%Y %I:%M %p')
                d2 = datetime.strptime('1/1/2015 4:50 AM', '%m/%d/%Y %I:%M %p')
                answer.data = random_date(d1, d2)
                rate = Rates()
                rate.count = number
                rate.save()
                number = randint(0,User.objects.count())
                for i in range(number):
                    rate.users.add(User.objects.all()[i])
                answer.rate = rate
                number = randint(0,len(titles)-1)
                answer.title = titles[ number ]
                number = randint(0,User.objects.count()-1)
                answer.author = User.objects.all()[number]
                answer.question = question
                answer.save()


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)