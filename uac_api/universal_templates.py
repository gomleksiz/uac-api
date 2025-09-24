# - create_universal_template(template_data)
# - delete_universal_template(template_id)
# - list_universal_templates()
# - modify_universal_template(template_id, **kwargs)
# - read_universal_template(template_id)
# - restore_default_universal_template_icon(template_id)
# - set_universal_template_icon(template_id, icon_data)
# - universal_template_delete_extension_archive(template_id)
# - universal_template_download_extension_archive(template_id)
# - universal_template_upload_extension_archive(template_id, file_data)
# - universal_template_export(template_id)
# - universal_template_import(file_data)
from .utils import prepare_payload, prepare_query_params


class UniversalTemplates:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_universal_template(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/universaltemplate"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_universal_template(self, payload=None, **args):
        url = "/resources/universaltemplate"
        field_mapping = {
            "sysId": "sysId",
            "name": "name",
            "description": "description",
            "variablePrefix": "variablePrefix",
            "logLevel": "logLevel",
            "templateType": "templateType",
            "agentType": "agentType",
            "useCommonScript": "useCommonScript",
            "script": "script",
            "scriptUnix": "scriptUnix",
            "scriptWindows": "scriptWindows",
            "scriptTypeWindows": "scriptTypeWindows",
            "alwaysCancelOnFinish": "alwaysCancelOnFinish",
            "sendVariables": "sendVariables",
            "credentials": "credentials",
            "credentialsVar": "credentialsVar",
            "agent": "agent",
            "agentVar": "agentVar",
            "agentCluster": "agentCluster",
            "agentClusterVar": "agentClusterVar",
            "broadcastCluster": "broadcastCluster",
            "broadcastClusterVar": "broadcastClusterVar",
            "runtimeDir": "runtimeDir",
            "sendEnvironment": "sendEnvironment",
            "exitCodes": "exitCodes",
            "exitCodeProcessing": "exitCodeProcessing",
            "exitCodeText": "exitCodeText",
            "exitCodeOutput": "exitCodeOutput",
            "outputType": "outputType",
            "outputContentType": "outputContentType",
            "outputPathExpression": "outputPathExpression",
            "outputConditionOperator": "outputConditionOperator",
            "outputConditionValue": "outputConditionValue",
            "outputConditionStrategy": "outputConditionStrategy",
            "autoCleanup": "autoCleanup",
            "outputReturnType": "outputReturnType",
            "outputReturnFile": "outputReturnFile",
            "outputReturnSline": "outputReturnSline",
            "outputReturnNline": "outputReturnNline",
            "outputReturnText": "outputReturnText",
            "waitForOutput": "waitForOutput",
            "outputFailureOnly": "outputFailureOnly",
            "elevateUser": "elevateUser",
            "desktopInteract": "desktopInteract",
            "createConsole": "createConsole",
            "agentFieldsRestriction": "agentFieldsRestriction",
            "credentialFieldsRestriction": "credentialFieldsRestriction",
            "environmentVariablesFieldsRestriction": "environmentVariablesFieldsRestriction",
            "exitCodeProcessingFieldsRestriction": "exitCodeProcessingFieldsRestriction",
            "automaticOutputRetrievalFieldsRestriction": "automaticOutputRetrievalFieldsRestriction",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_universal_template(self, payload=None, **args):
        """
        Arguments:
        - retainSysIds: retainSysIds
            False will ignore sysIds in the payload and create a new task
        """
        url = "/resources/universaltemplate"
        field_mapping = {
            "sysId": "sysId",
            "excludeRelated": "excludeRelated",
            "name": "name",
            "description": "description",
            "variablePrefix": "variablePrefix",
            "logLevel": "logLevel",
            "templateType": "templateType",
            "agentType": "agentType",
            "useCommonScript": "useCommonScript",
            "script": "script",
            "scriptUnix": "scriptUnix",
            "scriptWindows": "scriptWindows",
            "scriptTypeWindows": "scriptTypeWindows",
            "alwaysCancelOnFinish": "alwaysCancelOnFinish",
            "sendVariables": "sendVariables",
            "credentials": "credentials",
            "credentialsVar": "credentialsVar",
            "agent": "agent",
            "agentVar": "agentVar",
            "agentCluster": "agentCluster",
            "agentClusterVar": "agentClusterVar",
            "broadcastCluster": "broadcastCluster",
            "broadcastClusterVar": "broadcastClusterVar",
            "runtimeDir": "runtimeDir",
            "sendEnvironment": "sendEnvironment",
            "exitCodes": "exitCodes",
            "exitCodeProcessing": "exitCodeProcessing",
            "exitCodeText": "exitCodeText",
            "exitCodeOutput": "exitCodeOutput",
            "outputType": "outputType",
            "outputContentType": "outputContentType",
            "outputPathExpression": "outputPathExpression",
            "outputConditionOperator": "outputConditionOperator",
            "outputConditionValue": "outputConditionValue",
            "outputConditionStrategy": "outputConditionStrategy",
            "autoCleanup": "autoCleanup",
            "outputReturnType": "outputReturnType",
            "outputReturnFile": "outputReturnFile",
            "outputReturnSline": "outputReturnSline",
            "outputReturnNline": "outputReturnNline",
            "outputReturnText": "outputReturnText",
            "waitForOutput": "waitForOutput",
            "outputFailureOnly": "outputFailureOnly",
            "elevateUser": "elevateUser",
            "desktopInteract": "desktopInteract",
            "createConsole": "createConsole",
            "agentFieldsRestriction": "agentFieldsRestriction",
            "credentialFieldsRestriction": "credentialFieldsRestriction",
            "environmentVariablesFieldsRestriction": "environmentVariablesFieldsRestriction",
            "exitCodeProcessingFieldsRestriction": "exitCodeProcessingFieldsRestriction",
            "automaticOutputRetrievalFieldsRestriction": "automaticOutputRetrievalFieldsRestriction",
            "retainSysIds": "retainSysIds",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def restore_default_universal_template_icon(self, query=None, **args):
        url = "/resources/universaltemplate/restoredefaulticon"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.post(url, query=parameters, parse_response=False)

    def delete_universal_template(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/universaltemplate"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def get_extension_archive(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/universaltemplate/extension"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(
            url,
            query=parameters,
            parse_response=False,
            headers={"Accept": "application/octet-stream"},
        )

    def update_extension_archive(self, query=None, data=None, **args):
        """
        Arguments:
        - templateid: templatei
        - templatename: templatename
        """
        url = "/resources/universaltemplate/extension"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        headers = {
            "Content-Type": "application/zip",
        }
        return self.uc.post_data(
            url, query=parameters, headers=headers, data=data, parse_response=False
        )

    def delete_extension_archive(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/universaltemplate/extension"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def export_template(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        - excludeExtension: excludeExtension
        """
        url = "/resources/universaltemplate/exporttemplate"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
            "excludeExtension": "excludeExtension",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(
            url,
            query=parameters,
            headers={"Accept": "application/octet-stream"},
            parse_response=False,
        )

    def set_template_icon(self, payload=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/universaltemplate/seticon"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_universal_templates(self, query=None, **args):
        """
        Arguments:
        - templatename: templatename
        """
        url = "/resources/universaltemplate/list"
        field_mapping = {
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def import_template(self, query=None, data=None, **args):
        """
        Arguments:
        """
        url = "/resources/universaltemplate/importtemplate"
        field_mapping = {}
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.post_data(
            url,
            query=parameters,
            headers={"Content-Type": "application/zip"},
            parse_response=False,
            data=data,
        )
