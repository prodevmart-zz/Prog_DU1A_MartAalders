def new_password(oldpassword,newpassword):
	if newpassword != oldpassword and len(newpassword) > 6: 
		return True;
	else:
		return False;
print(new_password("Heello","dsfsd"))