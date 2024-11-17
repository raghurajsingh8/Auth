import re
# import dns.resolver

def is_valid_email(email):
    # Regular expression for basic email format validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def domain_exists(domain):
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except:
        return False

def check_email_existence(email):
    if not is_valid_email(email):
        return "Invalid email format"
    
    domain = email.split('@')[-1]
    if not domain_exists(domain):
        return "Domain does not exist"
    
    return "Email appears to be valid"

# Example usage
email = input("Enter an email address: ")
result = check_email_existence(email)
print(result)
