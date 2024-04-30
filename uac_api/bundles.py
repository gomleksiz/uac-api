# - bundle_report()
# - create_bundle(bundle_data)
# - delete_bundle(bundle_id)
# - list_bundles()
# - modify_bundle(bundle_id, **kwargs)
# - read_bundle(bundle_id)
# - bundleless_promotion()
# - cancel_scheduled_bundle_promotion(promotion_id)
# - delete_scheduled_bundle_promotion(promotion_id)
# - promote_bundle_or_schedule_bundle_promotion(bundle_id, promotion_data)
# - create_promotion_target(target_data)
# - modify_promotion_target(target_id, **kwargs)
# - list_promotion_targets()
# - delete_promotion_target(target_id)
# - read_promotion_target(target_id)
# - refresh_target_agents(target_id)

from .utils import prepare_payload, prepare_query_params, prepare_query_payload

class Bundles:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def promote(self, payload=None, **args):
        '''
        Arguments:
        - id: id 
        - name: name 
        - promotionTargetId: promotionTargetId 
        - promotionTargetName: promotionTargetName 
        - notificationOption: notificationOption 
        - overrideUser: overrideUser 
        - overridePassword: overridePassword 
        - date: date 
        - time: time 
        - schedule: schedule 
        - createSnapshot: createSnapshot 
        - allowUnvTmpltChanges: allowUnvTmpltChanges 
        - overrideToken: overrideToken 
        '''
        url="/resources/bundle/promote"
        field_mapping={
          "id": "id", 
          "name": "name", 
          "promotionTargetId": "promotionTargetId", 
          "promotionTargetName": "promotionTargetName", 
          "notificationOption": "notificationOption", 
          "overrideUser": "overrideUser", 
          "overridePassword": "overridePassword", 
          "date": "date", 
          "time": "time", 
          "schedule": "schedule", 
          "createSnapshot": "createSnapshot", 
          "allowUnvTmpltChanges": "allowUnvTmpltChanges", 
          "overrideToken": "overrideToken", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def get_bundle(self, query=None, **args):
        '''
        Arguments:
        - bundleid: bundleid 
        - bundlename: bundlename 
        '''
        url="/resources/bundle"
        field_mapping={
            "bundleid": "bundleid", 
            "bundlename": "bundlename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_bundle(self, payload=None, **args):
        url="/resources/bundle"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_bundle(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/bundle"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_bundle(self, query=None, **args):
        '''
        Arguments:
        - bundleid: bundleid 
        - bundlename: bundlename 
        '''
        url="/resources/bundle"
        field_mapping={
          "bundleid": "bundleid", 
          "bundlename": "bundlename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def create_bundle_by_date(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/bundle/{a}"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def get_bundle_report(self, query=None, **args):
        '''
        Arguments:
        - bundleid: bundleid 
        - bundlename: bundlename 
        '''
        url="/resources/bundle/report"
        field_mapping={
            "bundleid": "bundleid", 
            "bundlename": "bundlename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_bundles(self, query=None, **args):
        '''
        Arguments:
        - bundlename: bundlename 
        - businessServices: businessServices 
        - defaultPromotionTarget: defaultPromotionTarget 
        '''
        url="/resources/bundle/list"
        field_mapping={
            "bundlename": "bundlename", 
            "businessServices": "businessServices", 
            "defaultPromotionTarget": "defaultPromotionTarget", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def promote_1(self, payload=None, **args):
        '''
        Arguments:
        - itemType: itemType 
        - itemIds: itemIds 
        - itemNames: itemNames 
        - items: items 
        - promotionTargetId: promotionTargetId 
        - promotionTargetName: promotionTargetName 
        - overrideUser: overrideUser 
        - overridePassword: overridePassword 
        - excludeOnExistence: excludeOnExistence 
        - followReferences: followReferences 
        - allowUnvTmpltChanges: allowUnvTmpltChanges 
        - overrideToken: overrideToken 
        '''
        url="/resources/promote"
        field_mapping={
          "itemType": "itemType", 
          "itemIds": "itemIds", 
          "itemNames": "itemNames", 
          "items": "items", 
          "promotionTargetId": "promotionTargetId", 
          "promotionTargetName": "promotionTargetName", 
          "overrideUser": "overrideUser", 
          "overridePassword": "overridePassword", 
          "excludeOnExistence": "excludeOnExistence", 
          "followReferences": "followReferences", 
          "allowUnvTmpltChanges": "allowUnvTmpltChanges", 
          "overrideToken": "overrideToken", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def cancel_promotion_schedule(self, payload=None, **args):
        '''
        Arguments:
        - scheduleid: scheduleid 
        - bundleid: bundleid 
        - bundlename: bundlename 
        - date: date 
        - time: time 
        '''
        url="/resources/promotion/schedule/cancel"
        field_mapping={
          "scheduleid": "scheduleid", 
          "bundleid": "bundleid", 
          "bundlename": "bundlename", 
          "date": "date", 
          "time": "time", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def delete_promotion_schedule(self, query=None, **args):
        '''
        Arguments:
        - scheduleid: scheduleid 
        - bundleid: bundleid 
        - bundlename: bundlename 
        - date: date 
        - time: time 
        '''
        url="/resources/promotion/schedule"
        field_mapping={
          "scheduleid": "scheduleid", 
          "bundleid": "bundleid", 
          "bundlename": "bundlename", 
          "date": "date", 
          "time": "time", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def get_promotion_target(self, query=None, **args):
        '''
        Arguments:
        - targetname: targetname 
        - targetid: targetid 
        '''
        url="/resources/promotiontarget"
        field_mapping={
            "targetname": "targetname", 
            "targetid": "targetid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_promotion_target(self, payload=None, **args):
        url="/resources/promotiontarget"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_promotion_target(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/promotiontarget"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_promotion_target(self, query=None, **args):
        '''
        Arguments:
        - targetname: targetname 
        - targetid: targetid 
        '''
        url="/resources/promotiontarget"
        field_mapping={
          "targetname": "targetname", 
          "targetid": "targetid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_promotion_targets(self, query=None, **args):
        '''
        Arguments:
        - targetname: targetname 
        - businessServices: businessServices 
        '''
        url="/resources/promotiontarget/list"
        field_mapping={
            "targetname": "targetname", 
            "businessServices": "businessServices", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)
    
    def refresh_target_agents(self, query=None, payload=None, **args):
        '''
        Arguments:
        - targetname: targetname 
        - targetid: targetid 
        - username: username 
        - password: password 
        - token: token 
        '''
        url="/resources/promotiontarget/refreshtargetagents"
        query_fields={
          "targetname": "targetname", 
          "targetid": "targetid", 
        }
        payload_fields={
          "username": "username", 
          "password": "password", 
          "token": "token", 
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.post(url, query=_query, json_data=_payload, parse_response=False)