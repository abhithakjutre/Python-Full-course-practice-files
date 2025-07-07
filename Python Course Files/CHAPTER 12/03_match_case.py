def https_status(status):
    match status:
        case 200:
            return "Ok"
        case 404: 
            return "Not Found"
        case 500:
            return "Internal server Error"
        case _: 
            return "Unknown status"
        

print(https_status(500))