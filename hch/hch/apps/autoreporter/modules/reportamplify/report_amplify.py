from .report_amplify_base import ReportAmplifyBase
from hch.apps.autoreporter.models import Report


class ReportAmplify(ReportAmplifyBase):

    def __init__(self):
        super().__init__()

    def amplify(self, report: Report) -> None:

        prompt = "Im folgenden werde ich dir einen Bericht von eineme Handball spiel zusenden. "
        prompt += "Du arbeitets für den Handballverein HC Hohenems, welcher in dem Spiel um den es in den Bericht geht gespielt hat. "
        prompt += "Deine Aufgabe ist es die informationen aus diesem Bericht zu nehmen und einen pro HC Hohenems Bericht zu schreiben für unsere Website.\n\n"
        prompt += f"Der Bericht ist wie folgt: {report.report}"
        res = self._openai_cli.send_message(prompt)

        print(report.report)
        print("\n\n")
        print(res)
        exit(0)

        # res = self._openai_cli.send_message(report.report)

        # print(res)
        # exit(0)
