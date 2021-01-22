email = input("Enter email id: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f"Your Username is {username} and  domain is {domain}")