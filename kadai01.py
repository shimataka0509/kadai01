#敵の座標を格納する配列
Enemy = []

#味方の座標入力
Allies = input().rstrip().split(' ')
Allies = list(map(int,Allies))

#敵数入力
em = int(input())

#敵の座標入力
for i in range(em):
    enemy = input().rstrip().split(' ')
    enemy = list(map(int,enemy))
    Enemy.append(enemy)

#当たり判定
for j in range(em):
    disx = Enemy[j][0] - Allies[0]
    disx = abs(disx)
    a = Enemy[j][2]/2 + Allies[2]/2
    disy = Enemy[j][1] - Allies[1]
    disy = abs(disy)
    b = Enemy[j][3]/2 + Allies[3]/2

    if disx < a and disy < b:
        t = j + 1
        print("敵"+ str(t)+"と接触")
    

