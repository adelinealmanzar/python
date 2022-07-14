# exercise
is_magician = True
is_expert = False

#check if magicion AND expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")
#check if magician but not expert: "at least you're getting there"
elif is_magician and not(is_expert):
    print("at least you're getting there")
#if you're not a magician: "you need magical powers"
elif not(is_magician):
    print("you need magical powers")
