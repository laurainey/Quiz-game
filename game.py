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
question_box.move.ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
score_box.move_ip(700,50)
skip_box.move_ip(700,270)
timer_box.move_ip(700,170)

#Game variables

score = 0
timer_left = 10
question_count = 0
question_index = 0
is_game_over = False
qestion_file = "questions.txt"
marquee_msg = ""

questions = []
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]





pgzrun.go()