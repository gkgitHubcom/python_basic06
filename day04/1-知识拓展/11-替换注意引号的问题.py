
ss = '{"mobile_phone":#member_id#,"passwd":"123456789"}'
member_id = "16"
new_ss = ss.replace("#member_id#",member_id)
print(new_ss)