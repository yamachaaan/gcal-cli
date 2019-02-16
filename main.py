#!/usr/bin/env python
# _*_ coding:utf-8_*_

from lib.argument import Argument
from lib.auth import Auth
from gcal import Gcal

class Main():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def main(self):
        args = argument.get_argument()
        service = auth.get_auth()
        page_token = None
        cal_id_list = gcal.get_cal_id_list(service, page_token)

        if args.function.lower() == 'day':
            result_json = gcal.get_today(service, cal_id_list)
        elif args.function.lower() == 'week':
            result_json = gcal.get_week()
        elif args.function.lower() == 'week':
            result_json = gcal.get_tow_weeks()
        elif args.function.lower() == 'month':
            result_json = gcal.get_month()
        self.result_print(result_json)
        return

    def result_print(self,result_json):
        print(type(result_json))
        return

if __name__ == '__main__':
    argument = Argument()
    auth = Auth()
    gcal = Gcal()
    main = Main()
    main.main()
