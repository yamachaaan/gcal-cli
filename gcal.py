class Gcal():
    def get_cal_id_list(self, service, page_token):
        cal_list = service.calendarList().list(pageToken=page_token).execute()
        cal_id_list = []
        for cal in cal_list['items']:
            if (str(cal['accessRole'])) ==  'owner':
                cal_id_list.append(str(cal['id']))
        return cal_id_list

    def get_today(self, service, cal_id_list):
        import datetime
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        result = 'today'
        event_list = []
        for cal_id in cal_id_list:
            event = service.events().get(calendarId=cal_id, eventId='').execute()
            event_list.append(event['items'])
        return event_list

    def get_week(self):
        result = 'today'
        return result

    def get_tow_week(self):
        result = 'today'
        return result

    def get_month(self):
        result = 'today'
        return result
