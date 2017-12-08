#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
	Copyright (C) 2017 - All Rights Reserved
	模块名称: PlugingTest1.py
	创建日期: 2017/12/8 14:14
	代码编写: fanwen
	功能说明: 
	
'''
from IPlugin import IService



def Load_This_Plugin(hServiceManager):
    return CCephInstall(hServiceManager);

class CCephInstall(IService):
    def __init__(self, hServiceManager):
        IService.__init__(self, hServiceManager);
        self.name = "CephInstall";
        self.version = "0.0.12";

    def Start(self):
        print "%s Start OK!"%self.name;
        return True;

    def Stop(self):
        print "%s Stop OK!"%self.name;
        return True;

    def Exec(self, req):
        print "%s正在执行 %s ......!"%(self.name, req);
        return "{处理成功}";


