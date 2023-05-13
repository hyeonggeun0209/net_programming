class MyComplex:
    def __init__(self, a, b):
        if a[0] == '-':
            real_1, imaginary_1 = int(a[:2]), int(a[2:-1])
        else:
            real_1, imaginary_1 = int(a[0]), int(a[1:-1])
        
        if b[0] == '-':
            real_2, imaginary_2 = int(b[:2]), int(b[2:-1])
        else:
            real_2, imaginary_2 = int(b[0]), int(b[1:-1])
        calc_real1 = real_1 + real_2
        calc_imaginary1 = imaginary_1 + imaginary_2
        if calc_imaginary1  > 0:
            print(str(calc_real1) + '+' + str(calc_imaginary1) + 'i')
        else:
            print(str(calc_real1) + str(calc_imaginary1) + 'i')
        
        calc_real2 = real_1 - real_2
        calc_imaginary2 = imaginary_1 - imaginary_2
        if calc_imaginary2 > 0:
            print(str(calc_real2) + '+' + str(calc_imaginary2) + 'i')
        else:
            print(str(calc_real2) + str(calc_imaginary2) + 'i')    
        


mycalss = MyComplex('2-3i', '-5+4i')

mycalss