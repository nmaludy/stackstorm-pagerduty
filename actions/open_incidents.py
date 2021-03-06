from lib.action import PagerDutyAction


class OpenIncident(PagerDutyAction):
    def run(self):
        """List all open incidents, that is, incident.status = 'triggered' or 'acknowledged'"""
        open_incident = {}
        open_incident_list = []
        for incident in self.pager.Incident.find(statuses=['triggered', 'acknowledged']):
            open_incident = {'key': incident['id'], 'status': incident['status'],
                             'desc': incident['description']}
            open_incident_list.append(open_incident)
        return open_incident_list
