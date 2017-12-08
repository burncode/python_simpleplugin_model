#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
	Copyright (C) 2017 - All Rights Reserved
	模块名称: PluginMain.py
	创建日期: 2017/12/8 14:20
	代码编写: fanwen
	功能说明: 
	
'''

import os
import sys
from imp import find_module
from imp import load_module

class CPluginManager:
    def __init__(self):
        self.plugin_dict = {};
        self.plugin_path = "./plugin";

    def LoadAllPlugin(self):
        pluginPath = self.plugin_path;
        if not os.path.isdir(pluginPath):
            raise EnvironmentError, '%s is not a directory' % pluginPath;

        items = os.listdir(pluginPath);
        for item in items:
            if item.endswith('.py') and item != '__init__.py':
                moduleName = item[:-3];
                print moduleName;
                if moduleName not in sys.modules:
                    fileHandle, filePath, dect = find_module(moduleName, [pluginPath]);

                try:
                    moduleObj = load_module(moduleName, fileHandle, filePath, dect)
                finally:
                    if fileHandle: fileHandle.close();

                # 加载插件模块对应的IService
                HService = moduleObj.Load_This_Plugin(self);
                if HService != None:
                    print HService.name, HService.version;
                    self.plugin_dict[HService.name] = HService;

    def StartAllService(self):
        for service in self.plugin_dict.itervalues():
            service.Start();

    def StoptAllService(self):
        for service in self.plugin_dict.itervalues():
            service.Stop();

    def DispatchReq(self):
        for service in self.plugin_dict.itervalues():
            try:
                service.Exec("run cmd");
            except Exception as e:
                print e;

if __name__ == "__main__":
    # print sys.__getattribute__();
    pm = CPluginManager();
    pm.LoadAllPlugin();
    pm.StartAllService();
    pm.DispatchReq();
    pm.StoptAllService();