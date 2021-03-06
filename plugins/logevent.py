#coding=UTF8

"""
日志记录插件，编写完插件后，需要在PluginList.txt添加插件文件名
"""

import traceback
import os
import time
import plugin
QQPlugin = plugin.QQPlugin
webqqsdk = plugin.webqqsdk # webqqsdk模块
MsgEvent = webqqsdk.msgevent.MsgEvent

#from webqqsdk import entity



class LogMsgEvent(MsgEvent):
    __doc__ = u"处理日志信息"


    def main(self,msg):
        """
        main方法必须存在,注意此方法需存在一个参数用于传入消息实例
        """
            
        print msg.msg.encode("gbk","ignore")
        print time.ctime()
        


# 必须：
#    要有个类，类名是Plugin，且继承于QQPlugin
class Plugin(QQPlugin):

    def install(self):


        # 类继承的方式添加事件
        event = LogMsgEvent()
        self.qqClient.addLogMsgEvent(event)

        print u"插件%s被安装了"%(__file__)

    def uninstall(self):

        print u"插件%s被卸载了"%(__file__)




