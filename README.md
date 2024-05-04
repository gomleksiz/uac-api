# UAC-API - Api Wrapper for Universal Controller REST API

This Python package offers a comprehensive interface to the Stonebranch Universal Automation Center (UAC) APIs, designed to facilitate the straightforward management and execution of tasks, workflows, and more within the Stonebranch UAC environment. By providing a Pythonic way to interact with Stonebranch UAC, this package makes automation and orchestration tasks more accessible and manageable.

## Features

- **Comprehensive API Coverage**: Enables interaction with a wide array of Stonebranch UAC functionalities through Python functions.
- **Enhanced Task Management**: Simplify the creation, management, and monitoring of tasks and workflows.
- **Agent and Cluster Operations**: Manage agents and agent clusters with functions for updates, deletions, and status checks.
- **Advanced Scheduling Capabilities**: Utilize calendars, custom days, and triggers to precisely schedule tasks.
- **Resource Management**: Handle connections, credentials, properties, and variables for full control over your automation environment.
- **Audit and Reporting**: Access audit logs and generate reports for detailed insights into your automation activities.
- **Customization and Extension**: Manage custom days, email templates, scripts, and more, allowing for extensive customization and functionality extension.
- **Download Reports**: Download report in CSV, TSV, JSON, XML and PDF formats.


## Installation

```bash
pip install uac-api
```

## Quick Start
Here's a quick example to demonstrate how to start managing tasks:

```python
import uac_api

token = "ucp_<personal_access_token>"
uac = uac_api.UniversalController("https://universal.controller.url", token=token)

try:
    task = uac.tasks.get_task(task_name="Sleep 0")
    task["name"] = "Sleep 0 New" # Change task name
    # Create new task based on existing task
    response = uac.tasks.create_task(task, retainSysIds=False) 
    print(response)

    # Read new created task
    task = uac.tasks.get_task(task_name="Sleep 0 New")

    # Update the task
    task["summary"] = "Sleep 0 New Summary"
    response = uac.tasks.update_task(task)
    print(response)
finally:
    # Delete the new task
    response = uac.tasks.delete_task(task_name="Sleep 0 New")
    print(response)
```
### Launch a task and wait until it is completed
```python
import uac_api

token = "ucp_<personal_access_token>"
uac = uac_api.UniversalController("https://universal.controller.url", token=token)

response = uac.tasks.task_launch(name="Linux Sleep 10")
response = uac.task_instances.wait_for_status(id=response["sysId"], timeout=300)
print(response)
```
### Launch a task and wait alternate way
```python
import uac_api
import os

# Get the username and password from environment variables
credential = (
    os.environ.get("UAC_USERNAME"),
    os.environ.get("UAC_PASSWORD"),
)
uac = uac_api.UniversalController("https://universal.controller.url", credential=credential)

# This is a custom function of uac_api to launch a task and wait until it is completed
response = uac.tasks.task_launch_and_wait(name="Linux Sleep 10")
print(response)
```


# Functions
## UniversalController:

- init (self, base_url, credential=None, token=None, ssl_verify=True, logger=None, headers=None)

