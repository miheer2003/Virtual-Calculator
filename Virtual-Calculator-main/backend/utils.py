import cv2
import numpy as np

# TO DRAW CALC ON FRAME
def draw_calc(frame, a, b):
    # READ X,Y,H,W VALUES FOR CALC
    try:
        values = np.loadtxt('data/values.txt', int)
        x = values[0]
        y = values[1]
        h = values[2]
        w = values[3]
    except:
        x, y, h, w = 100, 100, 50, 50

    # DRAW HORIZONTAL LINES OF CALC
    color = (255, 0, 0)
    cv2.line(frame, (x, y), (x, y + h * 8), color, 2)
    cv2.line(frame, (x + w, y + h * 2), (x + w, y + h * 7), color, 2)
    cv2.line(frame, (x + w * 2, y + h * 2), (x + w * 2, y + h * 8), color, 2)
    cv2.line(frame, (x + w * 3, y + h * 2), (x + w * 3, y + h * 8), color, 2)
    cv2.line(frame, (x + w * 4, y), (x + w * 4, y + h * 8), color, 2)

    # DRAW VERTICLE LINES OF CALC
    cv2.line(frame, (x, y), (x + w * 4, y), color, 2)
    cv2.line(frame, (x, y + h * 2), (x + w * 4, y + h * 2), color, 2)
    cv2.line(frame, (x, y + h * 3), (x + w * 4, y + h * 3), color, 2)
    cv2.line(frame, (x, y + h * 4), (x + w * 4, y + h * 4), color, 2)
    cv2.line(frame, (x, y + h * 5), (x + w * 3, y + h * 5), color, 2)
    cv2.line(frame, (x, y + h * 6), (x + w * 4, y + h * 6), color, 2)
    cv2.line(frame, (x, y + h * 7), (x + w * 3, y + h * 7), color, 2)
    cv2.line(frame, (x, y + h * 8), (x + w * 4, y + h * 8), color, 2)

    # PUT TEXT IN EVERY CELL
    cv2.putText(frame, "C", (x + a, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "^", (x + w + a, y + 3 * h + b - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "<-", (x + 2 * w + a - 6, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "OFF", (x + 3 * w + a - 6, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.putText(frame, "%", (x + 0 * w + a, y + 4 * h + b - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "%", (x + 0 * w + a, y + 4 * h + b - 3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "/", (x + 1 * w + a, y + 4 * h + b - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.putText(frame, "*", (x + 2 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "-", (x + 3 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "7", (x + 0 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "8", (x + 1 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "9", (x + 2 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "4", (x + 0 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "5", (x + 1 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "6", (x + 2 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "1", (x + 0 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "2", (x + 1 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "3", (x + 2 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, " .", (x + 2 * w + a, y + 8 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "0", (x + int(0.5 * w) + a, y + 8 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "+", (x + 3 * w + a, y + int(5.5 * h) + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "=", (x + 3 * w + a, y + int(7.5 * h) + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

    return frame

# DO CALCULATION ON ANSWER AND PRODUCE RESULT
def calc(ans):
    a, b, y = "", "", ""
    c = 0
    for x in ans:
        if c == 0 and (
                x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "." or x == "0"):
            a += x
        elif x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "." or x == "0":
            b += x
        else:
            y = x
            c = 1

    bb = b
    try:
        a = float(a)
    except:
        a = 0.0
        
    if len(b) != 0:
        b = float(b)
    if len(y) == 0:
        return ans
    elif len(bb) == 0:
        return ""
    elif y == "^":
        a **= b
    elif y == "%":
        a %= b
    elif y == "/":
        if b != 0:
            a /= b
            a = round(a, 5)
        else:
            a = "Error"
    elif y == "*":
        a *= b
    elif y == "-":
        a -= b
    elif y == "+":
        a += b
    else:
        pass

    ans = str(a)
    return ans


# IF USER TRY TO CLICK THEN THIS FUNCTION CHECK WHICH BUTTON WAS CLICKED AND PREFORM APPROIATE ACTION
def press_key(ans, a, b):
    try:
        values = np.loadtxt('data/values.txt', int)
        x = values[0]
        y = values[1]
        h = values[2]
        w = values[3]
    except:
        x, y, h, w = 100, 100, 50, 50
        
    ab = ""
    # Offset 'a' to match the coordinate system if needed, but MediaPipe gives absolute coords on frame
    # The original code had `a = a + 400` because it was using ROI. 
    # MediaPipe uses full frame (800x600).
    # The calculator is drawn at specific coords.
    # Let's assume 'a' and 'b' are already in frame coordinates.
    
    if x < a < x + 4 * w and y + 2 * h < b < y + 8 * h:
        a -= x
        a /= w
        b -= y
        b /= h
        b -= 2
        a = int(a)
        b = int(b)
        if a == 0 and b == 0:
            ans = ""
            ab = "00"
        elif a == 1 and b == 0:
            ans = calc(ans)
            ans += "^"
            ab = "10"
        elif a == 2 and b == 0:
            ans = ans[:len(ans) - 1]
            ab = "20"

        elif a == 3 and b == 0:
            ans = "quit"
            ab = "30"

        elif a == 0 and b == 1:
            ans = calc(ans)
            ans += "%"
            ab = "01"
        elif a == 1 and b == 1:
            ans = calc(ans)
            ans += "/"
            ab = "11"
        elif a == 2 and b == 1:
            ans = calc(ans)
            ans += "*"
            ab = "21"
        elif a == 3 and b == 1:
            ans = calc(ans)
            ans += "-"
            ab = "31"

        elif a == 0 and b == 2:
            ans += "7"
            ab = "02"
        elif a == 1 and b == 2:
            ans += "8"
            ab = "12"
        elif a == 2 and b == 2:
            ans += "9"
            ab = "22"
        elif a == 3 and b == 2:
            ans = calc(ans)
            ans += "+"
            ab = "32"

        elif a == 0 and b == 3:
            ans += "4"
            ab = "03"
        elif a == 1 and b == 3:
            ans += "5"
            ab = "13"
        elif a == 2 and b == 3:
            ans += "6"
            ab = "23"
        elif a == 3 and b == 3:
            ans = calc(ans)
            ans += "+"
            ab = "32"

        elif a == 0 and b == 4:
            ans += "1"
            ab = "04"
        elif a == 1 and b == 4:
            ans += "2"
            ab = "14"
        elif a == 2 and b == 4:
            ans += "3"
            ab = "24"
        elif a == 3 and b == 4:
            ans = calc(ans)
            ab = "34"

        elif a == 0 and b == 5:
            ans += "0"
            ab = "05"
        elif a == 1 and b == 5:
            ans += "0"
            ab = "05"
        elif a == 2 and b == 5:
            ans += "."
            ab = "25"
        elif a == 3 and b == 5:
            ans = calc(ans)
            ab = "34"
        else:
            pass

        return ans, ab
    else:
        return ans, ab
