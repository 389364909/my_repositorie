
def catch(url):
    import requests
    code = (requests.get(url,timeout=10)).text
    #print(code)
    with open('code.txt','w') as code_:
        code_.write(code)

if __name__ == "__main__":
    url_ = input("url:")
    catch(url_)




