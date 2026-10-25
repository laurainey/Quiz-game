import pgzrun

WIDTH = 870
HEIGHT = 650
TITLE = "QUIZ GAME"

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
score_box = Rect(0,0, 150, 50)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
score_box.move_ip(700,50)
skip_box.move_ip(700,270)
timer_box.move_ip(700,100)

#Game variables

score = 0
timer_left = 10
question_count = 0
question_index = 0
is_game_over = False
question_file = "questions.txt"
marquee_msg = ""

questions = []
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

def draw ():
    global marquee_msg
    screen.clear()
    screen.fill("#20E2D7")
    screen.draw.filled_rect(marquee_box,"#20E2D7")
    screen.draw.filled_rect(question_box, "#FD88EA")
    screen.draw.filled_rect(timer_box, "#6F16CA")
    screen.draw.filled_rect(score_box, "#6F16CA")
    screen.draw.filled_rect(skip_box,"#FF006E")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "#74B31B")

    marquee_msg = f"Welcome to the quiz game Mastermind! You are at question {question_index}/{question_count}"

    screen.draw.textbox(marquee_msg,marquee_box, color = "#5200D6")
    screen.draw.textbox(f"{timer_left}",timer_box, color = "#F8E4C1",shadow= (0.5, 0.5),scolor= "gray")
    screen.draw.textbox(f"Score:{score}",score_box , color = "#F8E4C1" )
    screen.draw.textbox(f"SKIP",skip_box, color="#F7FF84",angle = -90)
    screen.draw.textbox(f"{question[0]}",question_box,color= "#4930E0" , shadow = (0.5,0.5), scolor= "#3F9491")

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(f"{question[index]}", answer_box, color= "#530854")
        index += 1

def update():
    move_marquee()

def move_marquee():
    global marquee_box
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0 :
        marquee_box.left = WIDTH

def read_question_file():
    global question_count, questions
    q_file = open(question_file,"r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")


def on_mouse_down(pos):
    index = 1
    for answer_box in answer_boxes:
        if answer_box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()

            else:
                game_over()
        index += 1

    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global question, timer_left, score, questions
    score += 1
    if questions:
        question = read_next_question()
        timer_left = 10

    else:
        game_over()

def game_over():
    global question, timer_left, is_game_over
    message = f"Game over!\n You final score is {score}!"
    question = [message,"-","-","-","-",5]
    timer_left = 0
    is_game_over = True

def skip_question():
    global question, timer_left
    if questions and not is_game_over:
        question = read_next_question()
        timer_left = 10
    else:
        game_over()

def update_timer_left():
    global timer_left
    if timer_left:
        timer_left -= 1
    else: 
        game_over()



read_question_file()
question = read_next_question()
clock.schedule_interval(update_timer_left, 1)

pgzrun.go()