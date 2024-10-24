#HTTP status codes program

#-------------------------
#Subprograms
#-------------------------
def http_status(status):
    match status:
        #400 error.
        case 400:
            return "Bad request"
        #401 and 403 errors
        case 401 | 403:
            return "Authentication error"
        #404 error.
        case 404:
            return "Not found"
        #All other errors.
        case _:
            return "Unknown error"

#-------------------------
#Main Program
#-------------------------
code = 404
print(http_status(code))