## Agents:
- get_agent(self, query=None, **args)
- update_agent(self, payload=None, **args)
- delete_agent(self, query=None, **args)
- list_agents(self)
- list_agents_advanced(self, query=None, **args)
- resume_agent(self, payload=None, **args)
- resume_agent_cluster_membership(self, payload=None, **args)
- set_agent_task_execution_limit(self, payload=None, **args)
- suspend_agent(self, payload=None, **args)
- suspend_agent_cluster_membership(self, payload=None, **args)
## AgentClusters:
- get_agent_cluster(self, query=None, **args)
- update_agent_cluster(self, payload=None, **args)
- create_agent_cluster(self, payload=None, **args)
- delete_agent_cluster(self, query=None, **args)
- list_agent_clusters(self)
- list_agent_clusters_advanced(self, query=None, **args)
- get_selected_agent(self, query=None, **args)
- resolve_cluster(self, payload=None, **args)
- resume_cluster(self, payload=None, **args)
- set_cluster_task_execution_limit(self, payload=None, **args)
- suspend_cluster(self, payload=None, **args)
## Audits:
- list_audit(self, payload=None, **args)
## Bundles:
- promote(self, payload=None, **args)
- get_bundle(self, query=None, **args)
- update_bundle(self, payload=None, **args)
- create_bundle(self, payload=None, **args)
- delete_bundle(self, query=None, **args)
- create_bundle_by_date(self, payload=None, **args)
- get_bundle_report(self, query=None, **args)
- list_bundles(self, query=None, **args)
- promote_1(self, payload=None, **args)
- cancel_promotion_schedule(self, payload=None, **args)
- delete_promotion_schedule(self, query=None, **args)
- get_promotion_target(self, query=None, **args)
- update_promotion_target(self, payload=None, **args)
- create_promotion_target(self, payload=None, **args)
- delete_promotion_target(self, query=None, **args)
- list_promotion_targets(self, query=None, **args)
- refresh_target_agents(self, payload=None, **args)
## BusinessServices:
- get_business_service(self, query=None, **args)
- update_business_service(self, payload=None, **args)
- create_business_service(self, payload=None, **args)
- delete_business_service(self, query=None, **args)
- list_business_services(self)
## Calendars:
- get_custom_days(self, query=None, **args)
- add_custom_day(self, payload=None, **args)
- remove_custom_day(self, query=None, **args)
- get_calendar(self, query=None, **args)
- update_calendar(self, payload=None, **args)
- create_calendar(self, payload=None, **args)
- delete_calendar(self, query=None, **args)
- list_calendars(self)
- list_qualifying_dates_for_local_custom_day(self, query=None, **args)
- list_qualifying_periods(self, query=None, **args)
## ClusterNodes:
- get_cluster_node(self)
- list_cluster_nodes(self)
## Connections:
- get_database_connection(self, query=None, **args)
- update_database_connection(self, payload=None, **args)
- create_database_connection(self, payload=None, **args)
- delete_database_connection(self, query=None, **args)
- list_database_connections(self)
- get_email_connection(self, query=None, **args)
- update_email_connection(self, payload=None, **args)
- create_email_connection(self, payload=None, **args)
- delete_email_connection(self, query=None, **args)
- list_email_connections(self)
- get_peoplesoft_connection(self, query=None, **args)
- update_peoplesoft_connection(self, payload=None, **args)
- create_peoplesoft_connection(self, payload=None, **args)
- delete_peoplesoft_connection(self, query=None, **args)
- list_peoplesoft_connections(self)
- get_sap_connection(self, query=None, **args)
- update_sap_connection(self, payload=None, **args)
- create_sap_connection(self, payload=None, **args)
- delete_sap_connection(self, query=None, **args)
- list_sap_connections(self)
- get_snmp_connection(self, query=None, **args)
- update_snmp_connection(self, payload=None, **args)
- create_snmp_connection(self, payload=None, **args)
- delete_snmp_connection(self, query=None, **args)
- list_snmp_connections(self)
## Credentials:
- change_password(self, payload=None, **args)
- get_credential(self, query=None, **args)
- update_credential(self, payload=None, **args)
- create_credential(self, payload=None, **args)
- delete_credential(self, query=None, **args)
- list_credentials(self)
- test_provider(self, payload=None, **args)
## CustomDays:
- get_custom_day(self, query=None, **args)
- update_custom_day(self, payload=None, **args)
- create_custom_day(self, payload=None, **args)
- delete_custom_day(self, query=None, **args)
- list_custom_days(self)
- list_qualifying_dates(self, query=None, **args)
- list_qualifying_periods(self, query=None, **args)
## EmailTemplates:
- get_email_template(self, query=None, **args)
- update_email_template(self, payload=None, **args)
- create_email_template(self, payload=None, **args)
- delete_email_template(self, query=None, **args)
- list_email_template(self)
## Ldaps:
- get_ldap(self)
- update_ldap(self, payload=None, **args)
## Metrics:
- get_metrics(self)
## OAuthClients:
- get_oauth_client(self, query=None, **args)
- update_oauth_client(self, payload=None, **args)
- create_oauth_client(self, payload=None, **args)
- delete_oauth_client(self, query=None, **args)
- list_oauth_clients(self)
## OmsServers:
- get_oms_server(self, query=None, **args)
- update_oms_server(self, payload=None, **args)
- create_oms_server(self, payload=None, **args)
- delete_oms_server(self, query=None, **args)
- list_oms_servers(self)
## Properties:
- get_property(self, query=None, **args)
- update_property(self, payload=None, query=None, **args)
- list_properties(self)
## Reports:
- run_report(self, query=None, report_format="csv", **args)
## Scripts:
- get_script(self, query=None, **args)
- update_script(self, payload=None, **args)
- create_script(self, payload=None, **args)
- delete_script(self, query=None, **args)
- list_scripts(self)
## ServerOperations:
- roll_log(self)
- temporary_property_change(self, payload=None, **args)
## Simulations:
- get_simulation(self, query=None, **args)
- update_simulation(self, payload=None, **args)
- create_simulation(self, payload=None, **args)
- delete_simulation(self, query=None, **args)
- list_simulations(self, query=None, **args)
## System:
- get_status(self)
## TaskInstances:
- delete_task_instance(self, query=None, **args)
- show_variables(self, query=None, **args)
- update_operational_memo(self, payload=None, **args)
- task_instance_set_priority(self, payload=None, **args)
- set_timewait(self, payload=None, **args)
- list_dependency_list(self, query=None, **args)
- task_insert(self, payload=None, **args)
- task_instance_cancel(self, payload=None, **args)
- task_instance_clear_dependencies(self, payload=None, **args)
- task_instance_clear_exclusive(self, payload=None, **args)
- task_instance_clear_instance_wait(self, payload=None, **args)
- task_instance_clear_predecessors(self, payload=None, **args)
- task_instance_clear_resources(self, payload=None, **args)
- task_instance_clear_timewait(self, payload=None, **args)
- task_instance_force_finish(self, payload=None, **args)
- task_instance_force_finish_cancel(self, payload=None, **args)
- task_instance_hold(self, payload=None, **args)
- task_instance_release(self, payload=None, **args)
- task_instance_rerun(self, payload=None, **args)
- task_instance_retrieve_output(self, query=None, **args)
- task_instance_skip(self, payload=None, **args)
- task_instance_skip_path(self, payload=None, **args)
- task_instance_unskip(self, payload=None, **args)
- list_status(self, payload=None, **args) - List Task Instances
- wait_for_status(self, id, statuses=FINAL_STATUS, timeout=300, interval=10): Waits until the task instance reaches one of the given statuses.
- set_complete(self, payload=None, **args)
## Tasks:
- get_task(self, query=None, **args)
- update_task(self, payload=None, **args)
- create_task(self, payload=None, **args)
- clone_task(self, task_name, new_task_name): Copy task with a new name
- delete_task(self, query=None, **args)
- list_tasks(self, payload=None, **args)
- list_tasks_advanced(self, query=None, **args)
- list_workflow_list(self, query=None, **args)
- task_clear_dependencies(self, payload=None, **args)
- task_clear_exclusive(self, payload=None, **args)
- task_clear_predecessors(self, payload=None, **args)
- task_clear_resources(self, payload=None, **args)
- task_clear_timewait(self, payload=None, **args)
- task_create_with_properties(self, payload=None, **args)
- list_dependency_list_1(self, query=None, **args)
- task_insert_1(self, payload=None, **args)
- task_launch(self, payload=None, **args)
- task_release(self, payload=None, **args)
- task_set_timewait(self, payload=None, **args)
- create_linux_task(self, name, agent, payload=None, command=None, script=None)
- create_windows_task(self, name, agent, payload=None, command=None, script=None)
- create_workflow(self, name, payload=None)
## Triggers:
- list_qualifying_times(self, query=None, **args)
- assign_execution_user_to_trigger(self, query=None, payload=None, **args)
- unassign_execution_user(self, payload=None, **args)
- create_temp_trigger(self, payload=None, **args)
- get_trigger(self, query=None, **args)
- update_trigger(self, payload=None, **args)
- create_trigger(self, payload=None, **args)
- delete_trigger(self, query=None, **args)
- list_triggers(self, payload=None, **args)
- list_triggers_advanced(self, query=None, **args)
- enable_disable(self, payload=None, **args)
## UniversalEventTemplates:
- get_universal_event_template(self, query=None, **args)
- update_universal_event_template(self, payload=None, **args)
- create_universal_event_template(self, payload=None, **args)
- delete_universal_event_template(self, query=None, **args)
- list_universal_event_templates(self, query=None, **args)
## UniversalEvents:
- publish(self, payload=None, **args)
- pushg(self, query=None, eventName=None, **args)
- push(self, payload=None, eventName=None)
## UniversalTemplates:
- get_universal_template(self, query=None, **args)
- update_universal_template(self, payload=None, **args)
- create_universal_template(self, payload=None, **args)
- delete_universal_template(self, query=None, **args)
- get_extension_archive(self, query=None, **args)
- update_extension_archive(self, payload=None, **args)
- delete_extension_archive(self, query=None, **args)
- export_template(self, query=None, **args)
- set_template_icon(self, payload=None, **args)
- list_universal_templates(self, query=None, **args)
## UserGroups:
- get_user_group(self, query=None, **args)
- update_user_group(self, payload=None, **args)
- create_user_group(self, payload=None, **args)
- delete_user_group(self, query=None, **args)
- list_user_groups(self)
## Users:
- change_user_password(self, payload=None, **args)
- get_user(self, query=None, **args)
- update_user(self, payload=None, **args)
- create_user(self, payload=None, **args)
- delete_user(self, query=None, **args)
- create_user_token(self, payload=None, **args)
- revoke_user_token(self, query=None, **args)
- list_auth_tokens(self, query=None, **args)
- list_users(self, query=None, **args)
## Variables:
- get_variable(self, query=None, **args)
- update_variable(self, payload=None, **args)
- create_variable(self, payload=None, **args)
- delete_variable(self, query=None, **args)
- list_variables(self, payload=None, **args)
- list_variables_advanced(self, query=None, **args)
- variable_set(self, payload=None, **args)
## VirtualResources:
- get_virtual_resource(self, query=None, **args)
- update_virtual_resource(self, payload=None, **args)
- create_virtual_resource(self, payload=None, **args)
- delete_virtual_resource(self, query=None, **args)
- list_virtual_resources(self, query=None, **args)
- list_virtual_resources_advanced(self, query=None, **args)
- update_limit(self, payload=None, **args)
## Webhooks:
- unassign_execution_user_1(self, payload=None, **args)
- get_webhook(self, query=None, **args)
- update_webhook(self, payload=None, **args)
- create_webhook(self, payload=None, **args)
- delete_webhook(self, query=None, **args)
- disable_webhook(self, payload=None, **args)
- enable_webhook(self, payload=None, **args)
- list_webhooks(self, query=None, **args)
## Workflows:
- get_edges(self, query=None, **args)
- update_edge(self, payload=None, **args)
- add_edge(self, payload=None, **args)
- delete_edge(self, query=None, **args)
- get_vertices(self, query=None, **args)
- update_vertex(self, payload=None, **args)
- add_vertex(self, payload=None, **args)
- delete_vertices(self, query=None, **args)
- get_forecast(self, query=None, **args)
- add_child_vertex(self, workflow_name, task_name, parent_task_name=None, parent_vertex_id=None, vertex_id=None, auto_arrange=True)
- auto_arrange_vertices(self, workflow_name=None, payload=None)

