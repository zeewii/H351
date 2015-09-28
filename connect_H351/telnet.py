#coding:utf-8
#Description:通过telnet远程操作路由器
__author__ = 'yinxia'
import time
import telnetlib
#description:通过telnet远程操作路由器，现只适用于H351
#
#Input:host-主机名或ip,cmd-命令
#
#Output:result-命令执行结果
def telnet_cmd(host,cmd):
    user = "100msh"
    pwd1 = "100msh"
    pwd2 = "@w$r^y*i90"
    try:
        tn = telnetlib.Telnet(host)
        tn.read_until('Username:')
        tn.write(user+'\n')

        tn.read_until('Password:')
        tn.write(pwd1+'\n')

        tn.read_until('router>')
        tn.write('sh\n')

        tn.read_until('Password:')
        tn.write(pwd2+'\n')

        tn.read_until('root@100msh:/#')
        tn.write(cmd+'\n')

        time.sleep(5)#防止网络延时，非常必要
        result = tn.read_very_eager()
        tn.close()
        return result
    except Exception,e:
        print u"telnet打开存在异常"
        print e

if __name__ == '__main__':
    user = '100msh'
    ip = '192.168.11.1'
    password1 = '100msh'
    password2 = '@w$r^y*i90'
    command = 'ifconfig br-lan'
    result = telnet_cmd(ip,command)
    print result