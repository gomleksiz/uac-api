from .utils import prepare_payload, prepare_query_params

# - create_custom_day(custom_day_data)
# - delete_custom_day(custom_day_id)
# - list_custom_day_qualifying_dates(custom_day_id)
# - list_custom_day_qualifying_periods(custom_day_id)
# - list_local_custom_day_qualifying_dates(custom_day_id)
# - list_local_custom_day_qualifying_periods(custom_day_id)


class CustomDays:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_custom_day(self, query=None, **args):
        '''
        Arguments:
        - customdayid: customdayid 
        - customdayname: customdayname 
        '''
        url="/resources/customday"
        field_mapping={
            "customdayid": "customdayid", 
            "customdayname": "customdayname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_custom_day(self, payload=None, **args):
        url="/resources/customday"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_custom_day(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/customday"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_custom_day(self, query=None, **args):
        '''
        Arguments:
        - customdayid: customdayid 
        - customdayname: customdayname 
        '''
        url="/resources/customday"
        field_mapping={
          "customdayid": "customdayid", 
          "customdayname": "customdayname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_custom_days(self):
        url="/resources/customday/list"
        return self.uc.get(url)

    def list_qualifying_dates(self, query=None, **args):
        '''
        Arguments:
        - customdayid: customdayid 
        - customdayname: customdayname 
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/customday/qualifyingdates"
        field_mapping={
            "customdayid": "customdayid", 
            "customdayname": "customdayname", 
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_qualifying_periods(self, query=None, **args):
        '''
        Arguments:
        - customdayid: customdayid 
        - customdayname: customdayname 
        - calendarid: calendarid 
        - calendarname: calendarname 
        '''
        url="/resources/customday/qualifyingperiods"
        field_mapping={
            "customdayid": "customdayid", 
            "customdayname": "customdayname", 
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)