# Classes
- Agents
- AgentClusters
- Audits
- Bundles
- Calendars
- Credentials
- Connections
- CustomDays
- EmailTemplates
- Ldaps
- Metrics
- OmsServers
- OAuthClients
- Properties
- Reports
- Scripts
- ServerOperations
- System
- Simulations
- Tasks
- TaskInstances
- Triggers
- UniversalEventTemplates
- UniversalEvents
- UniversalTemplates
- UserGroups
- Users
- VirtualResources
- Webhooks
- Workflows
- ClusterNodes

# Contributing
We welcome contributions! Please refer to our Contributing Guide for details on how to submit pull requests, propose bug fixes and improvements, and how to build and test your changes to this project.

# License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

### What this means

The CC BY-NC 4.0 License allows others to remix, adapt, and build upon the work non-commercially, as long as they credit the creator and license their new creations under the identical terms.

### Full Legal Code

You can read the full legal code of the license [here](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

### Summary of the License

This summary is a quick guide to the key elements of the full license, which is legally binding:

- **Attribution:** You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- **NonCommercial:** You may not use the material for commercial purposes.

- **ShareAlike:** If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

- **No additional restrictions:** You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For more information about what you can and can't do under this license, please review the license code and summary at the provided link.

# Disclaimer
This package is not officially affiliated with Stonebranch, Inc. It is a community-driven project aimed at simplifying the use of Stonebranch UAC APIs.
