# -*- coding:utf-8 -*-

import os, datetime, platform
import pm25_city
import rank_city



def run_Task():
    print('开始爬取...'+'\n'+'读取城市列表...')
    rank_city.getCity()
    pm25_city.one_thread()
    print('爬取结束...')

def timerFun(sched_Timer):
    while True:
        now = datetime.datetime.now()
        if sched_Timer <= now < (sched_Timer + datetime.timedelta(hours=1)):
            run_Task()
            sched_Timer += datetime.timedelta(hours=1)
        elif now >= (sched_Timer + datetime.timedelta(hours=1)):
            sched_Timer += datetime.timedelta(hours=1)
        '''
                elif num >= 3600:
            if (sched_Timer-now).total_seconds() > 0:
                pass
            else:
                sched_Timer += datetime.timedelta(hours=1)
        '''



if __name__ == '__main__':
    sched_Timer = datetime.datetime.now()
    print("定时爬取任务已开始，当前时间为 %s" % sched_Timer)
    timerFun(sched_Timer)