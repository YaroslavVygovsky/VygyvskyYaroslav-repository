list=['Юля','Виталий','Алексей']
message=f"Приглашаю вас на обед,{list[0],list[1],list[2]}"
print(message)
print(list[1])
list[1]='Жора(голубь)'
message2=f"Приглашаю вас, мои лучшие друзья, ко мне на обед (Жора будет на закусь), {list[0],list[1],list[2]}"
print(message2)
list.append('Максим')
list.insert(0,'Велимир')
list.insert(3,'Тимур')
message3=f"Гоу ко мне на обед, {list[0],list[1],list[2],list[3],list[4],list[5]}"
print(message3)
print('Нас еще больше!',list)
del_list=list.pop()
message4=f"Извини что ты не прийдешь, {del_list}"
print(message4)
del_list=list.pop()
message5=f"Извини что ты не прийдешь, {del_list}"
print(message5)
del_list=list.pop()
message6=f"Извини что ты не прийдешь, {del_list}"
print(message6)
del_list=list.pop()
message7=f"Извини что ты не прийдешь, {del_list}"
print(message7)
print(list)
message8=f"Предложение еще в силе, {list[0],list[1]}"
print(message8)
t=len(list)
print(t)
del(list[0])
del(list[0])
print(list)
