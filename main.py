#!/usr/bin/env python
# _*_ coding:utf-8_*_

from lib.argument import Argument
from lib.auth import Auth
from gcal import Gcal
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Main():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def main(self):
        args = argument.get_argument()
        if args.function.lower() == 'day':
            print('day')
        elif args.function.lower() == 'week':
            print('week')
        elif args.function.lower() == 'week':
            print('2week')
        elif args.function.lower() == 'month':
            print('month')
        return

if __name__ == '__main__':
    argument = Argument()
    auth = Auth()
    gcal = Gcal()
    main = Main()
    main.main()
