from flask import Flask                                                                            
app = Flask(__name__)                                                                              
                                                                                                                                                                                                      
@app.route('/')                                                                                    
def hello():                                                                                       
    return "Hello COOP Team!\nThis is Jenkins & ArgoCD CI/CI Pipeline test app v29"                                                                        
                                                                                                   
if __name__ == '__main__':                                                                         
    print('start app')     # print문 추가 후 저장                                                  
    app.run(host="0.0.0.0", port=8000) 

