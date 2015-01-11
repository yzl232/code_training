# encoding=utf-8
'''
假设有许多geographically distributed servers，用户可以向这些server request a ID。要求：1、ID必须globally unique；2、ID的ordering需要尽可能的反映现实时间；3、效率。
'''
'''
比如n台机器  我们可以用时间戳___机器id____每秒内的count     连接的形式 时间戳可以采取年月日时分秒，
'''