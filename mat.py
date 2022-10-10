def print_rangoli(n): 
    if n <=1:
        print("a")
    else:
        string = 'abcdefghijklmnopqrstuvwxyz'
        l = string[n-1]
        line = (n-1)*4+1
        i = int((line-1)/2)
        k = i-2
        j = n-2
        # 1st 
        print('-'*i+string[n-1]+'-'*i)
        # top 
        while k>=2:
            print('-'*k+'-'.join(string[n-1:j:-1])+'-'+'-'.join(string[j:n])+'-'*k)
            k= k-2
            j= j-1
        # mid
        print('-'.join(string[n-1:0:-1])+"-"+"-".join(string[0:n]))
        # bottom
        k = 2
        j=0
        while k<i:
            print('-'*k+'-'.join(string[n-1:j:-1])+'-'+'-'.join(string[j+2:n])+'-'*k)
            k = k+2
            j = j+1
        # last line
        print('-'*i+string[n-1]+'-'*i)

if __name__ == '__main__':
