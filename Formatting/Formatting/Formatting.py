def convert(temp):
    F = temp * 1.8 + 32
    return F

def table():
    print('   {:7}{}'.format('F', 'C'))
    for i in range(-30, 41, 10):
        C = i
        Far = convert(i)
        print('{:5}   {:5}'.format(Far, float(C)))

table()