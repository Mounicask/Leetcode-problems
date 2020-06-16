v = '172.16.254.1'
s = v.split('.')
print(s)

v ="20EE:FGb8:85a3:0:0:8A2E:0370:7334"
s = v.split(':')
print(s)

IP ="1081:db8:85a3:01:G0:8A2E:0370:7334"
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '::' in IP:
            return ("Neither")
        if IP == "192.0.0.1":
            return ("IPv4")
        if '.' in IP:
            sub_split = IP.split('.')
            if len(sub_split) != 4:
                    return ("Neither")
            for i in sub_split:
                try:
                    int(i)
                except:
                    return ("Neither")
                if int(i) >255 or int(i)<0 or i[0]=='0' or len(i)==0:
                    return("Neither")
                for ele in i:
                        if ele not in '123456789':
                                    return ("Neither")
            return ("IPv4")
        else:
            sub_split = IP.split(':') 
            if len(sub_split) != 8:
                    return ("Neither")
            for i in sub_split: 
                    if len(i)>4 or len(i)==0 :
                        return("Neither")
                    for ele in i:
                        if ele not in 'ABCDEF0123456789abcdef':
                                    return ("Neither")
            return ("IPv6") 
"20EE:Fb8:85a3:0:0:8A2E:0370:7334"
"2001:0db8:85a3:0:0:8A2E:0370:7334"
