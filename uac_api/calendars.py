# - add_existing_custom_day_to_calendar(calendar_id, custom_day_id)
# - create_calendar(calendar_data)
# - delete_calendar(calendar_id)
# - list_calendars()
# - modify_calendar(calendar_id, **kwargs)
# - read_calendar(calendar_id)
# - read_all_custom_days_of_calendar(calendar_id)
# - remove_custom_day_from_calendar(calendar_id, custom_day_id)

from .utils import prepare_payload, prepare_query_params

class Calendars:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc
    
    def get_custom_days(self, query=None, **args):
        '''
        Arguments:
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/calendar/customdays"
        field_mapping={
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def add_custom_day(self, payload=None, **args):
        '''
        Arguments:
        - calendarid: calendarid 
        - calendarname: calendarname 
        - customdayid: customdayid 
        - customdayname: customdayname 
        '''
        url="/resources/calendar/customdays"
        field_mapping={
          "calendarid": "calendarid", 
          "calendarname": "calendarname", 
          "customdayid": "customdayid", 
          "customdayname": "customdayname", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def remove_custom_day(self, query=None, **args):
        '''
        Arguments:
        - calendarid: calendarid 
        - calendarname: calendarname 
        - customdayid: customdayid 
        - customdayname: customdayname 
        '''
        url="/resources/calendar/customdays"
        field_mapping={
          "calendarid": "calendarid", 
          "calendarname": "calendarname", 
          "customdayid": "customdayid", 
          "customdayname": "customdayname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def get_calendar(self, query=None, **args):
        '''
        Arguments:
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/calendar"
        field_mapping={
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_calendar(self, payload=None, **args):
        url="/resources/calendar"
        _payload = payload
        return self.uc.put(url, json_data=_payload)

    def create_calendar(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/calendar"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def delete_calendar(self, query=None, **args):
        '''
        Arguments:
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/calendar"
        field_mapping={
          "calendarid": "calendarid", 
          "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_calendars(self):
        url="/resources/calendar/list"
        return self.uc.get(url)

    def list_qualifying_dates_for_local_custom_day(self, query=None, **args):
        '''
        Arguments:
        - customdayname: customdayname 
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/calendar/localcustomdays/qualifyingdates"
        field_mapping={
            "customdayname": "customdayname", 
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_qualifying_periods(self, query=None, **args):
        '''
        Arguments:
        - customdayname: customdayname 
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/calendar/localcustomdays/qualifyingperiods"
        field_mapping={
            "customdayname": "customdayname", 
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)