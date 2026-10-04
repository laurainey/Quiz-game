import pgzrun
WIDTH = 870
HEIGHT = 650
TITLE = "Computer Quiz game"

marqee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
skip_box = Rect(0,0,150,330)
score_box = Rect(0,0,150,50)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
timer_box = Rect(0,0,150,150)

marqee_box.move_ip(0,0)
question_box.move.ip(20,100)
skip_box.move.ip(700,270)
score_box.move.ip(700,50)
answer_box1.move.ip(20,270)
answer_box2.move.ip(370,270)
answer_box3.move.ip(20,450)
answer_box4.move.ip(370,450)
timer_box.move.ip(700,170)

score = 0
time_left = 10
question_count = 0
question_index=
is_game_over = False
question_file = ""
marquee_msg = ""

quetstion = []
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]


pgzrun.go()
