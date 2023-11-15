# def desp():
#     def show():
#         return "show function"
#     result=show()+"dispfunction"
#     return result
# print(desp())

# def desp(st):
#     def show():
#         return "show function"
#     result=show()+"dispfunction"
#     return result
# print(desp("geekyshows"))

def disp(sh):
    print("dispfunction"+sh())
def show():
    return "show function"
disp(show)