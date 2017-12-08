#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
	Copyright (C) 2017 - All Rights Reserved
	模块名称: IPlugin.py
	创建日期: 2017/12/8 13:56
	代码编写: fanwen
	功能说明: 
	
'''

def Load_This_Plugin(hServiceManager):
    """
    插件模块被装载的入口，每个插件都需要实现此接口，并且在此接口中返回所实现的插件句柄
    :param hServiceManager:
    :return:
    """
    return None;

class IService:
    def __init__(self, hServiceManager):
        self.name = "IService";         # 模块名称
        self.version = "0.0.1";         # 当前版本
        self.hServiceManager = hServiceManager;   # 上层插件控制句柄，可以通过此句柄获得相关的服务

    def Start(self):
        """
            启动服务
        :return: True or False
        """
        pass;

    def Stop(self):
        """
            停止服务
        :return: True or False
        """
        pass;

    def Exec(self, req):
        """
        服务调度函数, 该函数会被上层框架调用
        :param req: 待执行的请求
        :return:    返回执行结果
        """
        pass;


